#!/usr/bin/env python3
"""把文章中引用的知乎图片 (*.zhimg.com) 迁移到自有图床 pic.yvonshong.com (Cloudflare R2)。

三步走，每一步都可以单独重复运行：

  1. 下载：  python3 tools/migrate_zhimg.py download
             -> 图片保存到 tools/zhimg/，已下载的跳过，失败的列在最后
  2. 上传：  rclone copy tools/zhimg r2:<bucket> --progress
             （R2 remote 的配置见 tools/README-zhimg.md）
  3. 替换：  python3 tools/migrate_zhimg.py replace [--dry-run]
             -> 只替换 pic.yvonshong.com 上已经能访问 (HTTP 200) 的图片，
                没上传成功的链接保持原样，不会把文章改坏

文件名规则：去掉 query string，保留知乎原始文件名（v2-<hash>_<size>.<ext>），
.avis 改为 .avif。知乎文件名本身带内容哈希，不会冲突。
"""
import argparse
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "source"
OUT = Path(__file__).resolve().parent / "zhimg"
PIC_HOST = "https://pic.yvonshong.com/"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")

URL_RE = re.compile(r"https?://[a-z0-9]+\.zhimg\.com/[^\s)\"'<>]+")


def md_files():
    return sorted(POSTS.rglob("*.md"))


def local_name(url: str) -> str:
    name = url.split("?", 1)[0].rsplit("/", 1)[-1]
    if name.endswith(".avis"):
        name = name[:-5] + ".avif"
    return name


def collect_urls():
    urls = set()
    for f in md_files():
        urls.update(URL_RE.findall(f.read_text(encoding="utf-8")))
    return sorted(urls)


def fetch(url: str, timeout=30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def download_one(url: str):
    dest = OUT / local_name(url)
    if dest.exists() and dest.stat().st_size > 0:
        return url, "skip"
    last = None
    for attempt in range(3):
        try:
            data = fetch(url)
            if len(data) < 100:
                raise ValueError(f"响应过小 ({len(data)} bytes)")
            dest.write_bytes(data)
            return url, "ok"
        except (urllib.error.URLError, ValueError, TimeoutError) as e:
            last = e
            time.sleep(1 + attempt)
    return url, f"FAIL: {last}"


def cmd_download(args):
    OUT.mkdir(exist_ok=True)
    urls = collect_urls()
    print(f"共 {len(urls)} 个知乎图片链接，下载到 {OUT}")
    fails = []
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        for i, (url, status) in enumerate(ex.map(download_one, urls), 1):
            if status.startswith("FAIL"):
                fails.append((url, status))
            print(f"[{i}/{len(urls)}] {status:4.4} {local_name(url)}")
    print(f"\n完成：成功/跳过 {len(urls) - len(fails)}，失败 {len(fails)}")
    for url, status in fails:
        print(f"  {status}  {url}")
    if fails:
        print("\n失败的图片可以在浏览器里手动另存到 tools/zhimg/（文件名保持一致），再继续上传。")
    return 1 if fails else 0


def is_live(name: str) -> bool:
    req = urllib.request.Request(PIC_HOST + name, method="HEAD",
                                 headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except (urllib.error.URLError, TimeoutError):
        return False


def cmd_replace(args):
    urls = collect_urls()
    names = sorted({local_name(u) for u in urls})
    print(f"检查 {len(names)} 张图片在 {PIC_HOST} 上是否可访问…")
    with ThreadPoolExecutor(max_workers=args.jobs) as ex:
        live = {n for n, ok in zip(names, ex.map(is_live, names)) if ok}
    missing = [n for n in names if n not in live]
    print(f"可访问 {len(live)}，不可访问 {len(missing)}")
    for n in missing:
        print(f"  未上传: {n}")

    changed_files = replaced = 0
    for f in md_files():
        text = f.read_text(encoding="utf-8")

        def sub(m):
            nonlocal replaced
            name = local_name(m.group(0))
            if name in live:
                replaced += 1
                return PIC_HOST + name
            return m.group(0)

        new = URL_RE.sub(sub, text)
        if new != text:
            changed_files += 1
            print(f"  {'[dry-run] ' if args.dry_run else ''}更新 {f.relative_to(ROOT)}")
            if not args.dry_run:
                f.write_text(new, encoding="utf-8")
    print(f"\n替换 {replaced} 处链接，涉及 {changed_files} 个文件"
          f"{'（dry-run，未写入）' if args.dry_run else ''}")
    return 1 if missing else 0


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    d = sp.add_parser("download")
    d.add_argument("-j", "--jobs", type=int, default=8)
    d.set_defaults(func=cmd_download)
    r = sp.add_parser("replace")
    r.add_argument("-j", "--jobs", type=int, default=16)
    r.add_argument("--dry-run", action="store_true")
    r.set_defaults(func=cmd_replace)
    args = p.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()

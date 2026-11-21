# 知乎图片迁移到 R2

## 1. 下载

```bash
python3 tools/migrate_zhimg.py download
```

## 2. 配置 rclone 的 R2 remote（只需一次）

在 Cloudflare 控制台 → R2 → Manage R2 API Tokens 创建一个对该 bucket 有 Object Read & Write 权限的 token，然后：

```bash
rclone config create r2 s3 \
  provider=Cloudflare \
  access_key_id=<ACCESS_KEY_ID> \
  secret_access_key=<SECRET_ACCESS_KEY> \
  endpoint=https://<ACCOUNT_ID>.r2.cloudflarestorage.com \
  acl=private no_check_bucket=true
```

## 3. 上传

pic.yvonshong.com 绑定的 bucket 根目录对应 `https://pic.yvonshong.com/<文件名>`：

```bash
rclone copy tools/zhimg r2:<bucket> --progress
```

## 4. 替换文章里的链接

```bash
python3 tools/migrate_zhimg.py replace --dry-run   # 先预览
python3 tools/migrate_zhimg.py replace
```

只会替换 pic.yvonshong.com 上已经能访问的图片，可重复运行。

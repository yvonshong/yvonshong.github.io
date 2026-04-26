---
title: Hexo 图床方案和国内解析优化
date: 2026-04-26 20:30:00
tags:
  - hexo
  - vercel
  - cloudflare
categories:
  - tech
---

近期对博客的部署架构和访问速度进行了一次调整。主要包括主题更换、图床搭建，以及基于 Vercel 和 GitHub Pages 的双线路由部署。在此做个操作记录。

<!-- more -->

## 1. 更换 Butterfly 主题

之前使用的是 Yilia 主题。随着博客内容增多，开始需要全局本地搜索功能。

目前将主题切换到了 [Butterfly](https://butterfly.js.org/)。Butterfly 集成了丰富的第三方搜索插件接口，也提供了较大的自定义空间，能够更好地满足当前长篇文章和多标签的管理需求。

## 2. 图床方案：GitHub Actions + Cloudflare R2

**之前的方案**：通过代理节点加速 GitHub 原图访问，但稳定性不可控。国内的对象存储服务（如七牛云）绑定 HTTPS 又需要额外计费。

**当前的方案**：切换至 Cloudflare R2 存储，配合 GitHub Actions 实现图片的自动压缩和上传。

### 工作流逻辑：
1. 将文章原图（jpg/png）推送到独立的图片分支（如 `raw` 分支）。
2. GitHub 监听到改动后，触发 Actions 脚本：
   - 筛选出体积大于 128KB 的图片。
   - 将图片压缩并转换为 `.webp` 格式。
   - 自动上传至 Cloudflare R2 存储桶。
3. 取备用域名 `shong.win` 托管给 Cloudflare 解析。在 R2 控制台将该域名绑定为公开访问地址，Markdown 中直接使用该域名的链接引用图片。

### GitHub Actions 变量设置
在代码仓库的 `Settings -> Secrets and variables -> Actions` 中添加以下变量：
- `R2_ACCOUNT_ID`：Cloudflare 账户 ID。
- `R2_ACCESS_KEY_ID`：R2 API Token 的 Access Key ID。
- `R2_SECRET_ACCESS_KEY`：R2 API Token 的 Secret Access Key。
- `R2_BUCKET`：目标 R2 存储桶名称。

## 3. 多线路部署：Vercel + 腾讯云 DNS 分流

为了改善 GitHub Pages 在国内的访问连通率，引入了 Vercel 作为国内访问的节点，同时通过腾讯云 DNS 进行解析分流。

### 具体设置：
1. **DNS 线路分流**：
   在腾讯云域名解析平台添加两条 `www` 的 CNAME 记录：
   - **境外线路**：解析到 `yvonshong.github.io`。
   - **境内线路**：解析到 `cname.vercel-dns.com`。

2. **Vercel 绑定与部署配置**：
   - **绑定自定义域名**：Vercel 默认的 `.vercel.app` 域名在国内访问受限。需要在 Vercel 的 `Settings -> Domains` 中绑定自己的域名（本站绑定了 `yvonshong.com` 和 `shong.win`）。
   - **跳过构建阶段**：平时已经使用 `hexo d` 将编译好的静态页面推送到了 GitHub 的 `master` 分支。为了避免服务端二次构建报错，在 Vercel 中配置跳过构建步骤，直接托管 `master` 分支的静态页面文件。

---

## 附录：免费额度参考

本方案使用的各项服务免费版额度如下，供参考：

- **Cloudflare R2**：每月 10 GB 存储空间、1000 万次读取请求、100 万次写入请求，免下行流量费。
- **Vercel**：每月 100 GB 带宽。
- **Cloudflare**：基础 CDN 节点和 SSL 证书免费。
- **GitHub Actions**：公开仓库无限制；私有仓库每月 2000 分钟运行时间。

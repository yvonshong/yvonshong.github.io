---
title: Hexo 进阶与优化
date: 2017-02-20 15:39:00
categories: code
tags: hexo
toc: true
---
在经过申请域名到搭建hexo，以及利用AppVeyor实现持续集成，hexo已经实现了基本的编辑模式，就是我push文章的md文档，然后会自动发布hexo生成的静态网页，只需要git环境。接下来我们对博客进行优化，尝试各种插件。
<!-- more -->
- [qiniu sync](https://github.com/gyk001/hexo-qiniu-sync)
同步资源文件到七牛，能加速一些资源。


- SEO 搜索引擎优化
我们发现百度和谷歌并没有收录到此博客，于是我们去提交我们的站点

[Google搜索引擎提交入口](https://www.google.com/webmasters/tools/home?hl=zh-CN)

[百度搜索引擎入口](http://www.baidu.com/search/url_submit.htm)



>提供三种验证方式：文件验证、html标签验证、CNAME验证。
>　　1.文件验证：您需要下载验证文件，将文件上传至您的服务器，放置于域名根目录下。
>　　2.html标签验证：将html标签添加至网站首页html代码的<head>标签与</head>标签之间。
>　　3.CNAME验证：您需要登录域名提供商或托管服务提供商的网站，添加新的DNS记录。
>验证完成后，我们将会认为您是网站的拥有者。为使您的网站一直保持验证通过的状态，请保留验证的文件、html标签或CNAME记录，我们会去定期检查验证记录。

建议先使用文件验证，只需要从网上下载验证的html，然后同步到git仓库根目录下，就能成功。

- 提交sitemap
利用生成站点地图的插件
```
npm install hexo-generator-sitemap --save
npm install hexo-generator-baidu-sitemap --save
```
在博客目录的_config.yml中添加如下代码

```
# 自动生成sitemap
sitemap:
path: sitemap.xml
baidusitemap:
path: baidusitemap.xml
```

生成xml文件，然后让搜索引擎去访问，地址是

博客地址/sitemap.xml
和 博客地址/baidusitemap.xml

在这里 你可以进行站长管理 https://www.google.com/webmasters/tools/home?hl=zh-CN

http://zhanzhang.baidu.com/dashboard/index?site=http://www.shong.win/


- CDN加速

[百度云加速](https://su.baidu.com/)

更换DNS，或者设置CNAME记录

- 访问量计数
[不蒜子](http://busuanzi.ibruce.info/)
在主题的某个js文件下插入
```js
 <script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>
            <span id="busuanzi_container_site_pv">本站总访问量<span id="busuanzi_value_site_pv"></span>次</span>
```

- RSS
我记得以前看到一句话，叫做 
>支持RSS，是美德。
会用的人当然很喜欢RSS。
我们可以利用rss生成插件
```
npm install hexo-generator-feed --save
```

装完hexo-generator-feed后，将其配置到根目录的_config.yml
```yml
# Extensions
## Plugins: http://hexo.io/plugins/
#RSS订阅
plugin:
- hexo-generator-feed
#Feed Atom
feed:
type: atom
path: atom.xml
limit: 20
```

然后你便能在 博客地址/atom.xml 看到生成的rss了
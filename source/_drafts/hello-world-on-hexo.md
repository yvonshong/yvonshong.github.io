---
title: Hello world on Hexo, my new personal blog.
date: 2017-02-18 00:00:00
toc: true
---
利用Hexo在Github Pages上搭建个人博客
<!-- more -->
之前在腾讯云校园活动里购买了个一年.cn域名，于是用上了一阵子的腾讯云，用wordpress搭了个博客，可是腾讯云经常宕机需要跑到后台去重启（是的我就是那么简单粗暴😂），一年到头也没宣传也没分享没更什么文章，前几天觉得Github能直接给每个仓库开github pages，觉得太有用了，脑子一热，又打算重新搭博客了。
挑来挑去，最后买了shong.win十年域名，win可以理解为微软粉嘛，并利用hexo在github上搭静态博客。
这篇文章主要分享下搭博客的过程。

<!-- more -->
## 域名
在这里根据续费查询域名商以及挑选后缀
[在这里找到续费域名最便宜的域名商](http://www.domain265.com/renew/)
最后选择了在[西部数码](http://www.west.cn) 购买shong.win域名，十年。

### 子域名
在域名管理处增加url跳转，比如blog.shong.win 跳转到www.shong.win/blog 这样就实现了子域名。
## 邮箱
有了域名就可以作邮箱， .win域名由于不太常见，腾讯企业邮箱不支持，所幸的是网易域名邮箱支持[163域名邮箱](http://app.ym.163.com/ym/help/help.html)。并在域名管理处增加MX记录，起效后便能使用邮箱了。

## Github Page
Github Page是Github自带的功能，能够直接给仓库开展示页面，网址是username.github.io/reponame
在github中创建username.github.io仓库，然后便能开启pages功能，我们在这个仓库下添加一个名为CNAME无后缀的文件，内容是购买的域名，并在域名管理处增加记录，www的CNAME记录，指向pages仓库。然后便能使域名跳转到pages仓库的页面了。

## Hexo

由于在pages仓库里面自己写每个web的话太麻烦了，我们利用在本地nodejs环境下搭建[Hexo](https://hexo.io/)，hexo会自动将其环境下指定的markdown文件渲染成博客文章。自带首页，查询等一系列功能。详情请参见网上别人写的[更详细的中文教程](https://xuanwo.org/2015/03/26/hexo-intor/)

### Themes
然后我们给hexo更换主题，主题的配置也十分简单，参见文档[hexo.io/zh-cn/docs/themes.html](https://hexo.io/zh-cn/docs/themes.html)

我使用的是hexo-theme-yilia
### Plugin
hexo可以使用很多插件，并且内置了多说（让游客可以登录社交媒体账户对你的博文进行评论）[配置文档](https://github.com/iissnan/hexo-theme-next/wiki/%E8%AE%BE%E7%BD%AE%E5%A4%9A%E8%AF%B4-DISQUS)
也可以使用七牛同步你的照片和文件，减少对github仓库的占用，[配置hexo-qiniu-sync](https://github.com/gyk001/hexo-qiniu-sync)

接下来就可以愉快写博客啦！


### Create a new post
``` bash
$ hexo new [layout] <title>

```
More info: [Writing](https://hexo.io/zh-cn/docs/writing.html)
### Sync Pic with qiniu
七牛指定了 /static/image/ 这个文件为同步文件夹。

在文章中引用照片可以者直接利用七牛给的网址前缀，文章中直接在图片地址的前面加七牛前缀。

```
![](http://personalname.bkt.clouddn.com/static/image/folder/filename.jpg)
```


### Run server

``` bash
$ hexo s
```
### Generate static files

``` bash
$ hexo g
```
### Deploy to remote sites

``` bash
$ hexo d
```



## 个人觉得这个博客的好处
搭完网站后，我便将自己以前在自己开的微信公众号啊，豆瓣啊，知乎专栏啊，空间啊什么四处写的文章都迁移过来了，毕竟自己掌控的东西更能自主一点。
- 首先是支持直接将Markdown渲染成web。
- 自己写的博客，能够在发布后随时更改错别字。
- 可以迁移之前写的文章。
- hexo丰富的插件，能够有多说的评论，主题自带的打赏功能，搜索功能，tag，categories等功能。

## 下一阶段
接下来想尝试hexo的其他插件，并利用[coding](http://coding.net)试一试coding的功能，比如web IDE，增加coding.shong.win
后面可以再尝试在Microsoft Azure上搭建ss（之前一直失败。。。），就能充分利用子域名指向ip实现各种功能啦！
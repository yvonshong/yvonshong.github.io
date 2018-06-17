---
title: Hexo利用AppVeyor持续集成
date: 2017-02-20 02:18:00
categories: code
tags: 
- git
- appveyor
- hexo
toc: true
---
在第一天尝试了hexo之后，觉得这个静态博客远比不上wordpress托管到主机上的博客方便，因为太依赖本机环境，需要nodejs和git，每次更新后需要自己生成静态页面（虽然也就两行代码的事情），这一点都不cool！
并且有一大弊端，当你转移电脑的时候，你需要转移你根目录下很多配置文件和之前的md文件，（图片等资源文件我是利用插件同步到了七牛的，所以资源文件不用担心），这也需要备份！（这个时候我想到了利用我Github Pages的同一个仓库，通过建不同的分支来实现，比如我是username.github.io仓库，master分支为hexo生成同步的web展示页分支，我新建一个hexo分支，就是包含了我根目录下的themes/, source/ ,_config.yml,package.json 然后就能在其他环境下重新搭建hexo）

为了达到自动更新和在线编辑的目的，我遍寻方法。
<!-- more -->

- ide.coding.net

>Coding WebIDE 是 Coding 自主研发的在线集成开发环境。用户可以通过 WebIDE 创建项目的工作空间，进行在线开发，调试等操作。与此同时，WebIDE 还提供了可分享的开发环境功能，用户可以保存当前的 Terminal 环境，分享给团队的其他成员。
[利用coding WebIDE远程hexo教程](http://garth.im/2015/04/hexo-on-coding-net-webide/)

- 绿色版本的git和hexo

好吧这依旧不酷。。。。就是拷进U盘而已

- 百度云/Dropbox同步

没差，没有运行环境，也需要重新配置。

- 利用[AppVeyor](www.appveyor.com)远端**持续集成**！

上一次接触到持续集成这个概念，还是暑假我实习的时候，当时是我们利用公司自己搭的gitlab，利用git提交代码到服务器主机，也有ftp，然后主机自己会把汇集在一起的代码进行检测，检测通过后发布。（当时去查了下持续集成，持续发布等的概念。。。也算是学到的知识吧2333）

现在！我们也可以利用持续集成，通过push md文档到git，远端自己pull，然后自己hexo，然后push到我的github pages的仓库。（这里我依旧利用了两个分支，master分支发布，hexo分支编辑。）

当时主要是看到了[这篇文章](https://formulahendry.github.io/2016/12/04/hexo-ci/)，介绍了[AppVeyor](www.appveyor.com)，当然后面也有查阅到[使用Travis自动部署Hexo](http://www.jianshu.com/p/fff7b3384f46)，而且AppVeyor是唯一支持Windows的服务商。。（虽然hexo也并没有必须windows？？？）

下面介绍我使用appveyor趟的坑

1. 注册登陆AppVeyor
free for opensource project
2. appveyor新建project
Github授权，关联相关repo（更新文档的repo）（我都是在[/blog](http://github.com/yvon-shong/blog) ）
设置项目
- setting-general
![setting-general.jpg](http://oljkaeely.bkt.clouddn.com/static/image/hexo-ci/setting-general.jpg)
- setting-env
![setting-env.jpg](http://oljkaeely.bkt.clouddn.com/static/image/hexo-ci/setting-env.jpg)
3. 配置appveyor.yml到文档repo

需要利用GitHub Access Token，这玩意儿相当于你的git的密钥，[GitHub上生成token的相关官方文档](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)

然后由于你yml是在github上公开的，所以你的token必须利用appveyor的[加密工具进行加密](https://ci.appveyor.com/tools/encrypt)

```yml
clone_depth: 5
environment:
 access_token:
    secure: 
    【替换成自己加密后的GitHub Access Token】

install:
- node --version
- npm --version
- npm install
- npm install hexo-cli -g
build_script:
- hexo generate

artifacts:
- path: public
on_success:
- git config --global credential.helper store
- ps: Add-Content "$env:USERPROFILE\.git-credentials" "https://$($env:access_token):x-oauth-basic@github.com`n"
- git config --global user.email "%GIT_USER_EMAIL%"
- git config --global user.name "%GIT_USER_NAME%"
- git clone --depth 5 -q --branch=%TARGET_BRANCH% %STATIC_SITE_REPO% %TEMP%\static-site
- cd %TEMP%\static-site
- del * /f /q
- for /d %%p IN (*) do rmdir "%%p" /s /q
- SETLOCAL EnableDelayedExpansion & robocopy "%APPVEYOR_BUILD_FOLDER%\public" "%TEMP%\static-site" /e & IF !ERRORLEVEL! EQU 1 (exit 0) ELSE (IF !ERRORLEVEL! EQU 3 (exit 0) ELSE (exit 1))
- git add -A
- if "%APPVEYOR_REPO_BRANCH%"=="master" if not defined APPVEYOR_PULL_REQUEST_NUMBER (git diff --quiet --exit-code --cached || git commit -m "Update Static Site" && git push origin %TARGET_BRANCH% && appveyor AddMessage "Static Site Updated")

```

这是我第二次接触到yml，yml可以转换成json，语法严格，连冒号后空格都要限制必须只能一个。。。

yml仔细一看，都是bash操作啊！

4. 基本完成！
好吧这是网上的博主。。。我是又遇到bug了（配置什么的，最烦了！）
当时已经在appveyor上build了，遇到无数次报错！
- 拉取失败过
项目配置的branch有误，更新文档的repo的branch才有yml 

- hexo generate成功了
然后毫无反应。。。。我也不知道为什么

- 仔细查看yml
我查看yml，发现
```yml
build_script:
- hexo generate

```
欸只有generate呢？我就擅自加了个hexo deploy
然后遇到了权限报错，回想了一下hexo在部署的时候，我是需要手动输入git的密钥的。。。
看来是git上有问题，可是我明明有token啊？
我在查阅相关key配置时，发现有个东西叫credential？？诶yml文档里面也有这个欸！

```yml
- git config --global credential.helper store
- ps: Add-Content "$env:USERPROFILE\.git-credentials" "https://$($env:access_token):x-oauth-basic@github.com`n"
```
这里yml将环境变量，我传进去的access_token用到了，这里应该就是配置ssh免密。
于是我相通了，不应该用hexo自带的部署，直接用git bash命令上传，于是我把后面部分修改成

```yml
- git add -A
- git commit -m "Update Static Site" 
- git push origin %TARGET_BRANCH%
- appveyor AddMessage "Static Site Updated"
```
这里又回顾了一波git bash命令（通常都用sourcetree的我。。。）

然后终于成功了！！！
![success](http://oljkaeely.bkt.clouddn.com/static/image/hexo-ci/success.jpg)

至此，接下来只需要深入了解appveyor的自动集成周期等更详细的信息就行了。
appveyor还可以根据你git更新打的tag来触发！欢迎尝试！

（凌晨一点终于搞完hexo持续集成，然后又花了一个小时写博客。。。）
                                              
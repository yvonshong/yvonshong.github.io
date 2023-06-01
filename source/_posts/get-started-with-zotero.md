---
title: PDF 文献库解决方案——Zotero
date: 2023-05-29 17:00:00
categories: tech
toc: true
tags:
- zotero
- onedrive
---

论工作方式的形成，和效率工具，我言必及我大一开始使用的：

- outlook 日历：做日程管理，有时间跨度和排他性的任务；
- todo：之前是 wunderlist，做任务管理，有 ddl 和优先级的设定；
- 以及我之前最重要的文档工具 OneNote；

但是在存储管理 pdf 文件上，迷糊了很多年。

<!-- more -->

有时候会追求在 pdf 上手写笔记，有时候又追求键盘输入的可搜索性。先后尝试过：

1. 把 PDF 文件保存进 OneNote，在里面做批注。最后发现 OneNote 根本就不是做这个的，OneNote 会变得巨大打开变得巨慢，阅读体验也很差。
2. 还原到本质，用文件夹进行管理，Surface 上做批注。缺点是文件夹的层级会十分犹豫，因为论文类型的 PDF 更适合多 tag 的描述，当然其实在足够优秀的搜索效果面前，tag 也是可以忽略的。
3. 把 PDF 保存在 Notebility，在里面做批注。软件实现了 OneDrive 的保存，但是不跨平台，只支持 Mac + iPad 平台，Windows 用户震怒。
4. 尝试过 Mendeley，是专门的文献管理软件，虽然文献信息可上传至云端备份，但账户存储空间只有**2G的免费空间**，多余的文献将无法同步其文件。因此，重装系统或者更换电脑后，未同步 PDF 文件的文献将无法同步至新平台上。其对英文文献的友好程度较高，但不利于中文文献的管理。

最后终于用上了 Zotero，它的好处有：

- 文献信息整理，有文献库的基本功能，搜索，标签，一应俱全。
- 支持 OneDrive 同步！M365用户狂喜。
- 有很多插件，支持中文文献。

# Zotero

注册和下载： https://www.zotero.org/


# 基础设置

## 语言

- Edit 编辑 >> Preference 首选项 >> Advanced >> General >> Language >> 中文（简体）


## OneDrive 同步

- 编辑 >> 首选项 >> 同步 >> 登录 会用 `Zotero` 同步书目条例
- 编辑 >> 首选项 >> 高级 >> 文件和文件夹  >> 已链接附件的根文件夹 >> 选择 到 OneDrive 自己的 Zotero/storage 文件夹下
- 数据存储位置 为默认

Ubuntu 下 OneDrive 同步可参考 [Get started with Obsidian](https://www.yvonshong.com/2022/01/28/get-started-with-obsidian/)


# 插件

官方插件列表 https://www.zotero.org/support/plugins

## ZotFile

用于管理附件，自动PDF重命名，移动和附加到Zotero项目，下载： https://github.com/jlegewie/zotfile

设置：

- 工具 >> ZotFile Preference >> Source Folder for Attaching New Files >> 到自己的  `OneDrive/Documents/Zotero/storage`  文件夹下
- 工具 >> ZotFile Preference >> Location of Files >> 到自己的  `OneDrive/Documents/Zotero/storage`  文件夹下
- 工具 >> ZotFile Preference >> Location of Files >> Use subfolder defined by `/%t`

## 茉莉花 Jasminum

下载： [Jasminum - 茉莉花](https://github.com/l0o0/jasminum)

设置：

![](https://pic2.zhimg.com/80/v2-a12eb6a0a0d3b0a556c2f7eccc19efcd_720w.webp)

enjoy it!
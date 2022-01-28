---
title: Get started with Obsidian
date: 2022-01-28 12:00:00
toc: true
tags:
- obsidian
---


# Obsidian
Obsidian 是根据卢曼卡片盒方法论构建的次世代笔记系统，基于本地 markdown 编辑和双向链接特殊语法。具体使用方式可以参考《卡片盒阅读法》和 Notion。

<!-- more -->

官网 https://obsidian.md/ ，目前支持 Windows, macOS, Linux, iOS, iPadOS, Android.
同步支持 Obsidian 应用内付费同步， 苹果生态支持 iCloud 同步，可自建其他云盘同步和 Git 同步。

我个人的使用方案是：

Windows, Linux(Ubuntu 20.04), macOS, 都使用 Onedrive 同步；

手机上不使用。


## 安装 Install


官网 https://obsidian.md/

## 启动 Launch
Linux 下是 AppImage，每一次启动时都需要在 terminal 敲击命令，而不是点击图标，所以可以自制 launch 文件。

1. icon: 首先下载好 Obsidian 的图标；
2. 新建 `Obsidian.desktop` 文件:

```
[Desktop Entry]
Name=Obsidian
Exec=/home/song/OneDrive/Desktop/Obsidian-0.13.14.AppImage
Icon=/home/song/Desktop/obsidian.png
Type=Application
StartupNotify=true
```
- `Exec` 指向应用文件
- `Icon` 指向应用图标

3. 修改权限：对文件 右键 >> 属性 (Property) >> 权限 (Permissions) >> 允许作为程序执行文件 (Allow executing file as program)，打勾。

4. 移动该文件到 `/usr/share/applications`

5. 便可以在应用列表下搜索到该应用

## 在 Ubuntu 20.04 安装 OneDrive 进行同步


### Install OneDrive on Ubuntu 20.04

可以跟着以下[教程](https://github.com/abraunegg/onedrive/blob/master/docs/ubuntu-package-install.md#distribution-ubuntu-2004) 在 ubuntu 20.04 上安装 Onedrive。


1. Update `/etc/apt/sources.list`

```bash
sudo gedit /etc/apt/sources.list
```

在 `/etc/apt/sources.list` 末尾添加一行:


```bash
deb https://download.opensuse.org/repositories/home:/npreining:/debian-ubuntu-onedrive/xUbuntu_20.04/ ./
```

2. Download and add the release key
   
```bash
wget https://download.opensuse.org/repositories/home:/npreining:/debian-ubuntu-onedrive/xUbuntu_20.04/Release.key
apt-key add ./Release.key
```

3. Update your apt package cache

```bash
sudo apt-get update
```

4. Install 'onedrive'

```bash
sudo apt install onedrive
```

5. auth the application

在命令行中输入 `onedrive` 然后打开最后列出的授权链接,在链接中同意便可。

![](https://www.moerats.com/usr/picture/OneDrive_bf(1).png)

![](https://www.moerats.com/usr/picture/OneDrive_bf(2).png)

## sync

### 完全同步

```bash
# sync all to /root/OneDrive or /home/USER/OneDrive
onedrive --synchronize
```

![](https://www.moerats.com/usr/picture/OneDrive_bf(3).png)


此后如果 `OneDrive` 网盘或者 `~/OneDrive` 文件夹里的文件/文件夹有变动，再执行该命令会进行双向对应的变动/同步。



### 选择性同步

如果你不想同步整个网盘，而是某个文件夹，比如 `Obsidian`，使用命令：

```bash
# 使用前提是 OneDrive 网盘和 /root/OneDrive 文件夹都有这个文件夹
onedrive --synchronize --single-directory Desktop/Obsidian
```

### 单向同步
在某些情况下(如备份网站数据)，可能只需要上传到 `OneDrive`。这样我们可以使用以下命令：

```
onedrive --synchronize --upload-only
```

该命令只会单向同步 `VPS` 的 `~/OneDrive` 文件夹，不受 `OneDrive` 网盘文件变动影响

更多同步，具体可参考[该文](https://jiumbk.com/zjjc/294/)。

## 卸载客户端

```bash
cd ~/onedrive
make uninstall
rm -rf ~/.config/onedrive
```


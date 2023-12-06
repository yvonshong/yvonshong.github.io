---
title: 从零开始 NanoPi R2S
date: 2023-05-16 00:00:00
categories: tech
tags: 
- openwrt
toc: true
---

半年前购置了软路由，最近才配置上，全当做个笔记。

<!-- more -->


# 硬件

- NanoPi R2S
- TF 卡（8G 以上就够了， Class 10 以上标准，更好的可以上 Industrial ）
- Type-C 电源线（无需支持快充标准）
- 10W 以上充电头

![NanoPi R2S](https://s2.loli.net/2023/10/30/vhUpS5CFyaXo7OZ.png)

# 刷系统

## 刷机工具

[win32diskimager](https://win32diskimager.org/)

## 固件

无需忍受百度云小水管： 官方固件 [Google Drive 下载链接](https://drive.google.com/drive/folders/1Ua3c8OBCylhe9b41e_QW42xRDWs3eLcw)


在 Windows 下以管理员身份运行 win32diskimager，在界面上选择你的 TF 卡盘符，选择解压后的固件文件，点击 Write 按钮烧写到 TF 卡。


刷机完成后将 TF 卡插入，接电，会自动启动系统。此时 NanoPi 正面 SYS 灯红灯闪烁。

## 连线

### 电脑直连

![modem-router-nanopi-pc](https://s2.loli.net/2023/10/30/liRkbNPfaBwSdDt.png)


modem-router-nanopi-pc

接线方式：原家庭路由和光猫的接线方式不变，R2S 的 WAN 口连接原家庭主路由的 LAN 口，R2S 无需设置，R2S 的 LAN 口连接电脑网口；

验证方法：电脑网卡设置成“自动获得IP地址”就可正常上网。

此方法可快速检测 R2S 是否存在硬件故障，用命令 `ping www.baidu.com` 检测是否正常联网，能联网成功即可说明硬件正常。

### 路由器直连


![modem-nanopi-router-pc](https://s2.loli.net/2023/10/30/HDKQ3cbNxSeZICy.png)

modem-nanopi-router-pc

R2S 的 WAN 口连接光猫，R2S 的 LAN 口连接原家庭无线路由器的任意一个LAN口；
 
设置步骤：

1. 光猫拨号用户：R2S 无需设置，接线就可正常上网。
2. PPPOE拨号用户：浏览器输入 `192.168.2.1` 登录 R2S 后台—网络—接口—WAN修改协议为 PPPOE，填入宽带账户密码即可。


# 系统设置

在电脑浏览器上输入以下网址即可进入FriendlyWrt管理页面:  

-   [http://friendlywrt/](http://friendlywrt/)
-   [http://192.168.2.1/](http://192.168.2.1/)
-   [http://[fd00:ab:cd::1]](http://[fd00:ab:cd::1])

以上是 NanoPi R2S 的 LAN 口地址，WAN 口会从你的主路由器动态获取IP地址。

## 安全性设置

以下设置事项非常建议在将 NanoPi-R2S 接入互联网之前完成，因为在空密码或弱密码的状态下将NanoPi-R2S接入互联网，极易受到网络攻击。

-   设置一个安全的密码

进入 系统->管理权 界面设置密码。

-   禁止从wan访问ssh，更换端口

进入 系统->管理权->SSH访问，将接口限制为 lan，将端口设置为其他非常用端口，例如 23333。


## 安装软件包
进入菜单”系统“-》”软件包“, 在界面上点击”okpg配置“按钮, 在新弹出的界面上, 更改/etc/opkg/distfeeds.conf的文件内容即可,  
比如要切换至国内腾讯源, 可以替换成如下内容, 然后点击 “保存” 按钮:

```bash
src/gz openwrt_base https://mirrors.cloud.tencent.com/openwrt/releases/22.03.2/packages/aarch64_cortex-a53/base
src/gz openwrt_luci https://mirrors.cloud.tencent.com/openwrt/releases/22.03.2/packages/aarch64_cortex-a53/luci
src/gz openwrt_packages https://mirrors.cloud.tencent.com/openwrt/releases/22.03.2/packages/aarch64_cortex-a53/packages
src/gz openwrt_routing https://mirrors.cloud.tencent.com/openwrt/releases/22.03.2/packages/aarch64_cortex-a53/routing
src/gz openwrt_telephony https://mirrors.cloud.tencent.com/openwrt/releases/22.03.2/packages/aarch64_cortex-a53/telephony
src/gz friendlywrt_packages file://opt/packages
```

通过命令行切换国内源:
```bash
sed -i -e 's/downloads.openwrt.org/mirrors.cloud.tencent.com/g' /etc/opkg/distfeeds.conf
opkg update
```


## 插件
### openclash

github vernesong O p e n / C l a s h WIKI

### 广告过滤

[AdGuardHome](https://github.com/rufengsuixing/luci-app-adguardhome)

### 解锁网易云灰色音乐

https://github.com/UnblockNeteaseMusic/luci-app-unblockneteasemusic

[netease-cloudmusic-history-version](https://blog.amarea.cn/archives/netease-cloudmusic-history-version.html) 下载  [2.9.5](https://d1.music.126.net/dmusic/cloudmusicsetup2.9.5.199424.exe)

### 挂载硬盘

1. 把移动硬盘连接NanoPi-R2S作为外接存储设备，将移动硬盘插入NanoPi-R2S的USB接口，在FriendlyWrt中点击“系统->挂载点”进入挂载点设置界面：  

    ![R2s-wrt-jellyfin-006.jpg](https://wiki.friendlyelec.com/wiki/images/7/78/R2s-wrt-jellyfin-006.jpg)

2. 在界面下方找到挂载点存储设备设置，点击“添加”按钮：  

    ![R2s-wrt-jellyfin-007.jpg](https://wiki.friendlyelec.com/wiki/images/7/79/R2s-wrt-jellyfin-007.jpg)
    
3. 在弹出的对话框中UUID一栏选中刚刚接入的移动硬盘 /dev/sda1（实际情况请根据自身设备选择，如硬盘有多个分区可能会显示sda1/sda2……等）：  
    ![R2s-wrt-jellyfin-008.jpg](https://wiki.friendlyelec.com/wiki/images/8/80/R2s-wrt-jellyfin-008.jpg)

4. 在挂载点一栏中使用自定义，填入要挂载到的目标目录，这里以/jellyfin/videos 目录为例，勾选上方的“已启用”，然后点击“保存”：  
    ![R2s-wrt-jellyfin-009.jpg](https://wiki.friendlyelec.com/wiki/images/8/81/R2s-wrt-jellyfin-009.jpg)

    ![R2s-wrt-jellyfin-010.jpg](https://wiki.friendlyelec.com/wiki/images/5/50/R2s-wrt-jellyfin-010.jpg)

5. 设置完后点击“系统->重启”重启NanoPi-R2S使挂载点生效：  
    ![R2s-wrt-jellyfin-011.jpg](https://wiki.friendlyelec.com/wiki/images/0/0b/R2s-wrt-jellyfin-011.jpg)

6. 重启后再回到“挂载点”界面可看到“已挂载的文件系统”中显示刚刚挂载的移动硬盘信息，即设置成功（以后需要再新增或删减编辑挂载点都可以在下面的“挂载点”设置中操作）：  **注：每次操作后都需要重启后才能生效**  
    ![R2s-wrt-jellyfin-012.jpg](https://wiki.friendlyelec.com/wiki/images/f/fa/R2s-wrt-jellyfin-012.jpg)

### Wake on LAN

https://pkgs.org/download/luci-app-wol

# Reference

- [friendlywrt wiki](https://wiki.friendlyelec.com/wiki/index.php/NanoPi_R2S/zh)
- [巴掌大小的 Nanopi R2S 软路由 固件分享和体验](https://zhongce.sina.com.cn/article/view/72480)

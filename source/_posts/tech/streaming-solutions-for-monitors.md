---
title: 串流拯救跨平台显示
date: 2025-06-18 16:37:32
categories: tech
toc: true
tags:
- moonlight
- streaming

---

用 Moonlight + Sunshine + 虚拟显示器，把 iPad 变成 Windows/Ubuntu 的无线扩展屏，效果媲美 Mac 随航。

<!-- more -->

# 需求：iPad 作为扩展显示器

一直苦于 iPad 没法作为 Windows/Ubuntu 笔记本的副屏，十分羡慕 MacBook 的随航（Sidecar）功能。手头这台 Surface Book 2 用了六七年了，一直没坏就一直没换，但出差时又特别想让 iPad 充当第二块屏幕。

# 之前踩过的坑

spacedesk 是一个免费方案，在 Windows 上安装服务端，iPad 安装客户端，通过局域网把 iPad 变成副屏。听起来很美好，实际体验却是：

- 延迟高到感人，拖动窗口都有明显的拖影
- 画质模糊，文字锯齿严重
- 偶尔断连，稳定性差

跨平台键鼠共享（如 Barrier、Input Leap）解决了多设备键鼠共用的问题，但本质上 iPad 屏幕依然只是触控板，无法真正作为扩展显示输出。

Duet Display 效果相对好一些，但需要付费订阅，且 Linux 支持有限。

# 终极方案：Moonlight + Sunshine + 虚拟显示器

前段时间看到有人把 Windows 串流到 Apple Vision Pro 上，才重新注意到 Moonlight 这个工具。试了之后发现延迟和画质都远超 spacedesk，完全是另一个量级。

## Moonlight 和 Sunshine 的原理

**NVIDIA GameStream** 是 NVIDIA 官方内置于显卡驱动的串流协议，专为低延迟游戏串流设计，利用显卡硬件编码（NVENC）在本地网络上实现高帧率、低延迟的视频传输。

**Moonlight** 是对这套协议的开源逆向实现，作为客户端运行在 iPad/iPhone/Android/PC 上，接收并解码串流画面。

**Sunshine** 则是完全开源的串流服务端，不依赖 NVIDIA 官方驱动里的 GameStream，同时支持 NVIDIA / AMD / Intel 显卡以及 Linux/Windows/macOS，功能上可以完全替代官方 GameStream 服务端。

两者配合，就能把主机屏幕（或某一块特定显示器）以极低延迟无线串流到 iPad 上。

## 虚拟显示器：让系统"以为"接了第三块屏

串流本身只是把画面传输过去，但要让 iPad 显示一块**独立的扩展屏**而不是镜像主屏，操作系统必须真的输出一路独立的显示信号。这就需要虚拟显示器。

#### 方案一：物理欺骗器（HDMI/DP Dummy Plug）

最简单粗暴的方案：买一个 HDMI 或 DisplayPort 欺骗器（Dummy Plug），插入显卡的空闲接口。这个小东西内置了 EDID 芯片，会让显卡误以为真的接了一台显示器，系统因此会输出一路真实的显示信号。

优点是即插即用，对系统没有任何侵入；缺点是需要一个空闲的视频接口，且分辨率受 Dummy Plug 内置 EDID 限制。

### 方案二：软件虚拟显示器（Linux X11 + xrandr）

在 Linux + X11 + NVIDIA 独显环境下，可以通过修改 X11 配置，让 NVIDIA 驱动强制识别一个本不存在的显示接口，然后用 `xrandr` 和 `nvidia-settings` 动态设置分辨率和位置。

**第一步：写入 X11 配置**

在 `/etc/X11/xorg.conf.d/30-virtual-display.conf` 中添加：

```
Section "Device"
    Identifier     "Device0"
    Driver         "nvidia"
    VendorName     "NVIDIA Corporation"
EndSection

Section "Screen"
    Identifier     "Screen0"
    Device         "Device0"
    Option         "ConnectedMonitor" "DP-4, HDMI-0, DP-0"
EndSection
```

`ConnectedMonitor` 强制告诉 NVIDIA 驱动：DP-4、HDMI-0、DP-0 这三个接口都已连接显示器。其中 DP-0 实际上并没有物理连接，这样就创造出了一块虚拟的显示输出。写入后需要重启才能生效。

**第二步：用脚本动态开关虚拟屏**

重启后用 `nvidia-settings` 设置 MetaMode，把虚拟屏放到主屏右侧：

```bash
DISPLAY=:0 nvidia-settings -a "CurrentMetaMode=\
  DP-4: 1920x1080 +0+0, \
  HDMI-0: 1366x768 +1920+0, \
  DP-0: 2388x1668 +3286+0"
```

这里 `2388x1668` 是 iPad Pro 的原生分辨率，放在主屏和副屏的右侧（`+3286+0`）。

完整的开关脚本 `virtual_display.sh`：

```bash
#!/bin/bash
VIRTUAL_OUTPUT="DP-0"
PRIMARY_OUTPUT="DP-4"
SECONDARY_OUTPUT="HDMI-0"
WIDTH=2388
HEIGHT=1668

turn_on() {
    DISPLAY=:0 nvidia-settings -a "CurrentMetaMode=\
      ${PRIMARY_OUTPUT}: 1920x1080 +0+0, \
      ${SECONDARY_OUTPUT}: 1366x768 +1920+0, \
      ${VIRTUAL_OUTPUT}: ${WIDTH}x${HEIGHT} +3286+0"
}

turn_off() {
    xrandr --output "${VIRTUAL_OUTPUT}" --off
}

case "$1" in
    on)  turn_on  ;;
    off) turn_off ;;
esac
```

**第三步：配置 Sunshine 输出到虚拟屏**

在 Sunshine 后台（`https://localhost:47990`）的 **Configuration → Audio/Video** 中，将 **Output Name** 设为 `0`（对应 DP-0），保存并重启 Sunshine 服务。

**第四步：iPad 上打开 Moonlight 连接**

局域网内 Moonlight 会自动发现主机，连接后 iPad 显示的就是 DP-0 这块虚拟扩展屏。把主屏上的窗口往右拖，就会滑入 iPad 屏幕——和 Mac 随航体验完全一致。

## 效果

延迟在局域网 Wi-Fi 下基本感知不到，画质清晰，拖动窗口流畅。对比 spacedesk 简直是降维打击。唯一的前提是主机需要有 NVIDIA 显卡（或支持 NVENC 的 AMD/Intel 显卡），以及安装 Sunshine 服务端。

---
title: All-in-One HomeLab 和多设备多系统远程方案
date: 2025-12-17 07:00:00
categories: tech
toc: true
tags:
- homelab
---


# 🏡 打造 All-in-One 智能家庭实验室 (Homelab)

之前一直用自己的笔记本电脑跑脚本，总是受掣于电脑关机，ip，网络等等问题，于是就会想要有一台自己的服务器，搞过一段时间GCP，还是因为需求不高放弃了服务器方案，用我之前一台闲置的零刻 Mini 主机为核心，结合家里的软路由，构建了HomeLab的体系，来实现了一些我（创造出来）的需求。


* **智能控制：** 沿用之前给mini主机的 **小米智能开关**，来实现远程的开关上下电，出问题可以硬断电重启。
* **关键配置：** BIOS 设置了 **“上电自启”**，确保断电恢复后无需手动干预。同时，加装一个USB底部风扇散热，来保证长期运行。

## 💻 系统方案与核心功能栈

用 **Windows 系统** 作为 Homelab 的基础操作系统。虽然很多服务在 Linux 上更原生，但 Windows 提供了便利的远程可视化桌面（RDP），容器化部署的基础环境 DockerHub Desktop，以及我可以用Windows Subsystem Linux，WSL2, 则可以既要又要还要，还很方便使用 smb 构建家庭轻量 NAS。
* 对于一些自己开了发的浏览器自动化任务，由于 WSL 下的 Selenium 存在一些兼容性 Bug，也保留了 **Windows 系统下的 Python 环境**。

## 🚀 DockerHub 核心功能一览
DockerHub中，包含以下一些常用的镜像。

| 服务名称 | 描述 |
| --- | --- |
| `qbittorrent` | 专业的下载工具，提供强大的资源获取能力。 |
| `qd today` | 自动签到服务，管理各种日常网络任务。 |
| `openlist` | 开源版本 Alist 网盘聚合。 |
| `homeassistant` | 智能家居中枢，接入小米开关等设备，实现全屋自动化。 |
| `immich` | 私有照片云服务，取代公有云，保护个人隐私。 |
| `npm` | 提供 nginx实现反向代理。 |
| `cloudflared` | Cloudflare Tunnel 服务，用于安全地将选定服务暴露到公网，无需公网 IP，配合nginx打洞。|


## 🗄 SMB 轻 NAS

宿主机是 Windows，最简单的文件共享方式莫过于系统原生的 SMB (Server Message Block) 协议。不需要像 TrueNAS 那样直通硬盘，利用 Windows 的“高级共享”功能，配合局域网和 TailScale，就能实现一个内网跑满带宽，外网随时存取的轻量 NAS。
开启共享：右键点击想要共享的大容量硬盘或文件夹（例如 D:\Downloads 或 E:\Movies）。选择 属性 (Properties) -> 共享 (Sharing) -> 高级共享 (Advanced Sharing)。勾选 “共享此文件夹”。点击 权限 (Permissions) -> 添加 guest -> 给予 完全控制 (Full Control) 或 读取 (Read) 权限。网络发现： 确保当前网络连接属性为“专用网络”，并在“网络和共享中心”中开启了“启用网络发现”和“启用文件和打印机共享”。

多端挂载与访问，有了 SMB，家里的所有设备都能极其丝滑地访问 Homelab 里的资源：

|设备端|连接方式|用途|
|---|---|---|
|MacBook|Finder -> Cmd + K -> 输入 smb://192.168.xx.xx | 也就是前面提到的“轻负载工作流”，直接挂载远程磁盘剪辑视频或整理照片。
|iOS / iPad|自带“文件”App -> 连接服务器 或 nPlayer / InfuseiPad | 躺平看片神器，Infuse 配合 SMB 刮削海报墙体验极佳。|
| 电视/盒子 | Kodi / 这里的 Android TV 播放器 | 直接读取 PC 下载好的 4K 原盘电影，不占电视存储。|
|远程 NAS (配合 TailScale)|这是该方案的杀手锏。因为我在 Homelab 和 MacBook 上都装了 TailScale，在外网环境下，我只需要将 SMB 地址中的局域网 IP 换成 Homelab 的 TailScale IP，地址示例：smb://100.x.y.z (Tailscale IP)|效果： 即使人在咖啡馆，也能像在局域网一样挂载家里的硬盘，虽然速度受限于上行带宽，但用来存取文档、看非高码率视频完全够用，真正实现了私有云盘。|

## 💖 心跳监控
让 Homelab 保持“心跳”服务的稳定性至关重要。我使用 **`healthychecks.io`** 配合 **开机自启的 Python 脚本** 来实现心跳检测（Hearbeat）：

* 如果系统在预定时间内未收到信号，则会触发警报，发邮件提醒我主机或服务可能宕机。healthychecks可以设置一定的宽容时间，比如正常60s心跳，超过5min没有收到才报警。
* 脚本在 Homelab 启动后自动运行，并定期向 `healthychecks.io` 发送信号。文件后缀名从 .py 改为 .pyw（例如 heartbeat.pyw），这样它就会在后台静默运行。Win + R 键打开“运行”框,输入 `shell:startup`， 把.pyw创建的快捷方式丢到这个文件夹即可。

```python
import time
import requests
import datetime

# ================= 配置 =================
# 替换成你在 healthchecks.io 获取的那个 URL
HEARTBEAT_URL = "https://hc-ping.com/你的UUID-xxxx-xxxx"
CHECK_INTERVAL = 60  # 每60秒报一次平安
# =======================================

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    print(f"[{get_current_time()}] 💓 看门狗已启动...")
    print(f"   - 机制：每 {CHECK_INTERVAL} 秒向服务器发送一次心跳")
    print(f"   - 效果：如果脚本停止（断电/关机）超过设定时间，服务器将给你发邮件")
    
    while True:
        try:
            # 1. 发送“活着”的信号 (相当于“重置定时器”)
            # timeout=10 防止网络不好时脚本卡死
            requests.get(HEARTBEAT_URL, timeout=10)
            print(f"[{get_current_time()}] ✅ 咚-咚 (心跳发送成功，炸弹倒计时已重置)")
        
        except requests.exceptions.RequestException as e:
            # 网络不通时，只是打印错误，不要退出循环，等待网络恢复
            print(f"[{get_current_time()}] ⚠️ 网络连接失败: {e}")
            
        except KeyboardInterrupt:
            print("\n🛑 用户手动停止脚本 (警告：这会导致服务器误报关机！)")
            # 如果你正常关闭脚本，不想触发报警，通常需要去网页上点“暂停”，或者发送一个特殊的“完成信号”
            break
            
        # 2. 休息
        time.sleep(CHECK_INTERVAL)
```


# 🌐 网络篇：家庭软路由和远程方案

## 🛜 小米 BE7000 软路由

之前选择小米路由器 BE7000，是因为他是仅次于万兆路由器的次旗舰，wifi7+usb口，足够满足我的需求，之前一直用USB的U盘作为轻NAS，后来将NAS功能挪到homelab电脑上，U盘只供路由器内部的docker使用，跑软路由服务。

解锁 SSH 发烧模式： 为了获得完整的控制权，我参考了 [教程](https://www.gaicas.com/xiaomi-be7000.html) 解锁了 SSH。

常用连接命令（备忘）（因为内部rsa协议较老）：

```Bash
ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedKeyTypes=+ssh-rsa root@192.168.31.1
```
然后安装 [shellclash](https://blog.qust.me/be10000)，等以后买个双网口的再考虑把软路由集成到 HomeLab 吧。


## 🛰️ 远程访问方案

Homelab 必须有便捷安全的远程访问能力。我的方案结合了 TailScale 的零配置 VPN 和传统的远程桌面。


### 🛡️ 核心远程方案

1. **TailScale 零配置 VPN 远程**：这是我的首选方案，它在所有设备间建立安全、加密的网状网络，无需复杂的端口转发配置。网络内部可以 ssh+FTP，在这一点上就可以拓展出很多很多东西。
2. **Windows RDP 可视化**：通过 TailScale 网络，我可以安全地使用 **Windows 远程桌面（RDP）**，获得完整的可视化操作界面。其他系统如 macOS（Windows应用），Ubuntu（Remmina）都有对应的软件，只需要使用 TailScale 应用里面显示的设备局域网 IP。

### ✈️ TailScale Exit Node：实现免费版的“穿梭“

使用国内 IP 打开某些政府app网页。

* 在 Homelab 上TailScale配置 **Exit Node**。
* 在 **TailScale Admin Web** 界面授权该 Exit Node。
* 在随身携带的 **Client 端（如 MacBook）** TailScale 上开启使用该 Exit Node。
* 这样，我的设备流量就能通过家里的 Homelab 路由，从而实现**穿梭回国**的效果，享受国内网络服务。

## 🍎 多系统融合
从“重装”到“轻盈”，之前我不得不随身携带一台**高性能、高功耗的笔记本**拯救者 Legion（Ubuntu+Win 双系统，64GB 内存 + 4TB SSD外挂硬盘），不仅机身重，170W Type-C 充电器也成了负担，常常在咖啡馆遇到没插座的尴尬。

现在，我的移动工作流已经彻底转型为：**MacBook + 远程方案**。

1. **轻负载工作流：** **MacBook 拥有无敌续航**，我无需再担心电源问题。它可以轻装上阵，将高负载任务全部交给家里的 Homelab 或者 Ubuntu 笔记本。
2. **原生环境满足：** 通过 **VS Code Remote + RDP**，我的 MacBook 小硬盘不必再安装虚拟机，就能随时连接到 原生 **Ubuntu** Legion 笔记本或 Windows+WSL HomeLab 环境。
3. **可视化与 AI 赋能：**
    * **TailScale+RDP** 完美解决了云服务器难以实现的可视化问题，方便进行图形化代码调试。
    * **VS Code Remote** 也让我能更便利地本地调试，也能使用 **Gemini** 等 AI 插件，不需要靠 RDP来传递画面。
4. **iPad 随航显示器：** 配合 iPad 作为随航显示器，移动工作站的效率也得到了极大的提升。

---



# ✅️ TODO

Homelab 是一个 **“有生命周期的系统”**。目前的阶段是“可用且稳定”，未来的方向是“影音和数据备份”。

- 后续预期搞个双网口实现低功耗的server。
- 软路由买更好的梯子，可能家里搞一搞IPTV。
- 目前组NAS和RAID的需求不强，后续可能搞一个家人数据备份功能。

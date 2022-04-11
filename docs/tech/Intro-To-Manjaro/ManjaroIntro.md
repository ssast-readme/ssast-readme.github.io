# Manjaro 系统日常使用入门

作者：林地宁宁



## Arch Linux 简介

<center>
    <img alt="archlinux-logo" src="/tech/Intro-To-Manjaro/img/archlinux-logo.png" width="75%"/>
</center>

常听人说 Arch Linux 系统（以下简称 Arch）是一款自由度极高的 Linux 发行版，在维基百科上给出的描述如下：

> Arch Linux 是一款基于 x86-64 架构的 Linux发行版。系统主要由自由和开源软件组成，支持社区参与。系统设计以 KISS 原则（保持简单和愚蠢）为总体指导原则，注重代码正确、优雅和极简主义，期待用户愿意去理解系统的运作。Arch Linux 采用pacman作为默认的软件包管理器。

通常在我们的日常生活中，我们所最多接触的或许是 **Ubuntu** 系统，而这得益于 Ubuntu 所提供 GNOME 桌面环境，毕竟不是每个新生代码农都能在一开始接受全命令行的界面。当然，Ubuntu 能够作为目前最多用户的 Linux 版本，与其自身的稳定性有关。笔者在此也不再过多赘述 Ubuntu 的相关内容，而是转而关注 Arch 系统。

**Arch 为什么好？这和 Arch 的高自由度摆脱不了干系**。Arch 的设计初衷，就是为了 Do-It-Yourself，而这恰好劝退了所有刚入坑 Arch 的萌新——原生的 Arch 几乎只有必须的内核以及通用驱动，要想进一步 DIY，则需要在纯粹命令行模式下安装专有驱动并搭建桌面环境，其繁琐程度足够让一个老 Arch 玩家都吃上一壶。在极客圈里，完完整整地安装一个 Arch 系统，甚至可以作为对萌新的一个吹牛的谈资。

尽管 Arch 的安装如此复杂，一旦克服了上面这些过程，留下来的就是一个纯净的、完全掌握的 Arch 系统，而这让不少极客趋之若鹜。

虽然 Ubuntu 提供了一个预先配置好的系统，但是其也正在肉眼可见的臃肿起来。此外，如果想提高自己对于 Linux 系统的认识，加入 Arch 教或许能让你看起来更 Cool，更 Pro 一点。

在这里，笔者**推荐以下人群可以尝鲜 Arch 系统**：

- 不懂 Linux 系统，但又想尝试使用 Linux 作为日常机，并且需要有 DIY 能力以及探索精神的萌新
- 对 Linux 系统有所接触，但想有一个美观的桌面环境、干净的内置环境的系统，并足够支撑日常使用的人
- 痛恨 Windows 的环境配置的人
- 日常 Linux 服务器开发的人
- 厌烦 Ubuntu 虚拟机的人
- 希望软件保持最新版本的人
- 对 Redhat 及 Debian 系感到不满的人



## 初识 Manjaro

<center>
    <img alt="manjaro-logo" src="/tech/Intro-To-Manjaro/img/manjaro-logo.png" width="75%"/>
</center>

说了这么多关于 Arch 的事情，也该将话题转向本篇文章的主角——Manjaro 系统，在维基上的描述如下：

> Manjaro Linux（或简称 Manjaro）是基于 Arch Linux 的 Linux 发行版，使用 Xfce 、GNOME和 KDE Plasma 作为默认桌面环境，和 Arch 一样，采用滚动更新。其目标是为 PC 提供易于使用的自由的操作系统。

如果说 Arch 是没有躯壳的自由的灵魂，那 Manjaro 就是一个带着自由灵魂的健全人。Arch 系统繁杂的配置显然不能让所有人都满意，因此 **Manjaro 作为基于 Arch 的最流行发行版，在最大程度保留 DIY 自由度的情况下，简化了 Arch 的配置流程**。

在写下这篇文章的时候，笔者已经将 Manjaro 系统当作日常主力使用了 2 年时间，下面是笔者个人总结出的有关于 Manjaro 的优缺点：

- **优点**：
    - 完善且纯粹的 Linux 系统，再也不用担心 WIN 配环境炸裂惹，轻松种码和炼丹
    - Pacman 保证所有软件和库都在最新版本
    - 在 wine 加持下，可以使用许多常用的 WIN 软件，包括 QQ、微信、QQ音乐和腾讯会议等
    - 许多常见软件都有 Linux 版本，足以满足日常使用，例如 Chrome、Edge、网易云音乐、vscode 和 JetBrains 旗下产品等
    - 各种桌面环境自定义，让你的桌面极客风十足
    - ArchWiki 专治疑难杂症，关于系统相关的问题几乎都能在 ArchWiki 找到解决方案
    - **能更加熟悉 Linux 系统，再也不怕老板给你 Linux 服务器而你只会查 CSDN 惹**
- **缺点**：
    - 经常性的保持软件和库在最新状态，意味着经常性的依赖炸裂，甚至有可能导致炸机，因此**日常性的系统备份还原必不可少，更需要有一颗强大的心脏**
    - Linux 版本的商业软件，或多或少沾点 bug，需要用户有耐心去解决
    - wine 软件不是十全十美的，有些 WIN 软件也就是个勉强能用的程度
    - 不适合进行游戏，尽管通过 Steam 的 Proton 以达到游戏的目的

看完上述优缺点后，如果你已经下定决心尝试 Manjaro 的话，那就继续往下看吧。



## 安装 Manjaro

这一节，笔者将简单描述 Manjaro 的安装过程。相关内容参考于[官方用户手册](https://en.osdn.net/projects/manjaro/storage/Manjaro-User-Guide.pdf)，如有疑问，可自行查阅相关内容。

此处我也推荐优秀入门博文 [Manjaro KDE 安装配置全攻略](https://zhuanlan.zhihu.com/p/114296129)。

### 下载镜像

在 Manjaro 的官网的[下载页面](https://manjaro.org/download/)中，我们可以下载 Manjaro 的 ISO 镜像，目前可供选择的有 3 个版本，区别大致如下：

- Xfce：轻量级桌面环境，资源消耗少
- KDE Plasma（推荐）：功能完善，自定义程度高的桌面环境，资源消耗大
- GNOME：GNU 的桌面环境，也是 Ubuntu 默认的桌面环境，资源消耗中等

选定了想要的桌面环境后，下载对应的 ISO 即可。

<center>
    <figure>
    	<img alt="kde-example" src="/tech/Intro-To-Manjaro/img/kde-example.png" loading="lazy" />
        <figcaption>KDE Plasma 样式</figcaption>
    </figure>
</center>




### 烧录镜像

考虑到大多数同学不会使用 CD/DVD 烧录，因此此部分留于官方用户手册中自行查阅。我们将使用 USB 进行烧录。

首先，我们要准备 1 个**闲置的 USB**，将镜像烧录进去。**注意，此过程会清除 USB 上的内容！**

我们选择烧录软件 [Rufus](https://rufus.akeo.ie/) 或者 [Etcher](https://etcher.io/)。

对于使用 USB 的 Windows 用户来说，Rufus 是官方强烈推荐的。在挂载 USB 设备后，在设备菜单中选择要使用的 USB Drive。然后，选择所下载的光盘镜像并开始烧录。之后，在出现的窗口中选择 DD Image 即可。

对于 Etcher 而言，操作更加简单，只需要选择镜像和 USB Drive 进行烧录即可。

以上关于烧录 Manjaro 镜像的内容，也可以在百度等搜索引擎中查询到相关信息。

### 修改 BIOS 启动项顺序并以 USB 启动系统

这一步需要我们重启电脑，并进入 BIOS 界面，将 USB 启动项优先级调至最高，使得我们可以通过 USB 方式启动镜像中的安装系统。

具体步骤因各机差异，还请各位读者自行百度解决。

### 安装界面

成功进入 USB 的安装镜像后，将会自动进入 Installer。如果没有进入，也可以点击桌面图标进入。

### 兼容 Windows 双系统的安装

此处，我默认各位读者都有 Windows 系统，且 Manjaro 需要作为第二系统安装。

安装之前，需要在磁盘上预留足够的空间作为 Manjaro 安装的空间。之后的步骤跟随 Installer 进行即可。

如果曾经安装过 Ubuntu 系统的，这件事情不难。但是如果是一个萌新，在这里受限于篇幅，并且秉持着不重复造轮子的原理，笔者只附上几篇相关的安装教程，对安装过程有疑问者可自行参考。

- [知乎-保姆级 Manjaro 双系统安装教程](https://zhuanlan.zhihu.com/p/376787855)
- [简书-Manjaro 安装以及配置](https://www.jianshu.com/p/2ec565f17e00)
- [官方用户手册的第2章](https://en.osdn.net/projects/manjaro/storage/Manjaro-User-Guide.pdf)

这一步与安装 Ubuntu 时候类似，不过 Manjaro 会自动配置 GRUB 做到双系统引导（如果无法双系统引导，请阅览官方用户手册第 2 章相关内容）。如果嫌麻烦可以直接采用 Alongside 方法安装，但是更推荐使用自定义分区的方式安装，毕竟宗旨就是自己的电脑自己掌握！

分区方案要讲起来又是很大的东西呢！这里笔者建议同学们有兴趣了解一下“Linux 分区方案”，此处提供一些链接：

- [Linux 分区的那些方案](https://www.linuxprobe.com/forthe-linux-partition.html)
- [Linux 磁盘分区方案](https://www.cnblogs.com/hanrp/p/12551695.html)



## 基本配置

哦吼！现在如果你已经克服最大的安装难题来到此处，那么剩下的问题对你来说一定不是问题惹。

### 更换国内源（推荐）

```bash
sudo pacman-mirrors -c China
```

### 显卡驱动

Manjaro 默认会使用开源的显卡驱动 Nouveau，但开源驱动意味着适配性肯定不如闭源驱动，要想炼丹的话，就一定要配置闭源驱动。

如果在安装过程中已经选择了使用 Proprietary Graphic Driver 的话，就可以跳过这一步辣。

如果之前没有跳过，则需要进入“设置”界面中，选择

对于 A 卡用户，有需求的同学就查阅一下万能的 ArchWiki 中 [AMDGPU](https://wiki.archlinux.org/title/AMDGPU) 页面吧。

### AUR 包管理工具

Pacman 十分强大，不过为了更好的利用 AUR（Arch User Repository，[Wiki](https://wiki.archlinux.org/title/Arch_User_Repository_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))，[入口](https://aur.archlinux.org/)） 库中已有的包，因此市面上诞生出许多包管理工具：

- yay
- yaourt
- aurman
- pakku

这里推荐安装 yay 工具为例子：
```bash
sudo pacman -S --needed git base-devel yay
```

之后在日常生活中，我们就不直接调用 `sudo pacman` 命令来管理包，而是用 `yay` 直接平替。

### 输入法配置

Manjaro 上的输入法配置，根据用户的选择不同，有许许多多花样，在这里想把输入法配置写清楚，再考虑到各个输入法的优缺点，几乎可以再写一篇新文章了。

KDE 桌面推荐使用 fcitx5 或者 fcitx 作为输入法框架，GNOME 桌面用 IBus 更稳定。

因此在入门篇就列出几个经典输入法的安装教程，供同学们去自行参考并选择：

- [默认 fcitx5 输入法与美化](https://www.cnblogs.com/fatalord/p/13850072.html)
- [fcitx 的多种输入法](https://zhuanlan.zhihu.com/p/468429000)
- [IBus 配置](https://linuxacme.cn/559/)

输入法种类繁多，遇见合适的就好。个人目前使用默认的 fcitx5 + Material 皮肤。

<center>
    <figure>
    	<img alt="fcitx5-material" src="/tech/Intro-To-Manjaro/img/fcitx5-material.png" />
        <figcaption>Fcitx5 + Material 输入法样例</figcaption>
    </figure>
</center>



## 日常使用经验

经过漫长的配置时间，我们的 Manjaro 系统终于可以正常使用了！

下面，笔者将总结一些 Manjaro 日常使用经验和踩坑指南。

### AUR 是你最好的朋友

如果用 Arch 系统却不用 Pacman 及 AUR 库，那你的 Arch 之旅便是失败的！

在找寻需要的软件或者库之前，先去 [AUR](https://aur.archlinux.org/) 中搜索一下相关内容。在**大多数情况**下，**AUR 中都能够直接找到所需要的内容**，许多无私奉献的人会帮你打包好你所要的软件包。

只有实在找不到时，我才会选择自行编译或者安装。当然，也希望同学们能参与到 AUR 的建设中，把自己的痛苦经历整理起来，将来便能减少别人的苦痛。

### ArchWiki 是你最好的老师

Arch 的特色之一就是，**几乎任何你能想到的问题，都有人在 ArchWiki 上建立页面，并给出当前的一些解决方案**。一些国人常见问题上，甚至有中文页面。在 Arch 界，我们提到维基，通常就是指 ArchWiki 辣。

因此，想问问题前，先去搜一搜 ArchWiki 吧！

### 更新有风险，升级需谨慎

Arch 系统一向偏好将软件和依赖都升级到最新版本，这会让 Ubuntu 用户早期难以适应。每隔一两周，通常就能收到多达几个 G 的更新内容。

尽管升级软件包在 Arch 系中是常规操作，但笔者还是在这里提醒各位——**升级前一定要备份，这是笔者踩过的最大的坑，尤其是与内核和驱动相关的更新，更要小心谨慎**。

**你永远不知道这次升级会不会崩掉你哪个部分**。如果只是少数几个软件无法运行，兴许还是小事。倘若是网络模块、显卡驱动甚至是内核崩了，那可有的苦受了。

关于备份相关软件以及临时回退软件版本，在下面的“日常使用软件”一节中会涉及。

### 忍一忍风平浪静

软件追求最新版本的特性，导致 Manjaro 上一些软件不是十全十美的。作为对开源者的感谢，在使用 AUR 中软件时，我们应常怀**感恩**的心，多对其缺陷功能发 issue，并准备时刻容忍他的小缺漏。

这才是一名具有良好素质的码农该做的事。



## 日常使用软件

这一节我来总结一下个人日常所使用的软件。目前笔者能够将 Manjaro 系统机作为主力，也多亏于其丰富的软件生态。

当然，软件是无穷无尽的，这里笔者只介绍一些同学们热点关注的软件。

### zsh

如果你曾经是 Mac 用户，那你对 zsh 应该不会陌生。zsh 可以提供了比 bash 更加丰富的功能，例如命令自动补全，git 插件和高光等。

zsh 的配置此处建议自行搜索相关资料，此处提供两个参考：

- [Archlinux zsh 安装配置](https://ulomo.github.io/2019/04/25/Archlinux-zsh%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE/)
- [Manjaro终端美化](https://segmentfault.com/a/1190000022863791)

### 浏览器

通常情况下，开源的 firefox 浏览器会作为默认浏览器。当然，我们也可以换 Chorme 或者 Edge 来进行跨平台同步。

```bash
# chrome
yay -S google-chrome

# edge
yay -S microsoft-edge-stable-bin
```

### 腾讯系软件

腾讯系软件在日常生活中不可或缺。值得注意的是这些软件并没有 Linux 版本，或者其 Linux 版本十分复古难用，因此我们会使用 [wine](https://wiki.archlinux.org/title/Wine_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 或者 [deepin-wine](https://wiki.archlinux.org/title/Deepin-wine) 容器来运行。

下面是具体参考资料：

- [QQ/TIM ArchWiki](https://wiki.archlinux.org/title/Tencent_QQ_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
- [WeChat ArchWiki](https://wiki.archlinux.org/title/WeChat_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
- [腾讯会议-bin](https://aur.archlinux.org/packages/wemeet-bin)
- [腾讯会议-wine](https://aur.archlinux.org/packages/com.tencent.meeting.deepin)

### 文档编辑

文档编辑目前首推金山 WPS 套装，其他的用起来都不太舒服。

具体参见 [WPS](https://wiki.archlinux.org/title/WPS_Office_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 的维基页面。

TL;DR：
```bash
yay -S wps-office-cn wps-office-mui-zh-cn ttf-wps-fonts
```

### Markdown 编辑器

自从 Typora 收费后，市面上能打的免费 Markdown 编辑器就不多了，这里推荐其收费前最后的免费版。

```bash
yay -S typora-free
```

### Latex 编辑

Latex 还是逃不掉 Tex Live 的统治。当然，也可以用 Docker 自己搭一个 Overleaf，或者使用第三方提供的 Overleaf 服务。

具体参见 [Tex Live](https://wiki.archlinux.org/title/TeX_Live_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 的维基页面和 [TexStudio](https://archlinux.org/packages/community/x86_64/texstudio/) 软件包。

### 听歌

许多歌曲软件都能在 AUR 上找到现成的软件，下面列举了网易云音乐和 QQ 音乐的安装：
```bash
# 网易云音乐
yay -S netease-cloud-music

# QQ音乐
yay -S qqmusic-bin
```

### Docker

在 Linux 系统上的好处就是可以随心所欲的使用 Docker。具体请参考 [docker](https://wiki.archlinux.org/title/Docker_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)) 的维基页面。

使用 docker 搭建环境后，再也不用怕系统变得乱糟糟惹。

### 代码编辑

vscode 和 JetBrains 全家桶足够满足日常的使用需求。具体安装可参考：

- [vscode ArchWiki](https://wiki.archlinux.org/title/Visual_Studio_Code_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))
- [JetBrains Toolbox](https://aur.archlinux.org/packages/jetbrains-toolbox)：使用 Toolbox 来管理安装 JetBrains 全家桶

### 系统备份

为应对 Manjaro 中随时可能产生的炸机风险，经常做备份是一个良好的习惯。

市面上的备份软件非常多，这里只推荐一个 TimeShift。具体的配置和使用方式可以参考：

- [知乎-TimeShift：提前不备份，滚挂徒伤悲](https://zhuanlan.zhihu.com/p/346602946)



## 系统主题美化（KDE）

KDE 桌面的美化十分简单，例如：

- **主题更换**：在“设置”中切换到“主题”，便可以在 KDE Store 中选择自己想要的主题，甚至可以模仿 Mac、Win10 和 Win11 等。
- **桌面部件**：在桌面上右键后，可以添加小部件并移至桌面上。小部件也可以通过在线方式获取。
- **背景更换**：KDE 的桌面背景可以通过在桌面右键，并选择对应选项后更换。当然，如果你的 Steam 账号拥有 Wallpaper Engine 这款知名的动态壁纸软件，你也可以安装 [wallpaper-engine-plugin](https://github.com/catsout/wallpaper-engine-kde-plugin)，或者直接在 KDE Store 中选择安装此插件并配置后，即可调用 Wallpaper Engine 中的动态壁纸。



## 笔者杂谈

**将 Linux 系统当作日常主力机，这是需要勇气的**。Linux 的操作和 Windows 截然不同，而且 Linux 玩起来比 Windows 更容易玩崩。这在一开始的适应期，往往会给萌新带来压力。但是“有压力才能蒸出好排骨”，当我们渡过了这段“磨合期”，你就能发现自己对于 Linux 系统的了解突飞猛进，同时也对操作系统有了更加深刻的理解。

笔者写下这篇文章，更是希望将自己在走向 Manjaro 中所经历的流程，以及遇到的各种坑都记录下来，以供后人能在我的覆辙上更快的进步。

当别人还在 Windows 上捣鼓环境配置的时候，我只需要敲两行命令，就能将环境完美的装好，这或许就是我最初选择转向 Linux 的最大原因。

<center>
    <figure>
        <img alt="my-desktop" src="/tech/Intro-To-Manjaro/img/my-desktop.gif" loading="lazy" />
    	<figcaption>笔者的动态桌面</figcaption>
    </figure>
</center>

事实上，在使用 2 年 Manjaro 之前，我曾将 Ubuntu 作为主力机使用了将近 1 年。个人对 Ubuntu 算不上喜欢，总觉得它差了些什么东西，可能是自由度不够，也可能是界面不美观，或者是软件管理稀烂。但这些不协调感在我投入 Manjaro 怀抱以后便消失了。或许在真正使用 Arch 的大佬面前，我这种 Manjaro 仍然是小菜鸡，但这并不妨碍我对这款系统的喜爱，毕竟它让现在的我非常满足惹。

唯一美中不足的是，Linux 玩游戏的体验十分之差，这还是让我很苦恼的，毕竟自己还是半个 Gamer。好在 Manjaro 中内置了 Steam，再加上 Beta 版的 Proton 技术，让大多数 Steam 游戏都能在 Linux 上运行。尽管这些游戏的运行性能还是很差，但这还是让我看到了希望，说不定未来就能真正的在 Linux 上享受到完美的游戏体验了。

闲话不多说了，如果各位同学对上面的过程还有什么问题，或者想就相关内容介绍自己的经验，欢迎联系科协！

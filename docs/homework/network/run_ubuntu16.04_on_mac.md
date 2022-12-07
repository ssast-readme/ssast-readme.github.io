# Apple Silicon Mac配置Ubuntu16.04

> 作者：kirino
>
> 联系方式：he-jx@mails.tsinghua.edu.cn

计网的router大作业需要在Ubuntu16.04上运行，**对Mac用户，特别是使用Apple Silicon的用户十分不友好**。

一是使用16.04的Ubuntu本身就非常过时，腾讯云、华为云上的服务器都不支持直接安装，直接导致不能使用云服务器，因此不得不直接在本机安装虚拟机，而这就涉及到了第二个问题：Mac的处理器是arm架构，而程序能运行的是x86_64。架构不兼容，因此**虚拟机只能Emulation而不能Virtualization**，坑很多。

在此为各位同学梳理一下我遇到的坑，帮助各位更好地完成实验。

## 开发环境

- 宿主机环境：macOS 12.6, Apple M1 Pro
- 虚拟机环境：Ubuntu16.04 Server, Amd64

## 环境配置

### 安装虚拟机

个人认为Mac上最好用的虚拟机软件就是 [UTM](https://mac.getutm.app/)，由于是专门为Mac打造的，使用起来会比VirtualBox更加顺滑。可以从上面的官网链接下载，也可以直接在App Store中下载。UTM支持从 UTM 自带的镜像库下载虚拟机文件，也支持导入外部的镜像文件。<img src="/homework/network/img/utm.png" alt="utm界面" style="zoom:30%;" />

### 下载Ubuntu16.04镜像

Ubuntu16.04实在是太老了！我们并不能直接在UTM的镜像库中找到它（当然，镜像库中的资源也不算很多）。这里，我们可以直接到Ubuntu的官网上下载 [Ubuntu 16.04 的镜像](https://releases.ubuntu.com/16.04/)。**在这里，我们选择下载64-bit PC server image（第一个坑！）**为什么不下载桌面版的镜像？因为UTM的Emulation太慢了，桌面版根本跑不起来！除此之外，安装Server还有一个好处，留到后面说。

<img src="/homework/network/img/ubuntu.png" alt="截屏2022-12-07 14.56.14" style="zoom:30%;" />

### 在UTM中安装Ubuntu16.04

#### 导入镜像

如果对UTM不是很熟悉，那么在安装的时候也会踩很多坑。首先点击**新建一个虚拟机**后，选择**模拟Emulation**，系统预设选择**Linux**。由于我们要使用已经下载好的镜像，这里要从外部导入。在下图启动光盘镜像中找到我们刚才下载好的镜像文件。注意不要勾选“从内核镜像启动”。

<img src="/homework/network/img/linux.png" alt="截屏2022-12-07 15.02.54" style="zoom:40%;" />

点击**下一步**，后面是各种预留资源的分配，这里按照自己的实际情况来分配就可以。**注意检查架构是否是x86_64**，系统用默认的即可。下一步的存储器大小（实际就是虚拟机的硬盘大小）也如此。

#### 文件共享

之后设置和宿主机的文件共享，如果想要通过共享文件夹的方法访问到本机的作业文件，可以将文件夹共享设置为对应路径。但是在访问时，需要依赖插件，具体方法可以参考https://docs.getutm.app/guest-support/sharing/directory/。此外，根据@陈敬文同学的实践，发现mininet没办法在共享文件夹用，需要手动拷贝到虚拟机中。**因此，在这里我们可以不设置共享文件夹，后面有更好的方法。**

<img src="/homework/network/img/share.png" alt="截屏2022-12-07 15.12.58" style="zoom:40%;" />

后面保存即可。

#### 修改UEFI

**接下来是第二个坑**，由于UTM 2.2.4及以后版本修改了启用EFI（UEFI）的条件：“默认为PC，Q35和virt机器创建的新VMS将启用EFI”，因此会导致无法启动不支持UEFI启动的操作系统，并进入EFI shell环境。而我们刚才下载的镜像很有可能是不支持UEFI启动的（至少我的是），会导致安装后无法启动。

因此，我们在刚刚添加的虚拟机上**右键**，点击**编辑**，在QEMU下将**UEFI启动**取消勾选。

<img src="/homework/network/img/UEFI.png" alt="截屏2022-12-07 15.22.58" style="zoom:40%;" />

保存后，点击运行，就是普通的Ubuntu Server的安装过程了，在此就不多赘述，网上也有很多参考资料。**第2.5个坑，安装的时候语言请选择英文**，选中文会有Bug，容易安装失败。

**记得安装工具套件的时候把OpenSSH安装上去。**（也可以后面apt手动安装）

#### 退出安装

**第三个坑**，安装结束之后，**不要直接选择重启，直接将虚拟机关掉**。此时我们要将镜像安装文件退出（对应现实里就是把光盘从光驱中拿出来），否则再次进入的时候又会回到安装界面。

在UTM中，找到最下面的CD/DVD，把现在里面的文件清除即可。之后重新运行虚拟机，这时就可以进入系统了。

<img src="/homework/network/img/quit.png" alt="截屏2022-12-07 15.29.03" style="zoom:40%;" />

> 实在是太不容易了，我前后一共安装了6遍，才成功把系统安装上去。

### 使用VS Code连接虚拟机

这就是安装Server的好处，我们可以直接用VS Code的ssh连进去。这样连共享文件夹什么的都不需要了，本质上就和你用一个云服务器没有多大区别。

同时由于是Server，我们也不需要设置网络桥接，直接使用共享网络模式就可以从外面访问到。<img src="/homework/network/img/net.png" alt="截屏2022-12-07 15.39.59" style="zoom:40%;" />

之后的事情就很简单了，在虚拟机里使用 `ifconfig` 命令查看ip地址，就可以使用VS Code的SSH插件连接进去了。

```shell
$ ssh username@xxx.xxx.xxx.xxx
```

## 可能遇到的虚拟机的坑

由于虚拟机不是非常稳定，在使用VS Code连接的时候可能会遇到报错

```
The remote host may not meet VS Code Server‘s prerequisites for glibc and libstdc++
```

然后连不上去。

网上给出的解答是磁盘、缓存空间满了，但实际满没满可以使用 `df -h` 命令检查一下，满的可能性不大，不过也可以尝试使用 `apt-get clean` 命令清一下缓存。

> 如果清理重启/意外关机之后无法正常启动系统，并且报错unexpected inconsistency;RUN fsck MANUALLY则很有可能是磁盘文件系统损坏。这个时候请不要慌，上面会显示哪个磁盘需要修复，输入fsck -y ...即可。

不过，从个人的经验来看，还是因为系统的版本过低/架构不兼容导致不稳定，用下面的命令升级系统和磁盘

```shell
$ sudo apt-get update 
$ sudo apt-get upgrade
$ sudo apt-get dist-upgrade
```

升级之后，几乎就没有遇到上面的情况了。如果你有更好的解决方法，欢迎联系我（我也想学一下）。

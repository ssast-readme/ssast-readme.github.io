# 如何上网——关于Tsinghua Secure

清华无线校园网802.1x认证系统已正式开通，无线信号名称是“**Tsinghua-Secure**”。

用户只需通过校园网账号登录自服务系统（**http://usereg.tsinghua.edu.cn**）注册**802.1x**认证系统的密码，一次性配置用户终端设备（电脑、手机、PAD等），以后无需再做任何登录认证操作，直接可以上网。

使用802.1x认证系统需要进行以下两个操作步骤:

1. 注册 802.1x 的密码；
2. 配置用户端的设备。
   
详细操作说明如下:

## 一、注册802.1密码

1. **注册密码**：登录自服务系统： http://usereg.tsinghua.edu.cn，选择“ 802.1x 功能”下的“自注册及修改口令”。在密码及确认密码的区域输入密码后，点击“确定”按钮后，即注册802.1x密码成功。如下图所示：
![picture 1](images/f3159a9c04f8d6b98d36b079dbe71ddd4fba902293115592bd3d0178bff28748.png)

2. **注意事项**：为确保校园网账号安全，请勿将 802.1x 密码设置为校园网账号密码。

3. **若需更改密码**：登录自服务系统：http://usereg.tsinghua.edu.cn ，按照上述步骤操作。

## 二、配置用户端设备

用户终端设备需按不同的操作系统进行配置， Windows/Android/iOS/macOS/Linux 等不同系统下的配置方法如下:

### 2.1 Windows10 系统下配置 802.1x 的方法

1. 确认终端在信号覆盖范围内：查找是否能找到 802.1X SSID“ **Tsinghua-Secure**”如果能找到则可以进行下一步。
*如果找不该信号，这说明本地区不在信号覆盖范围内。*
2. 选择**Tsinghua-Secure**，点击“连接”
如下图所示：
![picture 1](images/07e2ef9c8f1e02d53d402a2585d4b9958a375f6b4064e1c11ce7525e8172297a.png)  
1. 输入用户名：即“**校园网账号**”
密码：对应账号下的**802.1X密码**
点击“确定”，之后继续点击“连接”
![picture 2](images/d85ca79def7d2859ee15c4a9f4160328e65ce2d78fb083c885c6cd73c84f6992.png)
![picture 3](images/581974ef03d0e008acb102c9096cf8ef396a0a6c7d913834571313fd954086b4.png)

### 2.2 Windows 7 系统下的配置 802.1x 的方法
 
1.  选择“控制面板”→“查看网络状态和任务”→“网络和共享中心”→“管理无线网络”→进入“管理无线网络窗口”,单击“添加”按钮；
![picture 17](images/8d392d69dcc206f6e97f913e31c48fe8c1373dba47f3929d991083d06d57f2b5.png)
      
2.  设置无线网络信息：选择“手动创建网络配置文件(M)”: 网络名:Tsinghua-Secure；安全类型:WPA2-企业； 加密类型：AES；其它保持缺省配置，然后单击“下一步”，点击：“更改连接设置”；
![picture 18](images/e397bfad7ea01b5382f2e718c0944280e53ec18ade91ede83c0cbd94f1e3e3d0.png)
![picture 19](images/6a83419135b9c8f35c1423e5e4121c9412f93491e02ece3d24ae4116f4a0453a.png)
![picture 20](images/1602e919d61e5e0ad3cd4d0afdcfb13406836860cc47307f9ff0681510d0a0c7.png)
   
3.  配置无线网络安全属性: 点击“安全”属性，按照下图中的标识进行配置：

1） 在“选择网络身份验证方法”-“**设置**”进入受保护的EAP属性页面
![picture 21](images/6621e5d770b9e82efd312522d49ff28bfe61e128c7c589d7d69010856e789672.png)

2） **取消勾选**“通过验证证书来验证服务器的身份”（，选择身份验证方法中选择“**安全密码（EAP-MSCHAP v2）**”选项，同时保持勾选“**启用快速重新连接**”，点击“配置”。
![picture 22](images/70b3ca8abd1cafda2aece061361cf63eeb3ed4cc772b045a0eff31c50ed29963.png)

3） 在弹出的“**EAP MSCHAPv2属性**”界面中：**取消勾选**“自动使用Windows登录名和密码”。
![picture 23](images/00bdaa6f0bec5f1b08eb6ba4fc922f066b926e23c5c188ce97ba31ba24961d2e.png)

4） 进入“**高级设置**”界面后，如下图，在“**802.1X设置**”栏下**勾选**“指定身份验证模式”，选择“**用户或计算机身份验证**”。
![picture 24](images/1780fc173e0c15ceb7c1e55ee8614267af12d4dd0c8aee2f5c7aac9e6a02dbae.png)

5） 选择“**802.11设置**”栏，如下图，在快速漫游栏目下**取消勾选**“启动成对主密钥（PMK）缓存”，点击“确定”。
![picture 25](images/5f953f710163c24fdfeefde6d7dbcef5206757b3de1b02bdfb54b44f23abe7b9.png)
![picture 26](images/620f45b0dbcbfc926c63c8af37dac508c013f236da6d5c4f520a65b05479b21d.png)
![picture 27](images/3ec6e66f6c65052882bf3c40f02a1be9ace7e910a9ccd963a84302a400027a4b.png)      
        
4.  选择并连接 SSID 为 Tsinghua-Secure 的无线网，输入校园网账号和在usereg.tsinghua.edu.cn 中设置的 802.1x 的密码，完成连接。
![picture 28](images/d5a27e5bc434de1e5c29b856f6191b07e0be1b6c4c88f971e5782f044efcb51d.png)
![picture 29](images/c247401deae2082c99696a713416a3081227dfde5ecf06987d91dba000f02ffd.png)
        
### 2.3 Android 系统下的配置 802.1x 的方法

1.  连接 82.1X SSID Tsinghua-Secure；
![picture 30](images/3b71eae9eca9f3d8f1cc29b0d19a68682507a5e6a7272647b578e60c1f3e34fd.png)   
        
2.  按下图填写，身份和密码为校园网账号和在 usereg.tsinghua.edu.cn 中设置的 802.1x的口令。点击连接后完成配置。
![picture 31](images/400a0bec532340e82c9d68792431d679c2196614058c7cdbdeaf20a5c05ed54c.png)  
        
### 2.4 iPhone、iPad 下的配置 802.1x 的方法

1.  设置---无线局域网中连接 802.1X SSID ：Tsinghua-Secure
![picture 32](images/250dddc5e79c27b6cd6601b7210cb35510ad405a03088bdd458b0a57bb758e49.png)

2.  输入校园网账号和口令，身份和密码为校园网账号和在 usereg.tsinghua.edu.cn 中设置的 802.1x 的口令。
![picture 33](images/399948f62238c1fa373b5ea7f257cd20cebb0a5c0480cfbdb910f655f40f7c8e.png)
        
3.  点击信任，首次连接会提示信任该证书，再次连接不会出现该提示。
![picture 34](images/1831a83cfda0beb53ebef0e2b81a4e0a4c4062620dc85dc0b708b5557697f276.png)    
        
### 2.5 macOS 下的配置 802.1x 的方法
    
1.  连接 802.1X SSID: Tsinghua-Secure；
![picture 35](images/7dbef2cbf7ce9c265011542e3c347f896de4d96fcf73971ac1d34ffe9684fdf1.png)  
    
2.  输入用户名密码：用户名和密码为校园网账号和在 usereg.tsinghua.edu.cn 中设置的802.1x 的口令，点击加入；
![picture 36](images/f02f09f6f6a6c32c923dbf64902fd2c4e7529b347267a7459104341128a0a966.png)
        
3.  点击继续；
![picture 37](images/a0921829a02cae8968bd71fd6d1d352bc3c58d4023021c3c032764808c81a947.png)

4.  连接 802.1XSSID: Tsinghua-Secure 后会提示输入 MAC 主机的账号和密码（并非校园网联网账号和密码）；第一次连接时会出现，之后不再出现。输入成功后完成配置。
![picture 38](images/0c4a8b66f10639e48ccb78a49bcaac83e1efe98b561fb9da5789463c586816b2.png)
          
### 2.6 Linux 系统下配置 802.1x 的配置方法

#### 1、以 CentOS 7.0 为例，内核版本号：Linux version 3.10.0-957.1.3.el7.x86\_64

1.1、图形化连接方法：
    
① 点击状态栏“声音”或者“电池”的图标，然后选择“select network”：
![picture 39](images/37aaff9922d64b583aeb0196bc35ad0437330caf06dd7dbf90714259a2b43f9c.png)

② 选择“Tsinghua-Secure”：
![picture 40](images/ceaa37e828ac593468aa149c1171948686e32dd894859c585803393cb35de901.png)
    
③ 在弹出的输入框中，将“Authentication”选择为“Protected EAP(PEAP)”，勾选“No CA certificate is required”，“ PEAP version”选择为“Automatic” ， “Inner authentication”选择为“MSCHAPv2”，最后输入用户名、密码，即可连接成功。
![picture 41](images/b0435b84c48e59f440cfcbdeed4260ae49b53642e48331da89be600f5db959b4.png)
    
1.2、命令行连接方法：

① 在 Terminal 中，通过命令“iw dev”查看无线网卡的标识：
![picture 42](images/7b51df8fba90bc70e50791607765094143bcced7a91cfd1da3d47acca809e8fb.png)  


② 通过如下命令，创建用于连接 802.1x 无线网络的配置文件：
![picture 43](images/9432fc95ec833449a8e8f646508d441de5f996e84c49417c3493e3f20fa9c6ac.png)

③ 通过如下命令，查看已经存在的网络配置文件：

\# nmcli connection show
![picture 44](images/3145398377a6f19f71d96644fc7f3f13a0ed21e743ed4d9761380083dc6c1302.png)

④ 通过如下命令，将刚创建的配置文件绑定到无线网卡上

\# nmcli connection up Tsinghua-Secure ifname wl01
![picture 45](images/7b51df8fba90bc70e50791607765094143bcced7a91cfd1da3d47acca809e8fb.png)

⑤ 查看是否成功连接到 802.1x 网络及网卡的 IP 地址

\# nmcli connection show 
\# ifconfig wlo1
![picture 46](images/7660e6239b1e82d4e3220c4b6d51b2272c943d0d7065b5b29bba8aafdb8ac06a.png)

#### 2、以 Ubuntu16.04 + GUI 为例

1.  选择认证方式为 PEAP 类型
    
2.  勾选不使用 CA 证书
    
3.  内部认证选择 MSCHAPV2 类型
    
4.  填写校园网用户名以及在 https://usereg.tsinghua.edu.cn 网站内注册的 802.1x 密码
![picture 47](images/8fd171ef826e396fdff35a321413eae0939628da5897bad7fe92d672c4c99278.png)

## 三、用户服务 

使用过程中，如有问题可通过以下方式获得帮助服务：热线电话：010-62784859

[服务邮箱：its@tsinghua.edu.cn](mailto:its@tsinghua.edu.cn)

接待服务：信息化技术中心用户服务大厅（李兆基大楼东2门A128室） 企业微信号：关注“清华大学信息服务”，通过网络服务选项进行咨询。
![picture 48](images/505a0422c552e4bab00fb3b9c977c6df80759b013406107331efa0912ce7f630.png)
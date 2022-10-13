# apache2简易指北

> 作者：glassesq
>
> 联系方式：glassesq@outlook.com



## run apache2

当我们需要一个在ubuntu下需要一个web server的时候，`$ sudo apt-get install apache2`会解决许多问题。这会给你一个比较新版本的apache2，你可以在`/etc/apache2`之下修改配置文件。

它拥有一个`sites-avaliable`的文件夹，以及一个`sites-enable`的文件夹，后者中的文件实际上是从前者软链接来的。第一次来到这里时，你会找到一个类似于`000-default.conf`的东西。这提供了一个默认的网站，路径来自于服务器机器的`/var/www`目录下。修改这里的`/var/www`下的`index.html`文件，就能对网站进行修改。

用systemctl进行管理， `$ systemctl status/restart/start/stop apache2`能够完成所有基本工作。



## 使用module

默认的apache2已经无法满足你的需求，人类想使用更多的module来完成他们的目标。比如说，一个均有极其详尽信息的人类可读的Log——`ForensicLog module`。

在使用`$ sudo apt-get install apache2`时，你收获了一些名为*"a2enmod"*以及*"a2dismod"*的东西，对于我们要使用的module，只需要在shell中输入

```shell
$ a2enmod/a2dismod the_module_you_want 
```

来启用它。

```html
+108363:633ae345:1|GET / HTTP/1.1|Host:140.82.51.134|Connection:keep-alive|Pragma:no-cache|Cache-Control:no-cache|Upgrade-Insecure-Requests:1|User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36|Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9|Accept-Encoding:deflate|Accept-Language:en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-HK;q=0.6,de;q=0.5
-108363:633ae345:1
```

好了，说回`ForensicLog`，要获得上述这样详尽的Log, 你需要使用`a2enmod log_forensic`（对于不同的module，你能在文档里找到他们的名字）。接着，就是简单地在conf文件中写好它们的路径。

```bash
$ ForensicLog the/path/to/your/logfile
```



## 更多的apache2/httpd

在某些极端情况下，你想使用某个特定版本的apache2，或者说，httpd。这时候，留给人类的选择很有限，仅能从源代码开始编译了。

除了httpd的包，还需要apr和apr-util的包（https://apr.apache.org/），并把它们放在srclib文件夹下，同时使用--with-included-apr选项。

但是此时可能还会缺少pcre，编译时仍然提示找不到某些依赖项。可以通过下面的方式解决

```shell
$ sudo apt-get install libpcre3-dev / libpcre3
$ ./configure
$ make
$ make install
```

这时一个你选择版本的包被默认装在/usr/local/apache2中了。（通过在./configure阶段指定不同的prefix，人们当然可以把apache2装在其他地方）

>  在某些极其极端的情况下，（可能不是apache2，但可能在其他想目中）./configure中的-Wall 和 -Werror会带来一些麻烦。尽管它们在某个版本中修复，但这没法给我们想要的版本。一个解决方案是手动删掉它们，从configure文件里。

ref: https://httpd.apache.org/docs/2.4/install.html



## 继续使用apache2（与module）

我们拥有一个装在`/usr/local/apache2`的指定版本apache2。它和我们通过`$ sudo apt-get install `安装的apache2配置文件看起来有很大的不同。

可以通过在`/usr/local/apache2/bin`目录下的`apachectl`管理这个对应版本的apache2.

```shell
$ apachectl -k start/stop/restart/graceful/graceful-stop
```

这个特定的apache2版本不从`/etc/apache2`下读取它的配置，而是从`/usr/local/apache2/conf`中。

module的管理变得不那么方便。在`/usr/local/apache2/modules`下，可以看到很多module的库文件。我们会在httpd.conf中使用类似于下述的命令进行module的载入。

```shell
$ LoadModule log_forensic_module modules/mod_log_forensic.so
```

但这样却不能成功，因为modules里根本没有mod_log_forensic选项。这是因为`./configure`在编译apache2时没有默认编译它。使用`$ ./configure --enable-log-forensic`来解决这个问题。



## 支持http2

使用http2_module来支持http2，在配置文件中使用Protocols h2c h2 http/1.1来指定你需要的协议。










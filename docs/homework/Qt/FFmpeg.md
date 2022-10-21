# FFmpeg的使用
> 作者: 此心光明
> [FFmpeg](https://www.ffmpeg.org/) 是视频处理一款常用的开源命令行软件。
> 它功能强大，用途广泛，大量用于视频网站和商业软件（比如 Youtube 和 iTunes），也是许多音频和视频格式的标准编码/解码实现。
> 某年软院大一的小学期要求写一个剪辑软件，为此笔者学习了FFmpeg的使用，在这里对FFmpeg的基本操作进行一些总结。


## 环境搭建
根据官方文档进行安装。[Download FFmpeg](https://www.ffmpeg.org/download.html)
+ Windows系统下需自行配置环境变量
+ ubuntu系统中可直接使用命令`sudo apt install FFmpeg`进行安装

安装成功后，在命令行中输入`ffmpeg -version`，即可查看当前安装的版本

## 基本操作

### 查看信息
视频文件本身其实是一个容器（container），里面包括了视频和音频，也可能有字幕等其他内容。
常见的容器格式有MP4、MKV、WebM、AVI。一般来说，视频文件的后缀名反映了它的容器格式。
```Shell
ffmpeg -formats # 查看支持的容器格式
```
视频和音频都需要经过编码，才能保存成文件。不同的编码格式（CODEC），有不同的压缩率，会导致文件大小和清晰度的差异。
```Shell
ffmpeg -codecs # 查看支持的编码格式
```
编码器（encoders）是实现某种编码格式的库文件。只有安装了某种格式的编码器，才能实现该格式视频/音频的编码和解码。
```Shell
ffmpeg -encoders # 查看已安装的编码器
```
查看视频的元信息（Metadata）。
```Shell
ffmpeg -i input.mp4 # 使用参数 -hide_banner 可减少冗余信息
```
注：用`ffmpeg -help`命令可查看FFmpeg的使用帮助。

### 常用参数
使用FFmpeg进行视频处理的基本格式如下，五个部分的参数依次为全局参数、输入文件参数、输入文件、输出文件参数、输出文件。
```Shell
ffmpeg {1} {2} -i {3} {4} {5} 
```

全局参数
```Shell
-y 不经过确认，输出时直接覆盖同名文件。
-n 不覆盖同名文件
-loglevel   设置日志级别
-ignore_unknown     忽略未知流类型
```
通用参数
```shell
-f   指定音/视频的格式
-t   指定输出音/视频的时长，单位秒
-to  指定输出音/视频结束点，单位秒
-fs  限定输出文件大小(上限)
-ss  指定输出音/视频的开始时间点，单位秒，也支持hh:mm:ss的格式
-re          以初始帧率读取
-preset      指定输出的视频质量，会影响文件的生成速度，
     可用的值有 ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow。
```
视频参数
```shell
-c:v  指定视频编码器
-r    指定帧率 (单位Hz)
-s    指定分辨率 (WxH)
-aspect   指定宽高比(4:3, 16:9 or 1.3333, 1.7777)
-vn       指定输出文件不包含视频
-vcodec   指定输出视频的编码格式 (使用 -vcodec copy 可直接复制，不经过重新编码，速度更快)
-vf   指定视频滤镜 (等效于 -filter_complex)
-b    指定码率（比特率），使用 -b:v 指定该值为平均码率 
-minrate 指定最小容忍度的编码码率
-maxrate 指定一个最大容忍度编码码率，该码率和bufsize相关联
-bufsize 指定解码缓冲大小, 决定了输出码率的可变特性
```
音频参数
```shell
-c:a  指定音频编码器
-aq   指定输出音频的质量
-ar   指定音频采样率 (单位 Hz)
-ac   指定音频声道数量
-an   输出的文件不带音频
-acodec  指定输出的音频编码类型(可使用 -acodec copy ) 
-vol     指定音频的音量 (256=normal)
-af    指定音效
-ab    指定输出音频的码率，使用 -b:a 指定该值为平均音频码率
```

### 基本操作
> 以下部分介绍FFmpeg的基本操作，建议读者在阅读时自行在命令行中进行操作，对命令的用法加以理解。

格式转换
```shell
# 将avi格式转换为mp4格式
ffmpeg -i input.avi output.mp4
# 转成 H.264 编码，一般使用编码器libx264
ffmpeg -i [input.file] -c:v libx264 output.mp4 
#  mp4 转 webm ，使用参数 -c copy (或 -vcodec copy )指定直接拷贝
ffmpeg -i input.mp4 -c copy output.webm 
# gif转图片
ffmpeg -i input.gif img_%d.png
```
改变分辨率和码率
```shell
# 改变视频分辨率（transsizing），从 1080p 转为 480p
ffmpeg -i input.mp4 -s 640x480 output.mp4 # 法一：比例不一样会变形
ffmpeg -i input.mp4 -vf scale=-1:480 output.mp4 # 法二：-1表示按照比例缩放，保证不变形  

# 使用法二时，可加上参数(过滤器）使长宽均为偶数，避免报错： -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2"

# 指定码率最小为964K，最大为3856K，缓冲区大小为 2000K
ffmpeg -i input.mp4 -minrate 964K -maxrate 3856K -bufsize 2000K output.mp4 
```
操作音频
```shell
# 从视频里面提取音频（demuxing），-vn表示去掉视频，-c:a copy表示不改变音频编码，直接拷贝。
ffmpeg -i input.mp4 -vn -c:a copy output.aac
# 添加音轨（muxing），将外部音频加入视频，比如添加背景音乐或旁白。
ffmpeg -i input.aac -i input.mp4 output.mp4 
```
视频剪辑
```shell
# 从指定时间开始，连续对1秒钟的视频进行截图
ffmpeg -y -i input.mp4 -ss 00:01:24 -t 00:00:01 output_%3d.jpg 
# 可使用参数 -vframes 1 指定只截取一帧，参数 -q:v 2 表示输出的图片质量，一般是1到5之间（1为质量最高）。
ffmpeg -ss 01:23:45 -i input -vframes 1 -q:v 2 output.jpg 

# 截取原始视频里面的一个片段，输出为一个新视频。可以指定开始时间（start）和持续时间（duration），也可以指定结束时间（end）。
ffmpeg -ss [start] -i [input] -t [duration] -c copy [output] 
ffmpeg -ss [start] -i [input] -to [end] -c copy [output] 
ffmpeg -ss 00:01:50 -i [input] -t 10.5 -c copy [output] # 截取1分50秒之后的10.5秒
ffmpeg -ss 2.5 -i [input] -to 10 -c copy [output] # 截取2.5秒到10秒

# 将音频文件转为带封面的视频文件
ffmpeg -loop 1 -i cover.jpg -i input.mp3 -c:v libx264 -c:a aac -b:a 192k -shortest output.mp4 
# 上面命令中，有两个输入文件，一个是封面图片cover.jpg，另一个是音频文件input.mp3。
# -loop 1参数表示图片无限循环，-shortest参数表示音频文件结束，输出视频就结束。
```

### 简单实例
```shell
# 截取封面图
ffmpeg -i input.mp4 -y -f image2 -s 640*480 -frames 1 cover.jpg
# 裁剪
ffmpeg -i input.avi -vcodec copy -y -r 25 -ss 8 -t 9 output.mp4

# 通过指令，scale把原图修改下分辨率，缺少的地方不剪切不拉伸而是加黑边，可再把所有处理后的图片二次处理成视频
ffmpeg -i /tmpdir/image%04d.jpg -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" -qscale 1 /tmpdir/iees33w43mage%04d.jpg

# 合并(两种方法) -f concat是指合并 -safe 为了避免权限报错
ffmpeg -f concat -safe 0 -i 1.mp4 -i 2.mp4 -i 3.mp4 -c copy output.mp4
ffmpeg -f concat -safe 0 -i filelist.txt -c copy -y o1.mp4

# 使用单张图片生成固定时长的视频
ffmpeg -r 25 -f image2 -loop 1 -i 1.jpg -vcodec libx264 -pix_fmt yuv420p -s 1920*1080 -t 30 -y fps.mp4

```
> 上述操作中使用的参数 ：
-r (或 -framerate ) 25  帧率，默认帧率为25，表示每秒播放帧数
-f image2  输入流文件格式
-loop 1  输入流循环次数，仅对图片有效，0表示无限循环
-i fps_%d.jpg  文件名，%d、%2d表示匹配数字序列
-vcodec libx264  视频编码，缺少时h5中可能无法播放
-pix_fmt yuv420p  视频格式，缺少时h5中可能无法播放



## 高级用法

### 过滤器的使用

在之前的改变分辨率的操作中用到了简单的过滤器(只含一个输入和一个输出)
```shell
# 将输入的1920x1080缩小到960x540输出:
ffmpeg -i input.mp4 -vf scale=960:540 output.mp4
```

在一些操作中，将使用到较复杂的过滤器语法，可能包含多个输入和多个输出，如图所示：
```
                [main]
input --> split ---------------------> overlay --> output
            |                             ^
            |[tmp]                  [flip]|
            +-----> crop --> vflip -------+
```
这里举出一些常用的例子作为参考：
+ 使用滤镜链添加图片
```shell
# 使用movie容器(;用于分隔过滤操作，:用于分隔参数)
# scale：图片显示大小 ； overlay：图片插入位置的左上角像素坐标
# enable='between (t,start_time,end_time)'  ：该滤镜作用时间段
ffmpeg -i input.mp4 -vf "movie=1.jpg,scale=456:280[mask1];movie=2.jpg,scale=456:280
[mask2];movie=3.jpg,scale=456:280[mask3];[in][mask1] overlay=400:200:enable='between
 (t,0,12)'[top];[top][mask2] overlay=400:200:enable='between (t,12,32)'[middle];
 [middle][mask3] overlay=400:200:enable='between (t,32,62)'[out]" output.mp4

ffmpeg -i input.mp4 -vf "movie=1.jpg,scale=456:280[mask1];[in][mask1]
overlay=200:100:enable='between (t,0,12)'[top]" output.mp4
```
+ 为视频添加水印
```shell
ffmpeg -i input.mp4 -i logo.png -filter_complex overlay output.mp4
# 设置位置：
# 右上角：
ffmpeg -i input.mp4 -i logo.png -filter_complex overlay=W-w output.mp4
# 左下角：
ffmpeg -i input.mp4 -i logo.png -filter_complex overlay=0:H-h output.mp4
# 右下角：
ffmpeg -i input.mp4 -i logo.png -filter_complex overlay=W-w:H-h output.mp4
# 可以设置坐标，视频的左上角为原点
ffmpeg -i input.mp4 -i logo.png -filter_complex overlay=480:10 output.mp4



ffmpeg -i image_source -vf "movie=logo_source,scale=logo_width:logo_height[watermask];
[in][watermask]overlay=from_x:from_y:enable='between (t,time1,time2)'[out]" -y  out_source
# logo_source为水印图片地址，logo_width为水印图片的宽度，logo_height为水印图片的高度
# opacity_num为水印图片的透明度，from_x为水印的起始X轴的位置，from_y为水印的起始Y轴的位置
# time1为水印起始时间，time2为终止时间

# 文字水印
ffmpeg -i image_source -vf "drawtext=fontfile=font_ttf_path:fontcolor=font_color:
fontsize=font_size:text=message_info:x=from_x:y=from_y"  out_source
# font_ttf_path为字体路径，此项必须设置否则会出现字体无法找到的错误;如果水印内容是中文需要设置中文字体否则会文字显示乱码
# 字体路径要设置绝对路径并且要注意路径正反斜线转义(例如C\\:/Windows/Fonts/simhei.ttf)
# font_color为字体的颜色，font_size为字体的大小，message_info为水印文字内容
# from_x为水印的起始X轴的位置，from_y为水印的起始Y轴的位置，

# 去掉视频的水印(sometimes something even uglier appear)
ffmpeg -i input.mp4 -vf delogo=0:0:220:90:100:1 output.mp4
# 语法：-vf delogo=x:y:w:h[:t[:show]]
# x:y 离左上角的坐标，w:h logo的宽和高，t: 矩形边缘的厚度默认值4
# show：若设置为1有一个绿色的矩形，默认值0。
```

一些实例(注意字体文件位置可能需要调整）
```shell

ffmpeg -i input.mp4 -vf "movie=1.jpg,scale=200:160[mask];[in][mask] overlay=20:20:enable='between (t,0,3)'[out]" -y  output.mp4
ffmpeg -i input.mp4 -vf "drawtext=fontfile=simhei.ttf: text='2022':x=10:y=10:fontsize=30:fontcolor=white:shadowy=2" output.mp4
ffmpeg -i input.mp4 -vf drawtext=fontcolor=white:fontsize=40:fontfile=msyh.ttc:text='一二三四':x=0:y=100 -b:v 3000K output.mp4
ffmpeg -i input.mp4 -vf drawtext=fontcolor=white:fontsize=40:fontfile=msyh.ttf:text='test':x=50:y=50:enable='between(t\,5\,10)'   -y output.mp4

# 高级用法（文字随时间移动）
ffmpeg -i input.mp4 -vf "drawtext=text=测试字幕 :expansion=normal:fontfile=SimSun-ExtB 常规.ttf: y=h-line_h-80:x=w-(t-4.5)*w/10: fontcolor=white@0.5: fontsize=36" output.mp4 
ffmpeg -i input.mp4 -vf "drawtext=text=THUSSAST:expansion=normal:fontfile=/Library/Fonts/Microsoft/Yahei.ttf:y=h-line_h-50:x=(mod(5*n\,w+tw)-tw): 
fontcolor=black:fontsize=35" output.mp4

# 加水印，显示10秒
ffmpeg -y -i input.mp4 -acodec libfaac -b:a 30k -ar 44100 -r 15 -ac 2 -s 480x272 -vcodec libx264 \
-refs 2 -x264opts keyint=150:min-keyint=15 -vprofile baseline -level 20 -b:v 200k \
-vf "drawtext=fontfile=/mnt/hgfs/zm/simhei.ttf: text='来源：THU':x=100:y=x/dar:
draw='if(gt(n,0),lt(n,250))':fontsize=24:fontcolor=yellow@0.5:shadowy=2"  output.mp4   

# 实现每3秒显示1秒，可将-vf后参数进行如下修改：
"drawtext=fontfile=/mnt/hgfs/zm/simhei.ttf: text='来源：THU':x=w-100:y=100:
draw=lt(mod(t\,3)\,1):fontsize=24:fontcolor=yellow@0.5:shadowy=2"

```
+ 字幕添加
```shell
ffmpeg -i input.mp4 -vf subtitles=test.srt output.mp4
ffmpeg -i E:/admin/Videos/clip_3.mp4 -vf "subtitles=subtitlesfile" -y output.mp4 
# subtitlesfile是字幕文件的地址
```
+ 特效添加
```shell
# 模糊
ffmpeg -i clip_.mp4 -vf boxblur=5:1:cr=0:ar=0 out.mp4

# 缩放
ffmpeg -loop 1 -i 1.jpg -vf "zoompan=z='if(lte(zoom,1.0),1.3,zoom-0.003)':
d=75" -c:v libx264 -t 10 -y zoomout.mp4 
ffmpeg -loop 1 -i 1.jpg -vf "zoompan=x='iw/2*(1-1/zoom)':y='ih/2*(1-1/zoom)':
z='if(eq(on,1),1.15,zoom-0.002)':d=25*3" -c:v libx264 -t 3 -y zoomout.mp4 
ffmpeg -i 1.jpg -vf "zoompan=x='(100+(on/25*4)*(400-100))*(1-1/zoom)':
y='(50+(on/25*4)*(300-50))*(1-1/zoom)':z='1.5':d=25*3" -c:v libx264 -t 3 -y move.mp4 

# 淡入淡出
ffmpeg -i clip_.mp4 -vf fade=in:0:50 -y fade.mp4
ffmpeg -i clip_.mp4 -vf fade=out:7*25-50:50 -y fade.mp4
# 设置不同效果
fade=in:0:30 # 30帧开始淡入 
fade=t=in:s=0:n=30 # 与上面等效
fade=out:155:45 fade=type=out:start_frame=155:nb_frames=45 # 在200帧视频中从最后45帧淡出 
fade=in:0:25, fade=out:975:25 # 对1000帧的视频25帧淡入，最后25帧淡出 
fade=in:5:20:color=yellow # 让前5帧为黄色，然后在5-24淡入 
fade=in:0:25:alpha=1 # 仅在透明通道的第25开始淡入 
fade=t=in:st=5.5:d=0.5 # 设置5.5秒的黑场，然后开始0.5秒的淡入 
# 通过overlay滤镜可以直接添加带淡入效果
ffmpeg -i test.mp4 -loop 1 -t 4 -i 1.jpg -filter_complex "[1:v]format=rgba,
fade=in:st=1:d=2:alpha=1[ovr]; [0][ovr] overlay" -codec:a copy out.mp4

```


> fade接受下面参数(逗号后为参数的简写）：
type, t ：指定类型是in代表淡入，out代表淡出，默认为in。
start_frame, s ：指定应用效果的开始时间，默认为0。
nb_frames, n ：应用效果的最后一帧序数。
对于淡入，在此帧后将以本身的视频输出，对于淡出此帧后将以设定的颜色输出，默认25.
alpha ：如果设置为1，则只在透明通道实施效果（如果只存在一个输入），默认为0
start_time, st ：指定按秒的开始时间戳来应用效果。
（如果start_frame和start_time都被设置，则效果会在更后的时间开始，默认为0）
duration, d ：按秒的效果持续时间。
（对于淡入，在此时后将以本身的视频输出，对于淡出此时后将以设定的颜色输出。）
（如果duration和nb_frames同时被设置，将采用duration值。默认为0（此时采用nb_frames作为默认））
color, c ：设置淡化后（淡入前）的颜色，默认为"black"。

## 更多
以上仅仅一些关于FFmpeg用法的简单介绍，后续学习可以参照FFmpeg的官方文档。
由于作者水平有限，如有错误，还请读者不吝赐教。联系邮箱为：liubf21@mails.tsinghua.edu.cn

参考资料:
1. [FFmpeg 视频处理入门教程 - 阮一峰的网络日志 (ruanyifeng.com)](http://www.ruanyifeng.com/blog/2020/01/ffmpeg.html)
2. [FFmpeg FilteringGuide](https://trac.ffmpeg.org/wiki/FilteringGuide)
3. [FFmpeg官方文档](https://www.ffmpeg.org/ffmpeg.html)
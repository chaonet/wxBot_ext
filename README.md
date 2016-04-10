# 微信机器人

基于[ **wxBot** ](http://github.com/liuwons/wxBot) ，一个用 Python 包装 Web微信协议 实现的微信机器人框架。

## 文件介绍

- `wxbot.py`是框架文件
- `bot.py`是框架作者开发的图灵机器人
- `test.py`是框架作者的测脚本
- `emotion.py`是自己开发的基于`微软表情识别 API`的微信机器人

## 环境与依赖

此版本只能运行于Python 2环境 。

```
# 下载源码
git clone git@github.com:chaonet/wxBot_ext.git
# 或者通过 HTTPS 下载:
git clone https://github.com/chaonet/wxBot_ext.git

cd wxBot_ext

# 安装依赖
pip install -r requirements.txt
```

### 登录微信

程序运行之后，会在当前目录下生成二维码图片文件 ***qr.png*** 并自动打开，用微信扫描此二维码并按操作指示确认登录网页微信。

如果运行在Linux下，还可以通过设置 **WXBot** 对象的 `conf['qr']` 为 `tty` 的方式直接在终端打印二维码(此方法只能在Linux终端下使用)，效果如下：

![login_on_ubuntu](img/login_on_ubuntu.png)

## 效果展示

测试代码 ***test.py*** 的运行效果：

![向机器人发送消息](img/send_msg.png)

![后台](img/backfront.jpg)


## 图灵机器人示例

***bot.py*** 用 **[图灵机器人](http://www.tuling123.com/)** API 以及 **wxBot** 实现了一个自动回复机器人.

此机器人会回复来自联系人的消息，以及群里@此账号的消息。

并且本帐号可以通过发送 *退下* 、 *走开* 、 *关闭* 、 *关掉* 、 *休息* 、 *滚开* 来关闭机器人的自动回复。

也可以通过发送 *出来* 、 *启动* 、 *工作* 来再次开启机器人的自动回复。

群聊时需要将对应的群保存到联系人列表。

群聊实现效果：

![群聊](img/group_chat.png)

![群聊后台](img/group_chat_backend.jpg)


***bot.py*** 的运行方法：

- 要接入图灵机器人API时：

  1. 在[图灵机器人官网](http://www.tuling123.com/)注册账号，申请图灵key: [图灵key申请地址](http://www.tuling123.com/html/doc/apikey.html)

  2. 在 ***bot.py*** 文件所在目录下新建 ***conf.ini*** 文件，内容为:(key字段内容为申请到的图灵key)

    ```txt
    [main]    
    key=1d2678900f734aa0a23734ace8aec5b1
    ```

  3. 运行 ***bot.py***

    ```python
    python bot.py
    ```

- 不接入图灵机器人API时(此时机器人对联系人消息以及群里@自己的消息统一回复 *知道了* )：
  1. 运行 ***bot.py***

    ```python
    python bot.py
    ```

## 表情识别

基于微软的[Emotion API](https://dev.projectoxford.ai/docs/services/5639d931ca73072154c1ce89/operations/563b31ea778daf121cc3a5fa)和 **wxBot** 实现的一个表情识别机器人。

此机器人开启后，会对来自联系人以及群里发来的图片中，人的表情进行识别。

联系人使用：

可以通过发送 *退下* 、 *走开* 、 *关闭* 、 *关掉* 、 *休息* 、 *滚开* 来关闭机器人的表情识别。

也可以通过发送 *出来* 、 *启动* 、 *工作* 来开启机器人的表情识别。

微信群：

`@ 运行的账号`，文字内容同上

***emotion.py*** 的使用方法：

1. 在[Microsoft 帐户](https://signup.live.com/signup?client_id=b5dbf12c-811e-4f91-aee1-da81da0a2c94&scope=wl.signin+wl.emails&response_type=code&redirect_uri=https%3a%2f%2fwww.microsoft.com%2fcognitive-services%2fExternal%2fLogOn%3fReturnUrl%3d%252Fcognitive-services%252Fen-us%252Fsubscriptions%26__provider__%3dmicrosoft%26__sid__%3d982ef9f4e2144c559ead125762275e8b&contextid=56BC9228173FD4B5&bk=1460244662&ru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3fclient_id%3db5dbf12c-811e-4f91-aee1-da81da0a2c94%26scope%3dwl.signin%2520wl.emails%26response_type%3dcode%26redirect_uri%3dhttps%253A%252F%252Fwww.microsoft.com%252Fcognitive-services%252FExternal%252FLogOn%253FReturnUrl%253D%25252Fcognitive-services%25252Fen-us%25252Fsubscriptions%2526__provider__%253Dmicrosoft%2526__sid__%253D982ef9f4e2144c559ead125762275e8b%26contextid%3d56BC9228173FD4B5%26mkt%3dZH-CN%26lc%3d2052%26bk%3d1460244662&uiflavor=web&uaid=9893f67eb6ee4346b986ae91c75543ad&mkt=ZH-CN&lc=2052&lic=1)注册账号，申请 API key。

2. 在 ***emotion.py*** 文件所在目录下新建 ***conf.ini*** 文件，内容为:(emotion_key字段内容为申请到的 微软emotion API 的key)

    ```
    [main]
    emotion_key=1d2678900f734aa0a23734ace8aec5b1
    ```

3. 运行 ***emotion.py***

    ```python
    python emotion.py
    ```

### 折腾历史

- 申请 emotion API 的 key

只需注册一个 Microsoft 帐户

- 传送图片的格式
`emotion API`可以通过两种方式接收图片文件。
   - 一种是`application/JSON`格式，原始内容为字典`{ "url": "http://example.com/picture.jpg" }`，在发送前需要通过`json.dumps(data)`编码为字符串，然后才能成功发送给`emotion API`，接收时需要`json.loads(data)`解码。但微信框架获取到的图片链接，格式：`https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetmsgimg?MsgID=5763688365154314773&skey=@crypt_115bea6f_2a9e4bb833ca9c156ebb3d71dd48f4bb`无法直接打开图片。
   - 第二种是`application/octet-stream`格式，也就是二进制的图片数据，因为框架自动在本地保存了接收到的图片，所以通过`open(fn, 'rb')`，以二进制方式打开，接收回复时同样需要`json.loads(data)`解码。

[Python - unhashable type error in urllib2](http://stackoverflow.com/questions/3893292/python-unhashable-type-error-in-urllib2)

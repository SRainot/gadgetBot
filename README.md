# gadgetBot
瞎搞！想到啥弄啥！基于[nonebot]框架的QQ机器人

[nonebot]: https://github.com/richardchien/nonebot

## 目前功能
1. 获取bilibili视频封面图片
2. 剑网3科举题
3. 智能聊天(基于腾讯ai,最好使用自己的APPKEY)
4. 语音合成

## TODO
### 剑网3系列
1. 开服监控
2. 金价查询
3. 宠物查询
4. 。。。

### B站系列
1. 开播通知
2. 在QQ跟弹幕聊天
3. 。。。

### 其他
1. 抽签
2. 签到
3. 。。。

###引用
aio.requests源码使用的是[aki]奶茶的源码(RCNB)

[aki]: https://github.com/cczu-osa/aki/tree/master/aki



#### 聊天跟语音合成说明
智能聊天使用的是[腾讯ai开放平台]的接口,使用QQ登陆创建一个应用，接入智能闲聊能力，拿到的appid跟appkey填入config.py.
代码原有的不知道啥时候会过期还是自己申请一个比较好
```bash 
TX_CHAT_APPID = 'appid'
TX_CHAT_APPKEY = 'appkey'
```
语音合成使用的是百度语音合成的接口，还是跟上面一样在config.py里面配置
```bash
BD_CLIENT_ID = '4LI50CEmqn4h4mNqfjwicu04'
BD_CLIENT_SECRET = 'PHBGwYHmWiz9Ce0eBV7jygGrUyKpSetn'
BD_TOKEN = '' #会通过ID跟SECRET自动获取这个不需要填写（）
```

#### 功能使用

[腾讯ai开放平台]:https://ai.qq.com/







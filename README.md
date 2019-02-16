# gadgetBot
瞎搞！想到啥弄啥！基于[nonebot]框架的QQ机器人

[nonebot]: https://github.com/richardchien/nonebot

## 目前功能
1. 获取bilibili视频封面图片
2. 剑网3科举题
3. 智能聊天(基于腾讯ai,最好使用自己的APPKEY)

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

### 智能闲聊说明
使用的是[腾讯ai开放平台]的接口,使用QQ登陆创建一个应用，接入智能闲聊能力，拿到的appid跟appkey填入config.py.
代码原有的不知道啥时候会过期还是自己申请一个比较好
```bash 
CHAT_APPID = 'appid'
CHAT_APPKEY = 'appkey'
```

[腾讯ai开放平台]:https://ai.qq.com/


###引用
aio.requests源码使用的是[aki]奶茶的源码(RCNB)

[aki]: https://github.com/cczu-osa/aki/tree/master/aki





# AI_for_Wechat_tiaoyitiao
人工智能助手 自动微信跳一跳 小游戏  

#### 作者：刘云飞  
 wechat：lyffly  
## 0x00
 支持手机：安卓Android系统 分辨率为1920 * 1080 pix   
 电脑端：windows  
 人工智能版差别在哪：期待AI理解距离的概念，在跳的时候只跳大概距离，不是每次跳中心，非一个精确的数值，这样也可以防止刷分被ban。
 
## 0x01
 首先按照下面进行配置adb和Python环境  
 
[https://github.com/wangshub/wechat_jump_game](https://github.com/wangshub/wechat_jump_game "https://github.com/wangshub/wechat_jump_game")

## 0x02
 安装tensorflow和keras
```shell
pip install tensorflow
pip install keras
```
## 0x03
 下载这里的所有文件

## 0x04
 打开 跳一跳 小游戏  
 在下载后的文件夹内，cmd中运行
```shell
python predict.py
```
即可开始游戏  

效果见视频
[http://www.bilibili.com/video/av17998366](http://www.bilibili.com/video/av17998366 "http://www.bilibili.com/video/av17998366")

截图  
![](https://github.com/lyffly/AI_for_Wechat_tiaoyitiao/blob/master/imgs/demo.png)

## 如果只想刷分，不要再往下看

## 0x05
 备注：本文代码除 深度学习 部分为本人编写  
       其他代码来源于https://github.com/wangshub/wechat_jump_game  

 训练使用的图片已经共享：  
 链接：https://pan.baidu.com/s/1mhCz1Bq 密码：lih7


## 0x06
  知识背景：深度学习，CNN  
  训练图片共3502张，准确率约95%，训练显卡（1050ti），时长约10小时。  

网络结构如下

![](https://github.com/lyffly/AI_for_Wechat_tiaoyitiao/blob/master/imgs/model.png)


持续更新中


# Bin2Protocol

## 项目说明
本项目支持读取bin文件，将其中的内容通过相关的协议封装成16进制通信协议。你可以根据该原理读取bin文件，发送到单片机或者别的什么，实现OTA升级。

## 运行项目
```shell
python app.py
```
## 打包项目
```shell
pyinstaller -F -w .\app.py # -F 表示生成单文件 -w 取消控制台唤起
```
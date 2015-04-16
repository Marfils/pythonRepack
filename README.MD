# python repack #

##### 只适用于windows #####

作用：用于对已打包完成的apk进行解包，替换、删除so文件后重新打包

为什么会去做：cocos2d-x打包后讲计费sdk中的so文件重新编译，导致计费失败

todo list:<br/>
1. 修改包名
2. 替换icon<br/>
3. 替换asserts文件中的特定文件<br/>
4. 替换AndroidManifest.xml文件中特定meta-data的值(渠道识别)

#### 使用说明 ####

1.替换自己的keystore文件


2.配置文件 user.ini<br/>
>targt_path 生成包的目标目录<br/>
>file1 需要删除的so文件<br/>
>keyfile 签名文件<br/>
>alias 签名文件别名<br/>
>storepassword 签名密码<br/>
>keypass 库密码<br/>

3.将apk文件放入apks目录

4.将需要替换的so文件放入jni目录

5.运行repack.py(**备份好原始apk文件，脚本运行完会被删除**)

#### 注意 ####

1.脚本运行完会自动删除生成的文件和apks目录下的文件

#所以要备份好原始的apk文件#
# PythonDemo

Python的学习工程，包括一些示例代码


## 在VSCode搭建Python环境

一、创建工程目录

二、在该工程目录下打开terminal

三、输入python.exe -m venv env命令创建虚拟环境，该虚拟环境文件在工程目录下

四、启动虚拟环境.\env\Scripts\activate

启动虚拟环境报错：
	无法加载文件 D:\project\alienInvasion\env\Scripts\Activate.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参阅 https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about *_Execution_* Policies。

    所在位置 行:1 字符: 1

+ .\env\Scripts\activate
+ CategoryInfo : SecurityError: (:) []，PSSecurityException
+ FullyQualifiedErrorId : UnauthorizedAccess

解决办法：

1. 开始处搜索powershell，以管理员的身份运行
2. 查询Powershell详细策略，在终端执行：get-ExecutionPolicy，显示Restricted（禁止状态）
3. 更新Powershell策略，在终端执行：set-ExecutionPolicy RemoteSigned (选择y)
4. 再次查询策略状态，在终端执行：get-ExecutionPolicy，显示RemoteSigned
5. 如果想还原设置set-ExecutionPolicy Restricted（选择y）

五、 在cscode左下角可以选择python执行的解释器

六、 再次启动terminal会自动切换成虚拟环境

## **比较好用的插件安装**

1. python snippets插件：自动代码补全
2. AREPL：显示代码的结果
3. **autoDocstring 用于编写接口说明等注释**

### 参考文档

> [vscode中python虚拟环境](https://www.cnblogs.com/wanjunbook/p/14585389.html)
> [https://www.bilibili.com/video/BV1yv41147rE?spm_id_from=333.337.search-card.all.click](https://www.bilibili.com/video/BV1yv41147rE?spm_id_from=333.337.search-card.all.click)

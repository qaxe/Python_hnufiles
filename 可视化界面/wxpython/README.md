##  一、wxPython简介
wxPython 是一个用于 wxWidgets （用C ++编写）的Python包装器，这是一个流行的跨平台GUI工具包。由Robin Dunn和Harri Pasanen共同开发，wxPython被实现为一个Python扩展模块。

就像wxWidgets一样，wxPython也是一个免费软件。它可以从官方网站http://wxpython.org下载。许多操作系统平台的二进制文件和源代码可在本网站上下载。

wxPython API中的主要模块包括一个核心模块。它由 wxObject 类组成，它是API中所有类的基础。控制模块包含GUI应用程序开发中使用的所有小部件。例如，wx.Button，wx.StaticText（类似于标签），wx.TextCtrl（可编辑文本控件）等。

wxPython API具有GDI（图形设备接口）模块。它是一组用于绘制小部件的类。像字体，颜色，画笔等类是其中的一部分。所有容器窗口类都在Windows模块中定义。

wxPython的官方网站也承载了Phoenix项目 - 一个用于Python3的wxPython的新实现。它侧重于提高速度，可维护性和可扩展性。该项目始于2012年，目前仍处于测试阶段  
————————————————  
##  二、wxPython Hello World
使用pip下载wxPython依赖库

pip installer wxPython

我们想要创建Hello World消息的简单GUI应用程序需要以下步骤构建 -

1、导入wx模块。
2、定义Application类的一个对象。
3、创建一个顶级窗口作为wx.Frame类的对象。标题和大小参数在构造函数中给出。
4、尽管可以在Frame对象中添加其他控件，但它们的布局不能管理。因此，将一个Panel对象放入框架中。
5、添加一个StaticText对象以在窗口内的所需位置显示’Hello World’。
6、通过show（）方法激活框架窗口。
7、输入Application对象的主事件循环。  
————————————————  

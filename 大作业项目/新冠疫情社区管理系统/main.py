#导入拓展
from function import *
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#读取数据
"""
总表:df
密码表:pw
电话号码/账号:ID
密码:PassWord
登录许可:passcard
跳转许可:jumpcard
"""
df=pd.read_excel('社区信息表 .xlsx',dtype=object)
#数据预处理
pw=df[['电话','密码']]
#登录菜单界面
title()
print('>>>请按提示输入账号密码以登录系统')
ID=input('>>>请输入您的电话号码以登录系统:')
PassWord=input('>>>请输入该号码的密码以登录系统:')
fgf()
#验证登录
passcard=0#登录许可
if ID in pw.values:
    if ID=='admin' and PassWord==pw[pw['电话']==ID].iloc[0,1]:
        print('>>>系统管理员登录')
        passcard,jumpcard=1,'0'#管理端登录许可
    elif PassWord==pw[pw['电话']==ID].iloc[0,1]:
        print('>>>登录成功')
        passcard,jumpcard=2,'0'#居民端登录许可
    else:
        print('>>>密码错误')
else:
    print('>>>没有此账号')
#社区端口
while passcard==1:
    if jumpcard=='0':#主菜单
        title()
        content.show()
        print('>>>1:居民信息管理')
        print('>>>2:物资信息管理')
        print('>>>3:防疫信息管理')
        print('>>>4:公告信息修改')
        print('>>>x:退出系统')
        fgf()
        jumpcard=input('请输入您的操作:')
    elif jumpcard=='1':#居民信息管理
        break
    elif jumpcard=='2':#物资信息管理
        break
    elif jumpcard=='3':#防疫信息管理
        break
    elif jumpcard=='4':#公告信息修改
        title()
        print('>>>注意:公告的请用英文逗号')
        content.change(input('请输入您要修改的公告：\n'))
        fgf()
        print('>>>公告修改成功\n>>>为您返回主页')
        jumpcard='0'
    elif jumpcard=='x':#退出系统
        save()
        break
        
        
        
#居民端口
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

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
密码错误次数:worrycount
"""
df=pd.read_excel('社区信息表 .xlsx',dtype=object)
#数据预处理DataFrame
pw=df[['电话','密码']]#密码系统需要的
pn=df.dropna()[['姓名','单元','楼栋','房间','核酸','电话']]#居民信息需要
#登录菜单界面
title()
print('>>>请按提示输入账号密码以登录系统')
ID=input('>>>请输入您的电话号码以登录系统:')
PassWord=input('>>>请输入该号码的密码以登录系统:')
fgf()

##########################################################################

#验证登录
passcard,worrycount=0,0#登录许可和错误计数
if ID in pw.values:
    if ID=='admin' and PassWord==pw[pw['电话']==ID].iloc[0,1]:
        print('>>>系统管理员登录')
        passcard,jumpcard=1,'0'#管理端登录许可
    elif PassWord==pw[pw['电话']==ID].iloc[0,1]:
        print('>>>登录成功')
        passcard,jumpcard=2,'0'#居民端登录许可
    else:#密码错误重试判断
        while worrycount<3:
            worrycount+=1
            print('>>>密码错误\n>>>您还有{}次重试机会'.format(3-worrycount))
            title()
            PassWord=input('>>>请输入该号码的密码以登录系统:')
            fgf()
            #重复的登录判断
            if ID=='admin' and PassWord==pw[pw['电话']==ID].iloc[0,1]:
                print('>>>系统管理员登录')
                passcard,jumpcard=1,'0'#管理端登录许可
                break
            elif PassWord==pw[pw['电话']==ID].iloc[0,1]:
                print('>>>登录成功')
                passcard,jumpcard=2,'0'#居民端登录许可
                break
        else:
            print('>>>密码错误次数过多\n>>>请联系系统管理员\n>>>终端关闭')
else:
    print('>>>系统中没有此账号\n>>>请联系管理员')
    
##########################################################################    
    
#社区端口
residents,find,supplies,epidemic='0','0','0','0'#默认子菜单跳转
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
        while jumpcard=='1':#居民信息跳转菜单
            if residents=='0':#子菜单
                title(' 居民信息管理系统 ')
                print('>>>1:查看居民信息')
                print('>>>2:查询居民信息')
                print('>>>3:修改账号信息')
                print('>>>x:返回主菜单')
                fgf()
                residents=input('请输入您的操作:')
            elif residents=='1':#查看居民信息
                for index in range(len(pn.index)):
                    print(list(pn.iloc[index,:]))
                    print('#'*56)
                residents=input('>>>请输入您的操作:')
            elif residents=='2':#查询居民信息
                if find=='0':#主页
                    title('   查询居民信息   ')
                    print('>>>1:按单元楼栋检索')
                    print('>>>2:按名字精确检索')
                    print('>>>x:返回管理员主菜单')
                    find=input('>>>请输入您的操作:')
                    fgf()
                elif find=='1':#按单元楼栋检索
                    print('>>>示例:搜索三单元7栋--3,7')
                    unit,build=eval(input('请输入要搜索的单元楼栋编号:'))
                    UNIT,build=change(unit)+'单元',str(build)+'栋'
                    if UNIT in pn['单元'].unique():#检索单元
                        if build in pn[pn['单元']==UNIT]['楼栋'].unique():
                            print('>>>为您查询到以下信息')
                            print(pn[(pn['单元']==UNIT)&(pn['楼栋']==build)])
                            judge=input('>>>是否要退出搜索(Y/N):')
                            if judge=='Y':
                                print('>>>正在为您返回主菜单')
                                find='x'
                        else:
                            inputerror()
                    else:
                        inputerror()
                elif find=='2':#按名字精确检索
                    findname=input('请输入要搜索的居民名字:')
                    if findname in list(pn['姓名']):
                        print('>>>为您查询到以下信息')
                        print(pn[pn['姓名']==findname])
                        fgf()
                    #判断是否继续搜索
                        judge=input('>>>是否要退出搜索(Y/N):')
                        if judge=='Y':
                            print('>>>正在为您返回主菜单')
                            find='x'
                        else:
                            inputerror()                   
                    else:
                        inputerror()
                elif find=='x':
                    print('>>>正在为您返回主菜单')
                    jumpcard='0'
            elif residents=='3':#修改账号信息
                pass#这部分邹书杰
            elif residents=='x':#返回主菜单
                print('>>>正在为您返回上级菜单')
                jumpcard='0'
                break
    elif jumpcard=='2':#物资信息管理
        while jumpcard=='2':#物资信息跳转菜单
            if supplies=='0':#子菜单
                pass#这部分杨小天
    elif jumpcard=='3':#防疫信息管理
        while jumpcard=='2':#防疫信息跳转菜单
            if epidemics=='0':#子菜单
                pass#这部分不知道
    elif jumpcard=='4':#公告信息修改
        title()
        print('>>>注意:公告的请用英文逗号')
        content.change(input('请输入您要修改的公告：\n'))
        fgf()
        print('>>>公告修改成功\n>>>为您返回主页')
        jumpcard='0'
    elif jumpcard=='x':#退出系统
        print('>>>正在为您退出系统')
        save()
        print('>>>终端关闭')
        break
    else:
        inputerror()
    
##########################################################################    
    
#居民端口
while passcard==2:
    if jumpcard=='0':#主菜单
        title()
        content.show()
        print('>>>1:个人信息管理')
        print('>>>2:物资信息系统')
        print('>>>3:防疫信息系统')
        print('>>>x:退出系统')
        fgf()
        jumpcard=input('请输入您的操作:')
    elif jumpcard=='1':#个人信息管理
        break#这部分肖守建
    elif jumpcard=='2':#物资信息系统
        break#这部分不知道
    elif jumpcard=='3':#防疫信息系统
        break#这部分肖守建
    elif jumpcard=='x':#退出系统
        print('>>>正在为您退出系统')
        save()
        print('>>>终端关闭')
        break
    else:
        print('>>>错误的输入\n>>>请重新检查您的操作')

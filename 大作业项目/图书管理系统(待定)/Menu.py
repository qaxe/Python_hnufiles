# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 21:06:35 2022

@author: 30505
"""
def ZS():
    '''
    这是一个小王同学自主研发设计的python图书管理系统
    ————————————————————————————————
    代码内一些没写出的注释
    ————————————————————————————————
        A是主菜单的跳转
        B是管理员系统的记住密码
        C是清除书籍子菜单的跳转
    ————————————————————————————————
    目前实现的功能
    ————————————————————————————————
    ①验证已有的学号姓名登录系统
    ②自动跳转返回上一级菜单或主菜单
    ③独立的管理员系统
    ④管理员系统独立密码
      -自动保存密码，防止重复输入
      -修改密码并保存
    ⑤归还和借阅保留历史记录和输出
    ⑥添加和删减书籍
    ⑦内容保存到文本，重启代码依旧不会重置内容
    ⑧进入管理员系统时自动按书籍编码整理字典
    ————————————————————————————————
    '''
    return None

def fgf():#分隔符
    print('##############################')
    
#书架库存在文本中
txt1=open('booklib.txt','r',encoding='utf-8')
booklib=eval(txt1.read())
txt1.close()

#图书管理员密码存放在文本中
txt2=open('IDcard.txt','r',encoding='utf-8')
IDcard=txt2.read()
txt2.close()

#学号姓名存放在文本中
txt3=open('IDcheck.txt','r',encoding='utf-8')
IDcheck=eval(txt3.read())
txt3.close()

#借书历史存放在文本中
txt4=open('history.txt','r',encoding='utf-8')
history=eval(txt4.read())
txt4.close()

#运行系统
import sys
A,B=input('>>>请输入0以确认运行系统:'),'0'
if A!='0':
    sys.exit()#终止文件运行
ID=input('>>>请输入你的学号以登录系统:')
XM=input('>>>请输入你的姓名以登录系统:')

#验证学号姓名
if XM in IDcheck.keys() and IDcheck[XM]==ID:
    print('>>>登录成功！')
    A='0'
else:
    print('>>>学号和姓名不符')
    A='00'
    
#图书管理系统
while True:
    #退出系统
    if A=='00':
        #保存图书馆内容
        txt1=open('booklib.txt','w',encoding='utf-8')
        txt1.write(str(booklib))
        txt1.close()
        print('>>>正在为您退出系统')
        break
    #主菜单#0
    elif A=='0':
        worrycount=0#管理员密码错误次数重置
        fgf()
        print('{}'.format('   ***   图书管理系统   ***'))
        fgf()
        print('>>>1:查找(借阅/归还)书籍')
        print('>>>2:查看库存')
        print('>>>3:管理员登录')
        print('>>>00:退出系统')
        fgf()
        A=input('>>>请输入你的操作:')
    
    #查找(借阅)书籍
    elif A=='1':
        CZ=input('请输入你要查找(借阅)的书籍名字:')
        for i in booklib.keys():
            if CZ==booklib[i]['书名']:
                print('>>>系统为您找到相关以下结果')
                fgf()
                print('编码     书名              库存    ')
                print(i,end='    ')
                print(booklib[i]['书名'],end='')
                print('{}{}'.format(' '*(20-2*(len(booklib[i]['书名']))),booklib[i]['库存']))
                fgf()
                JY=input('您想要进行借阅还是归还吗？(借阅请输入Y/G,返回主菜单请随意输入)')
                if JY=='Y':
                    booklib[i]['库存']=str(int(booklib[i]['库存'])-1)
                    #保存借阅记录到后台
                    history[len(history)+1]=XM+'成功借阅1本《'+'{}'.format(booklib[i]['书名'])+'》'
                    print('>>>恭喜你借阅成功！')
                    A='00'
                elif JY=='G':
                    booklib[i]['库存']=str(int(booklib[i]['库存'])+1)
                    history[len(history)+1]=XM+'成功归还1本《'+'{}'.format(booklib[i]['书名'])+'》'
                    print('>>>恭喜你归还成功！')
                    A='00'
                else:
                    print('>>>正在为您返回主菜单')
                    A='00'
                txt4=open('history.txt','w',encoding='utf-8')
                txt4.write(str(history))
                txt4.close()
                break
        else:
            print('系统没有查询到该书籍')
            A='0'

    #查看库存#2
    elif A=='2':
        fgf()
        print('{}'.format('   ***    查看库存    ***'))
        fgf()
        print('编码     书名              库存    ')
        for BM in booklib.keys():
            print(BM,end='    ')
            print(booklib[BM]['书名'],end='')
            print('{}{}'.format(' '*(20-2*(len(booklib[BM]['书名']))),booklib[BM]['库存']))
        fgf()
        print('>>>0:返回主菜单')
        fgf()
        A=input('>>>请输入你的操作:')
        
    #管理员系统
    elif A=='3':
        #避免重新登录
        if B!='1':
            fgf()
            print('{}'.format('   ***    管理员系统    ***'))
            fgf()
            testcard=input('>>>请输入管理员密码:')
            if testcard==IDcard:#管理员密码
                B='1'
                worrycount=0
            else:#密码错误
                worrycount+=1
                print('管理员密码错误')
                print('>>>自动为你返回登录系统')
                if worrycount==3:
                    print('管理员密码错误次数过多')
                    print('>>>自动为你退出系统')
                    A='0'
        else:#B='1'
        #成功进入系统
            fgf()
            print('{}'.format('   ***    管理员系统    ***'))
            fgf()
            print('>>>1:新书入库')
            print('>>>2:库存清理')
            print('>>>3:借阅历史')
            print('>>>GG:更改管理员密码')
            print('>>>quit:返回主菜单')
            fgf()
            #自动整理书架
            booklib=dict(sorted(booklib.items(),key=lambda x:x[0]))
            D=input('>>>请输入你的操作:')
            if D=='1':
                SM=(input('>>>请输入新书的书名:'))
                for k in booklib.keys():#检测是否为库中书籍 
                    if SM==booklib[k]['书名']:
                        SL=(input('>>>请输入新书的数量:'))
                        booklib[k]['库存']=booklib[k]['库存']+int(SL)
                        print('>>>新书入库成功！')
                        print('>>>新入库:{}{}{}本'.format(k,SM,SL))
                        break
                else:#执行新书入库
                    BM=(input('>>>请输入新书的编码:'))
                    SL=(input('>>>请输入新书的数量:'))
                    XS={'书名':'新书','库存':0}
                    XS['书名'],XS['库存']=SM,SL
                    booklib[BM]=XS
                    print('>>>新书入库成功！')
                    print('>>>新入库:{}{}{}本'.format(BM,SM,SL))
            elif D=='2':
                fgf()
                print('{}'.format('   ***    管理员系统    ***'))
                fgf()
                print('>>>1:根据编码清除')
                print('>>>2:根据书名清除')
                fgf()
                C=input('>>>请输入你的操作:')
                if C=='1':
                    BM=(input('>>>请输入书籍的编码:'))
                    del booklib[BM]
                elif C=='2':
                    SM=(input('>>>请输入书籍的书名:'))
                    for k in booklib.keys():
                        if SM==booklib[k]['书名']:
                            del booklib[k]
                print('>>>书籍库存清理成功！')
            elif D=='3':
                fgf()
                print('{}'.format('   ***    历史借阅    ***'))
                fgf()
                print('编号           借阅历史')
                for key,value in history.items():#编号,value借阅记录
                    print(key,value,sep='     ')
            elif D=='GG':
                IDcard=input('>>>请输入新的密码:')
                txt2=open('IDcard.txt','w',encoding='utf-8')
                txt2.write(str(IDcard))
                print('>>>成功更改管理员密码')
                A='0'
            elif D=='quit':
                A='0'
    else:
        A=='0'
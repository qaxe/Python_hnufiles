# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:27:57 2022

@author: sparking
"""
'''
---------简介------------
以收集到的'社区信息表.xlsx'文件为基础，格式如下：
 单元  楼栋   房间 核酸       电话号码
汪宏  1单元  2栋  202  阴     241562
进行'核酸阳性名单.xlsx'，'密接名单.xlsx'的统计和更新，和统计条形图的显示
以同楼层为标准进行密接人员筛选
使用时请保证spyde里存在此三个文件且三文件处于关闭状态
有疑问或需要修改的请联系杨小天
----------------
'''   
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
df=pd.read_excel('社区信息表 .xlsx')
#-------------控制台分割符号----------#
def fg():
    print('-'*30)
#------------------------------------#

#--------控制台显示名单函数-----------#
def  xs(x):
    print(x)
#------------------------------------#
#-------将人员地址信息转换为特殊编码，以{姓名：编码}输出---#
def dz_code(s):
    dict1={}
    for row_index,row in s.iterrows():   
        str1=str(row['单元'])
        str2=str(row['楼栋'])
        str3=str(row['房间'])
        str_value=str1[0:1]+str2[0:1]+str3
        dict1[row_index]=str_value
    return dict1
#---------------------------------
def yx_sx(df):
    yx=df[df['核酸']=='阳']
    yx.set_index('姓名',inplace=True)
    yx.to_excel('核酸阳性名单.xlsx')
    return yx
#--密接筛选函数，信息储存进df_mj(dataframe)中----#
def mj_sx(s,yx):  
    dict1=dz_code(s)#小区人员信息字典
    dict2=dz_code(yx)#阳性人员信息字典
    dict3={}#密接人员信息字典
    l=[]
    for key,value in dict2.items():
        for i,j in dict1.items():
            if j[-3]==value[-3]:
                  dict3[i]=j
    for key in dict3.keys():
        l.append(s.loc[key])
    df_mj=pd.DataFrame(l)
    df_mj.to_excel('密接名单.xlsx')
    return df_mj
#---------------------------------------#
#-------密接及阳性人数条形图显示---------#
def bar_s_show(df,yx,df_mj):  
    matplotlib.rcParams['font.family']='simHei'
    matplotlib.rcParams['axes.unicode_minus'] =False
    dy_list=df['单元'].unique()
    y1=[]
    y2=[]
    for i in dy_list:
        y1.append(len(yx[yx['单元']==i]))
    for i in dy_list:
        y2.append(len(df_mj[df_mj['单元']==i]))
        
    x = range((len(dy_list)))  
    p1=plt.bar(x, y1, width=0.2,color='red',label='阳性')
    p2=plt.bar([i + 0.2 for i in x], y2, width=0.2, color='orange',label='密接')
    plt.xticks([i + 0.1 for i in x], dy_list)
    plt.bar_label(p1,label_type='edge')
    plt.bar_label(p2,label_type='edge')
    plt.ylabel('人数')
    plt.xlabel('单元')
    plt.title('小区阳性及密接统计')
    plt.legend()
    plt.show() 
    
    dict4={}
    count=0
    for i in dy_list:
        dict4[i]=y1[count]+y2[count]
        count+=1
    for key,value in dict4.items():
        print('单元:',key,'隔离总人数:',value)
#-----------------------------------------#
#--------------堆积图显示------------------------# 
def bar_d_show(df,yx,df_mj):  
    matplotlib.rcParams['font.family']='simHei'
    matplotlib.rcParams['axes.unicode_minus'] =False
    dy_list=df['单元'].unique()
    y1=[]
    y2=[]
    for i in dy_list:
        y1.append(len(yx[yx['单元']==i]))
    for i in dy_list:
        y2.append(len(df_mj[df_mj['单元']==i]))
        
    x = range((len(dy_list)))  
    width=0.35
    xlabels=dy_list
    p1=plt.bar(xlabels,y1,width,color='red',label='阳性')
    p2=plt.bar(xlabels,y2,width,bottom=y1,color='orange',label='密接')
    #plt.axhline(0,color='grey',linewidth=0)
    plt.ylabel('隔离人数')
    plt.xlabel('单元')
    plt.title('小区阳性及密接统计')
    plt.legend()
    plt.bar_label(p1,label_type='center')
    plt.bar_label(p2,label_type='center')
    plt.bar_label(p2)
    plt.show()

    dict4={}
    count=0
    for i in dy_list:
        dict4[i]=y1[count]+y2[count]
        count+=1
    for key,value in dict4.items():
        print('单元:',key,'隔离总人数:',value)
#-----------------------------------------------------#
x=0
fg()
print('已进入小区阳性及密接筛选系统')
fg()
while True:
    if x==0:
        fg() 
        print('在操作台输入对应数字以执行相应操作')
        print('小区信息显示:1')
        print('个人信息索引:2')
        print('阳性筛选:3')
        print('密接筛选:4')
        print('密接及阳性人数条形图显示:5')
        print('密接及阳性人数条形堆积图:6')
        print('操作帮助中心:0')
        print('结束系统:9')
        fg()
        x=eval(input('输入操作:'))
    elif x==1:
        fg()
        xs(df) 
        fg()
        x=eval(input('输入操作:'))   
    elif x==2:
        fg()
        print('已进入索引:')
        fg()
        xx=input('请输入索引人信息(姓名或地址编码或联系方式):')
        
        
        
        
        
        
        fg()
        x=eval(input('输入操作:'))        
    elif x==3:
        fg()
        yx=yx_sx(df)
        print('完成阳性人员筛选')
        print('已写进excel文件:核酸阳性名单.xlsx')
        fg()
        s=input( '是否在控制台显示(Y/y N/n):')
        if s=='Y' or s=='y':
            xs(yx)
        fg()
        x=eval(input('输入操作:'))
    elif x==4:
        s=df.set_index('姓名')
        yx=yx_sx(df)
        df_mj=mj_sx(s,yx)
        fg()
        print('完成密接人员筛选')
        print('已写进excel:密接人员名单.xlsx')
        fg()
        s=input( '是否在控制台显示(Y/y N/n):')
        if s=='Y' or s=='y':
            xs(df_mj)
        fg()
        x=eval(input('输入操作:'))
    elif x==5:
        fg()
        s=df.set_index('姓名')
        yx=yx_sx(df)
        df_mj=mj_sx(s,yx)
        bar_s_show(df,yx,df_mj)
        fg()
        x=eval(input('输入操作:'))
    elif x==6:
        fg()
        s=df.set_index('姓名')
        yx=yx_sx(df)
        df_mj=mj_sx(s,yx)
        bar_d_show(df,yx,df_mj)
        fg()
        x=eval(input('输入操作:'))  
    else:
        fg()
        print('正在退出系统')
        fg()
        print('已退出系统')
        break
        

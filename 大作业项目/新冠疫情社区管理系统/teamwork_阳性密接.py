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
df=df.dropna()
df=df[['姓名','单元','楼栋','房间','核酸','电话']]
str_value_list=[]
for row_index,row in df.iterrows():   
    str1=str(row['单元'])
    str2=str(row['楼栋'])
    str3=str(row['房间'])
    str_value=str1[0]+str2[0]+str3
    str_value_list.append(str_value)   
df['编码']=str_value_list    
df=df.set_index('编码')
yx=df[df['核酸']=='阳']
list1=[i for i in yx.index]
yx=yx.set_index('姓名')
list2=[]
for i in list1:
    for row_index,row in df.iterrows(): 
        if row_index[0:2]==i[0:2]:
            list2.append(row)
            df_mj=pd.DataFrame(list2)
#-------------控制台分割符号----------#
def fg():
    print('-'*30)
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
print('>>>已进入小区阳性及密接筛选系统')
fg()
while True:
    if x==0:
        fg() 
        print('>>>在操作台输入对应数字以执行相应操作','>>>小区信息表显示:1','>>>个人信息索引:2','>>>阳性筛选:3','>>>密接筛选:4'
             '>>>密接及阳性人数条形图显示:5','>>>密接及阳性人数条形堆积图:6','>>>操作帮助中心:0','>>>结束系统:9',sep='\n')
        fg()
        x=eval(input('>>输入操作:'))
    elif x==1:
         fg()
         print(df)
         fg()
         x=eval(input('>>请输入下一步操作:'))
    elif x==2:
        fg()
        s='y'
        while True:
            if s in ['Y','y']:
                xx=input('>>请输入姓名或电话：')
                if xx in df['姓名'].tolist() or xx in df['电话'].tolist():
                  if ord(xx[0]) in [i for i in range(48,58)]:
                    print('>>查询结果如下:')
                    print(df[df['电话']==xx])
                    fg()
                    s=input('>>按(Y/y)继续查询，其他键结束查询：')
                    fg()
                  else:
                    print('>>查询结果如下:')
                    print(df[df['姓名']==xx])
                    fg()
                    s=input('>>按(Y/y)继续查询，其他键结束查询：')
                    fg()
                    
                else:
                    fg()
                    print('>>无此人信息或输入错误')
                    fg()
                    s=input('>>按(Y/y)继续查询，其他键结束查询：')
                    fg()
            else:
                print('>>查询系统结束')
                fg()
                print('>>已返回主系统')
                fg()
                print('>>输入0获取主菜单帮助')
                fg()
                break
        x=eval(input('>>请输入下一步操作:'))
                
    elif x==3:
        fg()
        print('>>已完成阳性筛选')
        yx.to_excel('核酸阳性名单.xlsx')
        print('>>已写入 核酸阳性名单.xlsx')
        fg()
        x=eval(input('>>请输入下一步操作:'))
    elif x==4:
       fg()
       print('>>已完成密接筛选')
       yx.to_excel('密接名单.xlsx')
       print('>>已写入 密接名单.xlsx')
       fg()
       x=eval(input('>>请输入下一步操作:'))
    elif x==5:
        bar_s_show(df,yx,df_mj)
        print('>>>图表已生成')
        fg()
        x=eval(input('>>请输入下一步操作:'))
    elif x==6:
        bar_d_show(df,yx,df_mj)
        print('>>>图表已生成')
        fg()
        x=eval(input('>>请输入下一步操作:'))
    else:
        print('>>>正在退出系统')
        fg()
        print('>>>已退出系统')
        break
        
        
                
                
                    
            



                
                    
            



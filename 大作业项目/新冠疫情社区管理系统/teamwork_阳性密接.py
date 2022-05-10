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
进行'核酸阳性名单.xlsx'，'密接名单.xlsx'的统计和更新
以同楼层为标准进行密接人员筛选
使用时请保证spyde里存在此三个文件且三文件处于关闭状态
有疑问或需要修改的请联系杨小天
----------------
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
import numpy as np
import matplotlib
matplotlib.rcParams['font.family']='simHei'
matplotlib.rcParams['axes.unicode_minus'] =False
df=pd.read_excel('社区信息表 .xlsx')
s=df.set_index('姓名')
#print(df[df['姓名']=='杨小'][['姓名','核酸','电话号码']])
yx=df[df['核酸']=='阳']
yx.set_index('姓名',inplace=True)
yx.to_excel('核酸阳性名单.xlsx')
dict1={}#小区人员信息字典
dict2={}#阳性人员信息字典
dict3={}#密接人员信息字典
l=[]
for row_index,row in s.iterrows():   
    str1=str(row['单元'])
    str2=str(row['楼栋'])
    str3=str(row['房间'])
    str_value=str1[0:1]+str2[0:1]+str3
    dict1[row_index]=str_value
for row_index,row in yx.iterrows():
    str1=str(row['单元'])
    str2=str(row['楼栋'])
    str3=str(row['房间'])
    str_value=str1[0:1]+str2[0:1]+str3
    dict2[row_index]=str_value
for key,value in dict2.items():
    for i,j in dict1.items():
        if j[-3]==value[-3]:
              dict3[i]=j
for key in dict3.keys():
    l.append(s.loc[key])
df_mj=pd.DataFrame(l)
df_mj.to_excel('密接名单.xlsx')
print('-----------------')
print('已统计进‘密接名单’')
print('-----------------')
dy_list=df['单元'].unique()
y1=[]
y2=[]
for i in dy_list:
    y1.append(len(yx[yx['单元']==i]))
for i in dy_list:
    y2.append(len(df_mj[df_mj['单元']==i]))
x = range((len(dy_list)))  
plt.bar(x, y1, width=0.2,color='#FF6347',label='阳性')
plt.bar([i + 0.2 for i in x], y2, width=0.2, color='#008B8B',label='密接')
plt.xticks([i + 0.1 for i in x], dy_list)   
plt.ylabel('人数')
plt.xlabel('单元')
plt.title('小区阳性及密接统计')
plt.show()    
dict4={}
count=0
for i in dy_list:
    dict4[i]=y1[count]+y2[count]
    count+=1
print('-------------------------')
print('小区阳性及密接统计')
for key,value in dict4.items():
    print('单元:',key,'隔离总人数:',value)
print('-------------------------')    
    

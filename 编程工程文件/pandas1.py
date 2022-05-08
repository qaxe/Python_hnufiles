import pandas as pd
'''
需要文件:
2017年国内主要城市年度数据.csv
'''
df=pd.read_csv('2017年国内主要城市年度数据.csv')
df.dropna(axis=1,inplace=True)
#print(df.info())
df['国内生产总值']=df.iloc[:,2]+df.iloc[:,3]+df.iloc[:,4]
df.sort_values(by='国内生产总值',ascending=False,inplace=True)
#ascending=False  降序排序
#print(df.head())
#df.to_excel('2017年国内主要城市年度数据.xlsx')

#画图
'''
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['simhei']
plt.figure(1)
plt.bar(df['地区'],df['国内生产总值'])
plt.show()

plt.figure(2)
plt.plot(df['地区'],df['社会商品零售总额'])
plt.plot(df['地区'],df['货物进出口总额']*6.6/100)
plt.legend()
plt.show()
'''
print(df[df['国内生产总值']>df['国内生产总值'].mean()]['地区'].values.tolist())
#末尾.values就是取值,但是返回的不是列表!!!
#末尾如果是.index就是取行索引
#最后的.tolist()才是变成列表
print(df.nlargest(10,'普通高等学校在校学生数')[['地区','普通高等学校在校学生数']])
#返回前n个最大值行
#返回前n个最小值行nsmallest

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('主要高耗能产品的进、出口量1.csv')
print(df.info())
df.dropna(axis=0,inplace=True)
columns=df.columns.to_list()
columns[-2]='锌及锌合金出口量(万吨)'
columns[-3]='铝材出口量(万吨)'
columns[-4]='铜材出口量(万吨)'
df.columns=columns
df['锌及锌合金出口量(万吨)']=df['锌及锌合金出口量(万吨)']/10000
df['铝材出口量(万吨)']=df['铝材出口量(万吨)']/10000
df['铜材出口量(万吨)']=df['铜材出口量(万吨)']/10000
df['金属总进口量']=df['钢材进口量(万吨)']+df['铜及铜合金进口量(万吨)']+df['铝及铝合金进口量(万吨)']
df['金属总出口量']=df['钢材出口量(万吨)']+df['铜材出口量(万吨)']+df['铝材出口量(万吨)']+df['锌及锌合金出口量(万吨)']
plt.rcParams['font.sans-serif']=['simhei']
plt.figure(1)
plt.plot(df['年份'],df['金属总进口量'],label='金属总进口量',marker='*')
plt.plot(df['年份'],df['金属总出口量'],label='金属总出口量',marker='P')
plt.legend()
plt.show()
print(df)




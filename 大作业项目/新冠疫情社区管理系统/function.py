#导入拓展
import pandas as pd
df=pd.read_excel('社区信息表 .xlsx',dtype=object)
#数据预处理
pn=df.dropna()[['姓名','单元','楼栋','房间','核酸','电话']]
#定义函数
def fgf():#分隔符
    print('#####################################')
def title(txt='新冠疫情社区管理系统'):#抬头显示
    fgf()
    print('   ***   ',txt,'   ***   ')
    print('   ***    疫情管理，高效快捷    ***   ')
    fgf()
def save():#保存表格
    df.to_excel('社区信息表 .xlsx',index=False)
class announcement():#公告系统
    def __init__(self):
        self.info=df.iloc[0,1]#从表格公告正文
    #修改公告正文
    def change(self,content):
        df.iloc[0,1]=content#修改表格公告正文
        self.info=content#修改显示公告
    def show(self):
        print('|  ***       社区公告       ***  |')
        for i in self.info.split(','):#换行输出
            if len(i)>15:#断句大于15
                print('|  '+i[:16])
                print('|  '+' '*(15-len(i[16:]))+i[16:]+' '*(15-len(i[16:])))
            else:
                print('|  '+' '*(15-len(i))+i+' '*(15-len(i)))
        fgf()
content=announcement()#实例化一个公告
def change(num):#数字大小写转化
    numlist=[1,2,3,4,5,6,7,8,9]
    NUMlist=['一','二','三','四','五','六','七','八','九']
    if num in numlist:
        return NUMlist[num-1]
def inputerror():#输入错误显示
    print('>>>错误的输入\n>>>请重新检查您的操作')

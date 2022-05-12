#导入拓展
import pandas as pd
df=pd.read_excel('社区信息表 .xlsx',dtype=object)
#定义函数
def fgf():#分隔符
    print('#####################################')
def title():#抬头显示
    fgf()
    print('   ***   新冠疫情社区管理系统   ***   ')
    print('   ***    疫情管理，高效快捷    ***   ')
    fgf()
def save():#保存表格
    df.to_excel('社区信息表 .xlsx',index=False)
class announcement():
    def __init__(self):
        self.info=df.iloc[0,1]#从表格公告正文
    #修改公告正文
    def change(self,content):
        df.iloc[0,1]=content#修改表格公告正文
        self.info=content#修改显示公告
    def show(self):
        print('   ***       社区公告       ***   ')
        for i in self.info.split(','):#换行输出
            if len(i)>15:#断句大于15
                print('>>>'+i[:16])
                print('>>>'+' '*(15-len(i))+i[16:]+' '*(15-len(i)))
            else:
                print('>>>'+' '*(15-len(i))+i+' '*(15-len(i)))
        fgf()
content=announcement()#实例化一个公告
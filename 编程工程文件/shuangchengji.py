import matplotlib.pyplot as plt
#读取文件
'''
需要文件:
双城记.txt
'''
plt.rcParams['font.sans-serif'] = ['SimHei']
file=open('双城记.txt','r')
data=file.read()
file.close()

print('包含标点的总字数:{}字'.format(len(data)))
puncs='，。：“”、；？！\n（）【】…[]？- ,.:";?!()><...'
#去重
uniqdata,wordlist=set(data.split()),[]
#去标点
for word in uniqdata:
    for a in word:
        if a in puncs:
            wordlist.append(word[:word.index(a)])
            break
    else:
        wordlist.append(word)

#二次去重
datawordnum=wordlist#不包含标点的全部英文单词数
wordlist=set(wordlist)
print('不包含标点的不同英文单词数',len(wordlist))
#重复率
worddict={}
for word in wordlist:
    worddict[word]=data.count(word)
del worddict['']#删除空值
sortlist=sorted(worddict.items(),key=lambda x:x[1],reverse=True)
count=0
print('前30个高频英文单词:')
for word in sortlist:
    count+=1
    print(word)
    if count==30:
        break
#前三十个高频英文单词出现次数画条形图
worddict30=dict(sortlist[:30])
plt.figure('fig1')
plt.bar(worddict30.keys(),worddict30.values())
plt.title('《双城记》中前30个高频单词出现次数')
plt.ylabel('出现频率')
plt.xlabel('英文单词')
plt.show()

#前三十个高频英文单词出现频率画折线图
plt.figure('fig2')
countnum=[]
for wordcount in list(worddict30.values()):
    countnum.append(wordcount/len(datawordnum))
plt.plot(list(worddict30.keys()),countnum,marker='*',color='red')
plt.grid()
plt.title('《双城记》中前30个高频单词出现频率')
plt.ylabel('出现频率')
plt.xlabel('英文单词')
plt.show()    
    


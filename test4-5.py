# 创建者：wzz
# 开发时间：2022/3/20 12:55
import random as rd
import pandas as pd
import numpy as np
import turtle as tl


def readnum():
    fd = pd.read_excel('体彩大乐透-问卷统计详情.xlsx')
    name = fd.iloc[5:, 0].values
    f5 = fd.iloc[5:, 8].values
    b2 = fd.iloc[5:, 9].values
    return name, f5, b2
    #print(f5)


if __name__ == '__main__':
    name, f5, b2 = readnum()
    #print(name, f5, b2)
    # 读入大家购买的彩票号码，name为姓名，f5为前区5个号，b2为后区两个号
    '''
    
    '''


def mngdata(name, f5, b2):
    origin = pd.DataFrame({'姓名': name, '前区': f5, '后区': b2})
    origin = origin.dropna()  # 去除Nan值
    ## 去除nan值之后，重置顺序
    origin = pd.DataFrame({'姓名': list(origin['姓名']), '前区': list(origin['前区']),
                           '后区': list(origin['后区'])})

    def mng1(origin, string, num):  # 返回bool列表
        orlst = []
        for i in origin[string]:
            if len(i) > 40:
                orlst.append(False)
                continue
            count = 0
            for j in i:
                try:
                    j = int(j)
                except:
                    j = str(j)
                    if j == ',' or j == '，':
                        count += 1
            orlst.append(count == num)
        return orlst

    # 去除那些数字的不够的同学
    newlst5 = mng1(origin, '前区', 4)
    newlst2 = mng1(origin, '后区', 1)

    # 手动实现交集
    endlst = []
    for i in range(len(newlst2)):
        if newlst2[i] == newlst5[i] and newlst2[i] == True:
            endlst.append(True)
        else:
            endlst.append(False)

    # 筛选出合格的抽奖同学
    new = origin.iloc[endlst]

    return new


new = mngdata(name, f5, b2)


# 提取抽奖的号码
def pklist(new, string):
    list5 = []
    for i in new[string]:
        temp = []
        temp1 = []
        for j in i:
            try:
                j = int(j)
                temp.append(j)
            except:
                if temp == []:
                    continue
                a = ''
                for i in temp:
                    a = a + str(i)
                temp1.append(a)
                temp = []
        a = ''
        for i in temp:
            a = a + str(i)
        temp1.append(a)
        list5.append(temp1)
    return list5


num5 = pklist(new, '前区')  # 形成前后区的数组
num2 = pklist(new, '后区')

# 把num5 的元素转成整型
for i in range(len(num5[0][:])):
    for j in range(len(num5)):
        num5[j][i] = int(num5[j][i])

# 把list2 的元素转成整型
for i in range(len(num2[0][:])):
    for j in range(len(num2)):
        num2[j][i] = int(num2[j][i])

# 生成一个抽奖用DataFrame
lottery = pd.DataFrame({'name': list(new['姓名']), 'f5': num5, 'b2': num2})
# lottery

# 随机生成一个抽奖列表，随机生成，如果已经存在，再重新生成一个，直到没有或满

def ltylist(num, bg, end):  # 数字、开始、结束范围
    ltylist = []
    count = 0
    while True:
        temp = rd.randint(bg, end)  # 使用randint函数
        if temp in ltylist:
            continue
        ltylist.append(temp)
        count += 1
        if count == num:
            break
    return ltylist


def awards(f5, b2):
    if f5 == 5 and b2 == 2:
        return '一等奖'
    if f5 == 5 and b2 == 1:
        return '二等奖'
    if f5 == 5 and b2 == 0:
        return '三等奖'
    if f5 == 4 and b2 == 2:
        return '四等奖'
    if f5 == 4 and b2 == 1:
        return '五等奖'
    if f5 == 3 and b2 == 2:
        return '六等奖'
    if f5 == 4 and b2 == 0:
        return '七等奖'
    if f5 == 3 and b2 == 1:
        return '八等奖'
    if f5 == 2 and b2 == 2:
        return '八等奖'
    if f5 == 3 and b2 == 0:
        return '九等奖'
    if f5 == 2 and b2 == 1:
        return '九等奖'
    if f5 == 1 and b2 == 2:
        return '九等奖'
    if f5 == 0 and b2 == 2:
        return '九等奖'
    else:
        return 0


# 查看中奖类型，通过计算号码相同的个数实现
def awdtyp(f2l, b2l):
    f5num = 0
    b2num = 0
    for i in f2l:
        if i in f5ltylist:
            f5num += 1
    for i in b2l:
        if i in b2ltylist:
            b2num += 1
    return awards(f5num, b2num)


# 创建一个字典计数器，再把它添加到一个列表中，再拿另外一个列表放名字，通过元素的位置来区分，每人的中奖情况
ZJdict = {}
ZJlist = []
ZJname = []


def awdlist(ZJname, ZJlist, ZJdict, f2l, b2l, i):
    if i not in ZJname:
        ZJname.append(i)
        ZJdict = {}
        ZJdict[awdtyp(f2l, b2l)] = 1
        ZJlist.append(ZJdict)
    else:
        inDEX = ZJname.index(i)
        if awdtyp(f2l, b2l) not in ZJlist[inDEX]:
            ZJlist[inDEX][awdtyp(f2l, b2l)] = 1
        else:
            ZJlist[inDEX][awdtyp(f2l, b2l)] += 1

#print(ZJdict)


# 抽
for _ in range(1):
    f5ltylist = (5, 1, 35)
    b2ltylist = ltylist(2, 1, 12)
    for i in range(len(lottery)):
        if awdtyp(lottery.loc[i]['f5'], lottery.loc[i]['b2']) != 0:
            awdlist(ZJname, ZJlist, ZJdict, lottery.loc[i]['f5'], lottery.loc[i]['b2'], lottery.loc[i]['name'])
            print(lottery.loc[i]['f5'], lottery.loc[i]['b2'], lottery.loc[i]['name'],
                  awdtyp(lottery.loc[i]['f5'], lottery.loc[i]['b2']))

            # 开始画图
            tl.screensize(600, 400, 'white')
            tl.pensize(2)
            tl.hideturtle()

            tl.penup()
            tl.goto(-120, 150)
            tl.write(lottery.loc[i]['f5'], True, align='center', font=("Arial", 25, "normal"))
            tl.goto(-120, 0)
            tl.write(lottery.loc[i]['b2'], True, align='center', font=("Arial", 25, "normal"))
            tl.goto(-120, -150)
            #tl.write(lottery.loc[i]['name'], True, align='center', font=("Arial", 25, "normal"))
            #tl.goto(90, -150)
            #tl.write(awdtyp(lottery.loc[i]['f5'], lottery.loc[i]['b2']),
            #         True, align='center', font=("Arial", 25, "normal"))
            tl.exitonclick()
            #tl.pendown()
            break
print(i)

#print(len(lottery))
'''
# 把中奖结果放到DataFrame中

ds1 = pd.DataFrame.from_dict(ZJlist[:])

namedf = pd.DataFrame({'姓名': ZJname})
ds2 = ds1.join(namedf)

# 重新排列列的顺序
ds2 = ds2[['姓名', '九等奖', '八等奖', '七等奖', '六等奖', '五等奖']]
ds2 = ds2.replace(np.nan, 0)
# ds2
'''
'''
#开始画图
tl.screensize(600, 400, 'white')
tl.pensize(2)
tl.hideturtle()
for j in range(0, 5):
    tl.penup()
    tl.goto(i*150-290, 150)
    tl.goto(i*125-290, 125)
    #turtle.write()
    tl.pendown()
    tl.circle(50)
'''

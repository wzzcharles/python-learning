# 创建者：wzz
# 开发时间：2022/4/3 15:41

import pandas as pd
import xarray as xr
import struct

#------------------文件处理-------------------#
f = open(r'E:\Work\Python\test6-7\rmm.74toRealtime.txt', 'r')     #打开文件
dat = f.readlines()                                             #按行读入文件
#print(dat)
d = []                                  #建立一个新数组以便于存放中间数据
for i in range(0, len(dat)):            #以行为单位循环，跳过前两行带字的内容
    if i >= 2:
        dat[i].rstrip(r'\n')            #去除字符串内的转义字符'\n'，右端去除
        d.append(dat[i].split())        #在d[]中添加新的数据，将原来的字符串打散，组为单位存入新的列表单位
        #print(d)
    else:
        continue
print(len(d))                           #查看新列表d[]元素个数
print(len(dat))                         #查看老列表（原始数据）的行数

year = []                               #建立列分类，列表形式，为之后存为Dataframe做准备
month = []
day = []
RMM1 = []
RMM2 = []
phase = []
amplitude = []
Final_Value = []
var = [year, month, day, RMM1, RMM2,
       phase, amplitude, Final_Value]    #分类列表放进大列表里面
for i in range(len(d)):
    for j in range(8):
        if (j == 0) or (j == 1) or (j == 2) or (j == 5):
            var[j].append(int(d[i][j]))           #分别存入数据到每个类别的列表里面
        elif j == 7:
            var[j].append(d[i][j])
        else:
            var[j].append(float(d[i][j]))

field = ['year', 'month', 'day', 'RMM1', 'RMM2',
         'phase', 'amplitude', 'Final_Value']
for i in range(len(d)):
    data = dict(zip(field, var))         #合成字典
df = pd.DataFrame.from_dict(data)        #字典变成Dataframe形式
print(df)
#print(data)
print(type(df))

#------------------保存为CSV格式文件--------------------#
df.to_csv('rmm.74toRealtime.csv')   #dataframe里面有直接保存为CSV格式文件的库
'''
    csvr = csv.reader(f)
with open('rmm.74toRealtime.csv', 'r') as f:
    for row in csvr:
        print(row)
'''


#------------------保存为Excel格式的文件-------------------#
df.to_excel('rmm.74toRealtime.xlsx')    #dataframe里面有直接保存为xlsx格式文件的库
f.close()


#------------------保存为二进制文件----------------------#
vars = ['RMM1', 'RMM2']     #建立两个变量
fb = open('rmm.74toRealtime.dat', 'wb')     #新建一个文件，wb是以二进制写入的标志
for i in vars:
    for j in df[i].values:
        tmp = struct.pack('f', j)       #dataframe里面挑选特定个变量的数据，遍历后改成二进制格式写入
fb.write(tmp)       #写入
fb.close()


#------------------保存为netCDF格式文件-------------------#
date = pd.date_range(start='1974-06-01', end='2022-03-25', freq='D')    #pandas里面有时间创建的函数date_range，直接帮你把时间写好
ds = xr.Dataset({'RMM1': (['time'], data['RMM1']),
                 'RMM2': (['time'], data['RMM2'])},
                coords={'time': date})      #dataset函数格式，{变量名：（【维度】，数据）， ...）coords={维度字典}
print(ds.data_vars)
ds.to_netcdf('rmm.74toRealtime.nc')     #to_netcdf是直接将dataset写成.nc格式文件的函数
ds.close()


#-------------------.grib文件转换----------------------#
dg = xr.open_dataset(r'E:\work\python\test6-7\20200405.grib', engine='cfgrib')      #cfgrib需要虚拟环境，需要安装库：将其读成dataset
dg.to_netcdf('20200405.nc')     #dataset写成.nc格式文件
dg.close()


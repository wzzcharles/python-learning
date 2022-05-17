# # 第八次作业：
# #这是一个学习matplotlib的小代码


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel(r'E:\work\python\test6-7\rmm.74toRealtime.xlsx')
# 筛选数据：2015-2020年, 14827行，2015年开始；17018行，2020年结束
data = df.loc[(df['year'] >= 2015) & (df['year'] <= 2020)]
print(len(df))
print(df.loc[0])


d1 = []
mt = []
mth = range(1, 13)
yr = range(2015, 2021)

for i in yr:
    for j in mth:
        c = data.loc[(data['year'] == i) & (data['month'] == j)]
        # print(c)
        a = c.groupby('month').mean()
        # print(a)
        d1.append(a)
# print(d1)

for i in range(len(d1) - 1):
    if i == 0:
        usedata = pd.concat([d1[i], d1[i + 1]])
    else:
        usedata = pd.concat([usedata, d1[i + 1]])
# usedata.drop(['Unnamed: 0', 'day'], axis=1, inplace=True)
print(usedata)


def drawpaper():  # 设置坐标轴样式，画图基本设置
    fig = plt.figure(figsize=(9, 6))
    ax = fig.subplots(1, 1)
    ax.set_xlabel('Time')
    ax.set_ylabel('amplitude')
    year = ['2015', '2016', '2017', '2018', '2019', '2020']
    plt.xticks(list(np.arange(0, 72, 12)), year)
    return ax, fig


# ------------------第一问———————————————————— #
# 画折线图
ax1, fig = drawpaper()
ax1.plot(np.arange(len(usedata)), usedata['amplitude'], color='b')
ax1.set_title('MJO_amplitude_plot')
plt.savefig(r'E:\Work\Python\test8\picture1-1.png')

# 画散点图
ax2, fig = drawpaper()
ax2.scatter(np.arange(len(usedata)), usedata['amplitude'], color='b')
ax2.set_title('MJO_amplitude_scatter')
plt.savefig(r'E:\Work\Python\test8\picture1-2.png')

# 画柱状图
ax3, fig = drawpaper()
ax3.bar(np.arange(len(usedata)), usedata['amplitude'], color='b')
ax3.set_title('MJO_amplitude_bar')
plt.savefig(r'E:\Work\Python\test8\picture1-3.png')

# 画阶梯状图
ax4, fig = drawpaper()
ax4.step(np.arange(len(usedata)), usedata['amplitude'], color='b')
ax4.set_title('MJO_amplitude_step')
plt.savefig(r'E:\Work\Python\test8\picture1-4.png')

# 画茎叶图
ax5, fig = drawpaper()
ax5.stem(np.arange(len(usedata)), usedata['amplitude'])
ax5.set_title('MJO_amplitude_stem')
plt.savefig(r'E:\Work\Python\test8\picture1-5.png')

# ------------------第二问------------------- #
ax, fig = drawpaper()
ax.plot(np.arange(len(usedata)), usedata['amplitude'], color='r')
ax_another = ax.twinx()
ax_another.plot(np.arange(len(usedata)), usedata['phase'], color='b')
ax_another.set_ylabel('phase')
ax.set_title('MJO_amplitude&phase_mutiple')
plt.savefig(r'E:\Work\Python\test8\picture2.png')

# ------------------第三问------------------ #
ax, fig = drawpaper()
ax.scatter(np.arange(len(usedata)), usedata['amplitude'], color='r')
ax_another = ax.twinx()
ax_another.stem(np.arange(len(usedata)), usedata['phase'])
ax_another.set_ylabel('phase')
ax.set_title('MJO_amplitude&phase_mutiple')
plt.savefig(r'E:\Work\Python\test8\picture3.png')

df['RMM1'] = df['RMM1'].replace(df['RMM1'].max(), 0)
df['RMM2'] = df['RMM2'].replace(df['RMM2'].max(), 0)

# -----------------第四问------------------- #
fig1 = plt.figure(figsize=(9, 6))
ax5 = fig1.subplots(1, 1)
ax5.hist(df['RMM1'])
ax5.set_title('MJO_RMM1_hist')
# plt.show()
plt.savefig(r'E:\Work\Python\test8\picture4-1.png')

# -----------------第五问------------------- #
fig2 = plt.figure(figsize=(9, 6))
ax6 = fig2.subplots(1, 1)
for i in np.arange(1, 9):
    ph = df['amplitude'].loc[df['phase'] == i]
    ax6.boxplot(ph, positions=[i])
ax6.set_title('MJO_amplitude_boxplot')
plt.savefig(r'E:\Work\Python\test8\picture5-1.png')

# ----------------第六问--------------------#
usermm1 = df['RMM1'].loc[:len(df)-16]
usermm2 = df['RMM2'].loc[15:]
fig3 = plt.figure(figsize=(9, 6))
ax7 = fig3.subplots(1, 1)
ax7.hist2d(usermm1, usermm2, cmap='Blues')
ax7.set_xlabel('usermm1')
ax7.set_ylabel('usermm2')
ax7.set_title('MJO_RMM1&RMM2_hist')
plt.savefig(r'E:\Work\Python\test8\picture6-1.png')

# ----------------第七问-------------------- #
fig4 = plt.figure(figsize=(9, 6))
ax8 = fig4.subplots(1, 1)
ph = []
for i in np.arange(1, 9):
    ph.append(len(df[df['phase'] == i]))
labels = ['1', '2', '3', '4', '5', '6', '7', '8']
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(labels)))
ax8.pie(ph, labels=labels, colors=colors, autopct='%1.1f%%')
ax8.set_title('MJO_phase_pie')
plt.savefig(r'E:\Work\Python\test8\picture7-1.png')

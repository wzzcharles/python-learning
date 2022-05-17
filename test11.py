#!/usr/bin/env python
# coding: utf-8

# # python第十一次作业
# 
# 关于ENSO的计算

# ## 前期处理

# In[1]:


import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.ticker import MultipleLocator


# In[2]:


plt.rcParams['font.sans-serif'] = ['SimHei']  # 防止无法显示中文并设置黑体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# In[3]:


# 读取文件
ds = xr.open_dataset(r'E:\Work\Python\test9\sst.mnmean.nc')['sst']
ds


# In[4]:


def drawmap():
    proj = ccrs.PlateCarree(central_longitude=180)
    fig = plt.figure(figsize=(9, 6))
    ax = fig.subplots(1, 1, subplot_kw={'projection': proj})
    # 海岸线
    ax.coastlines('110m')
    # 标注坐标轴
    majorticks = MultipleLocator(30)
    ax.gridlines(draw_labels={"bottom": "x", "left": "y"}, color='gray', alpha=0.5, 
                 linestyle=':', auto_inline=False, rotate_labels=False, xlocs=majorticks)
    return ax, fig


# In[5]:


def drawpaper():  # 设置坐标轴样式，画图基本设置
    fig = plt.figure(figsize=(9, 6))
    ax = fig.subplots(1, 1)
    ax.set_xlabel('Time')
    ax.set_ylabel('Tmeperature')
    return ax, fig


# ## 画图第一部分，计算2020年冬季平均

# In[6]:


winter = ds.loc[np.datetime64('2020-12-01'):np.datetime64('2021-02-01'), :, :]
winter = winter.mean(dim='time')
winter


# In[7]:


lonw = winter['lon'].data
latw = winter['lat'].data
print(winter.max(), winter.min())


# In[8]:


ax1, fig1 = drawmap()
line = ax1.contour(lonw, latw, winter, levels=np.arange(-2, 33, 3), colors='k', linewidths=1, transform=ccrs.PlateCarree())
ax1.clabel(line, inline=True, fontsize=10, fmt='%.0f')
shaded = ax1.contourf(lonw, latw, winter, levels=np.arange(-2, 33, 3), cmap='coolwarm', transform=ccrs.PlateCarree())
cb=fig1.colorbar(shaded, extendrect='True', pad=0.03, fraction=0.1, shrink=0.7, location='bottom', panchor=(0.5, 0.5))
ax1.set_title('winter-sst-2020')
plt.show()


# ## 画图第二部分

# In[9]:


# 168年平均二维
enso_ave = ds.loc[:, 6: -6, 170:240]
lone = enso_ave['lon'].data
late = enso_ave['lat'].data
# print(enso_winter.max(), enso_winter.min())
enso_ave = enso_ave.mean(dim='time')
enso_ave


# In[10]:


# 二维作图
ax2, fig2 = drawmap()
majorticks = MultipleLocator(10)
# ax2.xaxis.set_major_locator(majorticks)
line = ax2.contour(lone, late, enso_ave, levels=np.arange(24, 31, 0.5), colors='k', linewidths=1, transform=ccrs.PlateCarree())
ax2.clabel(line, inline=True, fontsize=10, fmt='%.1f')
ax2.contourf(lone, late, enso_ave, levels=np.arange(24, 30, 1), cmap='OrRd', transform=ccrs.PlateCarree())
ax2.gridlines(draw_labels={"bottom": "x", "left": "y"}, color='gray', alpha=0.5, linestyle=':', 
             auto_inline=False, rotate_labels=False, xlocs=majorticks)
ax2.set_title('winter-sst-2020-enso')
plt.show()


# In[11]:


# 168年，年平均一维
enso_yearave = ds.loc[:, 6: -6, 170:240].mean(dim=['lat', 'lon'])
enso_yearave = enso_yearave.groupby(enso_yearave.time.dt.year).mean(dim='time')
enso_yearave


# In[12]:


# 一维作图
ax22, fig22 = drawpaper()
ax22.plot(enso_yearave['year'], enso_yearave, color='steelblue')
ax22.set_xlim(1850,2024)
ax22.set_title('ENSO_ave_plot')
plt.show()


# ## 画图第三部分

# In[13]:


# 2020年平均二维，四季
spring = ds.loc[np.datetime64('2020-03-01'):np.datetime64('2021-05-01'), :, :]
summer = ds.loc[np.datetime64('2020-06-01'):np.datetime64('2021-08-01'), :, :]
autumn = ds.loc[np.datetime64('2020-09-01'):np.datetime64('2021-11-01'), :, :]
spring = spring.mean(dim='time')
summer = summer.mean(dim='time')
autumn = autumn.mean(dim='time')
print(spring.max(), spring.min())
print(summer.max(), summer.min())
print(autumn.max(), autumn.min())


# In[14]:


# 二维作图
ax3, fig3 = drawmap()
line = ax3.contour(lonw, latw, spring, levels=np.arange(-2, 33, 3), colors='k', linewidths=1, transform=ccrs.PlateCarree())
ax3.clabel(line, inline=True, fontsize=10, fmt='%.0f')
shaded = ax3.contourf(lonw, latw, spring, levels=np.arange(-2, 33, 3), cmap='coolwarm', transform=ccrs.PlateCarree())
cb=fig3.colorbar(shaded, extendrect='True', pad=0.03, fraction=0.1, shrink=0.7, location='bottom', panchor=(0.5, 0.5))
ax3.set_title('spring-sst')

ax4, fig4 = drawmap()
line = ax4.contour(lonw, latw, summer, levels=np.arange(-2, 33, 3), colors='k', linewidths=1, transform=ccrs.PlateCarree())
ax4.clabel(line, inline=True, fontsize=10, fmt='%.0f')
shaded = ax4.contourf(lonw, latw, summer, levels=np.arange(-2, 33, 3), cmap='coolwarm', transform=ccrs.PlateCarree())
cb=fig4.colorbar(shaded, extendrect='True', pad=0.03, fraction=0.1, shrink=0.7, location='bottom', panchor=(0.5, 0.5))
ax4.set_title('summer-sst')

ax5, fig5 = drawmap()
line = ax5.contour(lonw, latw, autumn, levels=np.arange(-2, 33, 3), colors='k', linewidths=1, transform=ccrs.PlateCarree())
ax5.clabel(line, inline=True, fontsize=10, fmt='%.0f')
shaded = ax5.contourf(lonw, latw, autumn, levels=np.arange(-2, 33, 3), cmap='coolwarm', transform=ccrs.PlateCarree())
cb=fig5.colorbar(shaded, extendrect='True', pad=0.03, fraction=0.1, shrink=0.7, location='bottom', panchor=(0.5, 0.5))
ax5.set_title('autumn-sst')
plt.show()


# In[15]:


# 168年四季，一维
enso_season = ds.loc[:, 6: -6, 170:240].mean(dim=['lat', 'lon'])
enso_season = enso_season.groupby(enso_season.time.dt.season).mean(dim='time')
enso_season


# In[16]:


# 一维作图
ax32, fig32 = drawpaper()
bar = ax32.bar(enso_season['season'], enso_season, width=0.5, color='steelblue')
plt.bar_label(bar, label_type='edge')
ax32.set_title('ENSO_season_bar')
plt.show()


# ## 画图第四部分

# In[17]:


# 168年nino3.4区范围平均值
enso_ave = enso_ave.mean(dim=['lat','lon'])
enso_ave


# In[18]:


enso_jp = enso_yearave - enso_ave
enso_jp


# In[19]:


ElNino = []
LaNina = []
for i in enso_jp['year']:
    if enso_jp.loc[i]>=0.5:
        ElNino.append(int(i.data))
    if enso_jp.loc[i]<=-0.5:
        LaNina.append(int(i.data))


# In[20]:


print(ElNino, LaNina)


# In[21]:


ax42, fig42 = drawpaper()
ax42.plot(enso_jp['year'], enso_jp, color='steelblue', label='距平')
ax42.axhline(y=0.5,color='k',linestyle="--", label='界定范围')
ax42.axhline(y=-0.5,color='k',linestyle="--")
ax42.set_xlim(1850,2024)
ax42.set_title('ENSO_jp_plot')
plt.show()


# In[ ]:





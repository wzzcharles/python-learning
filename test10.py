# 创建者：wzz
# 开发时间：2022/4/25 16:52

import numpy as np      # 数据处理用
import xarray as xr
import matplotlib.pyplot as plt     # 画图用
import cartopy.crs as ccrs      # 投影用
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
from cartopy.util import add_cyclic_point
import cartopy.feature as cfeature


# -----------------------作业1----------------------------#
def drawmap():
    fig = plt.figure(figsize=(9, 6))    # 画布大小
    ax_1 = fig.subplots(1, 1, subplot_kw={'projection': ccrs.PlateCarree()})      # 画图个数
    ax_1.coastlines('110m')
    ax_1.set_xticks(np.arange(-180, 181, 30), crs=ccrs.PlateCarree())     # 标注xy坐标轴
    ax_1.set_yticks(np.arange(-90, 91, 30), crs=ccrs.PlateCarree())
    lonformat = LongitudeFormatter(zero_direction_label=False)      # 坐标轴设置成经纬度格式，把0经度设置不加E和W
    latformat = LatitudeFormatter()
    ax_1.xaxis.set_major_formatter(lonformat)     # 经纬度格式确认
    ax_1.yaxis.set_major_formatter(latformat)
    ax_1.gridlines(draw_labels=False, color='gray', alpha=0.5, linestyle=':')
    ax_1.set_xlabel('longitude')
    ax_1.set_ylabel('latitude')
    return ax_1, fig


def drawmap_1():
    fig_2 = plt.figure(figsize=(9, 6))  # 画布大小
    ax_2 = fig_2.subplots(1, 1, subplot_kw={'projection': ccrs.Robinson()})     # 画图个数，类型
    ax_2.set_global()       # 坐标全屏
    ax_2.coastlines('110m')     # 海岸线（分辨率）
    ax_2.add_feature(cfeature.LAND, color='white')      # 陆地颜色：白色
    ax_2.add_feature(cfeature.OCEAN, color='skyblue')      # 海洋颜色： 蓝色
    ax_2.gridlines(draw_labels=True, color='gray', alpha=0.5, linestyle=':')    # 画网格线
    return ax_2, fig_2


# 数据处理
datas = xr.open_dataset(r'E:\Work\Python\test9\sst.mnmean.nc')     # 读数据
datav = xr.open_dataset('ERA5_uv_202111.nc')
# print(datas)
# print(datav)
sst1 = datas['sst'].loc[np.datetime64('2016-01-01'), :, :]      # 时间筛选
sst2 = datas['sst'].loc[np.datetime64('2017-07-01'), :, :]
# print(sst1)
print(sst1.max(), sst1.min())       # 挑出最大最小值
Latitude = datas['lat'].data        # 提取经纬度
Longitude = datas['lon'].data
lat = datav['latitude'].data        # 提取经纬度
lon = datav['longitude'].data
# Longitudes, Latitudes = np.meshgrid(Longitude, Latitude)
# print(Longitudes)
usesst1, uselongitude1 = add_cyclic_point(sst1, coord=Longitude)    # 防止画出白线，中心纬度添加
usesst2, uselongitude2 = add_cyclic_point(sst2, coord=Longitude)

# 画图
canvas = ccrs.PlateCarree(central_longitude=0)  # 中心纬度180
# 画第一张图
ax1, fig1 = drawmap()
contour = ax1.contour(uselongitude1, Latitude, usesst1, levels=np.arange(-3, 33, 3),
                      colors='k', linewidths=1, transform=canvas)     # 画等值线
plt.clabel(contour, inline=True, fontsize=8, fmt='%.0f')    # 标注等值线图
contour = ax1.contourf(uselongitude1, Latitude, usesst1, cmap='coolwarm', levels=np.arange(-3, 33, 3),
                       transform=canvas)     # 画填色图
plt.colorbar(contour, shrink=0.5, orientation='horizontal')    # 设置色标，使色标横向
ax1.set_facecolor('silver')
ax1.set_title('Picture1:sst_2016-1', loc='center')   # 写个标题，居中
fig1.savefig('picture1-sst_2016-1')     # 存文件
# 画第二张图
ax2, fig2 = drawmap()
contour = ax2.contour(uselongitude2, Latitude, usesst2, levels=np.arange(-3, 33, 3),
                      colors='k', linewidths=1, transform=canvas)     # 画等值线
plt.clabel(contour, inline=True, fontsize=8, fmt='%.0f')    # 标注等值线图
contour = ax2.contourf(uselongitude2, Latitude, usesst2, cmap='coolwarm', levels=np.arange(-3, 33, 3))     # 画填色图
plt.colorbar(contour, shrink=0.5, orientation='horizontal')    # 设置色标，使色标横向
ax2.set_facecolor('silver')
ax2.set_title('Picture2:sst_2017-7', loc='center')   # 写个标题，居中
fig2.savefig('picture2-sst_2017-7')     # 存文件


# ------------------------作业2-------------------------- #
ax3, fig3 = drawmap_1()
quiver = ax3.barbs(lon[::30], lat[::30],
                   datav['u10'].loc['2021-11-01', ::30, ::30].data,
                   datav['v10'].loc['2021-11-01', ::30, ::30].data,
                   sizes=dict(emptybarb=0.07, spacing=0.1, height=1), length=3,
                   color='k', barb_increments=dict(half=2, full=4, flag=20),
                   transform=ccrs.PlateCarree())     # 画矢量图
# ax3.quiverkey(quiver, 0.8, 0.9, 5, '5 m '+r'$s^{-1}$', labelpos='E', coordinates='figure')
ax3.set_title('Picture3:uv_2021-11', loc='center')   # 写个标题，居中
fig3.savefig('picture3-uv_2021-11')     # 存文件


# ------------------作业3---------------------- #
ax4, fig4 = drawmap()
contour = ax4.contourf(uselongitude1, Latitude, usesst1, cmap='coolwarm', levels=np.arange(-3, 33, 3))
plt.colorbar(contour, shrink=0.5, orientation='horizontal')    # 设置色标，使色标横向
ax4.barbs(lon[::30], lat[::30],
          datav['u10'].loc['2021-11-01', ::30, ::30].data,
          datav['v10'].loc['2021-11-01', ::30, ::30].data,
          sizes=dict(emptybarb=0.07, spacing=0.1, height=1), length=3,
          color='k', barb_increments=dict(half=2, full=4, flag=20),
          transform=ccrs.PlateCarree())
ax4.add_feature(cfeature.LAND, color='white')
# ax4.quiverkey(quiver, 0.8, 0.9, 5, '5 m '+r'$s^{-1}$', labelpos='E', coordinates='figure')
ax4.set_title('Picture4:sst_2016-1 & uv_2021-11', loc='center')   # 写个标题，居中
fig4.savefig('picture4-sst_2016-1_&_uv_2021-11')     # 存文件

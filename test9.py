# 创建者：wzz
# 开发时间：2022/4/23 20:17

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

# ------------------第一问------------------- #
data = xr.open_dataset('sst.mnmean.nc')     # 读数据
print(data)
# print(data['time'])
sst = data['sst'].loc[np.datetime64('2010-01-01'):np.datetime64('2020-12-01'), 0, 80:140]      # 时间以及经度筛选
# print(sst)

fig = plt.figure(figsize=(9, 6))    #画布大小
ax = fig.subplots(1, 1)     # 画图个数
contour = ax.contourf(sst['lon'].data, sst['time'].data, sst.data, cmap='bwr')      # 画填色图
plt.colorbar(contour, extendrect='True', pad=0.03, fraction=0.04, shrink=1)     # 色条标注
ax.set_xlabel = 'Longitude'     # x，y轴标记
ax.set_ylabel = 'Time'
fig.suptitle('Longitude-Time 2Dshade')      # 标题
fig.savefig('picture1-2Dsst')   # 存文件

# ------------------第二问------------------- #
data1 = xr.open_dataset('ERA5_uv_202111.nc')
print(data1)
fig1 = plt.figure(figsize=(9, 6))    #画布大小
ax1 = fig1.subplots(1, 1, subplot_kw={'projection': ccrs.PlateCarree()})      # 画图个数
ax1.coastlines('110m')
Latitude = data1['latitude'].data
Longitude = data1['longitude'].data
Longitudes, Latitudes = np.meshgrid(Longitude, Latitude)
print(Longitudes)
ax1.quiver(Longitudes[::50, ::50], Latitudes[::50, ::50],
           data1['u10'].loc['2021-11-01', ::50, ::50].data,
           data1['v10'].loc['2021-11-01', ::50, ::50].data,
           color='skyblue')
ax1.set_xticks(np.arange(-180, 181, 30), crs=ccrs.PlateCarree())     #标注xy坐标轴
ax1.set_yticks(np.arange(-90, 91, 30), crs=ccrs.PlateCarree())
lonformat = LongitudeFormatter(zero_direction_label=False)      # 坐标轴设置成经纬度格式，把0经度设置不加E和W
latformat = LatitudeFormatter()
ax1.xaxis.set_major_formatter(lonformat)     #经纬度格式确认
ax1.yaxis.set_major_formatter(latformat)
fig1.suptitle('uv_wind_quiver')      # 标题
fig1.savefig('picture1-uv_wind_quiver')   # 存文件

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# readfile()#读取测站坐标文件存放于列表 sites lons lats N_G N_E N_C N_J
plt.figure(figsize=(12,9))
mymap = Basemap(projection='robin', lat_0=0, lon_0=0,resolution='i',
                area_thresh=5000.0)
mymap.fillcontinents(color='white', lake_color='lightskyblue')
mymap.drawmapboundary(fill_color='skyblue')
mymap.drawmeridians(np.arange(0, 360, 60), labels=[1,0,0,1])
mymap.drawparallels(np.arange(-90, 90.001, 30), labels=[1,0,0,1])
# x, y = mymap(lons, lats)

# for name,lon,lat,n_G,n_E,n_J,n_C in zip(sites,x,y,N_G,N_E,N_J,N_C):
#     print (name, lon, lat,n_G,n_E,n_J,n_C)
#     if n_J>0:#可设置不同标记，大小和颜色，此处可根据需要替换为DOP值等
#         plt.plot(lon, lat, marker='o', color='red', markersize=9)
#     if n_C>0:
#         plt.plot(lon, lat, marker='o', color='blue', markersize=7)
#     if n_E>0:
#         plt.plot(lon, lat, marker='o', color='green', markersize=5)
#     if n_G>0:
#         plt.plot(lon, lat, marker='o', color='yellow', markersize=3)
plt.legend(loc=0)
plt.show()
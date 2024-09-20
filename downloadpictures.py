import re
import urllib.request

# ------ 通过网络代理的方法 ---
def httpGet(url):
	proxy = urllib.request.ProxyHandler(
		{"http": "username:psw@proxyadress:port", "https": "username:psw@proxyadress:port"})
	opener = urllib.request.build_opener(proxy)
	request = urllib.request.Request(url)
	response = opener.open(request)
	return response


# ------ 获取网页源代码的方法 ---
def getHtml(url):
	html = httpGet(url).read().decode('windows-1252')
	return html


# ------ getHtml()内输入URL ------
html = getHtml("https://apod.nasa.gov/apod/astropix.html")


# ------ 获取URL内所有图片地址的方法 ------
def getImg(html):
	reg = r'SRC="([.*\S]*\.jpg)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre, html)
	return imglist

imgList = getImg(html)

# ------ 以图片下载日期为文件命名 ------
from datetime import datetime
# import random

if imgList.__len__() > 0:
	img_url = "https://apod.nasa.gov/apod/" + imgList[0]
	date = datetime.now().date().strftime('%Y%m%d')
	f = open("D:\\pictures\\" + date + '.jpg', 'wb')
	f.write(httpGet(img_url).read())
	f.close()



    # key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
    #                         "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
        # win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # ------ 2拉伸适应桌面,0桌面居中 ------
    # win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bmpFile, 1 + 2)

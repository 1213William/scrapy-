import requests
from fake_useragent import UserAgent

headers = {
    'user-agent': UserAgent(verify_ssl=False).chrome
}

res = requests.get('http://pic1.win4000.com/wallpaper/2019-09-19/5d832c565ecb4.jpg', headers=headers).content

                  # http://pic1.win4000.com/wallpaper/2019-09-19/5d832c565ecb4.jpg
                  # http://pic1.win4000.com/wallpaper/2019-09-19/5d832c5821fe4.jpg
                  # http://pic1.win4000.com/wallpaper/2019-09-19/5d832c5933672.jpg
                  # http://pic1.win4000.com/wallpaper/2019-09-19/5d832c5a3ce27.jpg
                  # http://pic1.win4000.com/wallpaper/2018-11-26/5bfb4d7e1118c.jpg
with open('a.jpg', 'wb') as f:
    f.write(res)


print(res)

a ='fasdfa'
a.sp
# http://www.win4000.com/wallpaper_detail_136398.html
执行 run.py 启动爬虫。自动抓取贝壳找房武汉市房租信息，更改 start_url 可以更换新房，二手房及城市。

为了避免 ip 被封禁，设置了 DOWNLOAD_DELAY = random.randint(2,5) 延时操作。如需高效爬取可以设置代理服务器，以及分布式部署。

程序会自动将数据保存为 Excel 文件至windows桌面，可自行更改目录。
默认关闭了 MySQL、MongoDB 存储中间件，如有需要可以连接上自己的数据库。

最终效果如图所示![result](C:\Users\xiaobai\Desktop\github\program\fangzu\result.png)

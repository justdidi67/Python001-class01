使用scrapy框架爬取网站信息大概步骤
1，创建项目：scrapy startproject 项目名
2，创建一个spider：scrapy genspider spider_name 网址
3，在settings.py中，修改robots协议
4，在新建好的spider中，初始化start_urls列表，告诉scrapy要下载的网页有哪些
5，添加请求头，请求头需要在settings.py配置文件中设置，也可加cookies的设置
6，在spider文件中的parse方法里测试是否能够获取到页面数据
7，在items.py中，定义我们要爬取的字段是那些
8，在maoyan_spider.py的文件中的parse方法中实例化一个item，别忘了导包，并且提取数据
9，存数据：把所有数据获取，将提取出的数据存到item对象中
10，将拿到的数据，保存到mongoDB中的操作步骤
  a,将提取完全的item去yeild出来（yield item），次数scrpy就会将这个传入到下面
  b,要使用popelines.py中的item，必须需要配置
  c,在items.py中重新插入一个字段
  d,在popelines.py
  e,查询数据库是否有数据

  链接：https://blog.csdn.net/qq_40558166/article/details/103016042


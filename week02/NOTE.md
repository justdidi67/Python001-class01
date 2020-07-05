学习笔记

一、异常捕获
在python中所有的异常父类就是BaseException。
python中的异常可以分为四大类：
1.systemExit：python退出异常。
2.KeyboardInterrupt：键盘打断（CTRL + C）
3.GeneratorExit：生成器退出
4.Exception：普通异常（我们只会使用这部分异常）

二、pymysql
pymysql安装：pip install pymysql
pymysql中所有的有关更新数据（insert，update，delete）的操作都需要commit，否则无法将数据提交到数据库，既然有了commit()，就一定有对应的rollback（）,commit()表示提交，rollback()表示回滚
调用无参数存储过程：可以使用cursor.callproc('p2') #等价于cursor.execute("call p2()")
调用有参数的存储过程：cursor.callproc('p1', args=(1, 22, 3, 4))
关于pymysql防注入，字符串拼接查询，容易造成注入，为了避免注入，使用pymysql提供的参数化语句

三、Middleware

爬去一个资源链接的流程，首先我们配置spider相关的爬取信息，在启动爬取实例后，scrapy_engine从Spider取出Request（经过SpiderMiddleware），然后丢给Scheduler（经过SchedulerMiddleware），Scheduler接着把请求丢给Downloader（经过DownloadMiddlware），Downloader把请求结果丢还给Spider，然后Spider把分析好的结构化数据丢给Pipeline，Pipeline进行分析保存或丢弃，这里面有4个角色

scrapy有下面三种middlewares

SpiderMiddleware：通常用于配置爬虫相关的属性，引用链接设置，Url长度限制，成功状态码设置，爬取深度设置，爬去优先级设置等
DownloadMiddlware：通常用于处理下载之前的预处理，如请求Header（Cookie,User-Agent），登录验证处理，重定向处理，代理服务器处理，超时处理，重试处理等

1. SpiderMiddleware
爬虫中间件有下面几个方法
process_spider_input：当response通过spider的时候被调用，返回None（继续给其他中间件处理）或抛出异常（不会给其他中间件处理，当成异常处理）
process_spider_output：当spider有item或Request输出的时候调动
process_spider_exception：处理出现异常时调用
process_start_requests：spider当开始请求Request的时候调用

2. DownloaderMiddleware
下载中间件有下面几个方法
process_request：请求通过下载器的时候调用
process_response：请求完成后调用
process_exception：请求发生异常时调用
from_crawler：从crawler构造的时候调用
from_settings：从settings构造的时候调用

在爬取网页的时候，使用不同的User-Agent可以提高请求的随机性，定义一个随机设置User-Agent的中间件RandomUserAgentMiddleware
配置爬虫中间件的方式与pipeline类似，第二个参数表示优先级

3. 代理服务器
爬虫最怕的就是封ip，这时候就需要代理服务器来爬取，scrapy设置代理服务器非常简单，只需要在请求前设置Request对象的meta属性，添加proxy值即可，通常我们可以通过中间件来做



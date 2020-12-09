"""
http请求
    get
        便捷
        明文
        参数长度有限
    post
        较安全
        数据传递没有太大的限制
        上传文件
    不常用的请求：
        put
        delete：删除一些信息
        head：请求头

DNS：域名解析服务商，浏览器用域名从DNS获取IP地址，再向IP地址对应的服务器发送请求

请求头：
    accept：文本格式
    accept-encoding：编码
    connection：长链接 短链接
    cookie：缓存
    host：域名
    refer：从哪个网页进入当前网页
    user-agent：用户信息和用户的浏览器信息
    ……

爬虫作用：买卖信息、数据分析、流量……

爬虫分类：
    通用爬虫
        使用搜索引擎
        开放性
        速度快
        目标不明确
        返回的内容不精确
    聚焦爬虫
        目标明确
        返回内容较精确
    增量式
        翻页
        ……
    deep深度爬虫（分两种）
        静态数据：html、css
        动态数据：js、加密js

爬虫原理：
    确认目标url
    使用代码发送请求
    解析响应的数据
    数据持久化

通常爬取到的数据类型是bytes或str
    bytes==>str:decode("utf-8")
    str==>bytes:encode("utf-8")
"""
import urllib.request
import urllib.parse  # 用于转译
import string  # 用于转译


def load_data():
    # 要爬取的url
    url = "http://www.baidu.com/"
    # 发送请求并接收响应数据
    reponse = urllib.request.urlopen(url)
    # 返回reponse对象：<http.client.HTTPResponse object at 0x000001B2FA3F6C70>
    print(reponse)
    # 读取内容
    data = reponse.read()
    # 读取的内容是bytes类型
    print(data)
    # 转换成字符串
    str_data = data.decode("utf-8")
    print(str_data)
    # 将数据写入文件
    with open("baidu.html","w",encoding="utf-8") as f:
        f.write(str_data)


def load_data_with_params():
    url = "http://www.baidu.com/s?wd="
    # 搜索词（有中文字符）
    key_word = "帅哥"
    # http://www.baidu.com/s?wd=帅哥
    final_url = url + key_word
    print(final_url)
    # 如果直接发送请求：UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)
    # ascii不支持中文
    # reponse = urllib.request.urlopen(final_url)

    # 转译，将包含汉字的的网址进行转译
    encoding_url = urllib.parse.quote(final_url,safe=string.printable)
    # 转译后的网址：http://www.baidu.com/s?wd=%E5%B8%85%E5%93%A5
    print(encoding_url)
    response = urllib.request.urlopen(encoding_url)
    # <http.client.HTTPResponse object at 0x0000025A4F27C340>
    print(response)
    # 写入本地
    str_data = response.read().decode("utf-8")
    with open("baidu_帅哥.html", "w", encoding="utf-8") as f:
        f.write(str_data)


# load_data()
load_data_with_params()
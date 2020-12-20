"""
使用代理
    IP代理
        免费代理：时效性差，错误率高
        付费代理：要钱，也会有失效的时候
    IP代理分类：
        透明：对方知道我们的真实id
        匿名：对方不知道我们的真实id，知道我们使用了代理
        高匿：对方不知道我们的真实id，不知道我们使用了代理
"""
import urllib.request


def proxy_user():
    url = "https://www.baidu.com/"
    # 代理信息
    proxy = {"http": "183.166.103.185:9999"}
    # 创建代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 用代理器创建opener
    opener = urllib.request.build_opener(proxy_handler)
    # 使用opener进行访问
    response = opener.open(url)
    print(response)


def proxy_multiple_users():
    url = "https://www.baidu.com/"
    # 代理信息列表
    proxy_list = [
        {"http": "123.0.0.0:8118"},
        {"http": "183.166.103.185:9999"},
        {"http": "115.221.245.142:9999"},
        {"http": "175.42.68.59:9999"}
    ]
    # 循环使用多个代理
    for proxy in proxy_list:
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)

        try:
            response = opener.open(url, timeout=1)
            print("success")
        except Exception as e:
            print(e)


# proxy_user()
proxy_multiple_users()
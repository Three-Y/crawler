"""
请求头
"""
import urllib.request
import random

def add_header():
    url = "https://www.baidu.com/"
    header = {
        # 添加用户信息的请求头，模仿真实用户的访问
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        "abc": "hahahhahah"
    }
    request = urllib.request.Request(url, headers=header)
    # 获取全部请求头
    print(request.headers)
    # 获取指定请求头
    print(request.get_header("User-agent"))
    print(request.get_header("Abc"))
    # 动态添加请求头
    request.add_header("123", "lalalallalal")
    print(request.get_header("123"))
    response = urllib.request.urlopen(request)
    print(response)


def random_user_agent():
    url = "https://www.baidu.com/"
    # 一个User-agent列表
    user_agents_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
    ]
    user_agent = random.choice(user_agents_list)
    request = urllib.request.Request(url)
    request.add_header("User-agent", user_agent)
    response = urllib.request.urlopen(request)
    print(response)
    print(request.get_header("User-agent"))


# add_header()
random_user_agent()

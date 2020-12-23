# -*- coding:utf-8 -*-
import requests


def test_requests():
    """简单使用requests"""
    # url
    url = "https://i.taobao.com/"
    # 发送请求并获取响应
    response = requests.get(url)
    # 响应数据的字符串形式
    text_data = response.text
    print(text_data)
    print("====================end=======================")
    # 持久化数据
    with open("01_test_request.html","w",encoding="utf-8") as f:
        f.write(text_data)
        f.close()


def request_with_param():
    """带参请求"""
    # url
    url = "https://www.sogou.com/"
    # 参数
    param_dic = {
        "query": "爬虫"
    }
    # 请求加入参数
    response = requests.get(url, param_dic)
    # 响应数据的字符串形式
    text_data = response.text
    print(text_data)
    print("====================end=======================")


def request_with_header():
    """加入请求头"""
    # url
    url = "https://www.sogou.com/"
    # 请求头
    header = {
        # UA伪装：模仿浏览器发送请求
        # User-Agent：用户浏览器信息
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    # 参数
    param = {
        "query": "爬虫"
    }
    # 请求加入请求头
    response = requests.get(url=url, params=param, headers=header)
    print(response.text)
    print("====================end=======================")


if __name__ == '__main__':
    # test_requests()
    # request_with_param()
    request_with_header()
# -*- coding:utf-8 -*-
import requests
import json


def post_request():
    """需求：百度翻译，输入时有局部更新，发送了ajax请求（XHR），获取异步请求后响应的json数据"""
    url = "https://fanyi.baidu.com/sug"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    kw = input("请输入要翻译的单词：")
    params = {"kw": kw}
    # post请求
    response = requests.post(url, data=params, headers=headers)
    # 返回的是json数据，从响应获取json对象
    dict_obj = response.json()
    print(dict_obj)
    # 持久化json数据
    with open("02_" + kw + ".json", "w", encoding="utf-8") as f:
        json.dump(dict_obj, fp=f, ensure_ascii=False)  # 不使用ascii编码，因为内容有中文
        f.close()


if __name__ == '__main__':
    post_request()
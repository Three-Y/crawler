# -*- coding:utf-8 -*-
import requests
import json
import time
import random


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


def get_json_data():
    """需求：豆瓣电影，获取电影详情"""
    url = "https://movie.douban.com/j/chart/top_list"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    params = {
        "type": "24",
        "interval_id": "100:90",
        "action": "",
        "start": "0",  # 从第几部电影开始取
        "limit": "20"  # 一次取几部
    }

    response = requests.get(url=url, params=params, headers=headers)
    data_list = response.json()
    with open("./02_douban.json", "w", encoding="utf-8") as f:
        json.dump(data_list, fp=f, ensure_ascii=False)
        f.close()


def get_kfc_info(pageIndex):
    """需求：肯德基餐厅信息，获取全部页面"""
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
    params = {
        "cname": "",
        "pid": "",
        "keyword": "北京",
        "pageIndex": pageIndex,
        "pageSize": "10"
    }

    response = requests.get(url=url, params=params, headers=headers)
    data_dic = response.json()
    with open("./02_kfc_info.json", "a+", encoding="utf-8") as f:
        json.dump(data_dic, fp=f, ensure_ascii=False)
        f.close()


def get_kfc_info():
    """需求：国家药监局生产许可证信息"""
    # 获取各家公司id
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    user_agents_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
    ]


    params = {
        "on": "true",
        "page": "1",
        "pageSize": "15",
        "productName": "",
        "conditionType": "1",
        "applyname": "",
        "applysn": ""
    }

    headers = {"User-Agent": random.choice(user_agents_list)}

    response = requests.post(url=url, params=params, headers=headers)
    data_dic = response.json()
    id_list = []
    for company in data_dic["list"]:
        id_list.append(company["ID"])

    url2 = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    for id in id_list:
        params2 = {
            "id": id
        }
        headers = {"User-Agent": random.choice(user_agents_list)}
        detail = requests.post(url2, params2, headers).json()
        print(detail)
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    # post_request()
    # get_json_data()
    # i = 1
    # while i <= 7:
    #     get_kfc_info(i)
    #     i += 1

    get_kfc_info()
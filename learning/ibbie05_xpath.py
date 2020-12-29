from lxml import etree
import requests
import os
import time
import random
import re


def test_etree():
    """使用xpath解析"""
    # 获取小说页面
    page_url = "http://www.huaxiaci.com/35052/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
    page_text = requests.get(url=page_url, headers=headers).text
    html = etree.HTML(page_text)
    # "/" 一层
    print(html.xpath("/html/head/title"))
    # ”//“ 多层
    print(html.xpath("/html//meta"))
    print(html.xpath("//a"))
    # 添加属性条件
    print(html.xpath('//p[@class="bookintro"]'))
    # "/text()" 此层标签的文本
    print(html.xpath("//div[@class='book mt10 pt10 tuijian']/text()"))
    # "//text()" 此层以及子标签的所有文本
    print(html.xpath("//div[@class='book mt10 pt10 tuijian']//text()"))
    # "/@属性名" 取标签属性值
    print(html.xpath("//head/meta/@content"))
    # "[]" xpath返回的是list，可用索引取值
    print(html.xpath("//head/meta[3]/@content"))
    "//*[@id='Pl_Official_MyProfileFeed__20']/div/div[2]/div[1]/div[3]/div[4]"


def fs58():
    """58同城，二手房"""
    url = "https://fs.58.com/ershoufang/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
    page_text = requests.get(url=url, headers=headers).text
    html = etree.HTML(page_text)
    a_list = html.xpath("//div[@class='list-info']/h2/a")
    for a in a_list:
        house_title = a.xpath("./text()")[0]
        print(house_title)


def netbian():
    """
    会存在乱码问题
    两种解决办法
        设置响应的编码：response.encoding = "gbk"
        通用的解决中文编码问题的方式：encode('iso-8859-1').decode('gbk')
    """
    if not os.path.exists("./05_netbian/"):
        os.mkdir("./05_netbian/")

    url = "http://pic.netbian.com/4kfengjing/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
    response = requests.get(url=url, headers=headers)
    # 设置响应的编码：
    response.encoding = "gbk"
    html = etree.HTML(response.text)
    li_list = html.xpath('//ul[@class="clearfix"]/li')
    for li in li_list:
        pic_name = li.xpath("./a/b/text()")[0]+".jpg"
        # 通用的解决中文编码问题的方式
        # pic_name = pic_name.encode('iso-8859-1').decode('gbk')
        pic_src = li.xpath("./a/img/@src")[0]
        pic_url = "http://pic.netbian.com"+pic_src
        pic_data = requests.get(url=pic_url,headers=headers).content
        with open("./05_netbian/"+pic_name, "wb") as f:
            f.write(pic_data)
            print("%s %s 下载成功！" % (pic_name, pic_url))


def get_city():
    """使用 | 连接多个条件"""
    url = "https://www.aqistudy.cn/historydata/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)

    # 方式一：
    # a_list = tree.xpath("//ul[@class='unstyled']//li/a")

    # 方式二：使用 | 连接多个条件
    # 热门城市的层级关系：//ul[@class='unstyled']/li/a
    # 全部城市的层级关系：//ul[@class='unstyled']/div[2]/li/a
    a_list = tree.xpath("//ul[@class='unstyled']/li/a | //ul[@class='unstyled']/div[2]/li/a")
    city_list = []
    for a in a_list:
        city = a.xpath("./text()")[0]
        city_list.append(city)
    print(city_list)
    print(len(city_list))


def down_resume_template():
    """下载简历模板（未完成）"""
    url = "https://www.job592.com/doc/down.html"
    user_agents_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
    ]
    user_agent = random.choice(user_agents_list)
    headers = {"User-Agent": user_agent}
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath("//div[@class='plist']/ul/li")
    for li in li_list:
        resume_href = li.xpath("./div/div[@class='p-img']/a/@href")[0]
        # if not resume_href.startswith("/doc"):
        #     continue
        resume_url = "https://www.job592.com" + resume_href
        print("打开页面：" + resume_url)
        user_agent = random.choice(user_agents_list)
        headers = {"User-Agent": user_agent}
        resume_page_text = requests.get(url=resume_url, headers=headers).text
        # 取文件id
        resume_tree = etree.HTML(resume_page_text)
        resume_id = resume_tree.xpath("/html/head/script/text()")[0]
        resume_id = resume_id.split("docId = ")[1][:4]
        download_url = "https://my.job592.com/baike/doc_docGet.action?id={}&uid=6524fc21070ce624864e9801d030091b&time=1609249283".format(resume_id)
        print("正在下载：" + download_url)
        # 下载文件
        user_agent = random.choice(user_agents_list)
        headers = {"User-Agent": user_agent}
        file_response = requests.get(url=download_url, headers=headers)
        file_data = file_response.text
        # print(file_data)
        # with open("./05_resume/"+resume_id+".docx", "w", encoding="utf-8") as f:
        #     f.write(file_data)
        time.sleep(random.randint(1, 2))
        # resume_url = "https://www.job592.com/view/doc_toDownPage.show?uid=5f8c6078e4b0c3bc18072be6"
        # "https://my.job592.com/baike/doc_docGet.action?id=6228&uid=6524fc21070ce624864e9801d030091b&time=1609249283"
        # "https://my.job592.com/baike/doc_docGet.action?id=6228&uid=6524fc21070ce624864e9801d030091b&time=1609249283"


if __name__ == '__main__':
    down_resume_template()

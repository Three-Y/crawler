from lxml import etree
import requests


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


if __name__ == '__main__':
    fs58()

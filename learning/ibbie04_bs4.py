from bs4 import BeautifulSoup
import lxml
import requests
import time
import random


def test_bs4():
    """
    使用bs4进行数据解析
    需要下载安装bs4，以及bs4依赖的lxml
    bs4只适用于python
    """
    f = open("./test_ps4/test.html","r",encoding="utf-8")
    # 用lxml加载xml文件
    soup = BeautifulSoup(f, "lxml")
    # soup.xxx 返回第一次出现的xxx标签，xxx是tag name
    print(soup.a)
    # soup.find(xxx) 返回第一次出现的xxx标签
    print(soup.find("title"))
    # soup.find(xxx,属性名_=属性值) 注意，属性名要加下划线"_"
    print(soup.find("div", class_="single-share"))
    # soup.find_all(xxx) 返回所有符合条件的标签list
    print(soup.find_all("a")[1])
    # soup.select("某种选择器") 类、id或标签选择器，返回一个list
    print(soup.select(".thumb > a > img")[0])  # ">" 表示一层
    print(soup.select(".thumb img")[0])  # " " 空格，表示多层
    # 获取标签的文本内容
    print(soup.find("div", class_="single-share").text)  # 可以获取标签及其子标签的所有文本内容
    print(soup.find("div", class_="single-share").get_text())  # 可以获取标签及其子标签的所有文本内容
    print(soup.find("div", class_="single-share").string)  # 只可以获取当前标签的文本内容
    # 获取标签的属性值
    print(soup.meta["content"])


def get_youfei():
    # 获取小说页面
    page_url = "http://www.huaxiaci.com/35052/"
    user_agents_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
    ]
    headers = {"User-Agent": random.choice(user_agents_list)}
    page_text = requests.get(url=page_url, headers=headers).text
    page_bs = BeautifulSoup(page_text, "lxml")
    title_list = page_bs.select("#list-chapterAll > dd")
    f = open("./04_有匪.txt", "a+", encoding="utf-8")
    for chapter in title_list:
        title = chapter.a.text
        href = chapter.a["href"]
        # 获取每个章节的内容
        chapter_url = "http://www.huaxiaci.com" + href
        headers = {"User-Agent": random.choice(user_agents_list)}
        chapter_page_text = requests.get(url=chapter_url, headers=headers).text
        chapter_bs = BeautifulSoup(chapter_page_text, "lxml")
        content = chapter_bs.select("#rtext > p")
        f.write(title+"\n\n")
        for p in content:
            f.write(p.text+"\n")
        f.write("\n")
        time.sleep(0.5)
        print(title + " 爬取成功！")
    f.close()
    print("爬取结束！")

if __name__ == '__main__':
    get_youfei()

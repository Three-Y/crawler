import requests
import re
import os


def get_picture():
    """尝试获取图片"""
    url = "https://pic.qiushibaike.com/system/pictures/12391/123915969/medium/RL6T9R2V5K72GV3D.jpg"
    # 返回的是图片二进制数据，
    img_data = requests.get(url).content
    # wb 表示以二进制的方式打开，只写
    with open("./03_picture.jpg", "wb") as f:
        f.write(img_data)


def get_qiutu_img():
    """聚焦爬虫，使用正则抓取页面源码中需要的内容"""
    # 创建文件夹
    if not os.path.exists("./qiutu"):
        os.mkdir("./qiutu")
    # 获取整张页面(爬取3页)
    for pagenum in range(1, 3):
        url = "https://www.qiushibaike.com/imgrank/page/%s/" % pagenum
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
        page_text = requests.get(url=url, headers=headers).text
        # 从页面源码抓取图片的url
        pattern = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(pattern, page_text, re.S)  # re.S多行匹配
        for img_src in img_src_list:
            # 使用get请求获取所有图片
            src = "http:" + img_src
            img_data = requests.get(src, headers=headers).content
            img_name = src.split("/")[-1]
            with open("./qiutu/"+img_name, "wb") as f:
                f.write(img_data)
                print("%s 下载成功！" % img_name)


if __name__ == '__main__':
    get_qiutu_img()

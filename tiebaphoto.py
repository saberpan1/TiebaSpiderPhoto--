from lxml import html
import requests
import os
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
}

#解析网页,输入xpath参数，返回需要的值
def analysis(url,xpath):
    #返回网页
    rs = requests.get(url,headers=headers).text
    #生成etree
    etree = html.etree
    #解析网页
    html1 = etree.HTML(rs)
    xpath1 = html1.xpath(xpath)
    return xpath1

#爬取图片
def takephoto(url,xpath="//li[@class='l_reply_num'][1]/span[2]/text()"):
    #获取总页数
    page = analysis(url,xpath)
    #翻页爬取
    for i in range(1,int(page[1])+1):
        print(f'爬取第{i}页的图片')
        url2 = f'{url}?pn={i}'
        photo = analysis(url2, "//img[@class='BDE_Image']/@src")
        for i in photo:
            image_link = requests.get(i)
            image = image_link.content
            print(i)
            dirpath = os.getcwd() + '/afk-25'
            if not os.path.isdir(dirpath):
                os.makedirs(dirpath)
            imagename = i[-14:]
            print(f'正在下载{imagename}')
            a = open('afk-25/'+imagename,'wb')
            a.write(image)
            a.close()

url = 'https://tieba.baidu.com/p/6628443925'
takephoto(url)

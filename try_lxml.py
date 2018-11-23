from lxml import etree
import requests

url = "https://book.douban.com/"
headers = {
    "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}
response = requests.get(url, headers=headers)
html_str = response.content.decode()
# print(html_str)
elements = etree.HTML(html_str)
print(elements)
# dic_ret = elements.xpath("//ul[@class='list-col list-col5 list-express slide-item']/li/div/a/@href")
# print(dic_ret)
lis = elements.xpath("//ul[@class='list-col list-col5 list-express slide-item']/li")
for li in lis:
    book = {"href": li.xpath(".//div[@class='cover']/a/@href")[0],
            "title": li.xpath(".//div[@class='info']//div[@class='more-meta']/h4/text()")[0].strip(),
            "image": li.xpath(".//div[@class='cover']/a/img/@src")[0]}
    print(book)

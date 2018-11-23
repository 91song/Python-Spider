from lxml import etree
import requests
import json
from retrying import retry


class QiushiSpider:

    def __init__(self):
        self.temp_url = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
        }

    def get_url_list(self):
        return [self.temp_url.format(i) for i in range(1, 14)]

    @retry(stop_max_attempt_number=3)
    def _parse_html(self, url):
        response = requests.get(url, headers=self.headers, timeout=5)
        return response.content.decode()

    def parse_html(self, url):
        try:
            html_str = self._parse_html(url)
        except:
            html_str = None
        return html_str

    def get_content_list(self, html_str):
        elements = etree.HTML(html_str)
        div_list = elements.xpath("//div[@id='content-left']/div")
        content_list = []
        for div in div_list:
            item = {}
            item["author_name"] = div.xpath(".//h2/text()")[0].strip() if len(
                div.xpath(".//h2/text()")) > 0 else None
            item["content"] = div.xpath(".//div[@class='content']/span/text()")
            item["content"] = [i.strip() for i in item["content"]]
            item["img"] = div.xpath(".//div[@class='thumb']//img/@src")
            item["img"] = "https:" + item["img"][0] if len(item["img"]) > 0 else None
            content_list.append(item)
        return content_list

    def save_content_list(self, content_list):
        for content in content_list:
            with open("qiushi.json", "a", encoding="utf-8") as f:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            print("now paring:", url)
            html_str = self.parse_html(url)
            content_list = self.get_content_list(html_str)
            self.save_content_list(content_list)


if __name__ == '__main__':
    qiushi = QiushiSpider()
    qiushi.run()

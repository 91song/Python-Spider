import try_json
from try_retry import parse_html


class DoubanSpider:
    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=0"

    def get_content_list(self, html_str):
        dict_data = try_json.loads(html_str)
        content_list = dict_data["subject_collection_items"]
        total = dict_data["total"]
        return content_list, total

    def save_content_list(self, content_list):
        for content in content_list:
            with open("douban_spider.json", "a", encoding="utf-8") as f:
                f.write(try_json.dumps(content, ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self):
        num = 0
        total = 100
        while num < total + 18:
            url = self.temp_url.format(num)
            print(url)
            html_str = parse_html(url)
            content_list, total = self.get_content_list(html_str)
            self.save_content_list(content_list)
            num += 18


if __name__ == "__main__":
    douban = DoubanSpider()
    douban.run()

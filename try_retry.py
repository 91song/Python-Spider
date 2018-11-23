import requests
from retrying import retry


@retry(stop_max_attempt_number=3)
def _parse_html(url):
    print("*" * 100)
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        "Referer": "https://m.douban.com/tv/american"
    }
    response = requests.get(url, headers=headers, timeout=5)
    return response.content.decode()


def parse_html(url):
    try:
        html_str = _parse_html(url)
    except:
        html_str = None
    return html_str


if __name__ == "__main__":
    url = "https://www.baidu.com"
    # url = "www.baidu.com"
    print(parse_html(url)[:100])

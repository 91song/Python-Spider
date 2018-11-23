import requests

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}
response = requests.get(url, headers=headers)
# print(response)
# response.encoding = "utf-8"
# print(response.text)
print(response.content.decode())

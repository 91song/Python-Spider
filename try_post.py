import requests
import try_json

url = "https://fanyi.baidu.com/basetrans"
query_str = input("请输入要翻译的中文：")
data = {
    "query": query_str,
    "from": "zh",
    "to": "en"
}
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
response = requests.post(url, data=data, headers=headers)
print(response.content.decode())
print(response.request.url)
print(response.url)
print(response.request.headers)
print(response.headers)
dict_ret = try_json.loads(response.content.decode())
print(dict_ret)
print(type(dict_ret))
ret = dict_ret["trans"][0]["dst"]
print("翻译结果是：", ret)

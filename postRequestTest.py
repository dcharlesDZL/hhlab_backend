import requests
import json
import time

url = "http://127.0.0.1:80/"
url2 = 'http://127.0.0.1:8080/api/v3/mqtt/publish/'
url3 = "http://127.0.0.1:8080/api/c3/plugins/"
# 传上来的数据必须是字典格式的
data = {"data": "0103160064001122110023400a0cfeaa0103160064001122110023400a0cfeaa123456789012"}
data2 = {"qos":1, "retain": 'false', "topic":"world", "payload":"test" , "client_id": "C_1492145414740"}
request_data = json.dumps(data)


def requestTest():
    while True:
        r = requests.post(url2, data=data2)
        time.sleep(3)
        print(r.content)
    while False:
        r = requests.get(url3)
        time.sleep(2)
        print(r.content)

if __name__ == "__main__":
    requestTest()

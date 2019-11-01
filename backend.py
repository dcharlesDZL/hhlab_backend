import web
from modbus_process import *
from data_process import *
import requests
import hashlib
urls = (
    '/', 'index',
    '/wx', 'Handle'
)

servername = "http://101.132.151.192:100"
serverurl = ""
class index:
    def GET(self):
        return "hello,world"

    def POST(self):
        a = web.data()
        b = byte2dict(a)
        c = b["data"]
        d = modbus_data_process(c)
        e = postdata(d)
        headers = {"userkey:2512d8b672524137af5e85155276ec4b"}
        url = servername + serverurl
        f = requests.post(url=url, data=e, headers=headers)
        print(f.status_code)


# datawechat = {'timestamp': '1572229413',
#               'signature': '64dc5f2b9fc43323f05ffe0b878c879977084623',
#               'nonce': '1791110196',
#               'echostr': '3610724547134708069'}


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "douzhengli"
            # print(data)
            result = [token, timestamp, nonce]
            result.sort()
            sha1 = hashlib.sha1()
            sha1.update(''.join(result).encode())
            hashcode = sha1.hexdigest()
            # print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except:
            return ""


def main():
    app = web.application(urls, globals())
    app.run()


if __name__ == "__main__":
    main()

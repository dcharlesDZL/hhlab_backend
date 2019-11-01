# 导入 paho-mqtt 的 Client：
import paho.mqtt.client as mqtt
import threading
import time


# 用于响应服务器端 CONNACK 的 callback，如果连接正常建立，rc 值为 0
def on_connect(client, userdata, flags, rc):
    print("Connection returned with result code:" + str(rc))


# 用于响应服务器端 PUBLISH 消息的 callback，打印消息主题和内容
def on_message(msg):
    print("Received message, topic:" + msg.topic + "payload:" + str(msg.payload))


def on_publish():
    print("message published")


# 在连接断开时的 callback，打印 result code
def on_disconnect():
    print("Disconnection returned result:")



# 在订阅获得服务器响应后，从为响应列表中删除该消息 id
def on_subscribe():
    print("message subscribed")


# 构造一个 Client 实例
client = mqtt.Client(client_id="publisher")
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_publish = on_publish

client.connect("47.98.143.246", port=2568)  # 阿里云服务器


def client_loop():
    client.loop_forever()


def client_pub():
    while True:
        client.publish(topic="publisher/123456/appub", payload="abc", qos=0)
        time.sleep(2)


pub_threads = []
t1 = threading.Thread(target=client_loop)
t2 = threading.Thread(target=client_pub)
pub_threads.append(t1)
pub_threads.append(t2)
for i in range(2):
    pub_threads[i].start()



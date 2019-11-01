"""
模拟设备端发布消息
"""


# 导入 paho-mqtt 的 Client：
import paho.mqtt.client as mqtt
import threading
import json
import random


# 用于响应服务器端 CONNACK 的 callback，如果连接正常建立，rc 值为 0
def on_connect(client, userdata, flags, rc):
    print("Connection returned with result code:" + str(rc))


# 用于响应服务器端 PUBLISH 消息的 callback，打印消息主题和内容
def on_message(client, userdata, msg):
    print("Received message, topic:" + msg.topic + "payload:" + str(msg.payload))


def on_publish():
    print("message published")


# 在连接断开时的 callback，打印 result code
def on_disconnect(client, userdata, rc):
    # print("Disconnection returned result:"+ str(rc))
    pass


# 在订阅获得服务器响应后，从为响应列表中删除该消息 id
def on_subscribe(client, userdata, mid, granted_qos):
    print("message subscribed")


# 构造一个 Client 实例
client_machine = mqtt.Client(client_id="subscriber")
client_machine.on_connect = on_connect
client_machine.on_disconnect = on_disconnect
client_machine.on_message = on_message
client_machine.on_subscribe = on_subscribe

client_machine.connect("47.98.143.246", port=2568)  # 阿里云服务器


def client_loop():
    client_machine.loop_forever()


def client_sub():
    client_machine.subscribe("publisher/123456/appub")


sub_threads = []
t1 = threading.Thread(target=client_loop)
t2 = threading.Thread(target=client_sub)
sub_threads.append(t1)
sub_threads.append(t2)
for i in range(2):
    sub_threads[i].start()




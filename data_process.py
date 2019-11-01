"""
处理post请求来的数据
"""


def byte2str(data):
    """
    形参data 为字节类型值，将其转换为字符串格式的json包
    """
    return data.decode(encoding="gbk")


def str2dict(str):
    """
    形参str为字符串类型值将其转换为字典格式
    """
    return eval(str)


def strsplit(str):
    """
    将接收到的十六进制字符串两两分割
    """
    return [str[i[0]:i[0]+2] for i in enumerate(str) if not i[0] % 2]


def str2hex(str):
    """
    字符串转换为16进制
    """
    return '0x' + str


def hex2dec(hexnum):
    """
    16进制数转换为10进制数
    """
    return int(hexnum, 16)


def str2int(str):
    """
    字符串转换为10进制数
    """
    return int(('0x' + str), 16)


def byte2dict(data):
    """
    数据转换为字典格式
    :param data:
    :return:
    """
    a = byte2str(data)
    b = str2dict(a)
    return b


str1 = '010316006400112211002340'
str2 = ['01', '03', '22', '00', '64', '01', '0b', '01', '2c', '00', '00', '00', 'c8', '00', '00', '00', '00', '00',
        '00', '00', '00', '00', '00', '0b', 'b8', '00', '64', '05', 'dc', '00', '00', '00', '00', '00', '01', '00',
        '00', '2d', '7f']


def test():
    strsplit(str1)
    for i in str2:
        n = hex2dec(str2hex(i))
        print(n)


if __name__ == "__main__":
    test()

from data_process import str2int
import json

# example data
# 1号设备
tempdata = ['01', '03', '22', '00', '64', '01', '0b', '01', '2c', '00', '00', '00', 'c8', '00', '00', '00', '00', '00',
            '00', '00', '00', '00', '00', '0b', 'b8', '00', '64', '05', 'dc', '00', '00', '00', '00', '00', '01', '00',
            '00', '2d', '7f']


def modbus_data_process(data):
    device_addr = str2int(data[0])
    function_num = str2int(data[1])
    data_len = str2int(data[2])
    #########################
    machine_type = str2int(data[3] + data[4])
    temp = str2int(data[5] + data[6])
    set_temp = str2int(data[7] + data[8])
    speed = str2int(data[9] + data[10])
    set_speed = str2int(data[11] + data[12])
    set_hour = str2int(data[13] + data[14])
    set_min = str2int(data[15] + data[16])
    hour = str2int(data[17] + data[18])
    minute = str2int(data[19] + data[20])
    second = str2int(data[21] + data[22])
    temp_range_max = str2int(data[23] + data[24])
    speed_min = str2int(data[25] + data[26])
    speed_max = str2int(data[27] + data[28])
    alarm = str2int(data[29] + data[30])
    stop_status = str2int(data[31] + data[32])
    current_mode = str2int(data[33] + data[34])
    drop_bat_men = str2int(data[35] + data[36])
    #########################
    crc = str2int(data[37] + data[38])
    #########################
    machine_running_data = {'machine_type': machine_type, 'temp': temp,
                            'set_temp': set_temp, 'speed': speed, 'set_speed': set_speed, 'set_hour': set_hour,
                            'set_min': set_min, 'hour': hour, 'minute': minute, 'second': second,
                            'temp_range_max': temp_range_max, 'speed_min': speed_min, 'speed_max': speed_max,
                            'alarm': alarm, 'stop_status': stop_status, 'current_mode': current_mode,
                            'drop_bat_men': drop_bat_men
                            }
    return json.dumps(machine_running_data)


if __name__ == "__main__":
    print(modbus_data_process(tempdata))

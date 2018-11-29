# homework.py
# -*- coding: utf-8 -*-
import json
import os

ps_date = "1128_1\\"
ps_fix_path = "D:\\work\\POE\\POE_test_data\\POE_people\\"
ps_file_type = ".txt"


# read file data into string
def file_read(c_array, f_name):
    with open(f_name) as f:
        for line in f:
            c_array.append(line)
        return c_array


def file_to_dict_data(file_name):
    content_array = []
    i = 0
    a = ""
    file_read(content_array, file_name)

    for mac_data in content_array:
        i = i + 1
        mac_data = mac_data.lower().strip('\n').replace("\x00", "")
        sorted_data = mac_data.split(':')
        if len(sorted_data) > 9:  # if equal to 1 ,represent the end of file & >5 means data have 6 values
            rssi_data = 256 + ~int(sorted_data[6], 16)
            # text_file.write("%s. MAC:%s RSSI:-%s Time:%s \n" % (i, SortedData[:6], Rssi_data, SortedData[7:]))
            if a != "":
                a = a + ","+("%s:{'MAC':'%s','RSSI':'%s','TIME':'%s'}" % (i, sorted_data[0]+sorted_data[1]+sorted_data[2]+sorted_data[3]
                                                          + sorted_data[4]+sorted_data[5], rssi_data, str(int(sorted_data[7], 16))+"-"
                                                          + str(int(sorted_data[8], 16))+"-"+str(int(sorted_data[9], 16))))
            else:
                a = a + ("%s:{'MAC':'%s','RSSI':'%s','TIME':'%s'}" % (i, sorted_data[0]+sorted_data[1]+sorted_data[2]
                                                                   + sorted_data[3] + sorted_data[4]+sorted_data[5]
                                                                   , rssi_data, str(int(sorted_data[7], 16))+"-"
                                                                   + str(int(sorted_data[8], 16))+"-"+str(int(sorted_data[9], 16))))
        # print("%s. MAC:%s RSSI:-%s Time:%s" % (i, sorted_data[:6], rssi_data, sorted_data[7:]))

    json_data = "{" + a + "}"
    json_data = json.dumps(eval(json_data))
    json_data = json.loads(json_data)
    # print(json_data)
    # print (content_array)
    return json_data


def write_to_file(json_data_w, mac_file, mac_file_o1):
    text_file = open(mac_file_o1, 'a', newline='')
    sort_key = sorted(json_data_w, key=lambda k: json_data_w[k]['MAC'])
    text_file.write("\n %s" % mac_file)
    for key in sort_key:
        # print("%s: %s" % (key, json_data_w[key]))
        if json_data_w[key]['MAC'] != "d0d0d0d0d0d0":
            if (json_data_w[key]['MAC'] == "ec21e54475ac") | (json_data_w[key]['MAC'] == "ec21e59277ac"):
                # print("%s: %s" % (key, json_data_w[key]))
                text_file.write("\n %s: %s" % (key, json_data_w[key]))

    # for key, value in json_data_w.items():
    #     print('\nKey: %s' % key)
    #     print('Value: %s' % value)
    text_file.close()


def main():
    mac_file_i1 = "PF1_"
    mac_file_i2 = "PF2_"
    mac_file_i3 = "PF3_"
    mac_file_o1 = "parse_output_"
    current_path = ps_fix_path+ ps_date
    # json_data1 = file_to_dict_data(mac_file1)
    # json_data2 = file_to_dict_data(mac_file2)
    # json_data3 = file_to_dict_data(mac_file3)
    # write_to_file(json_data1, mac_file1)
    # write_to_file(json_data2, mac_file2)
    # write_to_file(json_data3, mac_file3)

    for ikey in range(1, 11):
        if os.path.exists(current_path + mac_file_o1 + str(ikey) + ps_file_type):
            os.remove(current_path + mac_file_o1 + str(ikey) + ps_file_type)

    for ikey in range(1, 11):
        json_data1 = file_to_dict_data(current_path + mac_file_i1 + str(ikey) + ps_file_type)
        json_data2 = file_to_dict_data(current_path + mac_file_i2 + str(ikey) + ps_file_type)
        json_data3 = file_to_dict_data(current_path + mac_file_i3 + str(ikey) + ps_file_type)
        write_to_file(json_data1, current_path + mac_file_i1 + str(ikey), current_path + mac_file_o1 + str(ikey) + ps_file_type)
        write_to_file(json_data2, current_path + mac_file_i2 + str(ikey), current_path + mac_file_o1 + str(ikey) + ps_file_type)
        write_to_file(json_data3, current_path + mac_file_i3 + str(ikey), current_path + mac_file_o1 + str(ikey) + ps_file_type)


if __name__ == '__main__':
    main()

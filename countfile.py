# -*- coding: utf-8 -*-
import json
import os

ps_date = "1203_7_in_out\\"
ps_fix_path = "D:\\work\\POE\\POE_test_data\\POE_people\\"
ps_file_type = ".txt"
filter_badge1 = "ec21e54475ac"  # Bob
filter_badge2 = "ec21e59776ac"  # rain_man
filter_badge3 = "ec21e53875ac"  # happy
filter_badge4 = "ec21e5ed6eac"  # sweet
filter_badge5 = "ec21e5476fac"  # eilieen
filter_badge6 = "ec21e5b066ac"  # alvin
filter_badge7 = "ec21e5a070ac"  # small
filter_badge8 = "ec21e5ce83ac"  # zhang
filter_rssi = 89
range_low = 22  # include equal
range_upper = 24  # not include equal


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
        if len(sorted_data) ==10:  # if equal to 1 ,represent the end of file & >5 means data have 6 values
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
    text_file = open(mac_file_o1, 'a', newline='')  # not to rewrite the file
    sort_key = sorted(json_data_w, key=lambda k: json_data_w[k]['MAC'])
    text_file.write("\n %s" % mac_file)
    for key in sort_key:
        # print("%s: %s" % (key, json_data_w[key]))
        if (json_data_w[key]['MAC'] != "d0d0d0d0d0d0") & (int(json_data_w[key]['RSSI']) < filter_rssi):
            if (json_data_w[key]['MAC'] == filter_badge1) | (json_data_w[key]['MAC'] == filter_badge2) \
                    | (json_data_w[key]['MAC'] == filter_badge3) | (json_data_w[key]['MAC'] == filter_badge4) \
                    | (json_data_w[key]['MAC'] == filter_badge5) | (json_data_w[key]['MAC'] == filter_badge6) \
                    | (json_data_w[key]['MAC'] == filter_badge7) | (json_data_w[key]['MAC'] == filter_badge8):
                print("%s , %s ,%s " % (json_data_w[key]['MAC'], json_data_w[key]['RSSI'], json_data_w[key]['TIME']))
                text_file.write("\n%s , %s ,%s " % (json_data_w[key]['MAC'], json_data_w[key]['RSSI'], json_data_w[key]['TIME']))

    # for key, value in json_data_w.items():
    #     print('\nKey: %s' % key)
    #     print('Value: %s' % value)
    text_file.close()


def main():
    mac_file_i1 = "PF1_"
    mac_file_i2 = "PF2_"
    mac_file_i3 = "PF3_"
    mac_file_o1 = "parse_output_"
    current_path = ps_fix_path + ps_date
    # json_data1 = file_to_dict_data(mac_file1)
    # json_data2 = file_to_dict_data(mac_file2)
    # json_data3 = file_to_dict_data(mac_file3)
    # write_to_file(json_data1, mac_file1)
    # write_to_file(json_data2, mac_file2)
    # write_to_file(json_data3, mac_file3)

    # if the file exist then delete the file
    for ikey in range(range_low, range_upper):
        temp_value = str(ikey)
        if os.path.exists(current_path + mac_file_o1 + temp_value + ps_file_type):
            os.remove(current_path + mac_file_o1 + temp_value + ps_file_type)

    for ikey in range(range_low, range_upper):
        temp_value = str(ikey)
        json_data1 = file_to_dict_data(current_path + mac_file_i1 + temp_value + ps_file_type)
        json_data2 = file_to_dict_data(current_path + mac_file_i2 + temp_value + ps_file_type)
        json_data3 = file_to_dict_data(current_path + mac_file_i3 + temp_value + ps_file_type)
        write_to_file(json_data1, current_path + mac_file_i1 + temp_value, current_path + mac_file_o1 + temp_value + ps_file_type)
        write_to_file(json_data2, current_path + mac_file_i2 + temp_value, current_path + mac_file_o1 + temp_value + ps_file_type)
        write_to_file(json_data3, current_path + mac_file_i3 + temp_value, current_path + mac_file_o1 + temp_value+ ps_file_type)


if __name__ == '__main__':
    main()

# homework.py
# -*- coding: utf-8 -*-
import json
import ast

MACfile = "MACADDR.txt"
outfile = 'Analysis_poe.txt'


# read file data into string
def file_read(carray , fname):
   with open(fname) as f:   
        for line in f:
            carray.append(line)              
        return carray


def main():

    content_array = []
    i = 0
    a = ""

    file_read(content_array,MACfile)
    text_file = open("outfile", "w")

    for macdata in content_array:
        i = i + 1
        macdata = macdata.lower().strip('\n').replace("\x00", "")
        SortedData=macdata.split(':')
        if(len(SortedData)  != 1):  # if equal to 1 ,represent the end of file
            Rssi_data = 256 + ~int(SortedData[6],16)
            text_file.write("%s. MAC:%s RSSI:-%s Time:%s \n" % (i, SortedData[:6], Rssi_data, SortedData[7:]))
            if a != "":
                a = a + ","+("'%s':[{'MAC':'%s'},{'RSSI':'-%s'},{'Time':'%s'}]" % (i, SortedData[1]+SortedData[2]+SortedData[3]
                                                          + SortedData[4]+SortedData[5], Rssi_data, SortedData[7]
                                                          + SortedData[8]+SortedData[9]))
            else:
                a = a +("'%s':[{'MAC':'%s'},{'RSSI':'-%s'},{'Time':'%s'}]" % (i, SortedData[1]+SortedData[2]+SortedData[3]
                                                          + SortedData[4]+SortedData[5], Rssi_data, SortedData[7]
                                                          + SortedData[8]+SortedData[9]))
            print("%s. MAC:%s RSSI:-%s Time:%s" % (i, SortedData[:6], Rssi_data, SortedData[7:]))
            print()
    # print (content_array)
    json_data = "{" + a + "}"
    json_data = json.dumps(eval(json_data))
    json_data = json.loads(json_data)
    print(json_data)
    print(sorted(json_data.keys()))
    text_file.close()


if __name__=='__main__':
    main()

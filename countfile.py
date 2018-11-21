# homework.py
# -*- coding: utf-8 -*-

MACfile  = "MACADDR.txt"
outfile = 'Analysis_poe.txt'

## read file data into string
def file_read(carray , fname):
   with open(fname) as f:   
        for line in f:
            carray.append(line)              
        return carray

def main():

    content_array = []
    i = 0

    file_read(content_array,MACfile)
    text_file = open("outfile", "w")
    print '=============Result============================='
    for macdata in content_array:
    	i = i + 1
        macdata = macdata.lower().strip('\n').replace("\x00",'')
        SortedData=macdata.split(':')
        if(len(SortedData)  != 1): ## if equal to 1 ,represent the end of file 
            Rssi_data = 256 + ~int(SortedData[6],16)
            text_file.write("%s. MAC:%s RSSI:-%s Time:%s \n" % (i,SortedData[:6],Rssi_data,SortedData[7:]))
            print ("%s. MAC:%s RSSI:-%s Time:%s" % (i,SortedData[:6],Rssi_data,SortedData[7:]))
    #print (content_array)
    text_file.close()
    print '==============End============================'

if __name__=='__main__':
    main()    
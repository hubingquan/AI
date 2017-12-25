#! /usr/bin/env python2
#coding=utf-8
'''
@author: hu bingquan
'''
import cv2
import sys
import numpy as np
import struct

inputfiles = sys.argv[1:-1]
outfile = sys.argv[-1]
print "output file:", outfile
file_num = len(sys.argv)
print "file_num:", file_num
print "input files", inputfiles
if inputfiles is None or outfile is None:
    sys.exit(1)
#image = cv2.imread("1.bmp",cv2.IMREAD_COLOR)
#杩斿洖澶氱淮鐭╅樀锛??#(384, 512, 3)锛??  
#ravel()灞曞钩n缁寸煩闃电殑鎵??鏈??  
#print image.ravel(), len(image.ravel())  
#imageClone = np.zeros((image.shape[0],image.shape[1],1),np.uint8)

#print "rows:" + bytes(rows) + "cols:" + bytes(cols) + "channels:" + bytes(channels)
#print "rows:" + bytes(rows) + "cols:" + bytes(cols)
fileSave = open(outfile,'wb')
fileSave.write("static unsigned char handpose_data[4][rows*cols] = {\n")

'''
for step in range(0,rows):
    for step2 in range(0,cols):
        fileSave.write(image[step,step2,2])
fileSave.write("\n")

for step in range(0,rows):
    for step2 in range(0,cols):
        fileSave.write(image[step,step2])
'''
for _file in inputfiles:
    fileSave.write("{\n")
    print _file
    image = cv2.imread(_file,cv2.IMREAD_GRAYSCALE)
    print type(image) 
    print image.shape, image.size, image.dtype
    rows = image.shape[0]
    cols = image.shape[1]
    for step in range(0,rows):
        for step2 in range(0,cols):
            #str = bytes(image[step,step2]) + ','
            fileSave.write(bytes(image[step,step2]))
            if step == rows-1 and step2 == cols -1:
                fileSave.write(" },\n");
            else:
                fileSave.write(",")
        fileSave.write("\n");

fileSave.write("};\n");
fileSave.close()

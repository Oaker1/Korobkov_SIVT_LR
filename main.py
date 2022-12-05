import cv2
import numpy as np

img = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)  # если не использовать grayscale, эта функция печатает 3д массив XD

f = open('imgresult.txt', 'w')
#STARTING PARAMS
DPI = 600
pixelsize = 25.4/DPI
in_row_count = 0
x=0
y=0
f.write('[ ')
for x in range(107): # 2nd number in paint
    for y in range(138): # 1st number in paint
        if img[x,y] == 255:
            print(x,y)
            in_row_count += 1
        else:
            result = in_row_count * pixelsize
            resultstring = str(round(result, 3)) + ' '
            if in_row_count != 0:
                f.write(resultstring)
                print('test3')
            in_row_count = 0
        y+=1
    x+=1
f.write(' ]')

f.close()

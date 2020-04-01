import cv2
import pandas as pd
import os
import numpy

img_folder_path='img1/00000011_000.png'
frame=cv2.imread(img_folder_path)


pd_bbox = 'bounding_box.txt'

def plot_bbox(img_folder_path, bbox_filename):
    actual_bbox=open(bbox_filename)
    img_folder_path=os.path.split(img_folder_path)[-1]
    #print(img_folder_path)
    count=0
    temp_count=0
    final_bbox_list=[]
    for img in actual_bbox :
        if img.find(img_folder_path) != -1:
            print('file exist:',count)
            print('given image',img)
            temp_count=count
            print("this is temp count",temp_count)
        if count > temp_count:

            if img.find('/') == -1 :
                final_bbox_list.append(img)
            else:
                break
        count+=1

    i=final_bbox_list[3]
    temp_i=list(i.split(" "))
    temp_i.pop(0)

    p = numpy.array(temp_i)
    k=p.astype(float)

    x1=int(k[0])
    y1=int(k[1])
    x2=int(k[2])
    y2=int(k[3])
    return x1,y1,x2,y2


x_1,y_1,x_2,y_2=plot_bbox(img_folder_path, pd_bbox)


cv2.rectangle(frame,(x_1,y_1),(x_2,y_2),(60,20,220),3)
print(frame)
cv2.imshow('image',frame)
cv2.imwrite("frame.png",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
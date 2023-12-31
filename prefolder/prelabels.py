import os
import cv2
import json
train_image_path = 'D:/SVHN-Data/mchar_train/'#下载好的数据集位置
val_image_path = 'D:/SVHN-Data/mchar_val/'
train_annotation_path = 'D:/SVHN-Data/mchar_train.json'
val_annotation_path = 'D:/SVHN-Data/mchar_val.json'
train_data = json.load(open(train_annotation_path))
val_data = json.load(open(val_annotation_path))
label_path = 'D:/git_ssh/coco/all_labels/'
j = 0
for key in train_data:
    if(j>=2000 and j<4000):
      f = open(label_path+key.replace('.png', '.txt'), 'w')
      img = cv2.imread(train_image_path+key)
      shape = img.shape
      label = train_data[key]['label']
      left = train_data[key]['left']
      top = train_data[key]['top']
      height = train_data[key]['height']
      width = train_data[key]['width']
      for i in range(len(label)):
          x_center = 1.0 * (left[i]+width[i]/2) / shape[1]
          y_center = 1.0 * (top[i]+height[i]/2) / shape[0]
          w = 1.0 * width[i] / shape[1]
          h = 1.0 * height[i] / shape[0]
          # label, x_center, y_center, w, h
          f.write(str(label[i]) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(w) + ' ' + str(h) + '\n')
      f.close()
    if(j>=4000):
      break
    j+=1
j = 0
for key in val_data:
    if(j>=2000 and j<4000):
      f = open(label_path+'val_'+key.replace('.png', '.txt'), 'w')
      img = cv2.imread(val_image_path+key)
      shape = img.shape
      label = val_data[key]['label']
      left = val_data[key]['left']
      top = val_data[key]['top']
      height = val_data[key]['height']
      width = val_data[key]['width']
      for i in range(len(label)):
          x_center = 1.0 * (left[i]+width[i]/2) / shape[1]
          y_center = 1.0 * (top[i]+height[i]/2) / shape[0]
          w = 1.0 * width[i] / shape[1]
          h = 1.0 * height[i] / shape[0]
          # label, x_center, y_center, w, h
          f.write(str(label[i]) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(w) + ' ' + str(h) + '\n')
      f.close()
    if(j>=4000):
      break
    j+=1

import os
import shutil
train_image_path = 'D:/SVHN-Data/mchar_train/'#下载好的存储路径
val_image_path = 'D:/SVHN-Data/mchar_val/'
dst_image_path = 'D:/git_ssh/coco/all_images/'#文件整合后的位置
train_image_list = os.listdir(train_image_path)
val_image_list = os.listdir(val_image_path)
i = 0
for img in train_image_list:
    if(i>=2000 and i<4000):
      shutil.copy(train_image_path+img, dst_image_path+img)
    if(i>=4000):
        break
    i+=1
i = 0
for img in val_image_list:
    if(i>=2000 and i<4000):
      shutil.copy(val_image_path+img, dst_image_path+'val_'+img)
    if(i>=4000):
        break
    i+=1
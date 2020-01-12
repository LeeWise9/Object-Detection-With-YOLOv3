# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:53:04 2019
@author: lenovo
"""
from keras.models import load_model
import help_function as f
from PIL import Image
import numpy as np
import cv2
model = load_model('../model/model.h5')   # 加载.h5模型文件
input_path   = '../example_video/a1.mp4' # '../example_fig/timg.jpg'  #'../example_video/white.mp4'
output_path  = './output/'
savepath = output_path + input_path.split('/')[-1]

if input_path[-4:] in ['.jpg', '.png', 'JPEG']:
    # 图片
    img = Image.open(input_path)
    img = f.predict_fig(img,model)
    img.save(savepath)
if input_path[-4:] == '.mp4':
    # 视频
    video_reader = cv2.VideoCapture(input_path)
    num, fps= int(video_reader.get(7)), int(video_reader.get(5))
    hei, wid= int(video_reader.get(4)), int(video_reader.get(3))
    video_writer = cv2.VideoWriter(savepath, cv2.VideoWriter_fourcc(*'XVID'), fps, (wid, hei))
    for i in range(num):
        (flag,image) = video_reader.read()
        if flag == True:
            image = Image.fromarray(np.uint8(image))
            image = f.predict_fig(image,model)
            image = np.asarray(image)
            video_writer.write([image][0])
    video_reader.release()
    video_writer.release()

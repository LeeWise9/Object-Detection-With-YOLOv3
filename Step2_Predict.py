# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:04:07 2019
@author: lenovo
"""
# 使用keras搭建YOLOv3
# step2_加载模型、文件并预测
from keras.models import load_model
import help_function as f

def predict_fig(photo_filename,model):
    # 加载图片并获取原图长宽
    labels = f.labels()                              # 定义标签类别
    anchors = f.anchors()                            # 定义anchors
    class_threshold=0.6                              # 设置置信度阈值
    input_w, input_h = 416, 416                      # 定义模型接收的图片大小
    image, image_w, image_h = f.load_image_pixels(photo_filename, (input_w, input_h))
    yhat = model.predict(image)                      # 预测（即识别过程）输出为array列表
    boxes = list()                                   # 创建空列表用以存储边界框信息
    for i in range(len(yhat)):                       # 解码边界框的坐标
    	boxes += f.decode_netout(yhat[i][0], anchors[i], class_threshold, input_h, input_w)
    # 矫正边界框大小
    f.correct_yolo_boxes(boxes, image_h, image_w, input_h, input_w)
    f.do_nms(boxes, 0.5)                             # 去除重叠边界框的预测类别（而非框本身）
    # 获取边界框详细信息
    v_boxes, v_labels, v_scores = f.get_boxes(boxes, labels, class_threshold)
    for i in range(len(v_boxes)):                    # 逐个打印目标物体和置信度
    	print(v_labels[i], v_scores[i])
    f.draw_boxes(photo_filename, v_boxes, v_labels, v_scores)           # 成图
    return None

model = load_model('./model/model.h5')           # 加载.h5模型文件
photo_filename = './example_fig/timg.jpg'        # 需要做目标检测的图片

predict_fig(photo_filename,model)
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:00:45 2019
@author: lenovo
"""
# 使用keras搭建YOLOv3
# step1_加载预训练权重构建模型并保存为.h5文件

import help_function as f

model = f.make_yolov3_model()                                    # 定义模型
weight_reader = f.WeightReader('./yolo3_weights/yolov3.weights') # 加载权重文件
weight_reader.load_weights(model)                                # 填充权重
model.save('./model/model.h5')                                   # 保存模型到.h5文件

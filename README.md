# Object-Detection-With-YOLOv3
Object Detection With YOLOv3 in Keras

这是一个基于YOLOv3的目标识别项目，使用keras编写。

该项目是一个目标检测 pipeline，主体功能是处理任意图像或视频，并在原图中用识别框标注出目标物，最后保存到指定文件夹。

主函数十分简洁，处理流程清晰，读者可以先弄清楚整体流程，再细细琢磨具体函数的功能以及如何实现它们。代码中重要的函数均写出了详细的标注和解释。

*注意：该项目直接使用了训练好的 YOLOv3 权值网络，没有另外搜集数据集做微调训练。

该项目总共包含两个步骤：1.加载模型，2.预测图片（predict）。

### Step1 加载模型<br>
本项目是基于YOLOv3的预训练模型[yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)的，为了构建keras能直接使用的.h5模型，需要将.weight文件转成.h5文件。这也就是Step1_Build_Model.py的功能。转好的文件将被存储到model文件夹。

### Step2 预测图片<br>
预测图片的整个过程被封装为 predict_fig(photo_filename,model) 函数，只需要输入图片名称和模型即可完成对图片的predict工作。对于任一张图片，预测结果包含两部分：1.模型识别出的每一个目标与其对应的置信度，2.标出了识别物体边界框的图片。

比如对于以下图片：<br>
<p align="center">
	<img src="https://github.com/LeeWise9/Object-Detection-With-YOLOv3/blob/master/example_fig/timg.jpg" alt="Sample"  width="400">
</p>

运行结果如下所示：<br>
> car 67.59340167045593 <br>
> car 65.72997570037842 <br>
> car 96.19730710983276 <br>
> car 90.57093858718872 <br>
> car 85.83642244338989 <br>
> ... <br>

标出识别边界框的图像为：<br>
<p align="center">
	<img src="https://github.com/LeeWise9/Img_repositories/blob/master/yolov3_opimg.jpg" alt="Sample"  width="400">
</p>


下面详细讲解预测图片过程中的几个重要步骤：1.图片预处理，2.调用模型做预测计算，3.处理计算结果，4.结果显示。

#### 1.图片预处理<br>
图片预处理是一个老生常谈的问题，主要就是图片缩放、归一化、增维等。<br>
值得一提的是，YOLOv3模型要求输入图片的尺寸为416x416x3，即长宽均为416的3通道彩色图像。生成的边界框是基于缩放之后的图片的，但图片打印时要维持原长宽比。为了使边界框适配原图，还需要借助原图的长宽信息修改边界框角点的位置。这一点相当重要，相关的函数包括：correct_yolo_boxes，load_image_pixels等。

#### 2.调用模型做预测计算<br>
这一点最简单，但是最耗时。比较消耗内存和CPU算力。

#### 3.处理计算结果<br>
模型处理完图片之后将输出识别结果的集合，需要两个主要的处理步骤：1.解码，2.筛选。<br>
先说筛选。结果中的一部分是我们期望的，还有一部分是冗余的，这就需要筛选。项目代码中设置了置信度的筛选阈值，置信度不足的识别框将被删除。这一点相当重要，相关函数包括：do_nms，get_boxes等。
而解码的工作主要是对满足筛选条件的边界框做坐标变换，将输出值转换为能够反映在图片上的坐标信息。相关的函数包括decode_netout等。

#### 4.结果显示<br>
预测结果如何显示呢？本项目中使用了matplotlib绘图显示，读者也可以借助OpenCV或者PIL等工具库重写draw_boxes函数，将预测结果绘图存储。



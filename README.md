# Object-Detection-With-YOLOv3
Object Detection With YOLOv3 in Keras

这是一个基于YOLOv3的目标识别项目，使用keras编写，应该是您能找到的全网最简洁的demo——使用5行代码[加载模型](https://github.com/LeeWise9/Object-Detection-With-YOLOv3/blob/master/Step1_Build_Model.py)，使用30行代码[处理一张图片](https://github.com/LeeWise9/Object-Detection-With-YOLOv3/blob/master/Step2_Predict.py)。当然，这是个小伎俩，因为我把功能性代码全部打包塞到了[help_function.py](https://github.com/LeeWise9/Object-Detection-With-YOLOv3/blob/master/help_function.py)里面了。

如前所述，该项目总共包含两个步骤：1.加载模型，2.预测图片（predict）。

### Step1 加载模型<pr>
本项目是基于YOLOv3的预训练模型[yolov3.weights](https://pjreddie.com/media/files/yolov3.weights)的，为了构建keras能直接使用的.h5模型，需要将.weight文件转成.h5文件。这也就是Step1_Build_Model.py的功能。转好的文件将被存储到model文件夹。

### Step2 预测图片<pr>
预测图片的整个过程被封装为 predict_fig(photo_filename,model) 函数，只需要输入图片名称和模型即可完成对图片的predict工作。对于任一张图片，预测结果包含两部分：1.模型识别出的每一个目标与其对应的置信度，2.标出了识别物体边界框的图片。

比如对于以下图片：<pr>
<p align="center">
	<img src="https://github.com/LeeWise9/Object-Detection-With-YOLOv3/blob/master/example_fig/timg.jpg" alt="Sample"  width="400">
</p>

运行结果如下所示：<pr>
> car 67.59340167045593 <pr>
> car 65.72997570037842 <pr>
> car 96.19730710983276 <pr>
> car 90.57093858718872 <pr>
> car 85.83642244338989 <pr>
> ... <pr>
标出识别边界框的图像为：<pr>
<p align="center">
	<img src="https://github.com/LeeWise9/Img_repositories/blob/master/yolov3.png" alt="Sample"  width="500">
</p>


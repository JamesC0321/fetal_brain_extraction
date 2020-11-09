The project including three stages: (1) coarse extraction, (2) refinement extraction and (3) fusion stage.

How to use the codes:

Firstly, before you use the codes for training and testing, it is strongly recomended you to install the 3D caffe environment, 
            which is described in https://github.com/ginobilinie/caffe3D

Secondly, for preprocessing the images, before using codes for n4 and histgram matching (n4processing.py and hisprocessing.py), it is better for you to 
            make all 3D images into same size, and rotate them into the same direction according to fetal brain.

Thirdly, For training, three models are need to be trained. 
            (1) When training the coarse segmentation model, you can use the PatchFetalWANDP.py to select patches randomly in the 3D image 
            with the same patch size (8*48*48 for example), and then use solver1.prototxt and train1.prototxt to train the model. 
           (2) Then using CutSmallPart.py to cut the original images and corresponding labels into small size for training, the training stage follows the step (1)
           Then you can training the refinement segmentation model. 
           (3) Now, you can use previous two model to test the images to obtain two probability maps by SegmentforPrMaps.py.
           (4) Then, for fusion network training, you can using PatchPr1.py to to select patches randomly in the 3D probability maps and then train
           the model by solver_SimpleNetPr.prototxt and train_SimpleNet.prototxt. 

           For testing.
           (1) For images after preprocessing, you can use the SegmentforPrMaps.py to obtain two probability maps from new images.
           (2) Then, you can use SegPr1.py to obtain the final segmenation results on previous two probability maps. 


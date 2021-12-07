# Gaze Based Annotation of Histopathology Images for Training of Deep Convolutional Neural Networks
This repo contains the code and data used for our work on Gaze-based annotation of histopathology images. Table of contents is given below
* [Dataset](#dataset)
   * Gaze
   * Hand
* [Training](#training)
* [Reference](#reference)

## Dataset
Download our dataset here:

**- Gaze:** Images used for training and testing of gaze-based object detectors can be downloaded from [here](https://1drv.ms/u/s!As_geBXhgCy1qjOElYHo5oWX_OQ0?e=L38qQ6). The labels corresponding to each file in the training and test dataset can be found in "Gaze_Data/labels/train" and "Gaze_Data/labels/test" respectively. 

**- Hand:** Images used for training and testing of object detectors on hand-labelled data can be downloaded from [here](https://1drv.ms/u/s!As_geBXhgCy1qwa3-NdukNHbLRsb?e=NT3Abi). The labels corresponding to each file in the training and test dataset can be found in "Hand_Data/labels/train" and "Hand_Data/labels/test" respectively. `NOTE:` Hand generated labels were used for performance evaluation of both gaze-based and hand-labelled object detectors. Therefore, the contents of both the "Gaze_Data/labels/test" and the "Hand_Data/labels/test" folders are identical. 

## Models
- Our pre-trained Yolo models are available [here](https://1drv.ms/u/s!As_geBXhgCy1rSjYGEV7aMdLiYnr?e=qLZOUz).

## Training
- The training code and required instructions are available for the following modules in their respective folder in the repository:
  - [Yolov3](https://github.com/OAfzal/GazeYoloModels/blob/master/Yolov3)
  - [Yolov4](https://github.com/OAfzal/GazeYoloModels/blob/master/Yolov4)

## Reference
This repo was used to generate the results for the following paper on Gaze-based labelling of Pathology data. 
   
   Komal Mariam, Osama Mohammed Afzal, Wajahat Hussain, Muhammad Umar Javed, Amber Kiyani, Nasir Rajpoot, Syed Ali Khurram and Hassan Aqeel Khan, **"On Smart Gaze based Annotation of Histopathology Images for Training of Deep Convolutional Neural Networks",** *submitted to IEEE Journal of Biomedical and Health Informatics.*

**BibTex Reference:** Available after acceptance.

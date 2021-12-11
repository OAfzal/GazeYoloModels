
<br>
<p>
YOLOv4 🚀 is a family of object detection architectures and models pretrained on the COCO dataset</p>

</div>

## <div align="center">Documentation</div>

### Pretrained Checkpoints

Download Coco Pretrained yolov4 weights and place them in the ./cfg folder
https://drive.google.com/uc?id=1fcbR0bWzYfIEdLJPzOsn4R5mlvR6IQyA

<br>

See the [YOLOv4 Docs](https://docs.ultralytics.com) for full documentation on training, testing and deployment.

## <div align="center">Quick Start Examples</div>

<details open>
<summary>Install</summary>

[requirements.txt](https://github.com/OAfzal/GazeYoloModels/blob/master/yolov4/requirements.txt) installed including

```bash
$ git clone https://github.com/OAfzal/GazeYoloModels
$ cd GazeYoloModels/yolov4
$ pip install -r requirements.txt
```

</details>
<br>

<details open>
<summary>Training with train.py</summary>

`train.py` trains the yolov4 models on the data.

```bash
$ python ./pytorch-YOLOv4/train.py \
  -b {batch_size} \
  -s {sub_divisions} \
  -l {learning_rate} \
  -g {gpu} \
  -pretrained {pth_to_pretrained model placed in ./cfg} \
  -classes {num_classes} \
  -dir {pth_to_train directory} \
  -epochs {num of epochs}
```
Tensorboard is used for logging and so logs can be visualized using the following commands:

```bash
$ tensorboard --logdir '{log_dir}'

```

</details>
<br>


<details open>
<summary>Inference with model.py</summary>

`model.py` runs inference on the data to generate the results.

```bash
$ python pytorch-YOLOv4/models.py \
    {num_classes} \
    {pth_to_model} \
    {Sample Image to Run on} \
    {pth to .classes file} \
    {nms_thresh} \
    {conf_thresh}
```

</details>
<br>

<details open>

* All models were trained for 1000 epochs with with default settings, hyperparameters and Early Stopping Callback with a patience of 100.
* All models stopped training early around the ~300th epoch
* The checkpoints for each of the model can be found [here](https://1drv.ms/u/s!Asufem_WXMfhiiguMXEDkW0ZLkQT?e=rcVJZ5)

</details>


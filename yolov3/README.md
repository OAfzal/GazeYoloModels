
<br>
<p>
YOLOv3 🚀 is a family of object detection architectures and models pretrained on the COCO dataset</p>

<!--
<a align="center" href="https://ultralytics.com/yolov3" target="_blank">
<img width="800" src="https://github.com/ultralytics/yolov5/releases/download/v1.0/banner-api.png"></a>
-->

</div>

## <div align="center">Documentation</div>

See the [YOLOv3 Docs](https://docs.ultralytics.com) for full documentation on training, testing and deployment.

## <div align="center">Quick Start Examples</div>

<details open>
<summary>Install</summary>

[**Python>=3.6.0**](https://www.python.org/) is required with all
[requirements.txt](https://github.com/OAfzal/GazeYoloModels/yolov3/blob/master/requirements.txt) installed including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/):
<!-- $ sudo apt update && apt install -y libgl1-mesa-glx libsm6 libxext6 libxrender-dev -->

```bash
$ git clone https://github.com/OAfzal/GazeYoloModels
$ cd GazeYoloModels/yolov3
$ pip install -r requirements.txt
```

</details>
<br>

<details open>
<summary>Train with train.py</summary>

`train.py` trains the yolo model on the data.

```bash
$ python train.py \
  --img {img_size} \
  --batch {batch_size} \
  --epochs {num_of_epochs} \
  --data {path to {modality}.yaml file} \
  --weights {path to pretrained model i.e. yolov3.pt}
```
Please go through documentation if further hyperparameters need to be adjusted

</details>
<br>


<details open>
<summary>Inference with val.py</summary>

`val.py` runs inference on the data to generate the results.

```bash
$ python val.py --data {path_to_yaml_file} --weights {path_to_model}
```

</details>
<br>

### Pretrained Checkpoints

<details open>

* All models were trained for 1000 epochs with with default settings, hyperparameters and Early Stopping Callback with a patience of 100.
* All models stopped training early around the ~300th epoch
* The checkpoints for each of the model can be found [here](https://1drv.ms/u/s!Asufem_WXMfhilpOnB9XmzLqZDpR?e=DyDm1H)
* Reproduce by `python val.py --data {modality}.yaml --img 640 --conf {} --iou {}`

</details>




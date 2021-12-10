
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
[requirements.txt](https://github.com/ultralytics/yolov3/blob/master/requirements.txt) installed including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/):
<!-- $ sudo apt update && apt install -y libgl1-mesa-glx libsm6 libxext6 libxrender-dev -->

```bash
$ git clone https://github.com/ultralytics/yolov3
$ cd yolov3
$ pip install -r requirements.txt
```

</details>

<details open>
<summary>Inference</summary>

Inference with YOLOv3 gaze or hand models

```python
import torch

# Model
model = torch.hub.load('OAfzal/GazeYoloModels', 'gaze_model')  # or hand_model

# Images
img = 'link to image'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
```

</details>



<details>
<summary>Inference with detect.py</summary>

`detect.py` runs inference on a variety of sources, downloading models automatically from
the releases in this repo and saving results to `runs/detect`.

```bash
$ python detect.py --source 0  # webcam
                            img.jpg  # image
                            vid.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                            'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

</details>

### Pretrained Checkpoints

[assets]: https://github.com/

<details open>
  <summary>Table Notes (click to expand)</summary>

* All checkpoints were trained for 1000 epochs with with default settings, hyperparameters and Early Stopping Callback with a patience of 100.
* All models stopped early around the ~300th epoch
* The checkpoints for each of the model can be found [here]()
* Reproduce by `python val.py --data {modality}.yaml --img 640 --conf {} --iou {}`

</details>

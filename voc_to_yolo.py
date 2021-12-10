"""
Validate a trained  model accuracy on a custom dataset

Usage:
    $ python voc_to_yolo --path GazeData/ 
"""

import argparse
import cv2
import glob
import xml.etree.ElementTree as ET
from tqdm import tqdm
import os
from PIL import Image
import shutil


def convert(img_size, box):
    # Width Scale Factor
    dh, dw = 1.0 / img_size[0], 1.0 / img_size[1]

    # Converting to the Middle
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0

    # Calculating Width and Height
    w = box[2] - box[0]
    h = box[3] - box[1]

    x, w = x * dw, w * dw
    y, h = y * dh, h * dh

    return [x, y, w, h]


def to_png(img_path):

    im = Image.open(img_path)
    os.remove(img_path)
    im.save(img_path.replace(".jpg", ".png"))


def read_region(xml_path):
    reg = []
    tree = ET.parse(xml_path)
    for obj in tree.findall("object"):
        name = obj.find("name").text
        bndbox = obj.find("bndbox")
        box = [
            int(bndbox.find("xmin").text),
            int(bndbox.find("ymin").text),
            int(bndbox.find("xmax").text),
            int(bndbox.find("ymax").text),
        ]
        reg.append((name, box))
    return reg


def voc_to_yolo(xml_path, classes):
    voc_regions = read_region(xml_path)

    yolo_regions = []

    img_path = xml_path.replace("labels", "images").replace("xml", "png")
    img = cv2.imread(img_path)
    img_shape = img.shape

    for lbl, xyxy in voc_regions:
        xywh = convert(img_shape, xyxy)
        xywh = list(map(str, xywh))

        row = f"{classes.index(lbl)} {' '.join(xywh)}"
        yolo_regions.append(row)

    with open(xml_path.replace(".xml", ".txt"), "w") as f:
        f.write("\n".join(yolo_regions))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data", type=str, required=True, help="path to a data folder i.e. Gaze_Data/}"
    )

    parser.add_argument("-c", "--classes", nargs="*", default=["Keratin_Pearl"])
    opt = parser.parse_args()
    classes = opt.classes

    pth_to_xml = os.path.join(opt.data, "**/*.xml")
    xml_files = glob.glob(pth_to_xml, recursive=True)

    print(opt)
    print(f"No of Files Found: {len(xml_files)}")

    assert len(xml_files) != 0

    train_images = glob.glob(os.path.join("/images/train/*.png"), recursive=True)
    train_images = ["/".join(os.path.realpath(i).split("/")[-5:]) for i in train_images]

    test_images = glob.glob("../data/Gaze_Data/images/test/*.png", recursive=True)
    test_images = ["/".join(os.path.realpath(i).split("/")[-5:]) for i in test_images]

    with open("../data/Gaze_Data/train.txt", "w") as f:
        f.write("\n".join(train_images))

    with open("../data/Gaze_Data/val.txt", "w") as f:
        f.write("\n".join(test_images))

    print(f"Converting voc to yolo format")
    for xml_f in tqdm(xml_files):
        voc_to_yolo(xml_f, classes)

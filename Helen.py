import os
import torch
import torchvision
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
from PIL import Image, ImageDraw, ImageFont
import Config as cfg
import random

def get_max_box(ann, size):
    min_x = 100000
    max_x = 0
    min_y = 100000
    max_y = 0
    for i in ann:
        if i[0] < min_x:
            min_x = i[0]
        if i[0] > max_x:
            max_x = i[0]
        if i[1] < min_y:
            min_y = i[1]
        if i[1] > max_y:
            max_y = i[1]
    min_x -= random.randint(0, 20)
    min_y -= random.randint(0, 20)
    max_x += random.randint(0, 20)
    max_y += random.randint(0, 20)
    if max_x > size[0]:
        max_x = size[0]
    if max_y > size[1]:
        max_y = size[1]
    return min_x, min_y, max_x, max_y


def read_all_annotation(path):
    files = os.listdir(path)
    annotation = {}
    for file in files:
        with open(path + "/" + file) as af:
            key = af.readline().strip()
            points = []
            annotation[key] = points
            for i in range(194):
                point = af.readline()
                sx, sy = point.split(',')
                x = float(sx)
                y = float(sy)
                points.append((x, y))
    return annotation


annotations = read_all_annotation(cfg.path + cfg.annotation)
font_size = 16
font1 = ImageFont.truetype(r'./Ubuntu-B.ttf', font_size)

for key in annotations:
    img = Image.open(cfg.path + "train/" + key + ".jpg")
    width = img.size[0]
    height = img.size[1]
    ann = annotations[key]
    face_area = get_max_box(ann)
    print(face_area)
    img = img.crop(face_area)

    # draw = ImageDraw.Draw(img)
    # draw.point(ann,  fill=(255, 0, 0))
    # for i in range(194):
    #     center_x = ann[i][0] - font_size/2
    #     center_y = ann[i][1] - font_size/2
    #     draw.text((center_x, center_y), str(i), fill=(0, 255, 0), font=font1)
    img.show()
    break

class HellenDataset(Dataset):
    def __init__(self, is_train, width, height):
        self.width = width
        self.height = height
        self.is_train = is_train
        if is_train:
            self.file_path = cfg.path+cfg.train_txt
        else:
            self.file_path = cfg.path + cfg.test_txt
        self.annotations = read_all_annotation(cfg.path + cfg.annotation)
        self.files = []
        with open(self.file_path) as f:
            self.files.append(f.readline())

    def __len__(self):
        return len(self.files)

    def __getitem__(self, item):
        file_name = self.files[item]
        img = Image.open(cfg.path + "train/" + file_name)
        ann = annotations[file_name.replace(".jpg", "")]
        face_area = get_max_box(ann, img.size)
        img = img.crop(face_area)




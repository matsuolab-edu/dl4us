import re
import json

import nltk
import numpy as np
from PIL import Image

nltk.download('punkt')

N_TRAIN_DATA = 50000
N_VALID_DATA = 1000
HEIGHT = 224
WIDTH = 224

TRAIN_IMG_DIR = 'download/train2014/'
VALID_IMG_DIR = 'download/val2014/'

TRAIN_CAP_PATH = 'download/annotations/captions_train2014.json'
VALID_CAP_PATH = 'download/annotations/captions_val2014.json'

TRAIN_X_PATH = 'data/x_train.npy'
TRAIN_Y_PATH = 'data/y_train.txt'

VALID_X_PATH = 'data/x_valid.npy'
VALID_Y_PATH = 'data/y_valid.txt'

# 参考: https://github.com/yunjey/show-attend-and-tell
def resize_img(img):
    w, h = img.size
    if w > h:
        l = (w - h) / 2
        r = w - l
        t = 0
        b = h
    else:
        t = (h - w) / 2
        b = h - t
        l = 0
        r = w
    img = img.crop((l, t, r, b))
    img = img.resize([HEIGHT, WIDTH], Image.ANTIALIAS)
    return img

def preprocess_cap(cap):
    cap = cap.lower()
    cap = ' '.join(nltk.word_tokenize(cap))
    return cap

def preprocess(images, annotations, n_data, dir_path):
    id_to_filename = {image['id']: image['file_name'] for image in images}

    x_data, y_data = [], []
    i = 0
    for annotation in annotations:
        img_id = annotation['image_id']
        img_path = dir_path + id_to_filename[img_id]
        img = Image.open(img_path)
        img = np.array(resize_img(img))

        # Load caption
        cap = annotation['caption']
        cap = preprocess_cap(cap)
        
        if img.shape != (HEIGHT, WIDTH, 3):
            continue
        
        x_data.append(img)
        y_data.append(cap)

        i += 1
        if i >= n_data:
            break
    
    x_data = np.stack(x_data, axis=0)
    y_data = '\n'.join(y_data) + '\n'
    
    return x_data, y_data

with open(TRAIN_CAP_PATH, 'r') as f:
    caption_train = json.load(f)
with open(VALID_CAP_PATH, 'r') as f:
    caption_valid = json.load(f)

x_train, y_train = preprocess(caption_train['images'], caption_train['annotations'], N_TRAIN_DATA, TRAIN_IMG_DIR)
x_valid, y_valid = preprocess(caption_valid['images'], caption_valid['annotations'], N_VALID_DATA, VALID_IMG_DIR)

np.save(TRAIN_X_PATH, x_train)
np.save(VALID_X_PATH, x_valid)

with open(TRAIN_Y_PATH, 'w') as f:
    f.write(y_train)
with open(VALID_Y_PATH, 'w') as f:
    f.write(y_valid)

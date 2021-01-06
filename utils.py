import pandas as pd
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os

# this function will help up to load images and preprocess them before inputting them into our model for testing (they need to be in jpg or png)

def get_imgs(path, size=(32, 32), grayscale=False):
    """ Returns a list of images from a folder as a numpy array """
    img_list = [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".jpg") or f.endswith(".png")]
    imgs = None 
    if grayscale:
        imgs = np.empty([len(img_list), size[0], size[1]], dtype=np.uint8) 
    else:
        imgs = np.empty([len(img_list), size[0], size[1], 3], dtype=np.uint8) 

    for i, img_path in enumerate(img_list):
        img = Image.open(img_path).convert('RGB')
        img = img.resize(size)
        im = np.array(to_grayscale(img)) if grayscale else np.array(img)
        imgs[i] = im

    return imgs
   
# display images contained in the img lists and their labels
def show_imgs(img_list, img_labels, title, cols=2, fig_size=(15, 15), show_ticks=True):
    """ Utility function to show us a list of traffic sign images """
    img_count = len(img_list)
    rows = img_count // cols
    cmap = None
    fig, axes = plt.subplots(rows, cols, figsize=fig_size)
    
    for i in range(0, img_count):
        img_name = img_labels[i]     
        img = img_list[i]
        
        if len(img.shape) < 3 or img.shape[-1] < 3:
            cmap = "gray"
            img = np.reshape(img, (img.shape[0], img.shape[1]))
        
        if not show_ticks:            
            axes[i].axis("off")
            
        axes[i].imshow(img, cmap=cmap)
    
    fig.suptitle(title, fontsize=12, fontweight='bold', y = 0.6)
    fig.tight_layout()
    plt.show()
    
    return
   
#Image processing functions

def to_normalize(img):
    """ Normalize the input images """
    gray_img  = np.sum(img, axis=3, keepdims=True)/3
    gray_img -= np.mean(gray_img, axis=0)
    gray_img /= (np.std(gray_img, axis=0) + np.finfo('float32').eps)
    
    return gray_img

def to_grayscale(img):
    """ Converts an image in RGB format to grayscale using OpenCV """
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


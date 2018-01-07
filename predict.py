# -*- coding: utf-8 -*- 
#  人工智能跳一跳助手 by 刘云飞
import sys
import numpy as np
import random
from keras import layers
from keras import models
from keras.preprocessing import image
import os
import shutil
import time
import math
from PIL import Image, ImageDraw
import random
import json
from mymodel import get_model

def pull_screenshot():
    
    os.system('adb shell screencap -p /sdcard/1.png')
    os.system('adb pull /sdcard/1.png .')

def maxNoOfArry(arry):
    i=0
    for a in arry:
        if abs(a - max(arry)) < 1e-6:
            no = i
            return no
        else:
            i =i + 1  
    return no 

model = get_model()
model.load_weights("first.h5")
print("Start---->>>>>>>")

while True:
        pull_screenshot()        
        img = image.load_img("1.png", target_size=(135, 240))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)        
        numa = model.predict(x)
        print(numa)
        numb = maxNoOfArry( numa[0] )
        holdtime = (int(numb))*30+200        
        print(holdtime)
        swipe_x1 = 320 +random.randint(1,50)
        swipe_y1 = 410 +random.randint(1,100)
        swipe_x2=swipe_x1
        swipe_y2=swipe_y1
        time.sleep(random.uniform(1.1, 1.8))
        cmd = 'adb shell input swipe {} {} {} {} {}'.format(swipe_x1, swipe_y1, swipe_x2, swipe_y2, holdtime)
        print(cmd)
        os.system(cmd)
        time.sleep(random.uniform(1.1, 2)) 

    



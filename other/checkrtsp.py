#!/user/bin/env python3
# -*- coding: utf-8 -*-
from asyncio.windows_events import NULL
import datetime
import numpy as np
import pandas as pd
import requests
import json
import urllib.parse
import re
import cv2
import eventlet


old_item = []

def get_data():
    old_df = pd.DataFrame(pd.read_excel("rtsp.xlsx"))
    for i,r in old_df.iterrows():
        item = str(r["key"])
        old_item.append(item)
    print(len(old_item))

def get_pic():
    i = 0
    for item in old_item:
        i = i+1
        
        try:
            workDone = False
            eventlet.monkey_patch() 
            with eventlet.Timeout(3, False):
                cap = cv2.VideoCapture("rtsp://admin:admin@"+item)
                ret, frame = cap.read()
                if ret :
                    cv2.imwrite(str(i) + '.jpg', frame)
                cap.release()
                workDone = True
            if workDone:
                print ("work is done")
            else:
                print ("url is dead!")
        except:
            cap.release()
            continue


if __name__ == '__main__':
    get_data()
    get_pic()
    
 



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:20:17 2023

@author: gabr4477
"""

import cv2
import glob
import os

#%%
# setting path and working directory 
path = '/Users/gabr4477/otoliths/GB_samples/New_Zealand/zoomed'
os.chdir(path)
#%% 
# loading in all images
file = os.path.join(path,'*.png')
glob.glob(file)
# Using List Comprehension to read all images
images = [cv2.imread(image) for image in glob.glob(file)]

#%%
for image in images:
    # change images to b&w
    b_w = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    # gaussian blurr
    blurred = cv2.GaussianBlur(b_w, (5, 5), 10, cv2.BORDER_DEFAULT)
    # adaptive thresholding
    frames = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 1)
    #defining columns and rows of new array 
    rows = frames.shape[0]
    cols = frames.shape[1]
    # selecting the middle column of the array to use for ring count for loop
    column_index = int(cols / 2)
    ring_count = 0

# Start with the second row
    for i in range(1, rows):
        # If this pixel is white and the previous pixel is black
        if 255 == frames[i, column_index] and 0 == frames[i - 1, column_index]:
            ring_count += 1
            
# prints ring count for image in order of images loaded into script. 
    print(ring_count, 'rings')
 
#%%

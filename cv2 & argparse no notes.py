# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:17:51 2019

@author: Student
"""
import argparse
import cv2
import numpy as np

def main():
    global image
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to the image", dest = 'img')
    ap.add_argument("--x1", required = True, help = "scales to image cropping", dest = 'x_start')
    ap.add_argument("--x2", required = True, help = "scales to image cropping", dest = 'x_end')
    ap.add_argument("--y1", required = True, help = "scales to image cropping", dest = 'y_start')
    ap.add_argument("--y2", required = True, help = "scales to image cropping", dest = 'y_end')
    inputs = ap.parse_args()
    image = cv2.imread(inputs.img)
    inputs = ap.parse_args()
    x1,x2,y1,y2 = inputs.x_start, inputs.x_end, inputs.y_start, inputs.y_end
    
    cv2.imshow("Original", image)
    cv2.waitKey(0)
    x1,x2,y1,y2 = 0,100,0,100
    crop(x1,x2,y1,y2)
    color(x1,x2,y1,y2,0,255,0)
    rotate (90, 1.0, None)
    resize (500, None)

def crop(x1,x2,y1,y2):
    global image
    cropped = image[x1:x2 , y1:y2]
    cv2.imshow("cropped", cropped)
    cv2.waitKey(0)
    
def color(x1,x2,y1,y2,R,G,B):
    global image
    colored = image+0
    colored[x1:x2 ,y1:y2] = (R,G,B)
    cv2.imshow("colored", colored)
    cv2.waitKey(0)
    
def rotate (angle, scale, center):
    global image
    (h, w) = image.shape[:2]
    if center == None:
        center = (w // 2, h // 2) 
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h)) 
    cv2.imshow("rotated", rotated)
    cv2.waitKey(0)
    
def resize (width, hight):
    global image
    if width == None and hight == None: cv2.imshow("Original", image)
    if width == None: 
        ratio = hight / image.shape[0]
        dim = (int(ratio * image.shape[1]), int(hight))
    if hight == None: 
        ratio = width / image.shape[1]
        dim = (int(width), int(ratio * image.shape[0]))
    
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
    cv2.imshow("resized", resized)
    cv2.waitKey(0)

main()
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:17:51 2019
@author: Yehonatan Tal
"""
import argparse
import cv2


def main():
    global image
    # gets the inputs from inpts() and getting the image and data from it.
    inputs = inpts()
    image = cv2.imread(inputs.img)
    y1,y2,x1,x2 = inputs.x_start, inputs.x_end, inputs.y_start, inputs.y_end
    y1,y2,x1,x2 = int(y1),int(y2),int(x1),int(x2)
    cv2.imshow("Original", image)
    cv2.waitKey(0)
    crop(y1,y2,x1,x2) #show croped image
    color(y1,y2,x1,x2,0,255,0) #show colored image
    rotate (int(inputs.angle), 1.0, None) #show rotated image
    if str(inputs.WHscale) == 'w': resize (int(inputs.rescale), None) #show resized image if width was given
    if str(inputs.WHscale) == 'h': resize (None, int(inputs.rescale)) #show resized image if hight was given
    
    
    
def inpts():
    # uses argparse via the anaconda prompt to get the image path & scales for cropping and coloring & rotate angle & resize details
    # a proper input int the prompt: python "program path" -i "image path" --x1 10 --x2 50 --y1 0 --y2 100 --angle 60 --WH h --rescale 650
    global image
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required = True, help = "Path to the image", dest = 'img')
    ap.add_argument("--y1", required = True, help = "y start scale for image cropping & coloring", dest = 'y_start')
    ap.add_argument("--y2", required = True, help = "y end scale for image cropping & coloring", dest = 'y_end')
    ap.add_argument("--x1", required = True, help = "x start scale for image cropping & coloring", dest = 'x_start')
    ap.add_argument("--x2", required = True, help = "x end scale for image cropping & coloring", dest = 'x_end')
    ap.add_argument("--angle", required = True, help = "rotate angle", dest = 'angle')
    ap.add_argument("--WH", required = True, help = "scale to resize (h or w)", dest = 'WHscale')
    ap.add_argument("--rescale", required = True, help = "new scale", dest = 'rescale')
    return ap.parse_args()


def crop(y1,y2,x1,x2):
    # cropping the image based on input and showing image until '0' is pressed
    global image
    cropped = image[y1:y2 , x1:x2]
    cv2.imshow("cropped", cropped)
    cv2.waitKey(0)
    
    
def color(y1,y2,x1,x2,R,G,B):
    # coloring green the area in image based on input and showing image until '0' is pressed
    global image
    colored = image+0
    colored[y1:y2 ,x1:x2] = (R,G,B)
    cv2.imshow("colored", colored)
    cv2.waitKey(0)
    
    
def rotate (angle, scale, center):
    # rotating the image based on input and showing image until '0' is pressed
    global image
    (h, w) = image.shape[:2]
    if center == None:
        center = (w // 2, h // 2) 
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h)) 
    cv2.imshow("rotated", rotated)
    cv2.waitKey(0)
    
    
def resize (width, hight):
    # resizing the image based on input (if it's w or h) while keeping scale ratio, and showing image until '0' is pressed.
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
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:40:57 2020

@author: uriel
"""

import os
import subprocess, sys
import face_recognition
import cv2
import dlib 
from PIL import Image


path_to_searching = input("pleasse Enter path to search")
list_of_path = list()
for root,dirs,files in os.walk(path_to_searching):
    for file in files:
        if file.endswith('jpg'):
            list_of_path.append(os.path.join(root, file))
            
image_comp_path = input("please enter the image path")
image_to_compare = face_recognition.load_image_file(image_comp_path)
image_to_encoding = face_recognition.face_encodings(image_to_compare)

index = 1

list_of_pic = list()
for image_path in list_of_path:
    temp_image_upload = face_recognition.load_image_file(image_path)
    every_face_detace = face_recognition.face_locations(temp_image_upload , model = 'hog')
    every_face_encoding = face_recognition.face_encodings(temp_image_upload, every_face_detace)
    
    for current_encoding in every_face_encoding:
        flag_for_match = face_recognition.compare_faces(image_to_encoding, current_encoding)
       
        if True in flag_for_match:
            if not list_of_pic.__contains__(image_path):
                list_of_pic.append(image_path)


for new_image in list_of_pic:
    im = Image.open(new_image)
    im.show()
 
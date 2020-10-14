#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:12:31 2020

@author: uriel
"""

import face_recognition
from PIL import Image , ImageDraw

face_image = face_recognition.load_image_file("Picture_for_test/uriel")

face_landmark_list = face_recognition.face_landmarks(face_image)

print(face_landmark_list)

for face_landmarks in face_landmark_list:
    pil_image = Image.fromarray(face_image)
    d = ImageDraw.Draw(pil_image)
    
    d.line(face_landmarks['chin'],fill=(255,255,255), width=2)
    d.line(face_landmarks['left_eyebrow'],fill=(255,255,255), width=2)
    d.line(face_landmarks['right_eyebrow'],fill=(255,255,255), width=2)
    d.line(face_landmarks['nose_bridge'],fill=(255,255,255), width=2)
    d.line(face_landmarks['nose_tip'],fill=(255,255,255), width=2)
    d.line(face_landmarks['left_eye'],fill=(255,255,255), width=2)
    d.line(face_landmarks['right_eye'],fill=(255,255,255), width=2)
    d.line(face_landmarks['top_lip'],fill=(255,255,255), width=2)
    d.line(face_landmarks['bottom_lip'],fill=(255,255,255), width=2)
    
    pil_image.show()

#save the image
pil_image.save("abhi_landmarks.jpg")

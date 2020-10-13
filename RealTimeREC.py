#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 17:53:21 2020

@author: uriel
"""

import cv2 
import dlib
import face_recognition

catch_web_stream = cv2.VideoCapture(0)

all_face_location = [] 

while True:
    #get the face in current frame from stream
    #if it catch flag will be boolean
    flag,current_frame = catch_web_stream.read()
    
    #for more faster prosses resize the image
    
    current_frame_small = cv2.resize(current_frame,(0,0),fx =0.25,fy=0.25)
    
    all_face_location = face_recognition.face_locations(current_frame_small,model = 'hog')
    
    for index,current_face in enumerate(all_face_location):
    #split the tuple of position to 4 
        top_pos,right_pos,bottom_pos,left_pos = current_face
        top_pos = top_pos * 4
        bottom_pos = bottom_pos * 4
        left_pos = left_pos * 4 
        right_pos = right_pos*4
        print('found face {} at top:{},right:{},bottom{},left:{}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))
        #resize to normal size after prosses
        cv2.rectangle(current_frame,(left_pos,top_pos) , (right_pos,bottom_pos), (0,0,255) ,2)
    cv2.imshow('webcam video', current_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
catch_web_stream.release()
cv2.destroyAllWindows()
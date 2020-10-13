#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 17:53:21 2020

@author: uriel
"""


#importing lib 

import cv2
import dlib
import face_recognition



# check how much face will be in the photo 
original_image = cv2.imread('/home/uriel/Desktop/test1')
 
image_to_detect_test1 = face_recognition.load_image_file('/home/uriel/Desktop/uriel')

image_face_encoding1 = face_recognition.face_encodings(image_to_detect_test1)[0]

image_to_detect_test2 = face_recognition.load_image_file('/home/uriel/Desktop/ron')

image_face_encoding2 = face_recognition.face_encodings(image_to_detect_test2)[0]

know_face_encoding = [image_face_encoding1 , image_face_encoding2]

know_face_names = ["uriel abergel" , "ron mizrahi"]

image_to_reco = face_recognition.load_image_file('/home/uriel/Desktop/test1')

all_face_location = face_recognition.face_locations(image_to_reco,model = "hog")

all_face_encoding = face_recognition.face_encodings(image_to_reco,all_face_location)

print('there are {}  of faces in this image' .format(len(all_face_location) )) 
name_of_person = 'none'
for current_face_loc,current_face_enco in  zip(all_face_location,all_face_encoding):
     top_pos,right_pos,bottom_pos,left_pos = current_face_loc
     all_matches = face_recognition.compare_faces(know_face_encoding, current_face_enco)
     
     if True in all_matches:
         first_match_index = all_matches.index(True)
         name_of_person = know_face_names[first_match_index]
         
     cv2.rectangle(original_image,(left_pos,top_pos) , (right_pos,bottom_pos), (0,0,255) ,2)
         
     font = cv2.FONT_HERSHEY_TRIPLEX
     cv2.putText(original_image, name_of_person, (left_pos,bottom_pos), font, 6, (0,0,0))
     
     current_frame_small = cv2.resize(original_image,(0,0),fx =0.40,fy=0.4)
     cv2.imshow("face:" , current_frame_small)
     
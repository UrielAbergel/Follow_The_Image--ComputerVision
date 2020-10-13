# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#importing lib 

import cv2
import dlib
import face_recognition



# check how much face will be in the photo 
 
 
image_to_detect = cv2.imread('/home/uriel/Desktop/test.jpg')

##print how much face will get in the photo

#given array of tupple that get face 
detect_face = face_recognition.face_locations(image_to_detect,model = "hog")

print('there are {}  of faces in this image' .format(len(detect_face) )) 


# print every face 

for index,current_face in enumerate(detect_face):
    #split the tuple of position to 4 
    top_pos,right_pos,bottom_pos,left_pos = current_face
    print('found face {} at top:{},right:{},bottom{},left:{}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))
    
    #print the faces
    current_face_to_print = image_to_detect[top_pos:bottom_pos,left_pos:right_pos]
    cv2.imshow("Face Number"+str(index+1), current_face_to_print)
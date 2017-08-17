"""
Pyhton script for loading and resizing positive and negative images for the haar cascade classification
@author: wimmer, simon-justus | https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
"""

print "Veraltet... bitte anderes Skript nutzen"
"""
import urllib
import cv2
import numpy as np
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# parameters
dir_negs = 'neg_p'
dir_pos = 'pos'
dir_info = 'info_p'

#function for loading and resizing (negative) images from urls for openCV cascade classification
def store_raw_image():
    neg_image_link = link_faces
    print(neg_image_link)
    neg_image_urls = urllib.urlopen(neg_image_link).read().decode()

    if not os.path.exists(dir_negs):
        os.mkdir(dir_negs)

    pic_num = 1

    for i in neg_image_urls.split('\n'):
        try:
            if 'adcomlive' not in i and 'homedepot' not in i:
                print(i)
                urllib.urlretrieve(i,dir_negs+'/'+str(pic_num)+'.jpg')
                img = cv2.imread(dir_negs+'/'+str(pic_num)+'.jpg', cv2.IMREAD_GRAYSCALE)
                resized_image = cv2.resize(img, (100,100))
                cv2.imwrite(dir_negs+'/'+str(pic_num)+'.jpg', resized_image)
                pic_num += 1
        except Exception as e:
            print (str(e))



# function deletes pics that are similar to the ones in directory ugly
def find_uglies():
    match = False
    for file_type in [dir_negs]:
        for img in os.listdir(file_type):
            for ugly in os.listdir('ugly'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('ugly/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()): # same dimension and
                        print('That is one ugly pic! Deleting!')                                  # nothing different..
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))

# function creates the description files for pos and neg images
def create_pos_n_neg():
    for file_type in [dir_negs]:

        for img in os.listdir(file_type):
            if file_type == dir_negs:
                line = file_type+'/'+img+'\n'
                with open('bg_p.txt', 'a') as f:
                    f.write(line)

            elif file_type == dir_pos:
                line = file_type+'/'+img+'1 0 0 50 50\n'
                with open(dir_info, 'a') as f:
                    f.write(line)


# find_uglies()
create_pos_n_neg()
# store_raw_image()
"""
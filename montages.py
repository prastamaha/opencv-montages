from imutils import paths
from imutils import build_montages
import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the image directory')
ap.add_argument('-s', '--sample', type=int, default=4, help='lots of pictures in montage')
args = vars(ap.parse_args())

# read all the images in the directory then change it become a list
imagePaths = list(paths.list_images(args['image']))
imagePaths = imagePaths[:args['sample']]

images = []
for imagePath in imagePaths:
    img = cv2.imread(imagePath)
    images.append(img)

# create montage
# build_montages(images_list, (width,height), (column,row))
montages = build_montages(images, (500,500), (2,2)) # return numpy array

randomName = str(np.random.randint(100,1000))

for montage in montages:
    cv2.imwrite(f'output-{randomName}.jpg', montage)
    cv2.imshow('montage', montage)
    cv2.waitKey(0)

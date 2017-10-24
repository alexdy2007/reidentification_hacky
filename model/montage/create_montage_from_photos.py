from imutils import build_montages
import math
import random
import cv2

def create_montage(image_list, samples=10):
    samples = min(len(image_list), samples)
    imagePaths = image_list
    random.shuffle(imagePaths)
    imagePaths = imagePaths[:samples]
    # initialize the list of images

    images = []
    # loop over the list of image paths
    for imagePath in imagePaths:
        # load the image and update the list of images
        image = cv2.imread(imagePath)
        images.append(image)

    # construct the montages for the images
    h = math.ceil(round(samples/2))
    w = 2
    print(len(images))
    if len(images) == 1:
        resized_img = cv2.resize(images[0], (256,256), interpolation=cv2.INTER_AREA)
        montages = [resized_img]
    elif len(images) > 1:
        montages = build_montages(images, (256, 256), (w, h))
    else:
        montages =[]

    for montage in montages:
	    cv2.imshow("Montage", montage)

    cv2.waitKey(0)
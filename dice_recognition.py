#from ..dataset.exploratory_analysis.ipynb import dataset_path
from dataset import labels.csv
import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd



# loading the images
img = cv.imread(f"{dataset_path}/**/*.jpg")

# color to gray
def gray(imagenes):
    for im in imagenes: 
        image_gray = []
        image_gray.append(cv.cvtColor(img, cv.COLOR_BGR2GRAY))
    return image_gray


plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()
import glob
import string
import time
from datetime import datetime
from multiprocessing.pool import ThreadPool
from typing import Any

from PIL import Image
from shutil import copyfile
import os, os.path
import cv2
import time

start = time.time()

resultPath = 'C:/Users/Vartotojas/OneDrive - Kaunas University of Technology/Darbalaukis/IN_Lygiagretus/Results/'
highResolutionPath = "C:/Users/Vartotojas/OneDrive - Kaunas University of Technology/Darbalaukis/IN_Lygiagretus/HighResolutionImages"
lowResolutionPath = "C:/Users/Vartotojas/OneDrive - Kaunas University of Technology/Darbalaukis/IN_Lygiagretus/LowResolutionImages"
def readImages(path):

    images = []
    valid_images = [".jpg", ".gif", ".png", ".tga",
                    ".jpeg", ".PNG", ".JPG", ".JPEG"]

    for file in os.listdir(path):
        ext = os.path.splitext(file)[1]
        if ext.lower() not in valid_images:
            continue
        images.append(file)
    return images


def filterImages(images: list, thresholdWidth: int, thresholdHeight: int, mypath: Any):
    count = 0
    for i in images:
        image = cv2.imread(str(mypath) + '/' + i)
        height = image.shape[0]
        width = image.shape[1]
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        if (width <= thresholdWidth and height <= thresholdHeight):
            img_rst = cv2.GaussianBlur(image, (9,9), cv2.BORDER_DEFAULT)
            cv2.imwrite(str(resultPath) + str(date_time) + str(count)+'.png', img_rst)
            count += 1

        elif (width <= thresholdWidth and height >= thresholdHeight):
            img_rst = cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)
            cv2.imwrite(str(resultPath) + + str(date_time) + str(count) + '.png', img_rst)
            count += 1

if __name__ == '__main__':
    highResolutionImages = list(readImages(highResolutionPath))
    lowResulutionImages = list(readImages(lowResolutionPath))

    num_process = 2
    task = filterImages(highResolutionImages, 1000, 1000, highResolutionPath)
    task2 = filterImages(lowResulutionImages, 1000, 1000, lowResolutionPath)
    print(f'MESSAGE: Running {num_process} process')
    ThreadPool(num_process).imap_unordered(task, highResolutionImages)
    end1 = time.time()
    ThreadPool(num_process).imap_unordered(task2, lowResulutionImages)
    end2 = time.time()
    print('Time taken to blur {}'.format(len(highResolutionImages)))
    print(end1 - start)
    print('Time taken to blur {}'.format(len(lowResulutionImages)))
    print(end2 - start)
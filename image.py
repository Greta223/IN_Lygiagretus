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

resultPathSmall = 'C:/Users/Vartotojas/OneDrive - Kaunas University of Technology/Darbalaukis/IN_Lygiagretus/ResultsSmall/'
resultPathMedium = 'C:/Users/Vartotojas/OneDrive - Kaunas University of Technology/Darbalaukis/IN_Lygiagretus/ResultsMedium/'
resultPathLarge = 'C:/Users/Vartotojas/OneDrive - Kaunas University of Technology/Darbalaukis/IN_Lygiagretus/ResultsLarge/'
smallResolutionPath = "C:/Users/Vartotojas/OneDrive - Kaunas University of Technology/Darbalaukis/IN_Lygiagretus/SmallResolutionImages10"
mediumResolutionPath = "C:/Users/Vartotojas/OneDrive - Kaunas University of Technology/Darbalaukis/IN_Lygiagretus/MediumResolutionImages10"
largeResolutionPath = "C:/Users/Vartotojas/OneDrive - Kaunas University of Technology/Darbalaukis/IN_Lygiagretus/LargeResolutionImages10"

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


def blurImages(images: list, resultPath: Any, mypath: Any):
    count = 0
    for i in images:
        image = cv2.imread(str(mypath) + '/' + i)
        img_rst = cv2.GaussianBlur(image, (9,9), cv2.BORDER_DEFAULT)
        cv2.imwrite(str(resultPath) + str(count)+'.png', img_rst)
        count += 1

if __name__ == '__main__':
    smallResolutionImages = list(readImages(smallResolutionPath))
    mediumResolutionImages = list(readImages(mediumResolutionPath))
    largeResolutionImages = list(readImages(largeResolutionPath))

    num_process = 200
    print(f'MESSAGE: Running {num_process} process')
    start1 = time.time()
    ThreadPool(num_process).imap_unordered(blurImages(smallResolutionImages, resultPathSmall, smallResolutionPath), smallResolutionImages)
    print(f'MESSAGE: Small images are finished bluring')
    end1 = time.time()
    start2 = time.time()
    ThreadPool(num_process).imap_unordered(blurImages(mediumResolutionImages, resultPathMedium, mediumResolutionPath), mediumResolutionImages)
    print(f'MESSAGE: Medium images are finished bluring')
    end2 = time.time()
    start3 = time.time()
    ThreadPool(num_process).imap_unordered(blurImages(largeResolutionImages, resultPathLarge, largeResolutionPath), largeResolutionImages)
    print(f'MESSAGE: Large images are finished bluring')
    end3 = time.time()
    print('Time taken to blur small images {}'.format(len(smallResolutionImages)))
    print(end1 - start1)
    print('Time taken to blur medium images {}'.format(len(mediumResolutionImages)))
    print(end2 - start2)
    print('Time taken to blur large images {}'.format(len(largeResolutionImages)))
    print(end3 - start3)
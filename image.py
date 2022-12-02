import glob
import string
import time
from datetime import datetime
from multiprocessing import Pool, Process
import multiprocessing as mp
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
results = 'C:/Users/Vartotojas/OneDrive - Kaunas University of Technology/Darbalaukis/IN_Lygiagretus/Results/'

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


def blurImages(picture):

    print(f'Process {mp.current_process().name} started working on task {picture}', flush=True)
    now = datetime.now()
    date_time = now.strftime("%m_%d_%Y%H_%M_%S")
    image = cv2.imread(str(smallResolutionPath) + '/' + picture)
    img_rst = cv2.GaussianBlur(image, (9, 9), cv2.BORDER_DEFAULT)
    cv2.imwrite(f'{str(results)}{str(picture)}.png', img_rst)
    print(f'Process {mp.current_process().name} ended working on task {picture}', flush=True)

if __name__ == '__main__':
    smallResolutionImages = list(readImages(smallResolutionPath))
    mediumResolutionImages = list(readImages(mediumResolutionPath))
    largeResolutionImages = list(readImages(largeResolutionPath))

    num_process = 4
    CPU_COUNT = mp.cpu_count()
    print(CPU_COUNT)
    start = time.monotonic()
    with Pool(4) as pool:
        iterator = pool.map(blurImages, smallResolutionImages)
    print(f'time took: {time.monotonic() - start:.4f}')

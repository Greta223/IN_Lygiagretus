import glob
import string
import time
from multiprocessing.pool import ThreadPool
from typing import Any

from PIL import Image
from shutil import copyfile
import os, os.path

start = time.time()

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

    filteredImages = []
    for i in images:
        #image = Image.open("C:/Users/Vartotojas/OneDrive - Kaunas University of Technology/Darbalaukis/IN_Lygiagretus/HighResolutionImages/pexels-flo-dahm-699466.jpg")
        # Storing width and height of a image
        image = Image.open(mypath + "/" + i)
        width, height = image.size

        # if only width exceeds the thresholdWidth
        if (width > thresholdWidth and
                height <= thresholdHeight):

            image.resize((thresholdWidth,
                          (thresholdWidth * height)
                          // width)).save(i)

        # if only height exceeds the thresholdHeight
        elif (width <= thresholdWidth and
              height > thresholdHeight):

            image.resize(((thresholdHeight * width)
                          // height, thresholdHeight)).save(i)

        # if both the parameters exceeds
        # the threshold attributes
        elif (width > thresholdWidth and
              height > thresholdHeight):

            image.resize((thresholdWidth, thresholdHeight)).save(i)

        copyfile(mypath + "/" + i,
                 mypath + "/filteredImages" + i)

        filteredImages.append(i)

    # returning the filteredImages array
    return filteredImages

def run_filtering(process: int, images: list):
    """
    Inputs:
        process: (int) number of process to run
        images_url:(list) list of images url
    """
    print(f'MESSAGE: Running {process} process')

    #results = ThreadPool(process).imap_unordered(filterImages(readImages(highResolutionPath), 1000, 1000, highResolutionPath), images)
    #for r in results:
     #   print(r)



if __name__ == '__main__':
    highResolutionImages = list(readImages(highResolutionPath))
    lowResulutionImages = readImages(lowResolutionPath)
    #filteredImages = filterImages(highResolutionImages, 1000, 1000, highResolutionPath)
    num_process = 10
    task = filterImages(highResolutionImages, 1000, 1000, highResolutionPath)

    print(f'MESSAGE: Running {num_process} process')
    ThreadPool(num_process).imap_unordered(task, highResolutionImages)

    end = time.time()
    print('Time taken to resize {}'.format(len(highResolutionImages)))
    print(end - start)
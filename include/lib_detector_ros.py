"""
Library for detecting a blob based on a color range filter in HSV space

   0------------------> x (cols)
   |
   |
   |         o center
   |
   |
   V y (rows)

Author: Yeser Morales

"""


# Standard imports
import cv2
import numpy as np;

def deNoise (image):

    blur = cv2.GaussianBlur(image, (9, 9), 0)
    print ("<< blur /image")
    
    return(blur)

#IMAGE BLURRING

# *@brief Apply gaussian filter to the input image to denoise it
# *@param inputImage is the frame of a video in which the
# *@param lane is going to be detected
# *@return Blurred and denoised image
 
def edgeDetector(image):

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    ret1,th1 = cv2.threshold(gray_image,140,255,cv2.THRESH_BINARY)

    
    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(th1,-1,kernel)


    print ("<< gray image")
    return(dst)



def mask(image):

    height = image.shape[0]
    width = image.shape[1]
    type1 = image.dtype

    imgnull = np.zeros(image.shape, type1)


    region_of_interest_vertices = [
        (290, 660),
        (555, 450),
        (720, 450),
        (1090, 660)
    ]

    fillimg = cv2.fillConvexPoly(imgnull, np.array([region_of_interest_vertices], np.int32), (100, 100, 1.0), 4, 0)

    masked_image = cv2.bitwise_and(fillimg, image)

    print ("<< Detected only the edges that form part of the lane")

    return(masked_image)


def houghLines(image):

    lines = cv2.HoughLinesP(image,
                            rho=2,
                            theta=np.pi/180,
                            threshold=50,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=100)

    print ("<< seek the images lines")
    return(lines)


def lineSeparation(image):

    print ("<< Subscribed to topic /image_raw camera pc")


def regression(image):

    print ("<< Subscribed to topic /image_raw camera pc")

def predictTurn(image):

    print ("<< Subscribed to topic /image_raw camera pc")

def plotLane(image):

    print ("<< Subscribed to topic /image_raw camera pc")

#=================================================================
#
#		Image Processing - Main
#		Copyright(c) KazukiAmakawa, all right reserved.
#
#=================================================================
#This is the main function of the program, all program will begin from this program
#May cannot compile under the Windows System.

#import head
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import math
import matplotlib.patches as patches
from scipy import misc
from collections import deque
from PIL import ImageFilter
import cv2
import random
import pywt 


#import files
import Init


#Definition Constant
Beta = 0.1
Lanbda = 0.1 
Gamma = 0.1
TotalKase = 3

def Wavelet(img):
	print(img[1])
	img1 = np.array([[np.float64(0.00) for n in range(len(img[0]))] for n in range(len(img))])
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img1[i][j] = float(img[i][j])
	coeffs = pywt.dwt2(img1, "haar")
	Init.ArrOutput(coeffs)
	return pywt.idwt2(coeffs, "haar")


def Gauss(img):
	img = cv2.GaussianBlur(img, (11, 11), 1.6)
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] += random.normalvariate(0, 1.4142135623730951)
	return img


def ADMM(img):
	#Pre-treatment
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = float(img[i][j])
	
	#Definition Iterator vartiables
	u = np.matrix(img)
	y = np.matrix([0.00 for n in range(0, len(img[0]))] for n in range(len(img)))
	mu = np.matrix([0.00 for n in range(0, len(img[0]))] for n in range(len(img)))

	#Definition Constant
	H = np.matrix(np.fft.fft2(img))


	#Main Algorithm
	for Kase in range(0, TotalKase):
		pass


	for i in range(0, len(u)):
		for j in range(0, len(u[i])):
			u[i][j] = int(u[i][j])
			u[i][j] = min(255, u[i][j])
			u[i][j] = max(0, u[i][j])














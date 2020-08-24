import sys
import numpy as np
import cv2

def upside_down(img):
	ans = np.zeros((img.shape[0],img.shape[1],img.shape[2]),np.int)
	for x in range(img.shape[0]):
		ans[x,:]=img[img.shape[0]-x-1,:]
	return ans

def right_side_left(img):
	ans = np.zeros((img.shape[0],img.shape[1],img.shape[2]),np.int)
	for y in range(img.shape[1]):
		ans[:,y]=img[:,img.shape[1]-y-1]
	return ans	
	
def diagonally_mirrored(img):
	ans = np.zeros((img.shape[0],img.shape[1],img.shape[2]),np.int)
	for x in range(img.shape[1]):
		for y in range(img.shape[0]):
			ans[x,y] = img[y,x]
	return ans

img = cv2.imread('lena.bmp')
cv2.imwrite('upsidedown.bmp', upside_down(img))
cv2.imwrite('rightsideleft.bmp', right_side_left(img))
cv2.imwrite('diagonallymirrored.bmp', diagonally_mirrored(img))

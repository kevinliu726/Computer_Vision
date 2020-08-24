import numpy as np
import cv2
import matplotlib.pyplot as plt

kernel = [  [0, 0], [0, 1], [0, 2], [0, -1], [0, -2],
			[1, 0], [1, 1], [1, 2], [1, -1], [1, -2],
			[-1, 0], [-1, 1], [-1, 2], [-1, -1], [-1, -2],
			[2, -1], [2, 0], [2, 1],
			[-2, -1], [-2, 0], [-2, 1]]

def dilation(img):
	ans = np.zeros((img.shape), np.int)
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			maxn = 0
			for idx in kernel:
				if img.shape[0] > x - idx[0] >= 0 and img.shape[1] > y-idx[1] >= 0:
					if img[x - idx[0], y - idx[1]]  > maxn:
						maxn = img[x - idx[0], y - idx[1]]
			ans[x, y] = maxn
	return ans

def erosion(img, k):
	ans = np.zeros((img.shape), np.int)
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			mini = 255
			for idx in kernel:
				if img.shape[0] > x + idx[0] >= 0 and img.shape[1] > y + idx[1] >= 0:
					if img[x + idx[0], y + idx[1]] < mini:
						mini = img[x + idx[0], y + idx[1]]
			ans[x, y] = mini
	
	return ans

def opening(img):
	ans = erosion(img, kernel)
	ans = dilation(ans)
	return ans

def closing(img):
	ans = dilation(img)
	ans = erosion(ans, kernel)
	return ans

img_gray = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imwrite("dilation.bmp", dilation(img_gray))
cv2.imwrite("erosion.bmp", erosion(img_gray, kernel))
cv2.imwrite("opening.bmp", opening(img_gray))
cv2.imwrite("closing.bmp", closing(img_gray))

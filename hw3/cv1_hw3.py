import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram(img):
	ans = np.zeros(256, np.int)
	for x in range(img.shape[1]):
		for y in range(img.shape[0]):
			ans[int(img[x][y])] += 1
	fig = plt.figure()
	plt.bar(range(len(ans)), ans)

def equalization(img):
	new_img = np.zeros((img.shape), np.int)
	eq = np.zeros(256, np.int)
	num = np.zeros(256, np.int)
	for x in range (img.shape[1]):
		for y in range (img.shape[0]):
			num[int(img[x, y])] += 1
	cdf = 0
	for x in range (256):
		cdf += num[x]
		eq[x] = (255 * cdf) // (512 * 512)
	for x in range (img.shape[1]):
		for y in range(img.shape[0]):
			new_img[x, y] = eq[int(img[x, y])]
	return new_img

img_gray = cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
histogram(img_gray)
plt.savefig("original_histogram.png")

img_divided = img_gray / 3
cv2.imwrite("divided3.bmp", img_divided)
histogram(img_divided)
plt.savefig("divided3_histogram.png")

img_equalization = equalization(img_divided)
cv2.imwrite("equalized.bmp", img_equalization)
histogram(img_equalization)
plt.savefig("equalization_histogram.png")




import numpy as np
import cv2
import sys
np.set_printoptions(threshold = sys.maxsize)

def downsample(img):
	ans = np.zeros((66, 66), np.int)
	for x in range(64):
		for y in range(64):
			if img[x * 8, y * 8] >= 128:
				ans[x + 1, y + 1] = 255
			else:
				ans[x + 1, y + 1] = 0
	return ans

def yokoi(img):
	check = [[0, 1], [1, 1], [1, 0], [1, -1],
			[0, -1], [-1, -1], [-1, 0], [-1, 1]]
	ans = np.zeros((66, 66), np.int)
	for x in range(1, 65):
		for y in range(1, 65):
			if img[x, y] ==  255:
				flag = 0
				count = 0
				cnt = 0
				for k in range(9):
					if img[x + check[k % 8][0], y + check[k % 8][1]] == 255:
						cnt += 1
						if flag == 1 and k == 8:
							count -= 1
						if flag == 0 and k % 2 == 0 and k < 8:
							count += 1
							flag = 1
					else:
						if flag == 1:
							flag = 0
				if cnt == 9:
					ans[x, y] = 5
				else:
					ans[x, y] = count
	return ans

def geth(arr):
	tmp = np.zeros((66, 66))
	for x in range(1, 65):
		for y in range(1, 65):
			if arr[x, y] == 1:
				if (x >= 2 and arr[x - 1, y] == 1) or (x < 64 and arr[x + 1, y] == 1) or (y >= 2 and arr[x, y - 1] == 1) or (y < 64 and arr[x, y + 1] == 1):
					tmp[x, y] = 200
			elif arr[x, y] != 0:
				tmp[x, y] = 99
	return tmp

def yokoi2(img, img2):
	check = [[0, 1], [1, 1], [1, 0], [1, -1],
			[0, -1], [-1, -1], [-1, 0], [-1, 1]]
	for x in range(1, 65):
		for y in range(1, 65):
			if img[x, y] ==  255:
				flag = 0
				count = 0
				cnt = 0
				for k in range(9):
					if img[x + check[k % 8][0], y + check[k % 8][1]] == 255:
						cnt += 1
						if flag == 1 and k == 8:
							count -= 1
						if flag == 0 and k % 2 == 0 and k < 8:
							count += 1
							flag = 1
					else:
						if flag == 1:
							flag = 0
				if count == 1 and img2[x, y] == 200:
					img[x, y] = 0
	return img

img_gray = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)
arr = downsample(img_gray)
for i in range(7):
	arr2 = yokoi(arr)
	tmp = geth(arr2)
	arr = yokoi2(arr, tmp)

arr3 = np.zeros((64, 64))
for x in range(64):
	for y in range(64):
		arr3[x, y] = arr[x + 1, y + 1]

cv2.imwrite("thining.bmp",arr3)



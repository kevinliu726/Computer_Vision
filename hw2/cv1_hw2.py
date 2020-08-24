import numpy as np
import cv2
import matplotlib.pyplot as plt
maxi = 1000000000

def threshold(img):
	ans = np.zeros((img.shape), np.int)
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			if img[x,y] >= 128:
				ans[x,y] = 255
			else:
				ans[x,y] = 0
	return ans

def histogram(img):
	ans = np.zeros(256, np.int)
	for x in range(img.shape[1]):
		for y in range(img.shape[0]):
			ans[img[x,y]] += 1
	plt.bar(range(len(ans)), ans, width = 2.0)
	plt.savefig("histogram.png")

def connect(img,img2):
	binary = threshold(img)
	final = img2.copy().astype(np.int32)
	visit = np.zeros(img.shape, np.int)
	for x in range(img.shape[0]):
		for y in range(img.shape[1]):
			cntr, cntc = 0, 0
			L, R, U, B, cnt = maxi, -maxi, maxi, -maxi, 0
			st = [(x, y)]
			while st:
				r, c = st.pop()
				if 512 > r >= 0 and 512 > c >= 0 and visit[r, c] == 0 and binary[r, c] != 0:
					visit[r, c] = 1
					cnt += 1
					cntr += r
					cntc += c
					L = min(L, c)
					R = max(R, c)
					U = min(U, r)
					B = max(B, r)
					st.extend([(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)])
			if cnt >= 500:
				cv2.rectangle(final, (L, B), (R, U), (255, 0, 0), 2)
				cv2.circle(final, (int(cntc / cnt), int(cntr / cnt)), 4, (0, 0, 255), -1)
	return final

img_gray = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)
img_ori = cv2.imread('lena.bmp')
cv2.imwrite("threshold.bmp", threshold(img_gray))
histogram(img_gray)
cv2.imwrite("connected.bmp",connect(img_gray,img_ori))

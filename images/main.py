import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

pic1 = 'WIN_20210405_11_16_12_Pro.jpg'
pic2 = 'WIN_20210405_12_35_23_Pro.jpg'
img = cv2.imread(pic1, 0)
scale_percent = 30  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

edges = cv2.Canny(img, 25, 100)

coord = cv2.findNonZero(edges)
coord2 = cv2.findNonZero(img)

points_list = list()
for ind in range(int(coord.size / 2 - 1)):
    points = list()
    for x in coord[ind][0]:
        points.append(x)
    points_list.append(tuple(points))

tpl = list()
compval = (158, 0)
for x in points_list:

    if math.isclose(x[1], compval[1], abs_tol=3) & math.isclose(x[0], compval[0], abs_tol=5):
        tpl.append(x)
        compval = x

for val in tpl:
    cv2.circle(img, val, 1, (255, 255, 255))

plt.subplot(121), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

while 1:
    plt.show()

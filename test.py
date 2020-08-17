import cv2
import numpy as np

# img = np.zeros((300,300,3), dtype='uint8')
# for i in range(0,25):
#     radius = np.random.randint(0, high=200)
#     color = np.random.randint(0, high=256, size=(3,)).tolist()
#     center = np.random.randint(0, high=300, size=(2,))

#     img = cv2.circle(img, tuple(center), radius, color, -1)
# cv2.imshow("random circle", img)
# cv2.waitKey(0)


img = cv2.imread('./opencv-tutorial/jp.png')

M = np.float32([[1,0,25], [0,1,50]])
img_trans = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
img_rot = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
# cv2.imshow("img", img)
# cv2.imshow('img_trans', img_trans)
# cv2.imshow("img_rot", img_rot)
# print(img.shape)
# cv2.waitKey(0)

#Blur
blurred = np.hstack((
    cv2.blur(img, (3,3)),
    cv2.blur(img, (5,5)),
    cv2.blur(img, (7,7))
))

r = float(300.0 / img.shape[1])
dim = (300, int(img.shape[0] * r))

cv2.namedWindow('Averaged')
blurred = cv2.resize(blurred, dim)

cv2.imshow("Averaged", blurred)
cv2.waitKey(0)
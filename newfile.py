import cv2
cv2.namedWindow("test")
while True:
    k = cv2.waitKey(1)
    if k % 256 == 27:
        break
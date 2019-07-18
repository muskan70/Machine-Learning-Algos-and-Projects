import cv2

img=cv2.imread('minion.jpg')
gray=cv2.imread('minion.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Minion Image',img)
cv2.imshow('Gray Image of Minion',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
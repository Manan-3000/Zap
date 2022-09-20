import cv2
img = cv2.imread('Photo1.png', cv2.IMREAD_COLOR)
cv2.imshow("image", img)
cv2.waitKey(0)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.imwrite("GrayscalePhoto.png",gray_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
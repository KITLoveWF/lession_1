import cv2

img = cv2.imread("D:\\Football_Analistic_System\\Week_1\\Test_OpenCv\\lession1\\lession_1\\img_crop.jpeg")

cv2.imshow("img",img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,near_max = cv2.threshold(img_gray,190,255,cv2.THRESH_BINARY)

cv2.imwrite("D:\\Football_Analistic_System\\Week_1\\Test_OpenCv\\lession1\\lession_1\\img_crop_gray.jpeg",near_max)


cv2.imshow("img1",near_max)
cv2.waitKey()

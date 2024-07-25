import cv2

img = cv2.imread("D:\\Football_Analistic_System\\Week_1\\Test_OpenCv\\lession1\\lession_1\\img_crop.jpeg")

cv2.imshow("img",img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,near_max = cv2.threshold(img_gray,190,255,cv2.THRESH_BINARY)

contour, _ = cv2.findContours(near_max,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("img2",near_max)

width = img.shape[1]/10 
height = img.shape[0]/10 

count = 0
for cnt in contour[:-1]:
    (x,y,w,h) = cv2.boundingRect(cnt)
    if w < width and h < height :
        count = count + 1
        #print(x,y) 
        #img_crop = img[y:y+h,x:x+w]
        #cv2.imwrite("D:\\Football_Analistic_System\\Week_1\\Test_OpenCv\\lession1\\lession_1\\img_crop.jpeg",img_crop)
        cv2.drawContours(img,[cnt],-1,(0,255,0),2,cv2.LINE_AA)

print(count)
cv2.imshow("img1",img)
cv2.waitKey()
from functools import cmp_to_key
def custom_compare(a, b):
    if abs(a[1] - b[1]) <= 2 :
        if (a[0] < b[0]): return -1  # a xếp trước b
        else: return 1
    else: return -1

def PAIR(a):
    b = int(a%10)
    c = 0
    while(a>0):
        a = int(a/10)
        if(a>0): c= a
    return (c,b)

import cv2

img = cv2.imread("D:\\Football_Analistic_System\\Week_1\\Test_OpenCv\\lession1\\lession_1\\img_crop.jpeg")

#cv2.imshow("img",img)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,near_max_block = cv2.threshold(img_gray,210,255,cv2.THRESH_BINARY)

contour_block, _ = cv2.findContours(near_max_block,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)


ret,near_max = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)

contour, _ = cv2.findContours(near_max,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow("img2",near_max_block)

width_number = img.shape[1]/10 * 0.3
height_number = img.shape[0]/10 

width_block = img.shape[1]/10 *0.9
height_block = img.shape[0]/10 *0.9


count_x = -1
count_y = 0
#150
pair_number =[]
pair_block = []
empty = []
for cnt in contour[:-1]:
    (x,y,w,h) = cv2.boundingRect(cnt)
    if w >= width_number and h <= height_number :
        pair_number.append((x,y,w,h))
        #print(x,y) 
        #img_crop = img[y:y+h,x:x+w]
        #cv2.imwrite("D:\\Football_Analistic_System\\Week_1\\Test_OpenCv\\lession1\\lession_1\\img_crop.jpeg",img_crop)
        #cv2.drawContours(img,[cnt],-1,(0,255,0),2,cv2.LINE_AA)

for cnt in contour_block[:-1]:
    (x,y,w,h) = cv2.boundingRect(cnt)
    if w>= width_block and h >= height_block :
        pair_block.append((x,y,w,h))
        #count = count + 1
        #print(x,y)
        #cv2.drawContours(img,[cnt],-1,(0,255,0),2,cv2.LINE_AA)

pair_number.sort(key=lambda x:(x[1], x[0]))
block = sorted(pair_block,key=cmp_to_key(custom_compare))

# count1 = 0
# for x_b,y_b,w_b,h_b in block:
#     count1 = count1 + 1
#    # print(x_b,y_b,w_b,h_b)

# #print("==============================================")

# count2 = 0
# for x_b,y_b,w_b,h_b in pair_number:
#     count2 = count2 + 1
    #print(x_b,y_b,w_b,h_b)

matrix = [[0 for _ in range(9)] for _ in range(9)]
#print(matrix)
# matrix=[]
# for i in range(1,9):
#     for j in range(1,9):
#         matrix[i][j] = 0
# print(matrix)


for x_b,y_b,w_b,h_b in block:
    count_x = count_x + 1
    if count_x == 9:
        count_y = count_y + 1
        count_x = 0
        if count_y == 9: count_y = 0
    for x_n,y_n,w_n,h_n in pair_number:
            x_b_2 = x_b + w_b
            y_b_2 = y_b + h_b
            x_2 = x_n + w_n
            y_2 = y_n + h_n
            if (x_n >= x_b and y_n >= y_b) and (x_2 <= x_b_2 and y_2 <= y_b_2):
                matrix[count_y][count_x] = 1

print(matrix)

#print(PAIR(1))
# for x in empty:
#     print(x)
#print(count)
# count = 0
# empt=[]
# for cnt_b in contour_block[:-1]:
#     (x_b,y_b,w_b,h_b) = cv2.boundingRect(cnt_b)
#     if w_b>= width_block and h_b >= height_block :
#         count = count + 1
#         #empt.append(count)
#         for cnt_n in contour[:-1]:
#             (x,y,w,h) = cv2.boundingRect(cnt_n)
#             if w >= width_number and h <= height_number :
#                 x_b_2 = x_b + w_b
#                 y_b_2 = y_b + h_b
#                 x_2 = x + w
#                 y_2 = y + h
#                 if (x >= x_b and y >= y_b) and (x_2 <= x_b_2 and y_2 <= y_b_2):
#                     empt.append(count)
                #cv2.drawContours(img,[cnt],-1,(0,255,0),2,cv2.LINE_AA)
#cv2.imshow("img1",img)

cv2.waitKey()

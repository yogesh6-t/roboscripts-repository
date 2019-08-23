'''

Author:- yogesh yadav

written on :- 12-8-19

latest updated :- 22-8-19   11:30 AM

'''


"time 05:00pm  12/8/19"
"passed for MI bg and arvind's phone with correct shapes as per lines not AREA"

"time 11:20am  14/8/19"
"passed for MI bg and arvind's phone with correct shapes as per lines not AREA"
"passsed for shape and text recognition, for iphone,mi,moto together"

"time 10:45am  19/8/19"
"passed for MI bg and arvind's phone with correct shapes as per lines not AREA"
"passsed for shape and text recognition, for iphone,mi,moto together"
"passing for rotated slides"

"time 5:00 pm 19/08/19"
"passed for MI bg and arvind's phone with correct shapes as per lines not AREA"
"passsed for shape and text recognition, for iphone,mi,moto together"
"passed for all contours bu cannot distinguish between correct and upside down phones"
"passed for rotated slides"

"time 6:00 pm 20/08/19"
"passed for MI bg and arvind's phone with correct shapes as per lines not AREA"
"passsed for shape and text recognition, for iphone,mi,moto together"
"passed for all contours bu cannot distinguish between correct and upside down phones"
"passed for rotated slides"
"passed for upside-down phones, and if found the text correctly, skips te rest of the code and moves to next patch"

"time 6:30 pm 21/08/19"
"passed for MI bg and arvind's phone with correct shapes as per lines not AREA"
"passsed for shape and text recognition, for iphone,mi,moto together"
"passed for all contours bu cannot distinguish between correct and upside down phones"
"passed for rotated slides"
"passed for upside-down phones, and if found the text correctly, skips te rest of the code and moves to next patch"
"passed for both the text images but not that effective if the tag is changed from 'PHONE' to anything else"
"passing for different tags apart from 'PHONE' like, 'TEST' : 'XYZ' : 'X' : '#84' "


import cv2
import numpy as np
import pytesseract
import imutils
import matplotlib.pyplot as plt
import math


def cart2pol(x, y):
    theta = np.arctan2(y, x)
    rho = np.hypot(x, y)
    return theta, rho
def pol2cart(theta, rho):
    x = rho * np.cos(theta)
    y = rho * np.sin(theta)
    return x, y
def rotate_contour(cnt, angle):
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cnt_norm = cnt - [cx, cy]
    coordinates = cnt_norm[:, 0, :]
    xs, ys = coordinates[:, 0], coordinates[:, 1]
    thetas, rhos = cart2pol(xs, ys)
    thetas = np.rad2deg(thetas)
    thetas = (thetas + angle) % 360
    thetas = np.deg2rad(thetas)
    xs, ys = pol2cart(thetas, rhos)
    cnt_norm[:, 0, 0] = xs
    cnt_norm[:, 0, 1] = ys
    cnt_rotated = cnt_norm + [cx, cy]
    cnt_rotated = cnt_rotated.astype(np.int32)

    return cnt_rotated

##cv2.resize()
##cv2.grey()
##cv2.blur()
##cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
##cv2.erode(thresh2, kernel, iterations = 1)
##cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
##cv2.contourArea()
##cv2.approxPolyDP(cnt, 0.04*cv2.arcLength(cnt, True), True)
##cv2.minAreaRect()
##cnt_rotate()
##cv2.drawContour()


########could also try this for rotation of contours but it did no work i this specific case
########
########cords = np.column_stack(np.where(thresh > 0))
########angle = cv2.minAreaRect(cords)[-1]
########print(angle)
########print(type(angle))
########print(str('before rotation angle is :')+ str(angle))
########if angle < -1:
########    angle = -(90 + angle)
########
##########else:
##########    angle = -angle
########
########(h, w) = resize.shape[:2]
########center = (w // 2, h // 2)
########M = cv2.getRotationMatrix2D(center, angle, 1.0)
########rotated = cv2.warpAffine(resize, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

print(str('######################'))
'''

contours, h = cv2.findContours(thresh5, 1, 2)
#contours = imutils.grab_contours(contours)
#cnt = contours[0]
#print(len(contours))

sd = Detect()

for i in contours:
    #peri = cv2.arcLength(i, True)
    #approx = cv2.approxPolyDP(i, 0.1*peri, True)
    #print(len(approx))
    #if len(approx) == 4:
        #(x,y,w,h) = cv2.boundingRect(approx)
        #ar = w/float(h)
    #print(cv2.contourArea(i))
    if cv2.contourArea(i) > 200:
        M = cv2.moments(i)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        #boundingRect finds the endpoints of the possible rectangle over the contour
##        x,y,w,h = cv2.boundingRect(i)
##        cv2.rectangle(resize,(x-1,y-1),(x+w+1,y+h+1),(0,255,0), 2)
##        rect = cv2.minAreaRect(i)
##        box = cv2.boxPoints(rect)
##        box = np.int0(box)
        #print(box[0,1])
        #print(box[0,0])
        #print(box[0:2])
        #print(box[1])
        #print(box[2:4])
        #print(box.shape)
        shape = sd.detect(i)
        #cv2.putText(resize, "rectangle", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        #print(box.shape)
        cv2.drawContours(gray, [i], 0, (255,255,255), 2)
        cv2.putText(gray,shape, (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
#cv2.imshow('boxed', resize)
cv2.imshow('ange box', gray)
'''
'''
for c in contours:
    approx = cv2.approxPolyDP(c, 0.1*cv2.arcLength(c, True), True)
    #print(len(approx))
    if len(approx) <= 4:
        print('Rectangle')
        cv2.drawContours(resize, [c], 0, (0,0,255), -1)
cv2.imshow('contour', resize)
'''
'''
minLineLength = 30
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,50, maxLineGap = 250)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(gray,(x1,y1),(x2,y2),(0,255,0),2)
#cv2.imwrite('houghlines5.jpg',img)
cv2.imshow('lines', gray)



##        X1,Y1 = cv2.minAreaRect(approx)[0]
##        X1 = np.int0(X1)
##        Y1 = np.int0(Y1)
##        W1,H1 = cv2.minAreaRect(approx)[1]
##        W1 = np.int0(W1)
##        H1 = np.int0(H1)
##        print(X1,Y1)
##        print(W1,H1)
        #cv2.imshow(str(count),resize[Y1:Y1+H1, X1:X1+W1])
        #cv2.rectangle(resize, (X1-(W1//2),Y1-(H1//2)),(X1+(W1//2),Y1+(H1//2)), (0,0,0), -1)
        #cv2.imshow(str(count),resize)
'''



print(str('----------------------'))

img = cv2.imread('TESTc20.jpg')
tag1 = "PHONE"
tag2 = "XYZ"
tag3 = "#84"
tag5 = "TEST"
tagx = "X"
print(img)
resize = imutils.resize(img, width = 400)
print(resize.shape)

##cv2.circle(resize, (330, 450), 40, (0), -1)
##cv2.rectangle(resize, (10,10),(70,70), (0,0,0), -1)


gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
plt.plot(gray)
plt.imshow(gray)
blur = cv2.GaussianBlur(gray, (3,3), 0)

_, thresh = cv2.threshold(gray, 62, 255, cv2.THRESH_BINARY_INV)
'''
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
#cv2.imshow('adaptive mean thresh', thresh)
thresh2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
#cv2.imshow('adaptive gaussian thresh', thresh2)
ret, thresh3 = cv2.threshold(blur, 210, 255, cv2.THRESH_BINARY)
#cv2.imshow('binary thresh3', thresh3)
ret, thresh4 = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
#cv2.imshow('binary thresh4', thresh4)
ret, thresh5 = cv2.threshold(blur, 42, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('binary thresh5', thresh5)
'''

thresh2 = thresh.copy()
kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(thresh2, kernel, iterations = 1)
#cv2.imshow('', erosion)
contours, _ = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img_copy = resize.copy()
img_copy2 = resize.copy()
img_copy3 = resize.copy()
        
count = 0

for cnt in contours:
    if cv2.contourArea(cnt) < 200000 and cv2.contourArea(cnt) > 2000:
        count +=1
        err = 5
        X, Y, W, H = cv2.boundingRect(cnt)
        roi = gray[Y-err:Y+H+err, X-err:X+W+err]
        #cv2.imwrite(str('roi') + str(count) + str('.png'), roi)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        cnt_norm = cnt-[cx, cy]

        approx = cv2.approxPolyDP(cnt, 0.045*cv2.arcLength(cnt, True), True)

        #bounding rectangle
##        x,y,w,h = cv2.boundingRect(cnt)
##        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        #angled rectangle
##        rect = cv2.minAreaRect(cnt)
##        box = cv2.boxPoints(rect)
##        box = np.int0(box)
##        im = cv2.drawContours(im,[box],0,(0,0,255),2)
        
        
        angle = cv2.minAreaRect(approx)[-1]
        print(str('angle::')+ str(abs(angle)))
        #print(str('Kept at an angle:') + str(abs(angle)))
        print(str('and has area of:') + str(cv2.contourArea(cnt)))
        #print(math.floor(abs(angle)))
        #cnt_rotated = rotate_contour(cnt, -(85 -(math.floor(abs(angle)))))
        #print(cnt_rotated[:-1])

        rows,cols = roi.shape
        print(roi.shape)
        #cv2.imshow(str(count), roi)
        if roi.shape[0] > roi.shape[1]:
            "image is upright"
            if angle < -45:
                "image is upright(tilted RIGHT), rotate by (90 - abs(angle)) counter-clockwise     then by 180   then pytesseract"
                M = cv2.getRotationMatrix2D((cols/2,rows/2), (90 - math.floor(abs(angle))),1)
                res = cv2.warpAffine(roi, M, (cols,rows))
                cv2.imshow(str(count)+str('rot'), res)
                _, thr = cv2.threshold(res, 200, 255, cv2.THRESH_BINARY)
                cv2.imshow(str(count) + str('roithresh'), thr)
                text = pytesseract.image_to_string(thr, lang = 'eng')
                print(str('found text thr:') + text)
                if text == tag1:
                    continue
                
                M2 = cv2.getRotationMatrix2D((cols/2,rows/2), 180,1)
                res2 = cv2.warpAffine(thr, M2, (cols,rows))
                cv2.imshow(str(count)+str('rot180'), res2)
                _, thr2 = cv2.threshold(res2, 200, 255, cv2.THRESH_BINARY)
                cv2.imshow(str(count) + str('roithresh'), thr)
                text180 = pytesseract.image_to_string(thr2, lang = 'eng')
                print(str('found text 180:') + text180)
                if text == tag1:
                    continue
                
            else:
                "image is upright(tilted LEFT), rotate by abs(angle) clockwise    then by 180   then pytesseract"
                M = cv2.getRotationMatrix2D((cols/2,rows/2), -(math.floor(abs(angle))),1)
                res = cv2.warpAffine(roi, M, (cols,rows))
                cv2.imshow(str(count)+str('rot'), res)
                _, thr = cv2.threshold(res, 200, 255, cv2.THRESH_BINARY)
                cv2.imshow(str(count) + str('roithresh'), thr)
                text = pytesseract.image_to_string(thr, lang = 'eng')
                print(str('found text thr:') + text)
                if text == tag1:
                    continue

                M2 = cv2.getRotationMatrix2D((cols/2,rows/2), 180,1)
                res2 = cv2.warpAffine(thr, M2, (cols,rows))
                cv2.imshow(str(count)+str('rot180'), res2)
                _, thr2 = cv2.threshold(res2, 200, 255, cv2.THRESH_BINARY)
                cv2.imshow(str(count) + str('roithresh'), thr)
                text180 = pytesseract.image_to_string(thr2, lang = 'eng')
                print(str('found text 180:') + text180)
                if text180 == tag1:
                    continue
                
        elif roi.shape[0] < roi.shape[1]:
            "image is flat"
            if angle < -45:
                "image is flat(tilted RIGHT), rotate by (90 - abs(angle)) counter-clockwise    then by 180   then pytesseract"
                M = cv2.getRotationMatrix2D((cols/2,rows/2), -(math.floor(abs(angle))),1)
                res = cv2.warpAffine(roi, M, (cols,rows))
                cv2.imshow(str(count)+str('rot'), res)
                _, thr = cv2.threshold(res, 200, 255, cv2.THRESH_BINARY)
                cv2.imshow(str(count) + str('roithresh'), thr)
                text = pytesseract.image_to_string(thr, lang = 'eng')
                print(str('found text thr:') + text)
                if text == tag1:
                    continue

                M2 = cv2.getRotationMatrix2D((cols/2,rows/2), 180,1)
                res2 = cv2.warpAffine(thr, M2, (cols,rows))
                cv2.imshow(str(count)+str('rot180'), res2)
                _, thr2 = cv2.threshold(res2, 200, 255, cv2.THRESH_BINARY)
                cv2.imshow(str(count) + str('roithresh'), thr)
                text180 = pytesseract.image_to_string(thr2, lang = 'eng')
                print(str('found text 180:') + text180)
                if text180 == tag1:
                    continue

            else:
                "image is flat(tilted LEFT), rotate by abs(angle) clockwise    then by 180   then pytesseract"
                M = cv2.getRotationMatrix2D((cols/2,rows/2), (90 - math.floor(abs(angle))),1)
                res = cv2.warpAffine(roi, M, (cols,rows))
                cv2.imshow(str(count)+str('rot'), res)
                _, thr = cv2.threshold(res, 200, 255, cv2.THRESH_BINARY)
                cv2.imshow(str(count) + str('roithresh'), thr)
                text = pytesseract.image_to_string(thr, lang = 'eng')
                print(str('found text thr:') + text)
                if text == tag1:
                    continue

                M2 = cv2.getRotationMatrix2D((cols/2,rows/2), 180,1)
                res2 = cv2.warpAffine(thr, M2, (cols,rows))
                cv2.imshow(str(count)+str('rot180'), res2)
                _, thr2 = cv2.threshold(res2, 200, 255, cv2.THRESH_BINARY)
                cv2.imshow(str(count) + str('roithresh'), thr)
                text180 = pytesseract.image_to_string(thr2, lang = 'eng')
                print(str('found text 180:') + text180)
                if text180 == tag1:
                    continue


        ######cnt_rotated = rotate_contour(approx, -(90 -(math.floor(abs(angle)))))      ##this is very intresting, look into it

        #(X1, Y1, W1, H1) = cv2.minAreaRect(cnt_rotated)
        
        #cv2.imshow(str(count),resize[Y1-err:Y1+H1+err, X1-err:X1+W1+err])
        #text = pytesseract.image_to_string(resize[Y1-err:Y1+H1+err, X1-err:X1+W1+err], lang = 'eng')
        #print(text)
'''
        #points for the original contour, making a polygon 
        pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
        pts = pts.reshape((-1,1,2))
        img = cv2.polylines(img,[pts],True,(0,255,255))

        rect = cv2.minAreaRect(approx)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
'''
        
        #cv2.imshow(str(count),resize[box])
        #img_copy3 = cv2.drawContours(img_copy3,[box],0,(255,0,0),2)
        
        #####cv2.drawContours(img_copy, [approx], -1, (0, 255, 255), 3)
        #cv2.imshow(str(count),img_copy)
        #####cv2.drawContours(img_copy2, [cnt_rotated], 0, (0, 0, 255), 3)
#    plt.figure()
        #cv2.imshow(str(count),img_copy2)


######cv2.imshow('no rotation',img_copy)
######cv2.imshow('rotation corrected',img_copy2)
#cv2.imshow('exp',img_copy3)
#plt.axis("off");

cv2.waitKey(0)
cv2.destroyAllWindows()

    

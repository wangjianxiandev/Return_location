# import the necessary packages
import argparse
import imutils
import cv2

# load the image, convert it to grayscale, blur it slightly,
# and threshold it
file_path = 'E:\\PythonProjects\\tuxiangshibie\\485jixiebi\\baidu\zuobiao'
image = cv2.imread("E:\\PythonProjects\\tuxiangshibie\\485jixiebi\\baidu\\test.png")
image = cv2.resize(image, (600, 600))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 灰度
blurred = cv2.GaussianBlur(gray, (5, 5), 0) # 5x5的内核的高斯平滑
thresh = cv2.threshold(blurred, 108, 255, cv2.THRESH_BINARY)[1] # 阈值化，阈值化后形状被表示成黑色背景上的白色前景。
cv2.imshow("Image", thresh)
# 在阈值图像中查找轮廓
# 找到白色对应的边界点的集合
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)


# 计算轮廓中心
# loop over the contours
for c in cnts:
    # compute the center of the contour
    # print(c)
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    # draw the contour and center of the shape on the image
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(image, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # show the image
    cv2.imshow("Image", image)
    with open(file_path, 'w') as w_obj:
        w_obj.write(str(cX) +' ' + str(cY)+ "\n")
    print(cX, cY)
    cv2.waitKey(0)

import urllib.request
import cv2
import numpy as np
import time
URL = "http://192.168.1.103:8080/shot.jpg"

back = cv2.imread('./image.jpg')

while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #cv2.imshow("hsv",hsv)

    #gray bgr = 128, 128, 128
    gray = np.uint8([[[128, 128, 128]]])
    hsv_gray = cv2.cvtColor(gray, cv2.COLOR_BGR2HSV)

    l_gray = np.array([0, 5, 50])
    u_gray = np.array([179, 50, 255])

    mask = cv2.inRange(hsv, l_gray, u_gray)
    #cv2.imshow("mask", mask)

    part1 = cv2.bitwise_and(back, back, mask=mask)
    #cv2.imshow("part1", part1)

    mask = cv2.bitwise_not(mask)

    part2 = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("cloak", part1 + part2)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

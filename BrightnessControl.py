import serial
import cvzone
import math
import cv2
import numpy as np
import screen_brightness_control as sbc
import HandTrackingModule as htm

bbar = 0
minBRIGHTNESS = 0
maxBRIGHTNESS = 100
serialcomm = serial.Serial('COM3', 9600)
serialcomm.timeout = 1
cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.8, maxHands=1)
l = []
while True:
    success, img = cap.read()
    img = cv2.resize(img, (500, 500))
    img = detector.findHands(img)
    l, box = detector.findPosition(img, draw=False)
    if l:
        # f=detector.fingersUp()
        x1 = l[4][1]
        y1 = l[4][2]
        x2 = l[8][1]
        y2 = l[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x1, y1), 7, (0, 255, 255), 1)
        cv2.circle(img, (x2, y2), 7, (0, 255, 255), 1)
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        d = int(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0))
        brightness = np.interp(d, [20, 100], [minBRIGHTNESS, maxBRIGHTNESS])
        bbar = np.interp(d, [50, 300], [400, 150])
        cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 255), 3)
        cv2.rectangle(img, (50, int(bbar)), (85, 400), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, f'{int(brightness)}%', (85, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 4, (255, 0, 255), 3)
        sbc.set_brightness(int(brightness), None)
        d = int((d / 110) * 255)
        e = '\n'
        if 0 < d < 256:
            cv2.putText(img, str(d), (20, 30), cv2.FONT_HERSHEY_COMPLEX, .7, (255, 255, 255), 1)
            serialcomm.write(str(d).encode())
            serialcomm.write(e.encode())

    cv2.imshow('Image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
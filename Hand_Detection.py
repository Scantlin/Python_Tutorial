import cv2
from cvzone import HandTrackingModule

cap = cv2.VideoCapture(1)
detector = HandTrackingModule.HandDetector()

while True: 
    success, img = cap.read()
    detector.findHands(img)  # Corrected method name
    cv2.imshow('image', img)
    cv2.waitKey(1)
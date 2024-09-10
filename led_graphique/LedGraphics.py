import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject
import time  # Import de la bibliothèque pour les délais

arduino = SerialObject("COM4")
cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)
    
    if bboxs:
        arduino.sendData([1, 0])
        time.sleep(2)  # Attendre 2 secondes avant de poursuivre
    else:
        arduino.sendData([0, 1])
        time.sleep(2)  # Attendre 2 secondes avant de poursuivre
    
    cv2.imshow("Image", img)
    
    # Utilisez un petit délai pour éviter un rafraîchissement trop rapide
    cv2.waitKey(1)

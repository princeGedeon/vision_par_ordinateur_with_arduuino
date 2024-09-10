from cvzone.HandTrackingModule import HandDetector
import cv2
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2, staticMode=False, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)
arduino = SerialObject("COM4")  # Assurez-vous que COM4 est le bon port

while True:
    Success, img = cap.read()
    hands, img = detector.findHands(img, draw=True, flipType=True)

    if hands:
        # Détection de la première main
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]  # Coordonnées de la bounding box autour de la première main
        center1 = hand1['center']  # Centre de la première main
        handType1 = hand1["type"]  # Type de la première main ("Left" ou "Right")

        # Liste des doigts levés pour la première main
        fingers1 = detector.fingersUp(hand1)

        # Si deux mains sont détectées
        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]  # Coordonnées de la bounding box autour de la deuxième main
            center2 = hand2['center']  # Centre de la deuxième main
            handType2 = hand2["type"]  # Type de la deuxième main ("Left" ou "Right")

            # Liste des doigts levés pour la deuxième main
            fingers2 = detector.fingersUp(hand2)

            # Calcul de la distance entre les index des deux mains
            index1 = lmList1[8][0:2]  # Coordonnées du bout de l'index de la première main
            index2 = lmList2[8][0:2]  # Coordonnées du bout de l'index de la deuxième main
            length, info, img = detector.findDistance(index1, index2, img, color=(255, 100, 55), scale=10)
            val = int(length)
            if(val>100):
                val=1
            else:
                val=0
            # Ajout de la distance à la liste des doigts levés de la première main
            fingers1.append(val)  # La 6ème valeur est la distance
            print(f"Fingers with distance: {fingers1}")

            # Envoi des données à l'Arduino : cinq doigts de la première main + la distance
            arduino.sendData(fingers1)
        
        else:
            # Si seulement une main est détectée, ajout de 0 comme sixième valeur
            fingers1.append(0)  # La 6ème valeur est 0
            print(f"Fingers with 0: {fingers1}")
            arduino.sendData(fingers1)

    # Affichage de l'image avec la détection des mains
    cv2.imshow("Image", img)
    cv2.waitKey(1)

import sys
import cv2
from matplotlib import pyplot as plt

# leggo il nome del file
file = sys.argv[1]

# leggo il video
cap = cv2.VideoCapture(file)

# il contatore serve per eseguire il plotting dei frame, per 5 volte ed ogni 10 frame
counter = 0
while cap.isOpened() and counter < 50:
    ret, frame = cap.read()
    if counter % 10 == 0:
        plt.imshow(frame, interpolation='bicubic')
        plt.show()
    if not ret:
        break
    counter += 1
cap.release()

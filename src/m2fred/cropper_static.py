import sys
import cv2
import math

# leggo il nome del file e lo salvo anche senza estensione
file = sys.argv[1]
filename = file[:-4]

# shape del frame
width = 200
height = 200

# questa è la lista di coordinate delle varie ROI
points = []
points.append([(264, 242), (470, 316)])
points.append([(264, 242), (470, 316)])
points.append([(264, 242), (470, 316)])
points.append([(264, 242), (470, 316)])
points.append([(264, 242), (470, 316)])

# leggo il video
cap = cv2.VideoCapture(file)

# il contatore serve a gestire il taglio delle ROI
counter = 0
while cap.isOpened() and counter < 50:
    ret, frame = cap.read()
    index = math.floor(counter / 10)
    if ret:
        # vertice in alto a sinistra ed in basso a destra
        (x1, y1) = points[index][0]
        (x2, y2) = points[index][1]

        # taglio la ROI e salvo il frame
        frame = frame[y1:y2, x1:x2]
        frame = cv2.resize(frame, (width, height))
        framename = filename+"_"+str(counter)+".jpeg"
        cv2.imwrite(filename+"/"+framename, frame)

        counter += 1
    else:
        break
cap.release()

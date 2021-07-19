import cv2
import dlib
import os

detector_dat = 'drive/MyDrive/mmod_human_face_detector.dat'
predictor_dat = 'drive/MyDrive/shape_predictor_68_face_landmarks.dat'
detector = dlib.cnn_face_detection_model_v1(detector_dat)
predictor = dlib.shape_predictor(predictor_dat)

# src_path è il path del dataset
# dst_path è il path in cui salveremo il dataset processato
src_path = "drive/MyDrive/M2FRED"
dst_path = "drive/MyDrive/dataset_cnn"


def find_highest_ref(landmarks):
    references = []
    references.append(landmarks.part(17).y)
    references.append(landmarks.part(18).y)
    references.append(landmarks.part(19).y)
    references.append(landmarks.part(20).y)
    references.append(landmarks.part(21).y)
    references.append(landmarks.part(22).y)
    references.append(landmarks.part(23).y)
    references.append(landmarks.part(24).y)
    references.append(landmarks.part(25).y)
    references.append(landmarks.part(26).y)
    return min(references)


def find_lowest_ref(landmarks):
    references = []
    references.append(landmarks.part(28).y)
    references.append(landmarks.part(36).y)
    references.append(landmarks.part(41).y)
    references.append(landmarks.part(40).y)
    references.append(landmarks.part(39).y)
    references.append(landmarks.part(42).y)
    references.append(landmarks.part(47).y)
    references.append(landmarks.part(46).y)
    references.append(landmarks.part(45).y)
    return max(references)


def manage_file(directory, file):
    subpath = directory+'/'+file
    cap = cv2.VideoCapture(src_path+'/'+subpath+'.avi')
    width = 200
    height = 200
    counter = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #gray = cv2.equalizeHist(gray)
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            gray = clahe.apply(gray)
            faces = detector(gray, 1)

            # lancia il predictor sulla viso
            for face in faces:
                landmarks = predictor(gray, face.rect)

                # fisso i riferimenti da usare
                left = landmarks.part(0).x
                top = find_highest_ref(landmarks) - 15
                right = landmarks.part(16).x
                bottom = find_lowest_ref(landmarks) + 15

                # taglio la ROI della pericoulare e la riadatto con shape widthxheigh
                frame = frame[top:bottom, left:right]
                if frame.size:
                    frame = cv2.resize(frame, (width, height))
                else:
                    break
                # salvo il frame processato
                framename = file+'_'+str(counter)+'.jpeg'
                cv2.imwrite(dst_path+'/'+subpath+'/'+framename, frame)

                counter += 1
        else:
            break

    # cleanup
    cap.release()


directories = os.listdir(dst_path)
for directory in directories:
  files = os.listdir(dst_path+'/'+directory)
  for file in files:
    frames = os.listdir(dst_path+'/'+directory+'/'+file)
    if len(frames) < 50:
      print("computing %s/%s..." % (directory, file))
      manage_file(directory, file)
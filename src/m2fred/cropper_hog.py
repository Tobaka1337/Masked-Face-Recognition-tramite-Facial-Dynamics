import cv2
import dlib
import os

dat = 'drive/MyDrive/shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(dat)

# src_path è il path del dataset
# dst_path è il path in cui salveremo il dataset processato
src_path = 'drive/MyDrive/M2FRED'
dst_path = 'drive/MyDrive/dataset_hog'


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
            faces = detector(gray, 1)

            # lancia il predictor sulla viso
            for face in faces:
                landmarks = predictor(gray, face)

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


directories = os.listdir(src_path)
for directory in directories:
    try:
        os.mkdir(dst_path+'/'+directory)
    except OSError:
        pass
    files = os.listdir(src_path+'/'+directory)
    for file in files:
        file = file[:-4]
        try:
            os.mkdir(dst_path+'/'+directory+'/'+file)
        except OSError:
            pass
        print("computing file %s/%s..." % (directory, file))
        manage_file(directory, file)

import os
import cv2

dataset = 'C:/Users/aferr/Documents/fvab/Progetto/data/XM2VTS'


def compute_video(dir_path, video):
    video_no_ext = video[:-4]
    subdir_path = dir_path+'/'+video_no_ext
    os.mkdir(subdir_path)

    cap = cv2.VideoCapture(dir_path+'/'+video)
    counter = 0
    while cap.isOpened() and counter<50:
        ret, frame = cap.read()
        framename = video_no_ext+'_'+str(counter).zfill(2)+'.jpeg'
        framepath = subdir_path+'/'+framename

        cv2.imwrite(framepath, frame)
        os.system('face-mask '+framepath)
        os.remove(framepath)
        framepath_mask = framepath[:-5]+'-with-mask.jpeg'
        os.rename(framepath_mask, framepath)
        counter += 1

    cap.release()


dirs = os.listdir(dataset)
for dir in dirs:
    dir_path = dataset+'/'+dir
    videos = os.listdir(dir_path)
    videos = videos[5:10]
    for video in videos:
        compute_video(dir_path, video)
        os.remove(dir_path+'/'+video)

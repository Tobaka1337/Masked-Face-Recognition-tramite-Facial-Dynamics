"""
Usato per trovare le sequenze sulle quali
è fallito il processo di detection:
le sequenze hanno meno di 50 frames
"""
import os

dataset_path = 'C:/Users/aferr/Documents/fvab/Progetto/data/XM2VTS'

n_videos = 0
dirs = os.listdir(dataset_path)
for dir in dirs:
    dir_path = dataset_path+'/'+dir
    sequences = os.listdir(dir_path)
    for sequence in sequences:
        sequence_path = dir_path+'/'+sequence
        frames = os.listdir(sequence_path)
        if len(frames) is not 50:
            n_videos += 1
            print(sequence_path)
print("Video non conformi: ", n_videos)

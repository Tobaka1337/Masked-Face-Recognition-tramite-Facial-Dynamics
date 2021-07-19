"""
Verifica se
il numero di video per soggetto,
il numero di frames per video,
il numero di video totali
ed il numero di frames totali
è conforme alle specifiche.
"""
import os

dataset_path = 'C:/Users/aferr/Documents/fvab/Progetto/data/my2fred/my2fred_dataset'

n_videos = 0
n_frames = 0
dirs = os.listdir(dataset_path)
for dir in dirs:
    dir_path = dataset_path+'/'+dir
    sequences = os.listdir(dir_path)
    n_videos += len(sequences)

    # controllo se la directory ha 15 sequenze
    if len(sequences) is not 15:
        print(dir_path+' non ha 15 sequenze')

    for sequence in sequences:
        sequence_path = dir_path+'/'+sequence
        frames = os.listdir(sequence_path)
        n_frames += len(frames)

        # controllo se la sequenza contiene 50 frames
        if len(frames) is not 50:
            print(sequence_path+' non ha 50 frames')

print("Numero totale di video: ", n_videos)
print("Numero totale di frames: ", n_frames)

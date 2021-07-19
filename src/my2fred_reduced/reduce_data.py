"""
[*] Questo script riduce il numero di dati orizzontali:
elimina 10 sequenze con mascherina
e 10 sequenza segna mascherina
da ogni soggetto, riducendo così
il numero di sequenze per ogni soggetto
da 15 a 5 (con mascherina e senza mascherina)
[*] Dal momento che le sequenze sono state create in
4 differenti momenti temporali, si preserva almeno
1 sequenza per ogni momento.
"""
import os

dataset_path = 'C:/Users/aferr/Documents/fvab/Progetto/data/my2fred_reduced/my2fred_reduced_dataset'


def destroydir(sequence_path):
    frames = os.listdir(sequence_path)
    for frame in frames:
        frame_path = sequence_path+'/'+frame
        os.remove(frame_path)
    os.rmdir(sequence_path)


dirs = os.listdir(dataset_path)
for dir in dirs:
    dir_path = dataset_path+'/'+dir
    sequences = os.listdir(dir_path)

    # se ttl = 0, la sequenza viene eliminata
    # state memorizza il tipo di sequenza precedente
    ttl = 2
    state = 1
    for sequence in sequences:
        sequence_path = dir_path+'/'+sequence

        # prendo il carattere che indica il tipo di sequenza
        new_state = int(sequence[-5])

        # se ho un cambio di tipologia, incremento lo stato
        # e setto il ttl ad 1 (così che la prima sequenza non venga cancellata)
        if new_state is not state:
            state += 1
            ttl = 1
        if ttl is 0:
            destroydir(sequence_path)
        else:
            ttl -= 1

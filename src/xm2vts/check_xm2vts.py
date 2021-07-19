"""
Precedentemente usato per:
[*] rimuovere i video con rotazione
[*] rimuovere l'ultimo video dalle dir con 11 video
Attualmente usato per:
[*] verificare che tutte le dir abbiano 10 video
"""
import os

start_path = 'C:/Users/aferr/Documents/fvab/Progetto/data/XM2VTS'
dirs = os.listdir(start_path)
for dir in dirs:
    dir_path = start_path+'/'+dir
    videos = os.listdir(dir_path)
    if len(videos) is not 10:
        print('> ' + dir_path)
        print(len(videos))

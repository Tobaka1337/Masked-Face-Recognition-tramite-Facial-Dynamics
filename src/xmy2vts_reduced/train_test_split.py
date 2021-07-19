"""
Divide il dataset in train e test set
inserendo nel train set, le sequenze senza mascherina
e nel test set, le sequenze con mascherina
"""
import os
from shutil import copytree

dataset_path = 'C:/Users/aferr/Documents/fvab/Progetto/data/xmy2vts_reduced/xmy2vts_reduced_dataset'
train_path = 'C:/Users/aferr/Documents/fvab/Progetto/data/xmy2vts_reduced/xmy2vts_reduced_train'
test_path = 'C:/Users/aferr/Documents/fvab/Progetto/data/xmy2vts_reduced/xmy2vts_reduced_test'

dirs = os.listdir(dataset_path)
for dir in dirs:
    dir_dataset_path = dataset_path + '/' + dir
    if dir[-1] is '0':
        dir_train_path = train_path+'/'+dir
        copytree(dir_dataset_path, dir_train_path)
    else:
        dir_test_path = test_path+'/'+dir
        copytree(dir_dataset_path, dir_test_path)

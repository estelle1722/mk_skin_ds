import os

import shutil


def rename(path='./isic_2017'):
    for name in os.listdir(path):
        abs_path = os.path.join(path, name)
        target_path = os.path.join(path, name.split('_')[1])
        os.rename(abs_path, target_path)

def clear(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

def copy(source_path, target_path):
    assert os.path.exists(source_path)
    shutil.copy(source_path, target_path)

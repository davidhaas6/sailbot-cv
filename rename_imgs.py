import os

dir_path = os.path.dirname(os.path.realpath(__file__))
src = dir_path + '/data/'
prev_f = ''

for i, f in enumerate(os.listdir(src)):
    path = src+f
    os.rename(path, src + str(i) +'.png')

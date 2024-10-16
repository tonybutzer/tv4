import sys
import os
import shutil

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as e:
        print(e.errno)
        pass


playlist = sys.argv[1]

print(playlist)

def _mkdir(dir):
    print(dir)

play_dir = f'/home/tony/Music/{playlist}'

mkdir_p(play_dir)

def read_m3u_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

files = read_m3u_file(f'/tmp/{playlist}.m3u')

for f in files:
    f = f.strip()
    print(f)
    shutil.copy(f, play_dir)

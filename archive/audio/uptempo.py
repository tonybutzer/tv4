'''

This audio program uptempo(s) an directory of MP3 files 

Parameters:
directory (str): directory of a bunch of mp3 files

# Usage
=======
python uptemp.py --directory [directory]

    Running examples:
    
    
'''

import sys
import argparse
import os
# import eyed3


def mp3towav(mp3, wav):
    cmd = f'ffmpeg -i {mp3} {wav}'
    os.system(cmd)
    os.unlink(mp3)

def wavtowavut(wav, wavut):
    cmd = f'sox {wav} {wavut} tempo 1.6'
    print(cmd)
    os.system(cmd)
    os.unlink(wav)

def wavtomp3(wav, mp3):
    cmd = f'ffmpeg -i {wav} {mp3}'
    os.system(cmd)
    os.unlink(wav)

def return_mp3s(directory):
    mp3s=[]
    extension = '.mp3'
    # extension = '.wav'
    for file in os.listdir(directory):
        if file.endswith(extension):
            mp3file = os.path.join(directory, file)
            mp3s.append(mp3file)
    mp3s.sort()
    return mp3s

    #os.system(f'ffmpeg -ss {start} -i {mp3file} -to {end} {outfile}')

def uptempo(mp3file):
    wav = mp3file.replace('.mp3', '.wav')
    wavut = wav.replace('.wav', '-ut.wav')
    mp3ut = wavut.replace('.wav', '.mp3')
    print(wav, wavut, mp3ut)
    mp3towav(mp3file, wav)
    wavtowavut(wav, wavut)
    wavtomp3(wavut, mp3ut)


 
def do_uptempo(directory):
    l = return_mp3s(directory)
    print (l)
    for mp3f in l:
        uptempo(mp3f)

def get_parser():
    parser = argparse.ArgumentParser(description='Run the aud code')
    parser.add_argument('directory', metavar='directory', type=str, nargs=None,
            help='the mp3file directory name')
    # parser.add_argument('-i', '--interval', help='time interval in seconds '  , default=1800, type=int)
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    directory = args['directory']
    print(directory)

    do_uptempo(directory)
    return(True)


if __name__ == '__main__':
    command_line_runner()


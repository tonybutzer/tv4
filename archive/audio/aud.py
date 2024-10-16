'''
This audio program splits an MP3 file into smaller segments

Parameters:
interval (int): seconds to split the file by

# Usage
=======
python aud.py --interval [seconds] [audiofile]

    Running examples:
    
    $ python aud.py --interval 1800 ./a.mp3 # cut into 1/2 hour segments
    
'''

import sys
import argparse
import os
import eyed3

def do_aud(mp3file, interval):
    audiofile = eyed3.load(mp3file)
    print(audiofile.info.time_secs)
    endr = int(audiofile.info.time_secs / interval + 2)

    
    for i in range(0,endr):
        outfile = f'../d{i:02}.mp3'
        start = i*interval
        do_split(mp3file, outfile, start, interval)
	

def do_split(mp3file, outfile, start, interval):
#ffmpeg -ss 1:0:0 -i a.mp3 -to 3600 b.wav
    end = interval

    os.system(f'ffmpeg -ss {start} -i {mp3file} -to {end} {outfile}')

def get_parser():
    parser = argparse.ArgumentParser(description='Run the aud code')
    parser.add_argument('mp3file', metavar='mp3file', type=str, nargs=None,
            help='the mp3file name')
    parser.add_argument('-i', '--interval', help='time interval in seconds '  , default=1800, type=int)
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    mp3file = args['mp3file']
    print(mp3file)

    interval = args['interval']
    print(interval)
    do_aud(mp3file, interval)
    return(True)


if __name__ == '__main__':
    command_line_runner()

'''
    try:
        command_line_runner()
    except:
        print('except')
    finally:
        print('aud final bye', flush=True)
'''




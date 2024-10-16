import sys
import os
import pandas as pd
import eyed3
from tqdm import tqdm

def get_mp3_headers(filepath):
    audiofile = eyed3.load(filepath)
    return {
        'Title': audiofile.tag.title,
        'Artist': audiofile.tag.artist,
        'Album': audiofile.tag.album,
        'Genre': audiofile.tag.genre.name if audiofile.tag.genre else None,
        'Year': audiofile.tag.getBestDate(),
        'Duration (seconds)': audiofile.info.time_secs if audiofile.info else None
    }

def find_mp3_files(directory):
    mp3_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3'):
                mp3_files.append(os.path.join(root, file))
    return mp3_files

def create_dataframe(mp3_files):
    headers_list = []
    #p_bar = tqdm(range(len(mp3_files)))
    for mp3_file in mp3_files:
        print(mp3_file)
        try:
            headers_list.append(get_mp3_headers(mp3_file))
        except:
            print("weird mp3 file:", mp3_file)
        #p_bar.update(1)
        #p_bar.refresh()
    return pd.DataFrame(headers_list)

if __name__ == "__main__":
    # directory_path = '/path/to/your/music/directory'  # Replace with your directory path
    directory_path = sys.argv[1]
    mp3_files = find_mp3_files(directory_path)
    df = create_dataframe(mp3_files)
    print(df)


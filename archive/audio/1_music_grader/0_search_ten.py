import pandas as pd


df = pd.read_csv('data/ten_thousand_songs.csv', index_col=0)

print(df.head())


# Read the text file
with open('data/file_list.txt', 'r') as file:
    lines = file.readlines()

# Create a DataFrame with one column
df1 = pd.DataFrame({'file_name': lines})

# Optionally, remove trailing newline characters
df1['file_name'] = df1['file_name'].str.strip()

# Print the DataFrame
print(df1.head())


def get_artist_songs(df1, artist):
    pattern = '|'.join(artist.split())
    df2=pd.DataFrame()
    try:
        df2 = df1[df1['file_name'].str.contains(pattern, case=False)]
    except:
        pass

    return df2

#print(df2)

def get_this_song_loose(df2, song):
    pattern = '|'.join(song.split())
    songs=pd.DataFrame()
    try:
        songs = df2[df2['file_name'].str.contains(pattern, case=False)]
    except:
        pass
    return songs

def get_this_song_robust(df2, song):
    search_words = song.split()
    matches=pd.DataFrame()
    try:
        matches = df2[df2['file_name'].apply(lambda x: all(word in x for word in search_words))]
    except:
        pass
    return matches


# df2 = get_artist_songs(df1, 'Toby Keith')
# songs = get_this_song(df2, 'boomtown')

pd.options.display.max_colwidth = 0

# print(songs.shape, songs['file_name'].values[0])

for i,row in df.iterrows():
    if True:
    #if 'Toby' in row['artist']:
        #print(row['artist'], row['song'])
        # songs = get_this_song(df2, row['song'])
        # print(songs['file_name'].values[0])
        df2 = get_artist_songs(df1, row['artist'])
        matches = get_this_song_robust(df2, row['song'])
        try:
            print(matches['file_name'].values[0])
        except:
            pass

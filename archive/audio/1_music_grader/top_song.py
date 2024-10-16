import sys
import pandas as pd

my_artist=sys.argv[1]

df = pd.read_csv('TopSongs.csv', index_col=0);

print (df.head() )
result = df[df['artist'].str.contains(my_artist)]

for i,row in result.iterrows():
    print(row['artist'], row['song'])

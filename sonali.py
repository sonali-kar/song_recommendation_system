#importing libraries
import pandas as pd
import numpy as np


#importing datasets

triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
songs_metadata_file = 'https://static.turi.com/datasets/millionsong/song_data.csv'
songmetadata = pd.read_csv(r'song_data.csv')   #(r'https://static.turi.com/datasets/millionsong/song_data.csv')
triplets_file = pd.read_fwf(r'10000.txt')               #'https://static.turi.com/datasets/millionsong/10000.txt')
songmetadata = pd.DataFrame(songmetadata)

triplets_file.columns = ['user_id','song_id','listen_count']
song_df = pd.merge(triplets_file, songmetadata.drop_duplicates(['song_id']), on="song_id", how ="left")
song_grouped = song_df.groupby(['title']).agg({"listen_count":"count"})
grouped_sum = song_grouped['listen_count'].sum()

#percentage share

song_grouped['percentage'] = song_grouped['listen_count'].div(grouped_sum)*100

#sorting the dataset with respect to listen count

song_grouped = song_grouped.sort_values(['listen_count'],ascending = True)
song_df = song_df['listen_count'].astype(float)
popular = song_grouped.sort_values(by = 'listen_count')

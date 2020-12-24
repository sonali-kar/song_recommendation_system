#importing libraries
import pandas as pd
import numpy as np


#importing datasets

triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
songs_metadata_file = 'https://static.turi.com/datasets/millionsong/song_data.csv'
songmetadata = pd.read_csv(r'song_data.csv')   #(r'https://static.turi.com/datasets/millionsong/song_data.csv')
triplets_file = pd.read_fwf(r'10000.txt')               #'https://static.turi.com/datasets/millionsong/10000.txt')

triplets_file.columns=['user_id','song_id','listen_count']
song_df = pd.merge(triplets_file,songmetadata.drop_duplicates(['song_id']), on="song_id", how="left")
x = song_df.to_excel("millionsong.xlsx")
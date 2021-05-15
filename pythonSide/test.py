import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv("songs.csv",'utf-8',engine='python')
features = ['artist','Genre','Album/Movie']
def combine_features(row):
    return row['artist']+" "+row['Genre']+" "+row['Album/Movie']
for feature in features:
    df[feature] = df[feature].fillna(' ') #filling all NaNs with blank string

df["combined_features"] = df.apply(combine_features,axis=1) #applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column
cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df["combined_features"]) #feeding combined strings(movie contents) to CountVectorizer() object
cosine_sim = cosine_similarity(count_matrix)
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]
song_user_likes = input()
type(song_user_likes)
song_index = get_index_from_title(song_user_likes)
similar_song = list(enumerate(cosine_sim[song_index])) #accessing the row corresponding to given movie to find all the similarity scores for that movie and then enumerating over it
sorted_similar_songs = sorted(similar_songs,key=lambda x:x[1],reverse=True)[1:]
i=0
print("Top 5 similar song to "+song_user_likes+" are:\n")
for element in sorted_similar_songs:
    print(get_title_from_index(element[0]))
    i=i+1
    if i>5:
        break
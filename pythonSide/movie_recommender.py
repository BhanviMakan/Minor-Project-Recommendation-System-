import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
df = pd.read_csv("C:\\Users\\Bhanvi\\Desktop\\minor project\\pythonSide\\pythonSide\\movies.csv")
features = ['actors','writers','genre','directors']
def combine_features(row):
    return row['actors']+" "+row['writers']+" "+row['genre']+" "+row['directors']
for feature in features:
    df[feature] = df[feature].fillna('') #filling all NaNs with blank string
df["combined_features"] = df.apply(combine_features,axis=1) #applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column
cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df["combined_features"]) #feeding combined strings(movie contents) to CountVectorizer() object
cosine_sim = cosine_similarity(count_matrix)
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
  return df[df.title == title]["index"].values[0]

movie_user_likes= sys.argv[1]
movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index])) #accessing the row corresponding to given movie to find all the similarity scores for that movie and then enumerating over it
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
i=0
print("Top 5 similar movies to  " + movie_user_likes+ " are:  ", end="--")
for element in sorted_similar_movies:
   print(get_title_from_index(element[0]) , end="----")
   i=i+1
   if i>5:
       break
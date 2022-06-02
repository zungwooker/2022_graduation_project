import gensim
import pickle
import pandas as pd

movie_genre_data = pd.read_csv("./dataset/movie.csv")
movie_rating_data = pd.read_csv("./dataset/rating.csv")

tmp_genres = movie_genre_data.loc[:, 'genres']
tmp_genres = list(set(list(tmp_genres)))
genres = list()

for str in tmp_genres:
    genres.append(str.split('|'))

genres = list(set(sum(genres, [])))
print(genres)
print(len(genres))



#model = gensim.models.KeyedVectors.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)
#print(model.vectors.shape)
#print(model.similarity('this', 'is'))
#print(model.similarity('post', 'book'))
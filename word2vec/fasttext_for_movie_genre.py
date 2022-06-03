import gensim
import pickle
import pandas as pd

movie_genre_data = pd.read_csv("./dataset_movie/movie.csv")
movie_rating_data = pd.read_csv("./dataset_movie/rating.csv")

tmp_genres = movie_genre_data.loc[:, 'genres']
tmp_genres = list(set(list(tmp_genres)))
genres = list()

for str in tmp_genres:
    genres.append(str.split('|'))

genres = list(set(sum(genres, [])))
print(genres)
# ['Thriller', 'Musical', 'Mystery', '(no genres listed)', 'Adventure', 'Horror', 'Fantasy', 'Action', 'Romance', 'Western', 'Comedy', 'Film-Noir', 'Documentary', 'Sci-Fi', 'Crime', 'Drama', 'War', 'Animation', 'IMAX', 'Children']

print(len(genres))
# 20



#model = gensim.models.KeyedVectors.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)
#print(model.vectors.shape)
#print(model.similarity('this', 'is'))
#print(model.similarity('post', 'book'))∏
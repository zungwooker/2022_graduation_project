from turtle import st
import gensim
import pickle
import pandas as pd

def v(str_list, dic):
    a = dic[str_list[0]]
    for data in str_list[1:]:
        a = a+dic[data]

    return a

movie_genre_data = pd.read_csv("./dataset_movie/movie.csv")
with open('genre_dic.pickle', 'rb') as f:
    genre_dic = pickle.load(f)

qq = 0
tmp_genres = movie_genre_data.to_numpy()
print(len(tmp_genres))
movies = []
for data in tmp_genres:
    if data[2] == '(no genres listed)':
        qq += 1
        continue

    movieID = data[0]
    movieName = data[1]
    movieGenres = data[2].split('|')
    movieVector = v(movieGenres, genre_dic)

    movies.append((movieID, {'name': movieName, 'genre': movieGenres, 'vector': movieVector}))

movies = dict(movies)

with open('movie_vector.pickle', 'wb') as f:
    pickle.dump(movies, f, pickle.HIGHEST_PROTOCOL)

print(movies[1])
print(movies[131262])
print(len(movies))
print(qq)
print(len(movies) + qq)

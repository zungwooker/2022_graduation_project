import pickle
from re import U
import numpy as np
"""
with open('dataset_movie/genre_dic.pickle', 'rb') as f:
    genre_dic = pickle.load(f)

with open('dataset_movie/movie_vec.pickle', 'rb') as f:
    movie_vec = pickle.load(f)

with open('dataset_movie/twitter_model.pickle', 'rb') as f:
    twitter_model = pickle.load(f)

with open('dataset_movie/user_rating_dic.pickle', 'rb') as f:
    user_rating_dic = pickle.load(f)

# genre_dic(dic): genre_dic['Thriller'] = np.array[25]
# movie_vec(list): movie_vec[movieID](movieID, {'name': movieName, 'genre': movieGenres, 'vector': movieVector})
# twitter_model(model): twitter['word'] = np.array[25]
# user_rating_dic(dic): user_rating_dic[1] = [1번 유저가 리뷰한 영화 리스트](movieID, Rating) 총 유저 수: 138493
print(len(movie_vec))
print(movie_vec[126560])
"""

"""
print(genre_dic['Thriller'])
print()
print(movie_vec[1])
print()
print(twitter_model['love'])
print()
print(user_rating_dic[1])
"""
"""
user_vec = []
for i in range(1, 138493 + 1):
    print("user"+str(i))
    user_v = np.zeros((1,25))
    for movie in user_rating_dic[i]:
        rating = 0
        if movie[1] > 3.5:
            rating = movie[1]*0.1
            user_v += movie_vec[movie[0]]['vector']*rating
    user_vec.append((i,user_v))



with open('dataset_movie/user_vec.pickle', 'wb') as f:
    pickle.dump(user_vec, f, pickle.HIGHEST_PROTOCOL)

print(user_vec[2])
print(user_vec[138493])
"""

with open('dataset_movie/user_vec.pickle', 'rb') as f:
    user_vec = pickle.load(f)

user_vec0 = []
user_vec = list(user_vec.items())
for i in range(len(user_vec)):
    tmp_id = user_vec[i][0]
    tmp_vec = user_vec[i][1].flatten()
    tmp_tuple = (tmp_id, tmp_vec)
    user_vec0.append(tmp_tuple)

user_vec0 = dict(user_vec0)
print(user_vec0[1])
print(user_vec0[138493])

with open('dataset_movie/user_vec.pickle', 'wb') as f:
    pickle.dump(user_vec0, f, pickle.HIGHEST_PROTOCOL)
"""
with open('dataset_movie/user_vec.pickle', 'wb') as f:
    pickle.dump(user_vec, f, pickle.HIGHEST_PROTOCOL)
"""

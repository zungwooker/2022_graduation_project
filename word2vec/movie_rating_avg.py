from turtle import st
import gensim
import pickle
import pandas as pd

# {'1': [(2, 3.5), (29, 3.5), ...], '2': ...} # 마지막 유저: 138493
movie_rating_data = pd.read_csv("./dataset_movie/rating.csv")
print(movie_rating_data.columns)
print(movie_rating_data[movie_rating_data['userId']==1])

user_rating_list = []

for i in range(1, 138493 + 1):
    tmp_user_data = movie_rating_data[movie_rating_data['userId']==i].to_numpy()
    tmp_user_rating_list = []

    for data in tmp_user_data:
        movie_rating_tuple = (data[1], data[2])
        tmp_user_rating_list.append(movie_rating_tuple)

    print("User " + str(i) + " done.")
    user_rating_list.append((i,tmp_user_rating_list))

user_rating_list = dict(user_rating_list)

with open('user_rating_dict.pickle', 'wb') as f:
    pickle.dump(user_rating_list, f, pickle.HIGHEST_PROTOCOL)

"""
print("err!!!")
user = [None]
rating_idx = 1
for user_idx in range(1, 3):
    tmp_user = []
    print(movie_rating_data[rating_idx])
    while(user_idx == movie_rating_data[rating_idx][0]):
        tmp_user.append((movie_rating_data[rating_idx][1], movie_rating_data[rating_idx][2]))
        rating_idx += 1
    user.append(tmp_user)

print(user)

"""
import pickle
import numpy as np
from numpy import dot
from numpy.linalg import norm

with open('dataset_movie/user_vec.pickle', 'rb') as f:
    user_vec = pickle.load(f)

def cos_sim(A, B):
    under = (norm(A)*norm(B))
    if under == 0:
        return -2
    return dot(A, B)/under

sims = []
user = user_vec[10]
for i in range(1, 131263+1):
    sims.append((i,cos_sim(user, user_vec[i])))

sims.sort(key = lambda x :(x[1], x[0]), reverse=True)
print(sims[:5])
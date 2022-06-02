import gensim
import numpy as np
from numpy import dot
from numpy.linalg import norm


"""
model = gensim.models.KeyedVectors.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)
model.vectors.shape
(3000000, 300)
# 파일의 크기가 3기가가 넘는 이유를 계산해보면 다음과 같다.
# 3 million words * 300 features * 4byte/feature = ~3.5GB
print(model.similarity('this', 'is'))
print(model.similarity('post', 'book'))
"""

ko_model = gensim.models.Word2Vec.load('./model/ko/ko.bin')
"""
dog_vector = ko_model.wv['강아지']
cat_vector = ko_model.wv['고양이']
print("dog:",dog_vector)
print("cat:",cat_vector)
dog_and_cat_vector = dog_vector + cat_vector
print("dog + cat:",dog_and_cat_vector)
what_is_dog_and_cat = ko_model.wv.most_similar(positive=[dog_and_cat_vector])
print("New word:",what_is_dog_and_cat)
"""

"""
cafe_vector = ko_model.wv['카페']
print("카페:",cafe_vector)
new_post = cafe_vector + cafe_vector
print(new_post)
what_is_posts = ko_model.wv.most_similar(positive=[new_post])
print("New word:",what_is_posts)
what_is_posts = ko_model.wv.most_similar(positive=[cafe_vector])
print("New word:",what_is_posts)
"""

user1_v = ko_model.wv['카페'] + ko_model.wv['등산'] + ko_model.wv['맥주']
user2_v = ko_model.wv['카페'] + ko_model.wv['카페'] + ko_model.wv['카페'] + ko_model.wv['맥주']
user3_v = ko_model.wv['카페'] + ko_model.wv['맥주']

post_user1 = ko_model.wv.most_similar(positive=[user1_v])
post_user2 = ko_model.wv.most_similar(positive=[user2_v])
post_user3 = ko_model.wv.most_similar(positive=[user3_v])

print("User1:", post_user1)
print("User2:", post_user2)
print("User3:", post_user3)

cafe = ko_model.wv['카페']

def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

print('문서 1과 문서2의 유사도 :',cos_sim(user3_v, cafe))
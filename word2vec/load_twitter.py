from statistics import mode
import gensim.downloader as api
import gensim.models
import pickle

"""
model = api.load("glove-twitter-25") 
with open('twitter_model.pickle', 'wb') as f:
    pickle.dump(model, f, pickle.HIGHEST_PROTOCOL)"""

# 25dim vector
with open('twitter_model.pickle', 'rb') as f:
    model = pickle.load(f)

thriller = model['thriller']
musical = model['musical']
mystery = model['mystery']
adventure = model['adventure']
horror = model['horror']
fantasy = model['fantasy']
action = model['action']
romance = model['romance']
western = model['western']
comedy = model['comedy']
noir = model['noir']
sf = model['sci-fi'] + model['sf']
crime = model['crime']
drama = model['drama']
war = model['war']
animation = model['animation']
imax = model['imax']
children = model['children']
documentary = model['documentary']

['thriller', 'musical', 'mystery', 'adventure', 'horror', 'fantasy', 'action', 'romance', 'western', 'comedy', 'film-noir', 'documentary', 'sci-fi', 'crime', 'drama', 'war', 'animation', 'imax', 'children']

genre_dic = {'Thriller': (thriller,'Thriller'), 'Musical': musical, 'Mystery': mystery, 'Adventure': adventure, 'Horror': horror, 'Fantasy': fantasy, 'Action': action, 'Romance': romance, 'Western': western, 'Comedy': comedy, 'Film-Noir': noir, 'Documentary': documentary, 'Sci-Fi': sf, 'Crime': crime, 'Drama': drama, 'War': war, 'Animation': animation, 'IMAX': imax, 'Children': children}

with open('genre_dic.pickle', 'wb') as f:
    pickle.dump(genre_dic, f, pickle.HIGHEST_PROTOCOL)

print(genre_dic)
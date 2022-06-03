import gensim.downloader as api

print(api.load("glove-twitter-25", return_path=True))

# https://radimrehurek.com/gensim/models/word2vec.html
# https://radimrehurek.com/gensim/downloader.html
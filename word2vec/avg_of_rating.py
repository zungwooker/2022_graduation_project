import pandas as pd

movie_genre_data = pd.read_csv("dataset_movie/rating.csv")['rating'].values.mean()
print(movie_genre_data) # 3.5255285642993797
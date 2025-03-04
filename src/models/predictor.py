import pickle

import pandas as pd
import numpy as np
ratings_dataframe = pd.read_csv('./src/models/dataframe.csv').set_index('title')
ratings_matrix = pd.read_csv('./src/models/ratings_matrix.csv').set_index('userId')
def get_prediction(movie_name):
    """Given a list of feature values, return a prediction made by the model"""
    user_ratings = ratings_matrix[movie_name]
    correlation_with_movie = pd.DataFrame(ratings_matrix.corrwith(user_ratings))
    print(ratings_dataframe.columns)
    correlation_with_movie = correlation_with_movie.join(ratings_dataframe['# of ratings'])
    correlation_with_movie.columns = [f'Corr. With {movie_name}', '# of ratings']
    correlation_with_movie.index.names = ['Movie Title']
    df = correlation_with_movie[correlation_with_movie['# of ratings'] > 50].sort_values(f'Corr. With {movie_name}', ascending = False).iloc[1:,:0].head(5)
    return df.reset_index().values

#def get_prediction(feature_values):
    """ Given a list of feature values, return a prediction made by the model"""
    
    #loaded_model = un_pickle_model()
    
    # Model is expecting a list of lists, and returns a list of predictions
    #predictions = loaded_model.predict(feature_values)
    # We are only making a single prediction, so return the 0-th value
    #return predictions[0]

#def un_pickle_model():
 ##  with open("src/models/model.pkl", "rb") as model_file:
   #     loaded_model = pickle.load(model_file)
    #return loaded_model
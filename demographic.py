#import the necessary libraries
import numpy as np
import pandas as pd


# !pip3 install wordcloud
# !pip install rake_nltk

def demographic():
    movies=pd.read_csv("tmdb_movies_data.csv")
    movies.drop_duplicates(inplace=True)
    movies = movies.drop(['imdb_id','homepage',], axis=1)
    movies['keywords'].fillna("No Keywords Aailable", inplace=True)
    movies['tagline'].fillna("No Tagline ", inplace=True)
    movies['production_companies'].fillna("Anonymous ", inplace=True)
    movies['cast'].fillna("Anonymous ", inplace=True)
    movies['director'].fillna("Anonymous ", inplace=True)
    movies['genres'].fillna("Not available ", inplace=True)
    movies['overview'].fillna("No overview ", inplace=True)
    movies['release_date'] = pd.to_datetime(movies['release_date'])

    movies.rename(columns={'genres':'genre', 'original_title':'movie_name', 'release_year':'year'}, inplace=True)


    movies = movies[['id', 'movie_name', 'director', 'genre', 'runtime', 'budget', 'tagline','overview','keywords',
                    'production_companies','cast', 'revenue', 'vote_average','vote_count',  'popularity', 'release_date', 'year']]

    movies['cast'] = movies['cast'].str.strip('[]').str.replace('|',' ').str.replace("'",'').str.replace('"','')
    movies['cast'] = movies['cast'].str.split(',')

    mean_vote= movies['vote_average'].mean()
    min_vote= movies['vote_count'].quantile(0.8)
    top_movies = movies.copy().loc[movies['vote_count'] >= min_vote]

    def weighted_rating(data, mean_vote=mean_vote, min_vote=min_vote):
        count_vote = data['vote_count']
        avg_vote = data['vote_average']
        rating =  (count_vote/(count_vote+min_vote) * avg_vote) + (min_vote/(min_vote+count_vote) * mean_vote)
        return round(rating, 3)

    top_movies['rating'] = top_movies.apply(weighted_rating, axis=1)
    #Sort movies based on rating calculated from weighted rating
    top_movies = top_movies.sort_values('rating', ascending=False)
    top_movies[['movie_name', 'vote_count', 'vote_average', 'rating','year']].head(10)

if __name__ == "__main__":
    demographic()

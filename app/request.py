from app import app
from .models import movie
import requests

Movie = movie.Movie

api_key = app.config['MOVIE_API_KEY']

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)

    search_movie_response = requests.get(search_movie_url).json()

    search_movie_results = None

    if search_movie_response['results']:
        search_movie_list = search_movie_response['results']
        search_movie_results = process_results(search_movie_list)
    return search_movie_results    


def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results
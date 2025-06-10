import requests 
import random

def get_genre_id(genre_name, api_key):
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US'
    response = requests.get(url)

    if response.status_code == 200:
        genres = response.json()['genres']
        for genre in genres:
            if genre['name'].lower() == genre_name.lower():
                return genre['id']
    
    return None

def recommend_movie(genre_name, api_key):
    genre_id = get_genre_id(genre_name, api_key)
    if genre_id is None:
        print('Genre not found')
        return
    
    url = f'https://api.themoviedb.org/3/discover/movie?{api_key}$with_genres={genre_id}'
    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()['results']
        if not movies:
            print('Movie not found')
            return
        movie = random.choice(movies)
        print(f'{movie["title"]}')
    else:
        print('Failed')

api_key = 'api_key'
user_genre = input('Enter genre: ')
recommend_movie(user_genre, api_key)
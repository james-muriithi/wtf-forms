from flask import render_template
from app import app
from .forms import ReviewForm

from .request import search_movie

# Views

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hello World'
    return render_template('index.html', message = message)

@app.route('/review', methods=['GET', 'POST'])

def review():
    form = ReviewForm()

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        return title

    return render_template('new_review.html', review_form=form)    
        
@app.route('/search/<movie_name>')

def search(movie_name):
    '''
    View function to display the search results
    ['spider' 'man'] spider+man
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)

    return render_template('search.html',movies = searched_movies)

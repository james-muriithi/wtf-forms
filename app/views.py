from flask import render_template
from app import app
from .forms import ReviewForm

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
        
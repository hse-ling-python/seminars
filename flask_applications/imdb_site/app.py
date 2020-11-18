from flask import Flask, render_template, request
from models import Film, Person, db, Rating, Type, Genre, FilmGenres

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///imdb_small_indexed.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/search')
def search():
    film_types = Type.query.all()
    genre_types = Genre.query.all()

    data = {
        "film_types": film_types,
        "genre_types": genre_types
    }
    return render_template("search.html", data=data)


@app.route('/results')
def results():
    if request.values:
        search_result = db.session.query(Film)\
            .join(Rating) \
            .join(FilmGenres) \
            .filter(
                Film.film_type_id == request.values.get("film_type"),
                Rating.votes > request.values.get("min_votes", int),
                Rating.value > request.values.get("min_rating", float),
                FilmGenres.genre_id == request.values.get("genre", int),
            )
        sorting = request.values.get("sort")
        if sorting == "rating":
            search_result = search_result.order_by(-Rating.value)
        elif sorting == "year":
            search_result = search_result.order_by(-Film.premiered)
        else:
            search_result = search_result.order_by(-Rating.votes)
        search_result = search_result.limit(250).all()
    else:
        search_result = []
    return render_template("results.html", results=search_result)


@app.route("/film/<film_id>")
def film_page(film_id):
    film = Film.query.get(film_id)
    return render_template("film.html", film=film)


@app.route("/person/<person_id>")
def person_page(person_id):
    person = Person.query.get(person_id)
    return render_template("person.html", person=person)


@app.route("/rating")
def rating():
    # rating = Film.query.limit(250).all() # .order_by(Film.rating.value)
    rating = db.session.query(Film)\
        .join(Rating)\
        .filter(Rating.votes > 100000)\
        .order_by(-Rating.value)\
        .limit(250).all()
    return render_template("rating.html", rating=rating)


if __name__ == '__main__':
    app.run(debug=True)

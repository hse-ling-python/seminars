from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Film(db.Model):
    __tablename__ = "titles"

    # имя колонки = специальный тип (тип данных, первичный ключ)
    film_id = db.Column('title_id', db.Integer, primary_key=True)

    # соединяем
    film_type_id = db.Column('type', db.Integer, ForeignKey('film_types.id'))
    film_type = db.relationship('Type')

    rating = db.relationship('Rating', uselist=False, primaryjoin="Film.film_id==Rating.film_id")

    title = db.Column('title', db.Text)
    premiered = db.Column('premiered', db.Integer)
    ended = db.Column('ended', db.Integer)
    runtime_min = db.Column('runtime_min', db.Integer)

    crew = db.relationship("Person", secondary='crew')
    genres = db.relationship("Genre", secondary='film_genres', lazy='dynamic')


class Type(db.Model):

    __tablename__ = "film_types"

    type_id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('film_type', db.Text)


class Genre(db.Model):

    __tablename__ = "genre_types"

    genre_id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('genre_name', db.Text)


class Person(db.Model):
    __tablename__ = "people"

    person_id = db.Column('person_id', db.Integer, primary_key=True)
    name = db.Column('name', db.Text)
    born = db.Column('born', db.Integer)
    died = db.Column('died', db.Integer)

    films = relationship("Film", secondary='crew')


class Crew(db.Model):
    __tablename__ = 'crew'
    __table_args__ = (PrimaryKeyConstraint('title_id', 'person_id'),)

    film_id = db.Column('title_id', db.Integer, ForeignKey('titles.title_id'))
    person_id = db.Column('person_id', db.Integer, ForeignKey('people.person_id'))


class FilmGenres(db.Model):
    __tablename__ = 'film_genres'
    __table_args__ = (PrimaryKeyConstraint('title_id', 'genre_id'),)

    film_id = db.Column('title_id', db.Integer, ForeignKey('titles.title_id'))
    genre_id = db.Column('genre_id', db.Integer, ForeignKey('genre_types.id'))


class Rating(db.Model):

    __tablename__ = "rating"

    film_id = db.Column('title_id', db.Integer, ForeignKey('titles.title_id'), primary_key=True)
    value = db.Column('rating', db.Float)
    votes = db.Column('votes', db.Integer)

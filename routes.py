import json

from models import Point
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from utils import *
from flask import render_template, request, Blueprint

routes = Blueprint('routes', __name__)

db = sa.create_engine('sqlite:///db.sqlite')
Session = sessionmaker(bind=db)

@routes.route('/')
def home():
    with Session() as session:
        points = session.query(Point).all()
        return render_template('home.html', data=points)


@routes.route('/add', methods=['POST', 'GET'])
def add_form():
    if request.method == 'POST':
        x = request.form['x']
        y = request.form['y']
        cat = request.form['category']

        try:
            x, y, cat = cast_input(x, y, cat)

            point = Point(x=x, y=y, cat=cat)

        except Exception:
            error = 400
            return render_template('error400.html', data=error), error

        with Session() as session:
            session.add(point)
            session.commit()
        return home()

    return render_template('add_form.html')


@routes.route('/delete/<int:record_id>', methods=['POST'])
def remove_point(record_id):
    if request.method == 'POST':
        with Session() as session:
            temp = session.query(Point).get(record_id)
            if temp is None:
                error = 404
                return render_template('error404.html', data=error), error
            else:
                session.delete(temp)
                session.commit()
        return home()


@routes.route('/predict', methods=['POST', 'GET'])
def predict_form():
    if request.method == 'POST':
        x = request.form['x']
        y = request.form['y']

        try:
            x, y, cat = cast_input(x, y, 0)
            all_data = get_points()
            predicted_cat = make_prediction(all_data, x, y)

            return render_template("predicted_cat.html", data=int(predicted_cat))
        except Exception:

            error = 400
            return render_template('error400.html', data=error), error

    return render_template("prediction_form.html")


@routes.route('/api/data', methods=['GET'])
def get_points():
    with Session() as session:
        points = session.query(Point).all()
        data = [json.loads(p.__repr__()) for p in points]
    return data


@routes.route('/api/data', methods=['POST'])
def post_points():
    data = request.json
    error_message = {"message": "Error 400, Invalid data"}
    error = 400
    required_keys = ['x', 'y', 'cat']

    if not data:
        return error_message, error

    if type(data) is not dict:
        return error_message, error

    for key in data:
        if key not in required_keys:
            return error_message, error

    try:
        x, y, cat = cast_input(data['x'], data['y'], data['cat'])

        point = Point(x=x, y=y, cat=cat)

    except Exception:
        return error_message, error

    with Session() as session:
        session.add(point)
        session.flush()
        session.refresh(point)
        primary_key = point.id
        session.commit()

    return {"id": primary_key}


@routes.route('/api/data/<int:record_id>', methods=['DELETE'])
def remove_point_api(record_id):

    data = {"id": None}

    with Session() as session:
        temp = session.query(Point).get(record_id)
        if temp is None:
            error_message = {"message": "Error 404, Record not found"}
            error = 404
            return error_message, error
        else:
            session.delete(temp)
            primary_key = temp.id
            session.commit()

            data['id'] = primary_key
            return data


@routes.route('/api/predictions', methods=['GET'])
def predict_api():
    x = request.args.get('x')
    y = request.args.get('y')

    try:
        x, y, cat = cast_input(x, y, 0)
        all_data = get_points()
        predicted_cat = make_prediction(all_data, x, y)

        return {"predicted_cat": predicted_cat}

    except Exception:
        error_message = {"message": "Error 400, Invalid data"}
        error = 400
        return error_message, error
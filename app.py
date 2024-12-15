import json

from flask import Flask, render_template, jsonify, request, Response
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped
from sqlalchemy.testing.schema import mapped_column

app = Flask(__name__)

db = sa.create_engine('sqlite:///db.sqlite')
Session = sessionmaker(bind=db)
Base = declarative_base()


class Point(Base):
    __tablename__ = 'points'
    id: Mapped[int] = mapped_column(primary_key=True)
    x: Mapped[float]
    y: Mapped[float]
    cat: Mapped[int]

    def __repr__(self):
        return json.dumps({'id': self.id, 'x': self.x, 'y': self.y, 'cat': self.cat})


def display_table_points(points):
    return render_template('home.html', data=points)

@app.route('/')
def home():
    with Session() as session:
        points = session.query(Point).all()
        return display_table_points(points)

@app.route('/add', methods=['POST', 'GET'])
def add_form():
    if request.method == 'POST':
        x = request.form['x']
        y = request.form['y']
        cat = request.form['category']

        try:
            x = float(x)
            y = float(y)
            cat = int(cat)

            point = Point(x=x, y=y, cat=cat)

        except Exception:
            error = 400
            return render_template('error400.html', data=error), error

        with Session() as session:
            session.add(point)
            session.commit()
        return home()

    return render_template('add_form.html')

@app.route('/remove/<int:record_id>', methods=['POST'])
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


@app.route('/api/data', methods=['GET'])
def get_points():
    with Session() as session:
        points = session.query(Point).all()
        data = [json.loads(p.__repr__()) for p in points]
    return data

@app.route('/api/data', methods=['POST'])
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
        x = float(data['x'])
        y = float(data['y'])
        cat = int(data['cat'])

        point = Point(x=x, y=y, cat=cat)

    except Exception:
        return error_message, error

    with Session() as session:
        session.add(point)
        session.flush()
        session.refresh(point)
        primary_key = point.id
        session.commit()
    data['id'] = primary_key

    return data






if __name__ == '__main__':
    app.run()
    # Base.metadata.create_all(bind=db) # dodac ze tworzy baze jesli nie ma

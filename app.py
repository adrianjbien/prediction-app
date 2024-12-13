import json

from flask import Flask, render_template, jsonify, request
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

def display_points(points):
    return render_template('index.html', data=points)

@app.route('/', methods=['GET'])
def home():
    with Session() as session:
        points = session.query(Point).all()
        return display_points(points)

@app.route('/api/data', methods=['GET'])
def get_points():
    with Session() as session:
        points = session.query(Point).all()
        data = [json.loads(p.__repr__()) for p in points]
    return data

@app.route('/api/data', methods=['POST'])
def post_points():
    data = request.json
    with Session() as session:
        points = session.query(Point).all()



if __name__ == '__main__':
    app.run()
    # Base.metadata.create_all(bind=db)

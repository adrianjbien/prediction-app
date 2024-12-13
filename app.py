import json

from flask import Flask
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
        return f'<Point ({self.x}, {self.y}), cat: {self.cat}>'

    def to_JSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

@app.route('/', methods=['GET'])
def display_points():
    try:
        with Session() as session:
            points = session.query(Point).all()

            point_text = '<ul>'
            for point in points:
                point_text += '<li>' + str(point.x) + ', ' + str(point.y) + ', ' + str(point.cat) +'</li>'
            point_text += '</ul>'
            return point_text

    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run()
    # Base.metadata.create_all(bind=db)
    # point1 = Point(x=5, y=2, cat=1)


    # with Session() as session:
    #     session.add(point1)
    #     session.commit()
    #     print(session.query(Point).all())

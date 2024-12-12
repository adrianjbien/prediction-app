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

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    Base.metadata.create_all(bind=db)
    point1 = Point(x=1, y=2, cat=3)

    with Session() as session:
        session.add(point1)
        session.commit()
        print(session.query(Point).all())

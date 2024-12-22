import json
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


class Point(Base):
    __tablename__ = 'points'
    id: Mapped[int] = mapped_column(primary_key=True)
    x: Mapped[float]
    y: Mapped[float]
    cat: Mapped[int]

    def __repr__(self):
        return json.dumps({'id': self.id, 'x': self.x, 'y': self.y, 'cat': self.cat})
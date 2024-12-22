from flask import Flask

from models import Base
from routes import routes
from routes import db

app = Flask(__name__)
app.register_blueprint(routes)


if __name__ == '__main__':
    Base.metadata.create_all(bind=db)
    app.run()

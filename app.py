from flask import Flask
from flask_migrate import Migrate 
from flask_restful import Api, Resource

from models import db, WorkoutModel, UserModel, ReviewModel, UserWorkoutModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrations = Migrate(app,db)
db.init_app(app)



if __name__ == '__main__':
    app.run(port = 5555, debug=True)
    
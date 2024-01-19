from flask import Flask
from flask_migrate import Migrate 
from flask_restful import Api, Resource
from resources.user import User,Login
from resources.workout import Workout
from resources.reviews import Review
from resources.user_workouts import UserWorkout
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from models import db, WorkoutModel, UserModel, ReviewModel, UserWorkoutModel

app = Flask(__name__)

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrations = Migrate(app,db)
db.init_app(app)

api.add_resource(User, '/users', '/users/<int:id>')
api.add_resource(Workout, '/workouts', '/workouts/<int:id>')
api.add_resource(Review, '/reviews', '/reviews/<int:id>')
api.add_resource(UserWorkout, '/userworkouts', '/userworkouts/<int:id>')
api.add_resource(Login, '/login')


if __name__ == '__main__':
    app.run(port = 5555, debug=True)
    
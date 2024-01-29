from flask import Flask
from flask_migrate import Migrate 
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta

from models import db , UserModel
from resources.users import User,Login
from resources.workouts import Workout
from resources.userworkouts import UserWorkout #,BookWorkoutResource , BookedWorkoutsResource
from resources.profile import ProfileResource
from resources.review import ReviewResource
from resources.announcements import AnnouncementResource

app=Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

#using the sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

#setting up jwt
app.config["JWT_SECRET_KEY"] = "super-secret"  # we should remember to change this
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)

#migrations set-up
db.init_app(app)
migrations = Migrate(app ,db)

api.add_resource(User, '/users', '/users/<int:id>')
api.add_resource(UserWorkout, '/userworkouts', '/userworkouts/<int:id>')
api.add_resource(Login, '/login')
api.add_resource(Workout, '/workouts', '/workouts/<int:id>')
api.add_resource(ProfileResource, '/profile')
api.add_resource(ReviewResource, '/reviews','/reviews/<int:id>')
api.add_resource(AnnouncementResource, '/announcements')
#api.add_resource(BookWorkoutResource, '/book-workout')
#api.add_resource(BookedWorkoutsResource, '/booked-workouts')

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UserModel.query.filter_by(id=identity).one_or_none().to_json()

   
if __name__ == '__main__':
    app.run(port = 5000, debug=True)
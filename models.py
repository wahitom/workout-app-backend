from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.Text, nullable=False)
    password = db.Column(db.String , nullable = False)

    #the workouts a user has selected
    user_workouts = db.relationship('UserWorkoutModel', back_populates='user')

    workouts = db.relationship('WorkoutModel', secondary='user_workout', back_populates='users')
    #uselist one to one -- one user can have only one profile
    profile = db.relationship('ProfileModel', backref='user', uselist=False)
    #cascade all orphan -- when a user is deleted all his reviews are deleted as well
    reviews = db.relationship('ReviewModel', back_populates='user', cascade='all, delete-orphan')
    
    def check_password(self, plain_password):
        return check_password_hash(self.password, plain_password)
    
    # @property
    # def username(self):
    #     return self.username
    
    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class WorkoutModel(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String , nullable=False)
    image = db.Column(db.String , nullable=False)
    trainer = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable=False)
    time= db.Column(db.String, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default= db.func.now())

    #workouts the user have selected 
    workout_users = db.relationship('UserWorkoutModel', back_populates='workout')
    #relationship between the currentmodel and UserModel
    users = db.relationship('UserModel', secondary='user_workout', back_populates='workouts')

class UserWorkoutModel(db.Model):
    __tablename__ = 'user_workout'
    id = db.Column(db.Integer, primary_key= True , nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))

    user = db.relationship('UserModel', back_populates='user_workouts')
    workout = db.relationship('WorkoutModel', back_populates='workout_users')

class ProfileModel(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    phone = db.Column(db.String ,unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    #user has only one profile
    #user = db.relationship('UserModel', backref='profile', uselist=False)

class ReviewModel(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    comment = db.Column(db.String)
     # Define the foreign key to link with UserModel
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Establish the back-reference to UserModel
    user = db.relationship('UserModel', back_populates='reviews')

class Anouncement(db.Model):
    __tablename__ = 'Announcements'

    id = db.Column(db.Integer, primary_key=True , nullable= False)
    title = db.Column(db.String , nullable = False)
    image = db.Column(db.String , nullable = False)
    description = db.Column(db.String , nullable = False)
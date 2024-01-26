from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash


db = SQLAlchemy()

# User model for storing user information
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255),  nullable = False) # nullability 
    last_name = db.Column(db.String(255),  nullable = False)
    email = db.Column(db.String(255), unique=True,  nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    password = db.Column(db.String(255),  nullable = False)
    age = db.Column(db.Integer,  nullable = False)
    weight = db.Column(db.Integer, nullable = False)
    gender = db.Column(db.String(10), nullable = False)
    role = db.Column(db.String, nullable = False)
    created_at = db.Column(db.TIMESTAMP, server_default= db.func.now())
    updated_at = db.Column(db.TIMESTAMP, server_default= db.func.now())

    workouts = db.relationship('UserWorkoutModel', back_populates='user')

    # def to_dict(self):

    #     return [{
            
    #         "id": self.id,
    #         "first_name": self.first_name,
    #         "last_name" : self.last_name,
    #         "email": self.email,
    #         "phone" : self.phone,
    #         "password" : self.password,
    #         "age" : self.age,
    #         "weight" : self.weight,
    #         "gender" : self.gender,
    #         "created_at" : self.created_at
    #     }]

    # Check if the provided password matches the stored hashed password
    def check_password(self, user_password):
        return check_password_hash(self.password,user_password)
    
    # Return a JSON representation of the user for token creation 
    def to_json(self):
        return {"id": self.id, "role": self.role}
      
# Workout model for storing workout information
class WorkoutModel(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    # was thinking about its importance here User_id and didnt see any 
    # a workout should be associated to a user only when he/she books it
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'),  nullable = False)
    name = db.Column(db.String(255), nullable = False)
    trainer = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    image = db.Column(db.String, nullable=False)
    time = db.Column(db.String(255), nullable = False)
    price = db.Column(db.String, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default= db.func.now())

    # these are a users workout so user_id is important here
    user_workouts = db.relationship('UserModel', backref='user_workouts') 
    users = db.relationship('UserWorkoutModel', back_populates='workout')
   

# Review model for storing workout reviews
class ReviewModel(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    workouts_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable = False)
    ratings = db.Column(db.String, nullable = False)
    body = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),  nullable = False)
    # status = db.Column(db.String(255),  nullable = False)
    created_at = db.Column(db.TIMESTAMP, server_default= db.func.now())
  
    #  this is for the relationships between reviews and users and workouts
    workout = db.relationship('WorkoutModel', backref='reviews')  # Updated relationship name
    user = db.relationship('UserModel', backref='reviews')  # Updated relationship name
    

# Model for storing user and workout associations
class UserWorkoutModel(db.Model):
    __tablename__ = 'user_workouts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),  nullable = False)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'),  nullable = False)
    created_at = db.Column(db.TIMESTAMP,server_default= db.func.now())

    # this is the relationship between users and workouts
    user = db.relationship('UserModel', back_populates='workouts')
    workout = db.relationship('WorkoutModel', back_populates='users')
    
# Model for storing announcements
class AnnouncementModel(db.Model):
    __tablename__ = 'announcements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String ,nullable = False)
    image = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)

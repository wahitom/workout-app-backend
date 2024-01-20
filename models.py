from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash


db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255)) # nullability 
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    phone = db.Column(db.Integer)
    password = db.Column(db.String(255))
    age = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    created_at = db.Column(db.TIMESTAMP, server_default= db.func.now())
    # updated_at = db.Column(db.TIMESTAMP, server_default= db.func.now())

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

    def check_password(self, user_password):
        return check_password_hash(self.password,user_password)
    
    #  logic for the access token 
    def to_json(self):
        return {"id": self.id}
      

class WorkoutModel(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))  
    name = db.Column(db.String(255))
    trainer = db.Column(db.String(255))
    description = db.Column(db.String(255))
    #image = db.Column(db.String)
    time = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, server_default= db.func.now())
    # user = db.relationship('User', backref='workouts')


class ReviewModel(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    workouts_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, server_default= db.func.now())
   
    # workout = db.relationship('Workout', backref='reviews')
    # user = db.relationship('User', backref='reviews')
     

class UserWorkoutModel(db.Model):
    __tablename__ = 'user_workouts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    created_at = db.Column(db.TIMESTAMP,server_default= db.func.now())




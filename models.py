from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Define User model
class UserModel(db.Model):
    __tablename__ = "users"
    
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    # Timestamps
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, onupdate=db.func.now())


# Define Workout model
class WorkoutModel(db.Model):
    __tablename__ = "workouts"
    
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    # Timestamp
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())

# Define Review model
class ReviewModel(db.Model):
    __tablename__ = "reviews"
    
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)

    # Timestamp
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())

# Define User_workout model
class UserWorkoutModel(db.Model):
    __tablename__ = "user_workouts"
    
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())

    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
            
        
        
        
        
        
        
        
    
    
    
    
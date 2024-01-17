from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


#models
class UserModel(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key = True )
    first_name= db.Column( db.String, nullable=False)
    last_name= db.Column( db.String, nullable=False)
    email= db.Column( db.String, nullable=False, unique=True)
    phone= db.Column( db.String, nullable=False , unique=True)
    password= db.Column( db.String, nullable=False)
    age= db.Column( db.Integer, nullable=False)
    weight= db.Column( db.String, nullable=False)
    gender= db.Column( db.String, nullable=False)
    created_at= db.Column( db.TIMESTAMP, server_default=db.func.now())
    updated_at= db.Column( db.TIMESTAMP, onupdate=db.func.now())
    
    
    
class WorkoutModel(db.Model):
    __tablename__ = "workouts"
    
    id = db.Column(db.Integer, primary_key = True )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),nullable=False)
    name = db.Column(db.String, nullable=False )
    trainer = db.Column(db.String, nullable=False )
    description= db.Column(db.String, nullable=False )
    time = db.Column(db.String, nullable=False )
    created_at= db.Column( db.TIMESTAMP, server_default=db.func.now())
        
        
class ReviewModel(db.Model):
    __tablename__ = "reviews"
            
    id = db.Column(db.Integer, primary_key = True ) 
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"),nullable=False)
    title = db.Column(db.String, nullable=False )
    body = db.Column(db.String, nullable=False )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),nullable=False)
    status= db.Column(db.String, nullable=False )
    created_at= db.Column( db.TIMESTAMP, server_default=db.func.now())
    
    
class User_workoutModel(db.Model):
    __tablename__ = "user_workouts"
    
    id = db.Column(db.Integer, primary_key = True ) 
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),nullable=False)
    created_at= db.Column( db.TIMESTAMP, server_default=db.func.now())
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
            
        
        
        
        
        
        
        
    
    
    
    
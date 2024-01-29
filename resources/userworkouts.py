from models import UserWorkoutModel, db
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask_restful import Resource,fields, marshal_with, reqparse
#from .users import user_fields
from .workouts import workout_fields
from models import UserModel, WorkoutModel

userWorkout_fields = {
    "id": fields.Integer,
    "user_id":fields.Integer,
    "workout_id": fields.Integer,
    #"user": fields.Nested(user_fields),  # Assuming you have defined user_fields for UserModel
    "workout": fields.Nested(workout_fields),
}

class UserWorkout(Resource):
    userworkout_parser = reqparse.RequestParser()
    #userworkout_parser.add_argument('user_id', required = True,type=int,help="Users id is required" )
    userworkout_parser.add_argument('workout_id', required = True,type=int,help="workout id is required" )
    
    #should get data of the user who is currently logged in and wants to see the workout he/she is currentry enrolled in
    @marshal_with(userWorkout_fields)
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        if current_user_id:
            userworkout = UserWorkoutModel.query.filter_by(user_id=current_user_id).all()
            return userworkout
        else:
            #userworkouts = UserWorkoutModel.query.all()
            return {"message":"you have not registered for any workout"}
        
    #  I added some things to this post method to deal with the relationships between user 
        # and workouts 
    #it will be posted to the profile page once a user books it
    @jwt_required()
    def post(self):
      data = UserWorkout.userworkout_parser.parse_args()
      current_user_id = get_jwt_identity()
      
      existing_booking = UserWorkoutModel.query.filter_by(user_id=current_user_id, workout_id=data['workout_id']).first()

      if existing_booking:
            # User has already booked for this workout
            return {"message": "You have already booked for this workout"}, 400

      data['user_id'] = current_user_id
      new_workout = UserWorkoutModel(**data)

      db.session.add(new_workout)
      db.session.commit()
      
      return {"message": "Workout booked successfully"}, 201
 
        
    @marshal_with(userWorkout_fields)
    def patch(self,id):
        data = UserWorkout.userworkout_parser.parse_args()
        userworkout = UserWorkoutModel.query.get(id)

        if userworkout:
            for key,value in data.items():
                setattr(userworkout,key,value)
            try:
                db.session.commit()

                return {"message":"userworkout updated successfully"}
            except:
                return {"message":"userworkout unable to be updated"}
            
        else:
            return {"message":"userworkout not found"}
        

    #once a user is finallly fit or satisfied with the exercise he/she can delete the workout from his profile
        # or once he/she is done with the classes 
    def delete(self,id):
        userworkout = UserWorkoutModel.query.filter_by(id = id).first()
        if userworkout:
            try:
                db.session.delete(userworkout)
                db.session.commit()

                return {"message":"userworkout deleted"}
            except:
                return {"message":"userworkout unable to be deleted"}
        else:
            return {"message":"userworkout not found"}


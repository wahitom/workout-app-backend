from models import UserWorkoutModel, db
from flask_restful import Resource,fields, marshal_with, reqparse
from .user import user_fields
from .workout import workout_fields
from models import UserModel, WorkoutModel

userWorkout_fields = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "workout_id": fields.Integer,
    "created_at": fields.DateTime,
    "user": fields.Nested(user_fields),  # Assuming you have defined user_fields for UserModel
    "workout": fields.Nested(workout_fields),
    
}

class UserWorkout(Resource):
    userworkout_parser = reqparse.RequestParser()
    userworkout_parser.add_argument('user_id', required = True,type=int,help="Users id is required" )
    userworkout_parser.add_argument('workout_id', required = True,type=int,help="workout id is required" )
    
    #should get data of the user who is currently logged in and wants to see the workout he/she is currentry enrolled in
    @marshal_with(userWorkout_fields)
    def get(self,id=None):
        if id:
            userworkout = UserWorkoutModel.query.filter_by(id=id).first()
            return userworkout
        else:
            userworkouts = UserWorkoutModel.query.all()
            return userworkouts
        
    #  I added some things to this post method to deal with the relationships between user 
        # and workouts 
    #it will be posted to the profile page once a user books it     
    def post(self):
        data = UserWorkout.userworkout_parser.parse_args()

        # Get the associated UserModel and WorkoutModel instances
        user = UserModel.query.get(data['user_id'])
        workout = WorkoutModel.query.get(data['workout_id'])

        # Check if both user and workout instances exist
        if user and workout:
            userworkout = UserWorkoutModel(**data)

            try:
                db.session.add(userworkout)
                db.session.commit()

                # Update the relationships
                user.workouts.append(userworkout)
                workout.users.append(userworkout)

                db.session.commit()

                return {"message": "UserWorkout created successfully"}
            except Exception as e:
                print(e)
                return {"message": "Unable to create UserWorkout"}
        else:
            return {"message": "User or Workout not found"}
        
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
        userworkout = UserWorkoutModel.query.get(id)
        if userworkout:
            try:
                db.session.delete(userworkout)
                db.session.commit()

                return {"message":"userworkout deleted"}
            except:
                return {"message":"userworkout unable to be deleted"}
        else:
            return {"message":"userworkout not found"}


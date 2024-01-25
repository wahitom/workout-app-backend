from models import UserWorkoutModel, db
from flask_restful import Resource,fields, marshal_with, reqparse

# Define fields for marshaling responses
userWorkout_fields = {
    "id" : fields.Integer,
    "user_id" : fields.Integer,
    "workout_id" : fields.Integer,
    "created_at" : fields.DateTime
    
}

# Request parser for handling user workout data in requests
class UserWorkout(Resource):
    userworkout_parser = reqparse.RequestParser()
    userworkout_parser.add_argument('user_id', required = True,type=int,help="Users id is required" )
    userworkout_parser.add_argument('workout_id', required = True,type=int,help="workout id is required" )
    
#Retrieve user workout(s) based on the provided ID.
    @marshal_with(userWorkout_fields)
    def get(self,id=None):
        if id:
            userworkout = UserWorkoutModel.query.filter_by(id=id).first()
            return userworkout
        else:
            userworkouts = UserWorkoutModel.query.all()
            return userworkouts
        
   # Create a new user workout record.
    def post(self):
        data = UserWorkout.userworkout_parser.parse_args()

        userworkout = UserWorkoutModel(**data)

        try:
            db.session.add(userworkout)
            db.session.commit()

            return {"message":"UserWorkout created successfully"}
        except:
            return {"message" : "unable to create userworkout"}
        
    #Update user workout information based on the provided ID
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
     
     #Delete a user workout record based on the provided ID.   
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


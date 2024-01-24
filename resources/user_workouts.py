from models import UserWorkoutModel, db
from flask_restful import Resource,fields, marshal_with, reqparse

userWorkout_fields = {
    "id" : fields.Integer,
    "user_id" : fields.Integer,
    "workout_id" : fields.Integer,
    "created_at" : fields.DateTime
    
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
        
    #it will be posted to the profile page once a user books it     
    def post(self):
        data = UserWorkout.userworkout_parser.parse_args()

        userworkout = UserWorkoutModel(**data)

        try:
            db.session.add(userworkout)
            db.session.commit()

            return {"message":"UserWorkout created successfully"}
        except:
            return {"message" : "unable to create userworkout"}
        
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


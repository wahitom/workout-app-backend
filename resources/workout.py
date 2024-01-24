from models import WorkoutModel, db
from flask_restful import Resource,fields, marshal, reqparse, marshal

workout_fields = {
    "id" : fields.Integer,
    "users_id" : fields.Integer,
    "name" : fields.String,
    "trainer" : fields.String,
    "description" : fields.String,
    "image":fields.String,
    "time" : fields.String,
    "created_at" : fields.DateTime
    
}
# jwt_required()
class Workout(Resource):
    workout_parser = reqparse.RequestParser()
    #workout_parser.add_argument('users_id', required = True,type=int,help="Users id is required" )
    workout_parser.add_argument('name', required = True,help="Name is required" )
    workout_parser.add_argument('trainer', required = True,help="Trainer is required" )
    workout_parser.add_argument('description', required = True,help="Description is required" )
    workout_parser.add_argument('image', required = True,help="Image is required" )
    workout_parser.add_argument('time', required = True,help="Time is required" )
    workout_parser.add_argument('price', required = True,help="price is required" )
   
    def get(self,id=None):
        if id:
            workout = WorkoutModel.query.filter_by(id=id).first()
            if workout == None:
               return {"message":"workout not found"}, 404
            return marshal(workout, workout_fields)
        else:
            workouts = WorkoutModel.query.all()
            return  marshal(workouts, workout_fields)
        
    def post(self):
        data = Workout.workout_parser.parse_args()

        workout = WorkoutModel(**data)

        try:
            db.session.add(workout)
            db.session.commit()

            return {"message":"Workout created successfully"}
        except:
            return {"message" : "unable to create workout"}
        

    def patch(self,id):
        data = Workout.workout_parser.parse_args()
        workout = WorkoutModel.query.get(id)

        if workout:
            for key,value in data.items():
                setattr(workout,key,value)
            try:
                db.session.commit()

                return {"message":"workout updated successfully"}
            except:
                return {"message":"workout unable to be updated"}
            
        else:
            return {"message":"workout not found"}
        
    def delete(self,id):
        workout = WorkoutModel.query.get(id)
        if workout:
            try:
                db.session.delete(workout)
                db.session.commit()

                return {"message":"workout deleted"}
            except:
                return {"message":"workout unable to be deleted"}
        else:
            return {"message":"workout not found"}


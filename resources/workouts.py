from models import WorkoutModel, db
from flask_restful import Resource,fields, marshal, reqparse, marshal
from flask_jwt_extended import current_user, jwt_required

workout_fields = {
    "id" : fields.Integer,
    "name" : fields.String,
    "description" : fields.String,
    "image":fields.String,
    "trainer" : fields.String,
    "price":fields.Integer,
    "time" : fields.String,
    "created_at" : fields.DateTime    
}

# jwt_required()
class Workout(Resource):
    workout_parser = reqparse.RequestParser()
    workout_parser.add_argument('name', required = True,help="Name is required" )
    workout_parser.add_argument('trainer', required = True,help="Trainer is required" )
    workout_parser.add_argument('description', required = True,help="Description is required" )
    workout_parser.add_argument('image', required = True,help="Image is required" )
    workout_parser.add_argument('time', required = True,help="Time is required" )
    workout_parser.add_argument('price', required = True,help="Price is required" )
   
   #getting them to be displayed in the frontend --React app
    def get(self,id=None):
        if id:
            workout = WorkoutModel.query.filter_by(id=id).first()
            if workout == None:
               return {"message":"workout not found"}, 404
            return marshal(workout, workout_fields)
        else:
            workouts = WorkoutModel.query.all()
            return  marshal(workouts, workout_fields)
 
    #admin can post a workout
        #we should impliment that
   # @jwt_required()  
    def post(self):
        # print(current_user)
        # if current_user['role'] != 'admin':
        #     return {"message": "Unauthorized request", "status": "fail"}, 403
        
        data = Workout.workout_parser.parse_args()

        workout = WorkoutModel(**data)


        try:
            db.session.add(workout)
            db.session.commit()

            return {"message":"Workout created successfully"}
        except:
            return {"message" : "unable to create workout"}
        
     #admin can update a workout
        #we should impliment that
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
        
     #admin can delete a workout
        #we should impliment that
    # @jwt_required() 
    def delete(self,id):
        # if current_user['role'] != 'admin':
        #     return {"message": "Unauthorized request", "status": "fail"}, 403
        
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


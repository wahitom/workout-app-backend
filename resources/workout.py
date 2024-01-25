from models import WorkoutModel, db
from flask_restful import Resource,fields, marshal_with, reqparse, marshal

# Define fields for marshaling
workout_fields = {
    "id" : fields.Integer,
    "users_id" : fields.Integer,
    "name" : fields.String,
    "trainer" : fields.String,
    "description" : fields.String,
    "time" : fields.String,
    "created_at" : fields.DateTime
    
}
# Request parser for handling input validation
# jwt_required()
class Workout(Resource):
    workout_parser = reqparse.RequestParser()
    workout_parser.add_argument('users_id', required = True,type=int,help="Users id is required" )
    workout_parser.add_argument('name', required = True,help="Name is required" )
    workout_parser.add_argument('trainer', required = True,help="Trainer is required" )
    workout_parser.add_argument('description', required = True,help="Description is required" )
    workout_parser.add_argument('time', required = True,help="Time is required" )

    # GET method to retrieve workout(s)
    def get(self,id=None):
        if id:
            # Retrieve a specific workout by ID
            workout = WorkoutModel.query.filter_by(id=id).first()
            if workout == None:
               return {"message":"workout not found"}, 404
            return marshal(workout, workout_fields)
        else:
            # Retrieve all workouts
            workouts = WorkoutModel.query.all()
            return  marshal(workouts, workout_fields)
    
    # POST method to create a new workout    
    def post(self):
        data = Workout.workout_parser.parse_args()

        # Create a new workout instance
        workout = WorkoutModel(**data)

        try:
            # Add the workout to the database and commit the changes
            db.session.add(workout)
            db.session.commit()

            return {"message":"Workout created successfully"}
        except:
            return {"message" : "unable to create workout"}
    
    # PATCH method to update a workout by ID    
    @marshal_with(workout_fields)
    def patch(self,id):
        data = Workout.workout_parser.parse_args()
        workout = WorkoutModel.query.get(id)

# Update the workout attributes based on the provided data
        if workout:
            for key,value in data.items():
                setattr(workout,key,value)
            try:
                # Commit the changes to the database
                db.session.commit()

                return {"message":"workout updated successfully"}
            except:
                return {"message":"workout unable to be updated"}
            
        else:
            return {"message":"workout not found"}
    
    # DELETE method to delete a workout by ID    
    def delete(self,id):
        workout = WorkoutModel.query.get(id)
        if workout:
            try:
                # Delete the workout from the database and commit the changes
                db.session.delete(workout)
                db.session.commit()

                return {"message":"workout deleted"}
            except:
                return {"message":"workout unable to be deleted"}
        else:
            return {"message":"workout not found"}


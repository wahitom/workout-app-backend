from models import ReviewModel, db
from flask_restful import Resource,fields, marshal_with, reqparse
from .workout import workout_fields
from .user import user_fields
from models import UserModel, WorkoutModel

review_fields = {
    "id": fields.Integer,
    "workout": fields.Nested(workout_fields),
    "user": fields.Nested(user_fields),
    "ratings": fields.String,
    "body": fields.String,
    "created_at": fields.DateTime
    
}
    # who can make a review ?
class Review(Resource):
    review_parser = reqparse.RequestParser()
    review_parser.add_argument('workouts_id', required = True,type=int,help="Workouts id is required" )
    review_parser.add_argument('user_id', required = True,type=int,help="User id is required")
    review_parser.add_argument('ratings', required = True,help="Rating is required" )
    review_parser.add_argument('body', required = True,help="Body is required" )
    #review_parser.add_argument('status', required = True,help="Description is required" )

    @marshal_with(review_fields)
    def get(self,id=None):
        if id:
            review = ReviewModel.query.filter_by(id=id).first()
            return review
        else:
            reviews = ReviewModel.query.all()
            return reviews
   
        
    #  added this to deal with the relationships between users and workouts and id 
    def post(self):
        data = Review.review_parser.parse_args()

        # Get the associated WorkoutModel and UserModel instances
        workout = WorkoutModel.query.get(data['workouts_id'])
        user = UserModel.query.get(data['user_id'])

        # Check if both workout and user instances exist
        if workout and user:
            # Create the ReviewModel instance with the associated objects
            review = ReviewModel(
                workouts_id=workout,
                user_id=user,
                ratings=data['ratings'],
                body=data['body']
            )

            try:
                db.session.add(review)
                db.session.commit()

                return {"message": "review created successfully"}
            except:
                return {"message": "unable to create review"}
        else:
            return {"message": "workout or user not found"}

        
        
    @marshal_with(review_fields)
    def patch(self,id):
        data = Review.review_parser.parse_args()
        review = ReviewModel.query.get(id)

        if review:
            for key,value in data.items():
                setattr(review,key,value)
            try:
                db.session.commit()

                return {"message":"review updated successfully"}
            except:
                return {"message":"review unable to be updated"}
            
        else:
            return {"message":"review not found"}
        
    def delete(self,id):
        review = ReviewModel.query.get(id)
        if review:
            try:
                db.session.delete(review)
                db.session.commit()

                return {"message":"review deleted"}
            except:
                return {"message":"review unable to be deleted"}
        else:
            return {"message":"review not found"}


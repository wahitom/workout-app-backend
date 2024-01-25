from models import ReviewModel, db
from flask_restful import Resource,fields, marshal_with, reqparse

# Define fields for marshaling responses
review_fields = {
    "id" : fields.Integer,
    "workouts_id" : fields.Integer,
    "user_id" : fields.Integer,
    "title" : fields.String,
    "body" : fields.String,
    "status" : fields.String,
    "created_at" : fields.DateTime
    
}


# Request parser for handling review data in requests
class Review(Resource):
    review_parser = reqparse.RequestParser()
    review_parser.add_argument('workouts_id', required = True,type=int,help="Workouts id is required" )
    review_parser.add_argument('user_id', required = True,type=int,help="User id is required")
    review_parser.add_argument('title', required = True,help="Title is required" )
    review_parser.add_argument('body', required = True,help="Body is required" )
    review_parser.add_argument('status', required = True,help="Description is required" )

    #Retrieve review(s) based on the provided ID.
    @marshal_with(review_fields)
    def get(self,id=None):
        if id:
            review = ReviewModel.query.filter_by(id=id).first()
            return review
        else:
            reviews = ReviewModel.query.all()
            return reviews
        
    #Create a new review.
    def post(self):
        data = Review.review_parser.parse_args()

        review = ReviewModel(**data)

        try:
            db.session.add(review)
            db.session.commit()

            return {"message":"review created successfully"}
        except:
            return {"message" : "unable to create review"}
        
     #Update review information based on the provided ID.   
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
        
    #Delete a review based on the provided ID.
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


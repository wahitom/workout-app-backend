from flask_restful import Resource, fields, marshal_with, reqparse,marshal
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import ReviewModel , db , UserModel
# from .users import user_fields

review_fields = {
    "id":fields.Integer,
    "comment": fields.String,
    "username": fields.String
}

class ReviewResource(Resource):
    review_parser = reqparse.RequestParser()
    review_parser.add_argument('comment', type=str, help="Enter the comment")
    review_parser.add_argument('username', type=str, help="Enter the username")

    #getting the comments to dislay
    @jwt_required()
    def get(self):
        reviews = ReviewModel.query.all()
        if not reviews:
            return {"message":"reviews not found"}
        return marshal(reviews, review_fields)

     #user posting a comment
    @jwt_required()
    def post(self):
        current_user_id = get_jwt_identity()
        data = ReviewResource.review_parser.parse_args()
        # user = UserModel.query.get(current_user_id)
        user_id = current_user_id
        data['user_id'] = user_id
        new_review = ReviewModel(**data)

        try:
            db.session.add(new_review)
            db.session.commit()
            return {"message": "Review created successfully", "status": "success"}, 201
        except:
            return {"message": "Unable to create review", "status": "fail"}, 500

    #user updating a comment
    @jwt_required()
    def put(self, id):
        data = ReviewResource.review_parser.parse_args()
        
        review = ReviewModel.query.get(id)

        if not review:
            return {"message": "Review not found", "status": "fail"}, 404

        # Check if the current user is the owner of the review
        current_user_id = get_jwt_identity()
        if review.user_id != current_user_id:
            return {"message": "You are not authorized to update this review", "status": "fail"}, 403

        # Update the review
        review.comment = data['comment']

        try:
            db.session.commit()
            return {"message": "Review updated successfully", "status": "success"}, 200
        except:
            return {"message": "Unable to update review", "status": "fail"}, 500
        
    @jwt_required()
    def delete(self, id):
        try:
          current_user_id = get_jwt_identity()

          review = ReviewModel.query.filter_by(id=id).first()

          if not review:
            return {"message": "Review not found", "status": "fail"}, 404

          # Check if the current user is the owner of the review
          if review.user_id != current_user_id:
            return {"message": "You are not authorized to delete this review", "status": "fail"}, 403

          db.session.delete(review)
          db.session.commit()
          return {"message": "Review deleted successfully", "status": "success"}, 200

        except:
           return {"message": "Unable to delete review", "status": "fail"}, 500

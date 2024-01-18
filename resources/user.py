from models import UserModel,db
from flask_restful import Resource, fields, marshal_with, reqparse

user_fields = {
    "id" : fields.Integer,
    "first_name" : fields.String,
    "last_name" : fields.String,
    "email" : fields.String,
    "phone" : fields.Integer,
    "password" : fields.String,
    "age" : fields.Integer,
    "weight": fields.Integer,
    "gender" : fields.String,
    "created_at" : fields.DateTime
}



class User(Resource):
    user_parser = reqparse.RequestParser()
    user_parser.add_argument('first_name', required=True, type=str, help="Enter the first name")
    user_parser.add_argument('last_name', required=True, type=str,help="Enter the last name")
    user_parser.add_argument('email', required=True, type = str, help="Enter the email")
    user_parser.add_argument('phone', required=True, type=int, help="Enter your phone number")
    user_parser.add_argument('password', required=True, type=str, help="Enter password")
    user_parser.add_argument('age', required=True, type=int, help="Enter your age")
    user_parser.add_argument('weight', required=True, type=int, help="Enter weight")
    user_parser.add_argument('gender', required=True, type=str, help="Enter your gender")

    @marshal_with(user_fields)
    def get(self,id=None):
        if id:
            user = UserModel.query.filter_by(id=id).first()
            return user
        else:
            users = UserModel.query.all()
            return users
        
    def post(self):
        user = User.user_parser.parse_args()
        # posting a new user using usermodel format
        new_user = UserModel(**user)

        try:
            db.session.add(new_user)
            db.session.commit()

            return {"message": "User added successfully"}
        except:
            return {"message": "Unable to create user"}


        
    
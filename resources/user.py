from models import UserModel,db
from flask_restful import Resource, fields, marshal_with, reqparse
from flask_bcrypt import generate_password_hash

from flask_jwt_extended import create_access_token, create_refresh_token

# Define fields for marshaling responses
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
    "role": fields.String,
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
    user_parser.add_argument('role', required=True, type=str, help="Enter your role")

    # @marshal_with(user_fields)
    # def get(self,id=None):
    #     if id:
    #         user = UserModel.query.filter_by(id=id).first()
    #         return user
    #     else:
    #         users = UserModel.query.all()
    #         return users
     
     # Parse user data from request   
    def post(self):
        user = User.user_parser.parse_args()

        user['password'] = generate_password_hash(user['password'])
        # posting a new user using usermodel format
        new_user = UserModel(**user)
        
        email = UserModel.query.filter_by(email = user['email']).one_or_none()

        if email:
            # Check if email or phone number is already taken
            return {"message": "Email already taken", "status": "fail"}, 400
        
        phone = UserModel.query.filter_by(phone = user['phone']).one_or_none()
        
        if phone:
            return {"message": "phone number already taken", "status": "fail"}, 400
        
        try:
            # Save the new user to the database
            db.session.add(new_user)
            db.session.commit()

            # get user from db after saving 
            db.session.refresh(user)

# Generate access and refresh tokens for the new user
            user_json = user.to_json()
            access_token = create_access_token(identity=user_json['id'])
            refresh_token = create_refresh_token(identity=user_json['id'])

             # return user object if this process was succesful
            # add access and refresh tokens so that they can be linked with our react app
            return{"message": "Account created successfully", 
                   "status": "success", 
                   "access_token": access_token, 
                   "refresh_token": refresh_token,
                   "user": user_json
                   }, 201 

        except:
            return {"message": "Unable to create user"}

    
    # @marshal_with(user_fields)
    # def patch(self,id):
    #     data =User.user_parser.parse_args()
    #     user = UserModel.query.get(id)

    #     if user:
    #         for key,value in data.items():
    #             setattr(user,key,value)
    #         try:
    #             db.session.commit()

    #             return {"message":"user updated successfully"}
    #         except:
    #             return {"message":"user unable to be updated"}
            
    #     else:
    #         return {"message":"user not found"}
        
    # def delete(self,id):
    #     user = UserModel.query.get(id)
    #     if user:
    #         try:
    #             db.session.delete(user)
    #             db.session.commit()

    #             return {"message":"user deleted"}
    #         except:
    #             return {"message":"user unable to be deleted"}
    #     else:
    #         return {"message":"user not found"}

class Login(Resource):
     user_parser = reqparse.RequestParser()
     user_parser.add_argument('email', required=True, type = str, help="Enter the email")
     user_parser.add_argument('password', required=True, type=str, help="Enter password")   
    
     # Parse login data from request
     def post(self):
         data = Login.user_parser.parse_args()

        # Query the database for the user with the provided email
         user = UserModel.query.filter_by(email = data['email']).first()

        # Check if the provided password matches the stored hashed password
         if user:
             checking_password = user.check_password(data['password'])
             if checking_password:
                 # dont forget access token and refresh token
                user_json = user.to_json()
                access_token = create_access_token(identity=user_json['id'])
                refresh_token = create_refresh_token(identity=user_json['id'])
                return {"message": "Login successful", 
                        "status": "success",
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                        "user": user_json
                        }, 200
             
    
             else:
                 # Invalid password
                return {"message": "Invalid email/password", "status": "fail"}, 403
         else:
             # User not found with the provided email
            return {"message": "Invalid email/password", "status": "fail"}, 403
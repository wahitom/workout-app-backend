from flask_restful import Resource, fields, marshal_with, reqparse
from models import ProfileModel,UserModel,db
# will help us get the identity of the logged in user
from flask_jwt_extended import jwt_required, get_jwt_identity

profile_fields = {
    "first_name": fields.String,
    "last_name": fields.String,
    "phone": fields.String,
}

class ProfileResource(Resource):
    profile_parser = reqparse.RequestParser()
    profile_parser.add_argument('first_name', type=str, help="Enter the first name")
    profile_parser.add_argument('last_name', type=str, help="Enter the last name")
    profile_parser.add_argument('phone', type=str, help="Enter the phone number")

    #getting identity of the logged in user jwt required
    @marshal_with(profile_fields)
    @jwt_required()
    #once in front end remove the user_id from the bracket
    def get(self):
        # Fetch the profile for a specific user

        #getting the user_id when a user logs in --- will do this in front-end
        current_user_id = get_jwt_identity()
        print(current_user_id)
        #use this on front end
        profile = ProfileModel.query.filter_by(user_id=current_user_id).first()
        #profile = ProfileModel.query.filter_by(user_id=user_id).first()

        if not profile:
            return {"message": "Profile not found", "status": "fail"}, 404

        return profile
    # once you login you will be required to edit your user profile
    
    # @marshal_with(profile_fields)
    # @jwt_required
    # def post(self):
    #    current_user_id = get_jwt_identity()
    #    data = ProfileResource.profile_parser.parse_args()

    #    # Check if the user exists
    #    user = UserModel.query.get(current_user_id)
    #    if not user:
    #         return {"message": "User not found", "status": "fail"}, 404

    # # Check if a profile already exists for the user
    #    existing_profile = ProfileModel.query.filter_by(user_id=current_user_id).first()
    #    if existing_profile:
    #          return {"message": "Profile already exists", "status": "fail"}, 400

    #    new_profile = ProfileModel(
    #         first_name=data['first_name'],
    #         last_name=data['last_name'],
    #         phone=data['phone'],
    #         user_id=current_user_id
    #          )

    #    try:
    #        db.session.add(new_profile)
    #        db.session.commit()

    #        return new_profile, 201
    #    except:
    #        return {"message": "Unable to create profile", "status": "fail"}, 500

    #this should be handled when save is clicked 
    @jwt_required()
    def put(self):
        data = ProfileResource.profile_parser.parse_args()

        # Check if the user exists
        current_user_id = get_jwt_identity()
        
        # Fetch the profile for the user
        profile = ProfileModel.query.filter_by(user_id=current_user_id).first()

        if not profile:
            # If the profile does not exist, create a new one
            profile = ProfileModel(user_id=current_user_id)

        # Update the profile
        profile.first_name = data['first_name']
        profile.last_name = data['last_name']
        profile.phone = data['phone']

        try:
            db.session.add(profile)
            db.session.commit()
            return {"message": "Profile updated successfully", "status": "success"}, 200
        except: 
            return {"message": "Unable to update profile", "status": "fail"}, 500
        
    @jwt_required
    def delete(self):
        # Check if the user exists
        current_user_id = get_jwt_identity()

        user = UserModel.query.get(current_user_id)
        if not user:
            return {"message": "User not found", "status": "fail"}, 404

        # Fetch the profile for the user
        profile = ProfileModel.query.filter_by(user_id=current_user_id).first()

        if not profile:
            return {"message": "Profile not found", "status": "fail"}, 404

        try:
            db.session.delete(profile)
            db.session.commit()
            return {"message": "Profile deleted successfully", "status": "success"}, 200
        except:
            return {"message": "Unable to delete profile", "status": "fail"}, 500

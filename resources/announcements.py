
from flask_restful import Resource , reqparse ,fields, marshal , marshal_with
from models import AnnouncementModel ,db
from flask_jwt_extended import current_user, jwt_required


response_fields = {
   "id":fields.Integer,
   "title": fields.String,
   "image":fields.String,
   "description":fields.String,
   "date":fields.String
}


class Announcement(Resource):
   
   anouncement_parse =  reqparse.RequestParser()
   anouncement_parse.add_argument('title', required = True,type=str,help="title is required" )
   anouncement_parse.add_argument('image', required = True,type=str,help="image is required" )
   anouncement_parse.add_argument('description', required = True,type=str,help="description is required" )
   anouncement_parse.add_argument('date', required = True,type=str,help="date is required" )


 
   def get(self,id=None):
        if id:
            announcement = AnnouncementModel.query.filter_by(id=id).first()
            if announcement == None:
               return {"message":"workout not found"}, 404
            return marshal(announcement, response_fields)
        else:
            announcements = AnnouncementModel.query.all()
            return  marshal(announcements, response_fields)

   @jwt_required()
   def post(self):
        # print(current_user)
       if current_user['role'] != 'admin':
            return {"message": "Unauthorized request", "status": "fail"}, 403
       data = Announcement.anouncement_parse.parse_args()


       announcement = AnnouncementModel(**data)


       try:
            db.session.add(announcement)
            db.session.commit()


            return {"message":"announcement created successfully"}
       except:
            return {"message" : "unable to create Announcement"}
       
   
   def patch(self,id):
        data = Announcement.anouncement_parse.parse_args()
        announcement = AnnouncementModel.query.get(id)


        if announcement:
            for key,value in data.items():
                setattr(announcement,key,value)
            try:
                db.session.commit()


                return {"message":"announcement updated successfully"}
            except:
                return {"message":"unable to be update announcement"}
        else:
            return {"message":"announcement not found"}
        
   @jwt_required() 
   def delete(self,id):
        if current_user['role'] != 'admin':
            return {"message": "Unauthorized request", "status": "fail"}, 403
        
        announcement = AnnouncementModel.query.get(id)
        if announcement:
            try:
                db.session.delete(announcement)
                db.session.commit()


                return {"message":"announcement deleted"}
            except:
                return {"message":"announcement unable to be deleted"}
        else:
            return {"message":"announcement not found"}

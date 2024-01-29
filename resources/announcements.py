from flask_restful import Resource, fields, marshal_with, reqparse
from models import db , Anouncement

announcement_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "image": fields.String,
    "description": fields.String,
}

class AnnouncementResource(Resource):
    announcement_parser = reqparse.RequestParser()
    announcement_parser.add_argument('title', type=str, help="Enter the title")
    announcement_parser.add_argument('image', type=str, help="Enter the image URL")
    announcement_parser.add_argument('description', type=str, help="Enter the description")

    @marshal_with(announcement_fields)
    def get(self):
        # Fetching announcements
        announcements = Anouncement.query.all()
        return announcements
    
    #only an admin can add an announcement
    @marshal_with(announcement_fields)
    def post(self):
        data = AnnouncementResource.announcement_parser.parse_args()

        new_announcement = Anouncement(
            title=data['title'],
            image=data['image'],
            description=data['description']
        )

        try:
            db.session.add(new_announcement)
            db.session.commit()
            return {"message": "Announcement created successfully", "status": "success"}, 201
        except:
            return {"message": "Unable to create announcement", "status": "fail"}, 500

    #only an admin can update an announcement
    @marshal_with(announcement_fields)
    def put(self,id):
        data = AnnouncementResource.announcement_parser.parse_args()
        
        announcement = Anouncement.query.get(id)

        if not announcement:
            return {"message": "Announcement not found", "status": "fail"}, 404

        # updating
        announcement.title = data['title']
        announcement.image = data['image']
        announcement.description = data['description']

        try:
            db.session.commit()
            return {"message": "Announcement updated successfully", "status": "success"}, 200
        except:
            return {"message": "Unable to update announcement", "status": "fail"}, 500

    #only an admin can update an announcement
    def delete(self,id):
        # deleting announcement
        announcement = Anouncement.query.get(id)

        if not announcement:
            return {"message": "Announcement not found", "status": "fail"}, 404

        try:
            db.session.delete(announcement)
            db.session.commit()
            return {"message": "Announcement deleted successfully", "status": "success"}, 200
        except :
            return {"message": "Unable to delete announcement", "status": "fail"}, 500

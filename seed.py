# Importing necessary modules and objects from your application
from app import app
from models import db,UserModel, WorkoutModel,ReviewModel, UserWorkoutModel

# Data for users, workouts, reviews, and user_workouts
users = [{
  "id": 1,
  "first_name": "Wanda",
  "last_name": "Epsly",
  "email": "wepsly0@wikispaces.com",
  "phone": "8546614991",
  "password": "aQ9&s?\"H+Jq",
  "age": 18,
  "weight": 81,
  "gender": "Female",
  "role": "member"
}, {
  "id": 2,
  "first_name": "Dean",
  "last_name": "Bonds",
  "email": "dbonds1@topsy.com",
  "phone": "1809468927",
  "password": "jP2+(a,H*n)!tS",
  "age": 35,
  "weight": 74,
  "gender": "Male",
  "role": "member"
}, {
  "id": 3,
  "first_name": "Kain",
  "last_name": "MacCawley",
  "email": "kmaccawley2@jiathis.com",
  "phone": "6418049117",
  "password": "rB2{8=nIN(4_O",
  "age": 19,
  "weight": 51,
  "gender": "Male",
  "role": "member"
}, {
  "id": 4,
  "first_name": "Thorpe",
  "last_name": "Sell",
  "email": "tsell3@lulu.com",
  "phone": "5885959768",
  "password": "uB9\"@'`_rs",
  "age": 19,
  "weight": 100,
  "gender": "Male",
  "role": "member"
}, {
  "id": 5,
  "first_name": "Fayina",
  "last_name": "Water",
  "email": "fwater4@jimdo.com",
  "phone": "6039536548",
  "password": "sQ9%?uqwI2",
  "age": 28,
  "weight": 92,
  "gender": "Female",
  "role": "member"
}]

workouts = [{
  "id": 1,
  "users_id": 1,
  "name": "Garshore",
  "trainer": "Leslie",
  "description": "McHaffy",
  "time": "7/13/2023"
}, {
  "id": 2,
  "users_id": 2,
  "name": "Lorimer",
  "trainer": "Marge",
  "description": "Woolmore",
  "time": "11/19/2023"
}, {
  "id": 3,
  "users_id": 3,
  "name": "Bengtson",
  "trainer": "Kristopher",
  "description": "Krzysztof",
  "time": "2/3/2023"
}, {
  "id": 4,
  "users_id": 4,
  "name": "Cumes",
  "trainer": "Tally",
  "description": "Lavell",
  "time": "12/28/2023"
}, {
  "id": 5,
  "users_id": 5,
  "name": "Di Frisco",
  "trainer": "Minette",
  "description": "Meritt",
  "time": "10/19/2023"
}]

reviews = [{
  "id": 1,
  "workouts_id": 1,
  "title": "Fowgies",
  "body": "Bink",
  "user_id": 1,
  "status": "Torrie"
}, {
  "id": 2,
  "workouts_id": 2,
  "title": "Parfrey",
  "body": "Judye",
  "user_id": 2,
  "status": "Wallie"
}, {
  "id": 3,
  "workouts_id": 3,
  "title": "Amer",
  "body": "Lula",
  "user_id": 3,
  "status": "Reinhard"
}, {
  "id": 4,
  "workouts_id": 4,
  "title": "Bounds",
  "body": "Doro",
  "user_id": 4,
  "status": "Terrijo"
}, {
  "id": 5,
  "workouts_id": 5,
  "title": "Echelle",
  "body": "Pace",
  "user_id": 5,
  "status": "Arlette"
}]

user_workouts = [{
  "id": 1,
  "user_id": 1,
  "workout_id": 1
}, {
  "id": 2,
  "user_id": 2,
  "workout_id": 2
}, {
  "id": 3,
  "user_id": 3,
  "workout_id": 3
}, {
  "id": 4,
  "user_id": 4,
  "workout_id": 4
}, {
  "id": 5,
  "user_id": 5,
  "workout_id": 5
}]


# Adding users to the database
with app.app_context():
    db.session.add_all(UserModel(**user) for user in users)
    db.session.commit()

# Adding workouts to the database
with app.app_context():
    db.session.add_all(WorkoutModel(**workout) for workout in workouts)
    db.session.commit()

# Adding reviews to the database
with app.app_context():
    db.session.add_all(ReviewModel(**review) for review in reviews)
    db.session.commit()

# Adding user_workouts to the database
with app.app_context():
    db.session.add_all(UserWorkoutModel(**user_workout) for user_workout in user_workouts)
    db.session.commit()
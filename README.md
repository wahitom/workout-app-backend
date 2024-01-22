## Title
Workout App with Flask


## Description
This is a Workout App built using Flask, a lightweight web application framework in Python. The app allows users to create accounts, design workout plans, track progress, and achieve their fitness goals.

## Features
User Authentication: Allow users to create accounts, log in, and manage their profiles securely.

Workout Plans: Design custom workout plans or choose from pre-built ones.

Exercise Library: A comprehensive library of exercises with detailed instructions and visuals.

Progress Tracking: Track workout history, achievements, and set fitness goals.
Social Integration: Share workout achievements on social media platforms.
Reminders and Notifications: Set reminders for upcoming workouts and receive motivational notifications.

## Getting Started
## Prerequisites
Python installed
Pip installed
Virtualenv recommended for virtual environment management

## Installation
Clone the repository: git clone https://github.com/yourusername/workout-app-flask.git

Navigate to the project directory: cd workout-app-flask

Create and activate a virtual environment: virtualenv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

## Set up the database:
flask db init
flask db migrate
flask db upgrade


## Usage
Run the Flask application: flask run
Open your browser and navigate to http://localhost:5000.
Register a new account or log in if you already have one.
Explore the app features, design a workout plan, and start tracking your progress.

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


























 

For this assignment, we'll be working with a Yelp-style domain.
 

We have three models:
- `Restaurant`
- `Customer`
- `Review`
 

For our purposes, a `Restaurant` has many `Reviews`, a `Customer` has many `Review`s, and a `Review` belongs to a `Customer` and to a `Restaurant`.
 

`Restaurant` - `Customer` is a many-to-many relationship.
 

**Note**: You should draw your domain on paper or on a whiteboard _before you start coding_. Remember to identify a single source of truth for your data.
 

## Topics
- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions
To get started, use this PipfileLinks to an external site. to install all dependencies required for this project.
Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.


Note!  - You'll need to create your own test sample instances so that you can try/test out your code. Make sure your relationships and methods work in the console before submitting.
Writing error-free code is more important than completing all of the deliverables listed - prioritize writing methods that work over writing more methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.

Before you submit! - Save and run your code to verify that it works as you expect. If you have any methods that are not working yet, feel free to leave comments describing your progress.
 

NB: Pipfile sample for reference
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
ipdb = "*"

[dev-packages]

[requires]
python_version = "3.10"
Deliverables
Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.
Initializers, Readers, and Writers

## Customer
- `Customer __init__()`
  - Customer should be initialized with a given name and family name, both strings (i.e., first and last name, like George Washington)"
- `Customer given_name()`
  - returns the customer's given name
  - should be able to change after the customer is created
- `Customer family_name()`
  - returns the customer's family name
  - should be able to change after the customer is created
- `Customer full_name()`
  - returns the full name of the customer, with the given name and the family name concatenated, Western style.
- `Customer all()`
  - returns **all** of the customer instances

## Restaurant
- `Restaurant __init__()`
  - Restaurants should be initialized with a name, as a string
- `Restaurant name()`
  - returns the restaurant's name
  - should not be able to change after the restaurant is created
 

## Review
- `Review __init__()`
  - Reviews should be initialized with a customer, restaurant, and a rating (a number)
- `Review rating()`
  - returns the rating for a restaurant.
- `Review all()`
  - returns all of the reviews
Object Relationship Methods

## Review
- `Review customer()`
  - returns the customer object for that review
  - Once a review is created, should not be able to change the

  ## customer
- `Review restaurant()`
  - returns the restaurant object for that given review
  - Once a review is created, should not be able to change the restaurant

## Restaurant
- `Restaurant reviews()`
  - returns a list of all reviews for that restaurant
- `Restaurant customers()`
  - Returns a **unique** list of all customers who have reviewed a particular restaurant.


## Customer
- `Customer restaurants()`
  - Returns a **unique** list of all restaurants a customer has reviewed
- `Customer add_review(restaurant, rating)`
  - given a **restaurant object** and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.
 

## Aggregate and Association Methods
## Customer
- `Customer num_reviews()`
  - Returns the total number of reviews that a customer has authored
- `Customer find_by_name(name)` class method
  - given a string of a **full name**, returns the **first customer** whose full name matches
- `Customer find_all_by_given_name(name)`

## class method
  - given a string of a given name, returns an **list** containing all customers with that given name
 

## Restaurant
- `Restaurant average_star_rating()`
  - returns the average star rating for a restaurant based on its reviews
  - Reminder: you can calculate the average by adding up all the ratings and dividing by the number of ratings

  ## Author
Caroline Akinyi Opiyo ("https://github.com/Budabos") Email: opiyocaroline20@gmail.com

## Collaborators
Nelson Murithi ("https://github.com/NellieMK65")

## License
License (" MIT License")
 

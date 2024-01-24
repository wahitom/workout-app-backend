## Table Of Content

## Title
## Learning Goals
## Description
## Requirements
## Features
## Project Setup
## Project Guidance
## Planning
## User Stories
    ## Example
## Models and Relationships
## Technologies
## Getting Started
## Prerequisites
## Installation
## Set up the database
## Usage
## Collaborators
## Deploying
## Contributing
## License


## Title
Full-Stack Project: Workout Tracking App

## Learning Goals
Build a full-stack project with a React frontend and a Flask backend.
Apply skills learned throughout the program.
Prepare for building a capstone project in Phase 5.
Develop a high-quality project for your portfolio.


## Description
Welcome to the journey of building a workout app! This project aims to consolidate the skills you've acquired during the program, providing hands-on experience in creating a full-stack application with a robust backend framework.

## Requirements
Utilize a Flask API backend with a React frontend.
Include at least three models on the backend, featuring:
At least two one-to-many relationships.
At least one reciprocal many-to-many relationship.
Implement full CRUD actions for at least one resource.
Implement a minimum of create and read actions for EACH resource.
Use forms and validation for all input.
Include at least one data type validation and one string/number format validation. Alternatively, validate input via client-side tools like Formik and Yup for all inputs.
Have at least three different client-side routes using React Router. Include a navigation bar or another UI element for seamless navigation.
Connect the client and server using either fetch() or socket.io.
Ensure users can only edit and delete resources if they are logged in and are the creator of that resource.

## Features
User Authentication: Allow users to create accounts, log in, and manage their profiles securely.

Workout Plans: Design custom workout plans or choose from pre-built ones.

Exercise Library: A comprehensive library of exercises with detailed instructions and visuals.

Progress Tracking: Track workout history, achievements, and set fitness goals.
Social Integration: Share workout achievements on social media platforms.
Reminders and Notifications: Set reminders for upcoming workouts and receive motivational notifications.


## Project Setup
The project begin with using the structure described in the "Full-Stack Development" module. The   client and server code are segregate.


## Project Guidance
## Planning
## User Stories
Defining the primary purpose of your workout app.
Break down user stories between MVP-required features and stretch goals.

## Example:
MVP: A user,  can sign up, log in, log out, view a list of  workouts, create a new workout, modify/delete  workouts, and view workout details.

Stretch: A user,  can track workout progress over time, share workouts with friends, and receive workout recommendations based on goals.

Explore additional functionalities, such as integrating a workout database or utilizing fitness APIs.
Models and Relationships


![Alt text](<Untitled (1)-1.png>)



Design models based on identified user stories.
Identify relationships between models for the Entity Relationship Diagram (ERD).

## Technologies

## Flask:
Description: Flask is a lightweight and flexible web application framework for Python.
Role in Project: Used as the backend framework to create a RESTful API to handle server-side logic and communicate with the database.

## React:
Description: React is a JavaScript library for building user interfaces, particularly for single-page applications where data can change over time.
Role in Project: Used for building the frontend, allowing for the creation of dynamic and responsive user interfaces.

## Chakra UI:
Description: Chakra UI is a set of accessible and customizable UI components for React applications.
Role in Project: Used for designing and styling the frontend components of the workout app, ensuring a consistent and visually appealing user interface.


## Figma:
Description: Figma is a collaborative design tool used for creating wireframes, prototypes, and UI designs.
Role in Project: Employed for planning and creating wireframes to visualize the layout and design of the workout app's frontend.

## Flask-SQLAlchemy:
Description: Flask extension that simplifies database integration with Flask applications using SQLAlchemy, an SQL toolkit and Object-Relational Mapping (ORM) library.
Role in Project: Facilitates interaction between the Flask application and the relational database, managing models and relationships.

## Thunder Client:
Description: Thunder Client is a REST API client extension for Visual Studio Code, simplifying the testing of API endpoints.
Role in Project: Potentially used for testing and interacting with the Flask API during development.

## React Router:
Description: React Router is a standard library for routing in React applications, enabling navigation between different views or components.
Role in Project: Used to create and manage different client-side routes, enhancing user navigation within the React frontend.

## Render:
Description: Render is a platform for deploying and scaling web applications and static websites.
Role in Project: Used for deploying both the Flask backend and the React frontend, making the workout app accessible online.

## Virtualenv:
Description: Virtualenv is a tool for creating isolated Python environments, ensuring dependencies for different projects don't interfere with each other.
Role in Project: Used for managing Python dependencies and creating a virtual environment for the Flask application.



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

## Collaborators
Miriam Maina ("https://github.com/wahitum")
Edwin Rukuno ("https://github.com/erukuno")
Nelson Murithi ("https://github.com/NellieMK65")
Caroline Akinyi Opiyo ("https://github.com/Budabos")
Joy Cheruto ("https://github.com/cheruto23")
https://github.com/mbari60


## Deploying
Deploy a Flask App - Render
Deploy a React App Static Site - Render


## Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


























 

# Full Stack Trivia API Final Project

## Table of Contents
- [About the project](#About-the-project)  
- [Prerequisites and Installation](#Prerequisites-and-Installation)
  - [Frontend Dependencies](#Frontend-Dependencies)
  - [Backend Dependencies](#Backend-Dependencies)
- [Database Setup](#Database-Setup)
- [Running the server](#Running-the-server)
- [Running Frontend in Dev Mode](#Running-Frontend-in-Dev-Mode)
- [Testing](#Testing)
- [API Reference](#API-Reference)
  - [Error Handling](#Error-Handling)
  - [Endpoints](#Endpoints)
    


## About the project 

This project is about trivia game where the users test their general information by answering the questions, with the ability to create and delete questions. The task of the project is to build and test an API that implement the following:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

## Getting Started

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)


## Prerequisites and Installation

### Frontend Dependencies

**Installing Node and NPM**

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

**Installing project dependencies**

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
$ npm install
```
>_tip_: **npm i** is shorthand for **npm install**

### Backend Dependencies

**Python 3.7**

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).
    
**Virtual Enviornment**

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```bash
$ cd YOUR_PROJECT_DIRECTORY_PATH/
$ virtualenv --no-site-packages env
$ source env/bin/activate
```
**PIP Dependencies**

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
$ pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup

With Postgres running, restore a database using the `trivia.psql` file provided. From the `backend` folder in terminal run:
```bash
$ psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Running Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
$ npm start
```

## Testing
To run the tests, run
```
$ dropdb trivia_test 
$ createdb trivia_test
$ psql trivia_test < trivia.psql
$ python test_flaskr.py
```

## API Reference

### Getting Started

- Base URL: presently this application is only be able to run locally and not hosted as a base URL.
   The backend application is hosted at the default `http://127.0.0.1:5000/`   
- Authentication: This version of the app does not require authentication or API keys.

### Error Handling

Errors are returned as JSON in the following format:
```
{
    "success": False,
    "error": 422,
    "message": "unprocessable"
}
```
The API will return three types of errors when unsuccessful request occur:

- 400: bad request
- 404: resource not found
- 422: unprocessable

### Endpoints 

#### GET `/categories`

- General: 
  - Returns a list of categories, success value.
- Sample: `http://127.0.0.1:5000/categories`

    ```
    {
      "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
      }, 
      "success": true
    }
    ```
#### GET `/questions`

- General: 
  - Returns a list of questions, categories, success value, number of questions.
  - Results are paginated in group of 10.
- Sample: `curl http://127.0.0.1:5000/questions`
- Sample with specifying page number : `curl http://127.0.0.1:5000/questions?page=1`

    ```
    {
      "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
      }, 
      "questions": [
        {
          "answer": "Apollo 13", 
          "category": 5, 
          "difficulty": 4, 
          "id": 2, 
          "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
          "answer": "Tom Cruise", 
          "category": 5, 
          "difficulty": 4, 
          "id": 4, 
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
          "answer": "Maya Angelou", 
          "category": 4, 
          "difficulty": 2, 
          "id": 5, 
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
          "answer": "Edward Scissorhands", 
          "category": 5, 
          "difficulty": 3, 
          "id": 6, 
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
          "answer": "Muhammad Ali", 
          "category": 4, 
          "difficulty": 1, 
          "id": 9, 
          "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
          "answer": "Brazil", 
          "category": 6, 
          "difficulty": 3, 
          "id": 10, 
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        }, 
        {
          "answer": "Uruguay", 
          "category": 6, 
          "difficulty": 4, 
          "id": 11, 
          "question": "Which country won the first ever soccer World Cup in 1930?"
        }, 
        {
          "answer": "George Washington Carver", 
          "category": 4, 
          "difficulty": 2, 
          "id": 12, 
          "question": "Who invented Peanut Butter?"
        }, 
        {
          "answer": "Lake Victoria", 
          "category": 3, 
          "difficulty": 2, 
          "id": 13, 
          "question": "What is the largest lake in Africa?"
        }, 
        {
          "answer": "The Palace of Versailles", 
          "category": 3, 
          "difficulty": 3, 
          "id": 14, 
          "question": "In which royal palace would you find the Hall of Mirrors?"
        }
      ], 
      "success": true, 
      "total_questions": 19
     }

    ```
#### DELETE `/questions/<int:id>`

- General: 
  - Delete the question with the given ID if exist.
  - Returns the deleted question ID and success value.
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/14`

    ```
    {
      "question": 14, 
      "success": true
    }
    ```
#### POST `/questions`

This endpoint for creating a question or returning search results.

**if `searchTerm` is EXISTS in the request --> `SEARCH FOR QUESTIONS`**

- General: 
  - Search for questions that include the given search term.
  - Returns the list of matching questions, the search term, number of questions and success value.
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "name"}'`

    ```
    {
      "questions": [
        {
          "answer": "Muhammad Ali", 
          "category": 4, 
          "difficulty": 1, 
          "id": 9, 
          "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
          "answer": "Brazil", 
          "category": 6, 
          "difficulty": 3, 
          "id": 10, 
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        }
      ], 
      "searchTerm": "name", 
      "success": true, 
      "total_questions": 2
    }

    ```
    
**if `searchTerm` DO NOT EXISTS in the request --> `CREATE QUESTION`**

- General: 
  - create new question by submiting the question and answer text, category, and difficulty score.
  - Returns question ID, lsit of questions, number of questions and success value.
- Sample: `curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/questions -d '{"question": "When Michael Jordan played for the Chicago Bulls, how many NBA Championships did he win?", "answer": "Six", "difficulty": "3", "category": "6"}'`

    ```
    {
      "created_question": 24, 
      "questions": [
        {
          "answer": "Apollo 13", 
          "category": 5, 
          "difficulty": 4, 
          "id": 2, 
          "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
          "answer": "Tom Cruise", 
          "category": 5, 
          "difficulty": 4, 
          "id": 4, 
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
          "answer": "Maya Angelou", 
          "category": 4, 
          "difficulty": 2, 
          "id": 5, 
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
          "answer": "Edward Scissorhands", 
          "category": 5, 
          "difficulty": 3, 
          "id": 6, 
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
          "answer": "Muhammad Ali", 
          "category": 4, 
          "difficulty": 1, 
          "id": 9, 
          "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
          "answer": "Brazil", 
          "category": 6, 
          "difficulty": 3, 
          "id": 10, 
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        }, 
        {
          "answer": "Uruguay", 
          "category": 6, 
          "difficulty": 4, 
          "id": 11, 
          "question": "Which country won the first ever soccer World Cup in 1930?"
        }, 
        {
          "answer": "George Washington Carver", 
          "category": 4, 
          "difficulty": 2, 
          "id": 12, 
          "question": "Who invented Peanut Butter?"
        }, 
        {
          "answer": "Lake Victoria", 
          "category": 3, 
          "difficulty": 2, 
          "id": 13, 
          "question": "What is the largest lake in Africa?"
        }, 
        {
          "answer": "Agra", 
          "category": 3, 
          "difficulty": 2, 
          "id": 15, 
          "question": "The Taj Mahal is located in which Indian city?"
        }
      ], 
      "success": true, 
      "total_questions": 19
    }
    ```

#### GET `/categories/<int:id>/questions`

- General:
  - Returns list of questions by category ID, current category, number of total questions and success value.
  - Results are paginated no more than group of 10 per page.
- Sample: `curl http://127.0.0.1:5000/categories/1/questions`

    ```
    {
      "current_category": "Science", 
      "questions": [
        {
          "answer": "The Liver", 
          "category": 1, 
          "difficulty": 4, 
          "id": 20, 
          "question": "What is the heaviest organ in the human body?"
        }, 
        {
          "answer": "Alexander Fleming", 
          "category": 1, 
          "difficulty": 3, 
          "id": 21, 
          "question": "Who discovered penicillin?"
        }, 
        {
          "answer": "Blood", 
          "category": 1, 
          "difficulty": 4, 
          "id": 22, 
          "question": "Hematology is a branch of medicine involving the study of what?"
        }
      ], 
      "success": true, 
      "total_questions": 19
    }
    ```
#### POST `/quizzes`

- General:
  - start the quiz app
  - Returns a random question in specific category or in all categories and success value.
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [13], "quiz_category": {"type": "Geography", "id": "3"}}'`

    ```
    {
      "question": {
        "answer": "Lake Victoria", 
        "category": 3, 
        "difficulty": 2, 
        "id": 13, 
        "question": "What is the largest lake in Africa?"
      }, 
      "success": true
    }
    ```

## Author

The API was built `__init__` and tested `test_flaskr.py` by Aya Khashoggi 
The rest of the app was written by [Udacity](https://www.udacity.com) as an API final project for [Full Stack Web Developer Nanodgree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044)

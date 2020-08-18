# Full Stack Trivia API Final Project

## Table of Contents
- [About the project](#About-the-project)  
- [Getting Started](#Getting-Started) 
  - [Prerequisites](#Prerequisites)
  - [Installation](#Installation)
  - [Database Setup](#Database-Setup)
    


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

## Prerequisites

 - <a href="https://www.python.org/downloads/" target="_blank">`Python3`</a>
 - <a href="https://pip.pypa.io/en/stable/installing/" target="_blank">`pip`</a>
 - <a href="https://nodejs.org/en/download/package-manager/" target="_blank">`node`</a>
 - [`npm`](#Installation)

## Installation

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

## Running Your Frontend in Dev Mode

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














____
There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

### Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

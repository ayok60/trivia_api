# Full Stack Trivia API Final Project

## Table of Contents
- [About the project](#About-the-project)  
- [Getting Started](#Getting-Started) 
  - [Prerequisites](#Prerequisites)
  - [Installation](#Installation)
    


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

### Prerequisites

 - <a href="https://www.python.org/downloads/" target="_blank">`Python3`</a>
 - <a href="https://pip.pypa.io/en/stable/installing/" target="_blank">`pip`</a>
 - <a href="https://nodejs.org/en/download/package-manager/" target="_blank">`node`</a>
 - [`npm`](#Installation)

### Installation

#### Frontend Dependencies

#### Backend Dependencies

- **Python 3.7**

    Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).
    
- **Virtual Enviornment**

    We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
    
- **PIP Dependencies**

  Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

    ```bash
    pip install -r requirements.txt
    ```

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

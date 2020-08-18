import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in selection]
  current_questions = questions[start:end]

  return current_questions


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @DONE: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app, resources={r"/api/*" : {'origins': '*'}})

  '''
  @DONE: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
    response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
    return response

  '''
  @DONE: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  # curl http://127.0.0.1:5000/categories
  @app.route('/categories')
  def retrieve_categories():
    categories = Category.query.all()
    categories_dict = {category.id: category.type for category in categories}
   
    if not categories_dict:
        abort(404)

    return jsonify({
        'success': True,
        'categories': categories_dict
    }),200
  '''
  @DONE: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  # curl http://127.0.0.1:5000/questions 
  # curl http://127.0.0.1:5000/questions?page=1
  @app.route('/questions')
  def retrieve_questions():

    categories = Category.query.all()
    questions = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, questions)
    

    if (len(current_questions) == 0):
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(questions),
      'categories': {category.id: category.type for category in categories}
    }),200
  '''
  @DONE: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  # curl -X DELETE http://127.0.0.1:5000/questions/question_id
  @app.route('/questions/<int:id>', methods=['DELETE'])
  def delete_question(id):

    question = Question.query.filter(id == Question.id).one_or_none()

    if question is None:
      abort(404)

    question.delete() 

    return jsonify({
      'success': True,
      'question': question.id,
    }),200
      


  '''
  @DONE: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  # curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/questions -d '{"question": "My Name?", "answer": "Aya", "difficulty": "3", "category": "2"}'
  '''
  @DONE: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  # curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "which"}'
  @app.route('/questions', methods=['POST'])
  def create_question():
    
    body = request.get_json()

    if body.get('searchTerm'):

      search = body.get('searchTerm')

      questions = Question.query.filter(Question.question.ilike(f'%{search}%')).all()
      current_questions = paginate_questions(request, questions)

      if not questions:
        abort(404)

      return jsonify({
          'success': True,
          'searchTerm': search,
          'questions': current_questions,
          'total_questions': len(questions)
      }),200

    else:
      
      created_question = Question(
        question = body.get('question'),
        answer = body.get('answer'),
        category = body.get('category'),
        difficulty = body.get('difficulty')
      )

      if not (created_question.question and created_question.answer and created_question.category and created_question.difficulty):
        abort(422)

      try: 
        created_question.insert()
        current_questions = paginate_questions(request, Question.query.order_by(Question.id).all())

        return jsonify({
          'success': True,
          'created_question': created_question.id,
          'questions': current_questions,
          'total_questions': len(Question.query.all()),
        }),201

      except:
        abort(422)

  '''
  @DONE: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  # curl http://127.0.0.1:5000/categories/1/questions
  @app.route('/categories/<int:id>/questions')
  def get_questions_by_category(id):

    category = Category.query.get(id)

    if category is None:
      abort(404)


    questions = Question.query.filter_by(category = category.id).all()
    current_questions = paginate_questions(request, questions)    

    return jsonify({
        'success': True,
        'questions': current_questions,
        'total_questions': len(Question.query.all()),
        'current_category': category.type
    }),200

  '''
  @DONE: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  # curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20, 21], "quiz_category": {"type": "Science", "id": "1"}}'
  @app.route('/quizzes', methods=['POST'])
  def get_quizz_questions():
    body = request.get_json()
    previous_questions = body.get('previous_questions')
    category = body.get('quiz_category')

    if previous_questions is None or category is None:
      abort(400)

    if category['id'] == 0:
      questions = Question.query.all()
    else:
      questions = Question.query.filter_by(category = category['id']).all()
      
    total_questions = len(questions)

    while(len(previous_questions) < len(questions)):
      filtered_questions = [question for question in questions if not question.id in previous_questions]

      if filtered_questions:
        random_question = random.choice(filtered_questions)
      else:
        random_question = []
        
      return jsonify({
        'success': True,
        'question': random_question.format()
    }) 

    print('end')
    return jsonify({
      'success': True
    })

        
  '''
  @DONE: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'resource not found'
    }),404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': 'unprocessable'
    }),422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': 'bad request'
    }),400

  @app.errorhandler(500)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 500,
      'message': 'internal server error '
    }),400
  
  return app

    
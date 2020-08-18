import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app , QUESTIONS_PER_PAGE
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    """
    Retrieve categories TEST
    """
    def test_retrieve_categories(self):
        print(f"\nRetrieve Categories Test:")
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200) 
        self.assertEqual(data['success'],True)
        self.assertTrue(data['categories'])
        print(f" --> [Success: {data['success']}] .... Done")
        

    """
    Retrieve Paginated Questions TEST
    """
    def test_retrieve_paginated_questions(self):
        print(f"\nRetrieve Paginated Questions Test:")
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertEqual(len(data['questions']), QUESTIONS_PER_PAGE) # check Paginated with 10
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])
        print(f" --> [Success: {data['success']}] .... Done")


    def test_404_sent_requesting_beyond_vaild_page(self):
        print(f"\nRequest Beyond Vaild Page Test:")
        res = self.client().get('/questions?page=100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        print(f" --> {data['error']} {data['message']} error ... Done")

    
    """
    Delete Question TEST
    """ 

    def test_delete_question(self):
        print(f"\nDelete Question Test:")
        test_data = {
            'question': 'Test question',
            'answer': 'Test answer',
            'difficulty': 1,
            'category': 1,
        }

        question = Question(
            question=test_data['question'], 
            answer=test_data['answer'],
            category=test_data['category'], 
            difficulty=test_data['difficulty']
        )

        question.insert()

        
        num_of_questions_before = len(Question.query.all())
        
        res = self.client().delete(f'/questions/{question.id}')
        data = json.loads(res.data)

        num_of_questions_after = len(Question.query.all())

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertFalse(num_of_questions_before == num_of_questions_after) # check the change in total num of questions 
        self.assertIsNone(Question.query.get(data['question'])) # check if the question has been deleted 
        print(f" --> [Success: {data['success']}] .... Done")


    def test_404_delete_question(self):
        print(f"\nDelete a Question that Does Not Exist Test:")
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        print(f" --> {data['error']} {data['message']} error ... Done")


    """
    Create Question TEST
    """ 
    def test_create_question(self):
        print(f"\nCreate Question Test:")
        test_data = {
            'question': 'Test question',
            'answer': 'Test answer',
            'difficulty': 1,
            'category': 1,
        }

        num_of_questions_before = len(Question.query.all())

        res = self.client().post('/questions', json = test_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,201)
        self.assertEqual(data['success'], True) 
        self.assertEqual(len(data['questions']), QUESTIONS_PER_PAGE) # check pagaineted
        self.assertEqual(data['total_questions'] - num_of_questions_before, 1) # check only one quesion is created
        self.assertIsNotNone(Question.query.get(data['created_question'])) # check if question created 
        print(f" --> [Success: {data['success']}] .... Done")


    def test_422_create_question(self):
        print(f"\nCreate Question Unprocessed Test:")
        test_data = {
            'question': 'Test question',
            'answer': 'Test answer',
        }

        res = self.client().post('/questions', json = test_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
        print(f" --> {data['error']} {data['message']} error ... Done")


    """
    Search Questions TEST
    """     
    def test_search_questions(self):
        print(f"\nSearch Questions Test:")
        res = self.client().post('/questions', json = {'searchTerm': 'name'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertLessEqual(len(data['questions']), QUESTIONS_PER_PAGE) # check pagaineted
        self.assertTrue(data['total_questions'])
        print(f" --> [Success: {data['success']}] .... Done")



    def test_404_search_questions(self):
        print(f"\nUnvalid Search Question Test:")
        res = self.client().post('/questions', json = {'searchTerm': 'NO_QUESTION'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        print(f" --> {data['error']} {data['message']} error ... Done")


    """
    Get Questions by Category TEST
    """      
    def test_get_questions_by_category(self):
        print(f"\nGet Questions by Category Test:")
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertLessEqual(len(data['questions']), QUESTIONS_PER_PAGE) # check pagaineted
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])
        print(f" --> [Success: {data['success']}] .... Done")


    
    def test_404_get_questions_by_category(self):
        print(f"\nRequest Beyond Vaild category Test:")
        res = self.client().get('/categories/1000/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        print(f" --> {data['error']} {data['message']} error ... Done")



    """
    Get quizz Questions TEST
    """ 
    def test_get_quizz_questions(self):
        print(f"\nGet quizz Questions Test:")
        test_data = {
            'previous_questions': [],
            'quiz_category': {
                'type': 'Art', 
                'id': 2
            }
        }

        res = self.client().post('/quizzes', json = test_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["question"])
        print(f" --> [Success: {data['success']}] .... Done")


    
    def test_get_quizz_questions(self):
        print(f"\nGet quizz Questions unvalid request Test:")
        res = self.client().post('/quizzes', json = {})
        data = json.loads(res.data)

        self.assertEqual(res.status_code,400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')
        print(f" --> {data['error']} {data['message']} error ... Done")
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
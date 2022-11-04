import os
import unittest
import json
from api import create_app
from database.models import setup_db, Articles
from flask_sqlalchemy import SQLAlchemy

database_name = 'postgres_test'
database_path =  'postgresql://{}:{}@{}/{}'.format('postgres','admin','localhost:5432', database_name)

class First_mobile_app_test(unittest.TestCase):
    
    """this class implement mobile-app Test"""
      
    def setup(self):
        """ Define test variable and intialize app"""
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_name = database_name
        self.database_path = database_path
        setup_db(self.app, self.database_path)
        

        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
        
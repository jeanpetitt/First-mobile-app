import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
import json


database_name = 'postgres'
database_path = 'postgresql://{}:{}@{}/{}'.format('postgres','admin','localhost:5432', database_name)

db = SQLAlchemy()
"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    
class Article(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __init__(self, name, descripton):
        self.name = name
        self.description = descripton
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
    
        
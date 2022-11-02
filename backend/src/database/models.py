import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import Column, String, Integer, Text
import json


database_name = 'postgres'
database_path = 'postgresql://{}:{}@{}/{}'.format('postgres','admin','localhost:5432', database_name)

db = SQLAlchemy()
ma = Marshmallow()
"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    ma.app = app
    db.init_app(app)
    db.create_all()
    
class Articles(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(Text)

    def __init__(self, title, descripton):
        self.title = title
        self.description = descripton
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }
    
class ArticleSerialisation(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')
        
article_schema = ArticleSerialisation()
article_schemas = ArticleSerialisation(many=True)
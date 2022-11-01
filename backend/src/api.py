from crypt import methods
from flask import Flask, jsonify, request
from flask_cors import CORS
from database.models import setup_db

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    #headers cors
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,POST,PATCH,DELETE,OPTION"
        )
        return response

    @app.route('/', methods=['GET'])
    def get_article():
        return jsonify({
            'title':'babouche',
            'description': 'it is not strong article'
        })
        
    return app
    

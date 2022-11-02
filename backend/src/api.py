from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from database.models import setup_db, Articles, db

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

    # obtenir la liste des aricles
    @app.route('/articles', methods=['GET'])
    def get_article():
        list_articles = Articles.query.all()
        
        articles = [art.format() for art in list_articles]
        
        return jsonify({
            'succes': True,
            'articles': articles,
            'total_article': len(list_articles)
        })
    
    # ajouter un nouvelle article  
    @app.route('/articles', methods=['POST'])
    def add_new_article():
        body = request.get_json()
        new_title = body.get('title', None)
        new_description = body.get('description', None)
        
        try:  
            article = Articles(new_title, new_description)
            article.insert()
            articles = [art.format() for art in Articles.query.all()]
        except:
            abort(422)
        
        return jsonify({
            'success': True,
            'created_id': article.id,
            'articles': articles,
            'total_article': len(Articles.query.all())
        })
        
        
        
    return app
    

from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from database.models import setup_db, Articles, db, article_schema, articles_schema

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
        
        # articles = [art.format() for art in list_articles]
        articles = articles_schema.dump(list_articles)
        
        # return jsonify({
        #     'succes': True,
        #     'articles': articles,
        #     'total_article': len(list_articles)
        # })
        return jsonify(articles)
    
    # ajouter un nouvelle article  
    @app.route('/articles/add', methods=['POST'])
    def add_new_article():
        body = request.get_json()
        new_title = body.get('title', None)
        new_description = body.get('description', None)
        
        try:  
            article = Articles(new_title, new_description)
            article.insert()
            articles = [art.format() for art in Articles.query.all()]
            
        #     return jsonify({
        #     'success': True,
        #     'created_id': article.id,
        #     'articles': articles,
        #     'total_article': len(Articles.query.all())
        # })
        
            return article_schema.jsonify(article)
            
        except:
            abort(422)
        
        
    
    # get detail of articles
    @app.route('/articles/<int:article_id>')
    def get_article_detail(article_id):
        try:
            
            article = Articles.query.get(article_id)
            if article is None:
                abort(404)
                
            return article_schema.jsonify(article)
        except:
            abort(404)
        
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
        "success": False,
        "error": 404,
        "message": "ressource Not found"
        }), 404
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad request"
        }), 400
        
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
        }), 422
    
    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        })
        
    return app
    

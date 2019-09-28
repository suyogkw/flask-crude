"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify
from learnflask import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/add/<entity_type>',methods=['POST'])
def insert_entity(entity_type):
    # entity to database table
    entity = request.json
    databasehelper.add(entity_type,entity)
    return jsonify(request.json)
    

@app.route('/update/<entity_type>',methods=['POST'])
def update_entity(entity_type):
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/getall/<entity_type>',methods=['GET'])
def get_entity(entity_type):
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/getquerydata/<query>',methods=['GET'])
def get_query(query):
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

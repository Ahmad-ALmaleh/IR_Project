from flask import Blueprint, render_template, request, jsonify
from app.services.process_text import process_text
from app.services.search_antique import search_engine_antique
from app.services.search_lotte import search_engine_lotte
main = Blueprint('main', __name__)

@main.route('/search')
def index():
    return render_template('index.html')

@main.route('/process_query', methods=['POST'])
def process_query():
    query = request.form.get('query')
    category = request.form.get('category')
    clean_query=process_text(query)
    
    if category == 'lotte':
        result = search_engine_lotte.search_query(clean_query)
        # print(result)
    elif category == 'antique':
        result =  result = search_engine_antique.search_query(clean_query)
        # print(result)
    else:
       result = "Invalid category selected"

    return render_template('result.html', result=result)
@main.route('/execute_function', methods=['POST'])
def execute_function():
    document_id = request.json.get('documentId')
    result_data = "Your result data here"
    # قم بتمرير البيانات إلى القالب لعرضها
    return render_template('document.html', result_data=result_data)
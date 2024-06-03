from flask import Blueprint, request, jsonify, render_template
import app.services.preprocessing.file_processing as fp
import tqdm
import os
from context.shared_objects import searcher
from context.shared_objects import clustering
from services.preprocessing.data_preprocessing import process_text
search = Blueprint('search', __name__)


@search.route('/search_query', methods=['POST'])
def search_query():
    query=request.form['query']
    
    query =process_text(query)
    
    
    
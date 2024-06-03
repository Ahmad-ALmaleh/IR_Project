import os
import json
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict



class SearchEngine:
    def __init__(self, data_directory, index_filepath):
        self.data_directory = data_directory
        self.index_filepath = index_filepath
        self.documents, self.ids, self.file_ids = self.read_data()
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)
        self.inverted_index = self.load_compressed_index()

    def read_data(self):
        documents = []
        ids = []
        file_ids = []

        for filename in os.listdir(self.data_directory):
            if filename.endswith('.json'):
                file_path = os.path.join(self.data_directory, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        for line in file:
                            try:
                                data = json.loads(line)
                                documents.append(data['text'])
                                ids.append(data['id'])
                                file_ids.append(filename)
                            except json.JSONDecodeError as e:
                                print(f"Error decoding JSON from line in file {file_path}: {e}")
                except FileNotFoundError:
                    print(f"File {file_path} not found.")
                except Exception as e:
                    print(f"An unexpected error occurred while processing file {file_path}: {e}")
        
        return documents, ids, file_ids

    def load_compressed_index(self):
        with open(self.index_filepath, 'rb') as f:
            return joblib.load(f)
    
    def search_query(self, query):
        query_vec = self.vectorizer.transform([query])

        scores = defaultdict(float)
        
        for idx, value in zip(query_vec.indices, query_vec.data):
            term = self.vectorizer.get_feature_names_out()[idx]
            if term in self.inverted_index:
                doc_ids, file_ids, term_scores = self.inverted_index[term]
                for doc_id, file_id, score in zip(doc_ids, file_ids, term_scores):
                    scores[(doc_id, file_id)] += value * score

        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        return sorted_scores

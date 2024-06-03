from app.services.search import SearchEngine
from app.services.process_text import process_text



# model_filepath_antique = r'C:\Users\Khaldoun Alhalabi\Desktop\New folder\project\antique_tfidf_model.joblib'

# # إنشاء محرك البحث
# search_engine_antique = SearchEngine(model_filepath_antique)

data_directory_antique = r'C:\Users\Khaldoun Alhalabi\Desktop\antique_proc'
index_filepath_antique = r'C:\Users\Khaldoun Alhalabi\Desktop\New folder\project\antique_inverted_index.joblib'
search_engine_antique = SearchEngine(data_directory_antique,index_filepath_antique)

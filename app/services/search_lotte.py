from app.services.search import SearchEngine
from app.services.process_text import process_text



# model_filepath_lotte = r'C:\Users\Khaldoun Alhalabi\Desktop\New folder\project\lotte_tfidf_model.joblib'

# # إنشاء محرك البحث
# search_engine_lotte = SearchEngine(model_filepath_lotte)


data_directory_lotte = r'C:\Users\Khaldoun Alhalabi\Desktop\lotte_proc'
index_filepath_lotte = r'C:\Users\Khaldoun Alhalabi\Desktop\New folder\project\lotte_inverted_index.joblib'
search_engine_lotte = SearchEngine(data_directory_lotte,index_filepath_lotte)

import re
import pandas as pd
import string
from  tqdm import tqdm
from dateutil import parser
from nltk.corpus import stopwords
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from dateutil import parser
from dateutil.parser import ParserError
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')
def remove_punctuation(tokens):
    all_punctuation = string.punctuation
    punctuation_regex = re.compile(f"[{re.escape(all_punctuation)}]")
    # إزالة علامات الترقيم والأسهم من كل توكن
    cleaned_tokens = [
        punctuation_regex.sub('', token) for token in tokens
    ]
    # إزالة التوكنات الفارغة التي نتجت عن إزالة جميع علامات الترقيم والأسهم
    cleaned_tokens = [token for token in cleaned_tokens if token]
    return cleaned_tokens
def convert_to_lowercase(tokens):

    lowercase_tokens = [token.lower() for token in tokens]
    return lowercase_tokens
def process_dates_brackets(tokens):

    processed_tokens = []

    for token in tokens:
        # إزالة الأقواس
        token = re.sub(r'[()]', '', token)
        
        # الاحتفاظ بالأرقام بغض النظر عن طولها
        if re.match(r'^\d+$', token):
            processed_tokens.append(token)
        else:
            # محاولة تحويل التوكن إلى تاريخ وتنسيقه
            try:
                parsed_date = parser.parse(token, fuzzy=False)
                # تحويل التاريخ إلى تنسيق 'YYYY-MM-DD'
                standardized_date = parsed_date.strftime('%Y-%m-%d')
                processed_tokens.append(standardized_date)
            except (ParserError, ValueError, OverflowError):
                # إذا لم يكن تواريخًا، قم بإضافة الكلمة كما هي
                processed_tokens.append(token)
    return processed_tokens
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return filtered_tokens
def stem_tokens(tokens):
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens
def process_text(text):
    tokens = word_tokenize(text)
    tokens=convert_to_lowercase(tokens)
    tokens=remove_punctuation(tokens)
    tokens=process_dates_brackets(tokens)
    tokens = remove_stopwords(tokens)
    tokens=stem_tokens(tokens)
    return ' '.join(tokens)


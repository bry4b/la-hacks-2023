import nltk
nltk.download('punkt')
import OCRtoText as ott
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

stringwithtext = ott.imagetotext('test.png')

def extract_keywords(prompt):
    # Tokenize the prompt into words
    words = word_tokenize(prompt)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if w.lower() not in stop_words]
    
    # Create a string of remaining words
    text = " ".join(words)
    
    # Compute TF-IDF scores for each word
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([text])
    feature_names = tfidf_vectorizer.get_feature_names()
    tfidf_scores = tfidf_matrix.toarray()[0]
    
    # Create a list of (word, score, pos) tuples sorted by score
    keyword_scores = sorted(zip(feature_names, tfidf_scores, nltk.pos_tag(feature_names)), key=lambda x: x[1], reverse=True)
    
    # Filter the keywords to include only nouns, verbs, and adjectives
    keywords = []
    for word, score, pos in keyword_scores:
        if pos[1].startswith('N'):  # nouns
            keywords.append((word, score, 'noun'))
        elif pos[1].startswith('V'):  # verbs
            keywords.append((word, score, 'verb'))
        elif pos[1].startswith('J'):  # adjectives
            keywords.append((word, score, 'adjective'))
        else:
            keywords.append((word, score, 'other'))
    
    return keywords

keywords = extract_keywords(stringwithtext)
print(keywords) 
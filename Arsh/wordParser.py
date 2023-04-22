import nltk
nltk.download('punkt')
nltk.download('stopwords')
#import OCRtoText as ott
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer



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
    feature_names = tfidf_vectorizer.get_feature_names_out()
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


def extract_keywords_plain(prompt):
    # Tokenize the prompt into words
    words = word_tokenize(prompt)
    
    # Remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    words = [w for w in words if w.lower() not in stop_words]
    
    # Identify keywords based on part-of-speech tags
    keywords = []
    for word, pos in nltk.pos_tag(words):
        if pos.startswith('NN'):  # nouns
            keywords.append(word)
        elif pos.startswith('VB'):  # verbs
            keywords.append(word)
        elif pos.startswith('JJ'):  # adjectives
            keywords.append(word)
    
    return keywords

#keywords = extract_keywords_plain(stringwithtext)
#print(keywords) 

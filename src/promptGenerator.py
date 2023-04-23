import spacy
import random
import sys

# Load the spacy model
nlp = spacy.load("en_core_web_sm")

# Define the snippet of text and the list of words
#snippet1 = "The quick brown fox jumps over the lazy dog. Then the dog gets angry at the fox. The dog then tries to eat the fox, but the fox starts to run away. The fox runs far. A fox won't be able to run far."
#words2 = ["cat", "jumps", "lazy", "mad", "elephant"]

def promptGenerator(snippet, words):
    # Create a blank spacy Doc object
    blank_doc = nlp(" ".join(words))

    if snippet is None:
        return " ".join([token.text for token in blank_doc])
    
    doc = nlp(snippet)

    # Find the highest-scoring Token in the original Doc for each Token in the blank Doc
    substitutions = []
    for blank_token in blank_doc:
        best_token = max(doc, key=lambda x: x.similarity(blank_token))
        substitutions.append(best_token)

    # Create a new doc with the substituted tokens
    new_doc = []
    for token in doc:
        if token in substitutions:
            new_doc.append(blank_doc[substitutions.index(token)])
        else:
            new_doc.append(token)

    # Join the Tokens in the new doc into a sentence
    sentence = " ".join([token.text for token in new_doc])
    return sentence

def promptAlt(snippet, words):
    doc = nlp(snippet)

    # Find the highest-scoring Token in the original Doc for each Token in the blank Doc
    substitutions = []
    for word in words:
        blank_token = nlp(word)[0]
        best_token = max(doc, key=lambda x: x.similarity(blank_token))
        substitutions.append(best_token)

    # Generate a sentence by randomly selecting the substitutions and appending their text
    sentence = ""
    num_words = 0
    while num_words < 10 and substitutions:
        selected_token = random.choice(substitutions)
        sentence += " " + selected_token.text
        num_words += 1
        substitutions.remove(selected_token)

    # Remove leading/trailing spaces and punctuation from the generated sentence
    sentence = sentence.strip()
    sentence = sentence.rstrip(".,;:?!")
    return sentence

'''
sentence = promptGenerator(snippet, words)
max_length = 10

words = sentence.split()[:max_length]
truncated_sentence = " ".join(words)

print(truncated_sentence)
'''

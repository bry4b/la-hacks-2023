#import spacy
import openai
import os
import sys
import utils.constants as ct

# Load the spacy model
#nlp = spacy.load("en_core_web_sm")

# Set up the OpenAI API credentials
openai.api_key = ct.OPENAI_API_KEY
#openai.api_key = os.environ[constants.OPENAI_API_KEY]

def promptGenerator(snippet, words, mood):
    if mood != None and snippet != None:
        gpt_request = "There are two texts on a presentation slide. Focus more on the first and less on the second. \"" + \
        words + ".\" \"" + snippet + ".\" " + "A " + mood + " image is also present on the presentation slide. Write me a 20 to 30 " + \
        "word descriptive sentence for a caption to the image that describes the subject matter and it's style"
    elif mood == None and snippet != None:
        gpt_request = "There are two texts on a presentation slide. Focus more on the first and less on the second. \"" + \
        words + ".\" \"" + snippet + ".\" " + "A image is also present on the presentation slide. Write me a 20 to 30 " + \
        "word descriptive sentence for a caption to the image that describes the subject matter and it's style"
    elif snippet == None and mood != None:
        gpt_request = "There are two texts on a presentation slide. Focus more on the first and less on the second. \"" + \
        words + ".\" " + "A " + mood + " image is also present on the presentation slide. Write me a 20 to 30 " + \
        "word descriptive sentence for a caption to the image that describes the subject matter and it's style"
    else: 
        gpt_request = "There are two texts on a presentation slide. Focus more on the first and less on the second. \"" + \
        words + ".\" \"" + ".\" " + "A image is also present on the presentation slide. Write me a 20 to 30 " + \
        "word descriptive sentence for a caption to the image that describes the subject matter and it's style"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gpt_request,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Print the response
    return response.choices[0].text.strip()





    '''
    blank_doc = nlp(words)

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
'''


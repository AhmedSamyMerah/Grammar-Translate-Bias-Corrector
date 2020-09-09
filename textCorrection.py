import spacy
from spacy.tokenizer import Tokenizer

#Load large French model
nlp = spacy.load("fr_core_news_lg")

#Processing method
def gender_corrector(trText):
    
    #Doc for processing original GT translation
    doc = nlp(trText)

    
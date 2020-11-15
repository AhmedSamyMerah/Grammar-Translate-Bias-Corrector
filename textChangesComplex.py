import spacy
import spacy.attrs
import spacy.lang.fr
from spacy.tokenizer import Tokenizer
from spacy.lookups import Lookups

#Load large French model
nlp = spacy.load("fr_core_news_lg")
ennlp = spacy.load("en_core_web_sm")

def sentTagComplex(trText, orText):
    print('complex')
    if("elle" not in trText):
        if("her" not in orText):
            return print(trText)
    
    doc = nlp(trText)
    sents = list(doc.sents)
    ds = sents[0]
    s1 = str(sents[0])
import spacy
from spacy.tokenizer import Tokenizer

#Load large French model
nlp = spacy.load("fr_core_news_lg")

#Processing method
def gender_corrector(trText):
    
    #Doc for processing original GT translation
    doc = nlp(trText)

    #Sentence breakdown
    sents = list(doc.sents)
    ds1 = sents[0]
    ds2 = sents[1]
    s1 = str(sents[0])
    s2 = str(sents[1])
    print(s1, s2)

    #Variables for token storing
    dn =None
    sn =None
    index =None
    hv= None

    if('elle' in s2):
        for n in ds1:
            if(n.pos_ == 'NOUN'):
                if('Gender=Masc' in n.tag_):
                    index=n.i
                    dn = str(n)
                    sn = str(n)

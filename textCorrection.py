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

    #Pronoun check
    if('elle' in s2):
        #Loop to check if a noun is masculine
        for n in ds1:
            if(n.pos_ == 'NOUN'):
                if('Gender=Masc' in n.tag_):
                    #get index of token
                    index=n.i
                    #Stringify token
                    dn = str(n)
                    sn = str(n)

                    if(sn[-2:] == 'on'):
                        sn = sn.replace('on', 'onne')
                        hv = nlp(sn)
                    for v in hv:
                        if(v.has_vector):
                            s1 = s1.replace(dn, sn) 
                    continue
                    
                    if(sn[-2:] == 'in'):
                        sn = sn.replace('in', 'ine')
                        hv = nlp(sn)
                    for v in hv:
                        if(v.has_vector):
                            s1 = s1.replace(dn, sn)
                    continue


    print(s1,s2)
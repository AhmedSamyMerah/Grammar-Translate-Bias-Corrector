import spacy
import spacy.lang.fr
from spacy.tokenizer import Tokenizer
from spacy.lookups import Lookups

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
    #print(s1, s2)

    #Variables for token storing
    dn =None
    sn =None
    index =None
    hv= None

    #Pronoun check
    if('elle' or 'sa' in s2):
        #Loop to check if a noun is masculine
        for n in ds1:
            if(n.pos_ == 'NOUN'):
                if('Gender=Masc' in n.tag_):
                    #get index of token
                    index=n.i
                    #Stringify token
                    dn = str(n)
                    sn = str(n)

                    #Noun endings check for replacement of suffix
                    if(sn[-2:] == 'on'):
                        sn = sn.replace('on', 'onne')
                        hv = nlp(sn)
                        #Checks if replacement is valid by looking at Vocab
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

                    if(sn[-1:] == 'e'):
                        sn = sn.replace('e', 'esse')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue
                
                    if(sn[-2:] == 'er'):
                        sn = sn.replace('er', 'ère')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue
                    
                    if(sn[-4:] == 'teur'):
                        sn = sn.replace('teur', 'trice')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue
                
                    if(sn[-3:] == 'eur'):
                        sn = sn.replace('eur', 'euse')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-3:] == 'ien'):
                        sn = sn.replace('ien', 'ienne')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                #Plural endings
                    if(sn[-3:] == 'ons'):
                        sn = sn.replace('ons', 'onnes')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-3:] == 'ins'):
                        sn = sn.replace('ins', 'ines')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-2:] == 'es'):
                        sn = sn.replace('es', 'esses')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-3:] == 'ers'):
                        sn = sn.replace('ers', 'ères')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue
                    
                    if(sn[-5:] == 'teurs'):
                        sn = sn.replace('teurs', 'trices')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue
                
                    if(sn[-4:] == 'eurs'):
                        sn = sn.replace('eurs', 'euses')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-4:] == 'iens'):
                        sn = sn.replace('iens', 'iennes')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

    #print(s1,s2)
    
    #New sentence after changes if occured
    ns = s1 + ' ' + s2
    
    #Determiners and Articles fix
    
    #Tokenization of new sentence
    nounCorrectedDoc = nlp(ns)
    
    #new sentence breakdown
    sents = list(nounCorrectedDoc.sents)
    ds1 = sents[0]
    ds2 = sents[1]
    s1 = str(sents[0])
    s2 = str(sents[1])
    

    #checks gender of noun
    for n in ds1:
        if('NOUN' and 'Gender=Fem' in n.tag_):
            #Replacement of possessive Determinents
            for p in ds1:
                index=p.i
                dn = str(p)
                sn = str(p)
                    
                if(sn == 'mon'):
                    sn = sn.replace('mon', 'ma')
                    s1 = s1.replace(dn, sn)

                if(sn == 'ton'):
                    sn = sn.replace('ton', 'ta')
                    s1 = s1.replace(dn, sn)

                if(sn == 'son'):
                    sn = sn.replace('son', 'sa')
                    s1 = s1.replace(dn, sn)

            #Replacement of articles/determinents if noun gender is maculine
            for d in ds1:     
                if('DET' and 'Gender=Masc' in d.tag_):
                    index=d.i
                    dn = str(d)
                    sn = str(d)
                
                if(sn == 'le'):
                    sn = sn.replace('le', 'la')
                    s1 = s1.replace(dn, sn)
                    
                if(sn == 'un'):
                    sn = sn.replace('un', 'une')
                    s1 = s1.replace(dn, sn)
                
                if(sn == 'ce'):
                    sn = sn.replace('ce', 'cette')
                    s1 = s1.replace(dn, sn)
    
            for a in ds1:
                if('ADJ' and 'Gender=Masc' in a.tag_):
                    #Replacement of singular adjective  
                    index=a.i
                    dn = str(a)
                    sn = str(a)

                    if(sn[-3:] == 'ien'):
                        sn = sn.replace('ien', 'ienne')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue        

                    if(sn[-3:] == 'eil'):
                        sn = sn.replace('eil', 'eille')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue      

                    if(sn[-3:] == 'eau'):
                        sn = sn.replace('eau', 'elle')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue 

                    if(sn[-3:] == 'eux'):
                        sn = sn.replace('eux', 'eille')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-2:] == 'ai'):
                        sn = sn.replace('ai', 'aie')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-2:] == 'on'):
                        sn = sn.replace('on', 'onne')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-2:] == 'el'):
                        sn = sn.replace('el', 'elle')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue  

                    if(sn[-2:] == 'ul'):
                        sn = sn.replace('ul', 'ulle')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-2:] == 'et'):
                        sn = sn.replace('et', 'ette')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue 

                    if(sn[-2:] == 'ot'):
                        sn = sn.replace('ot', 'ote')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue   

                    if(sn[-2:] == 'ou'):
                        sn = sn.replace('ou', 'olle')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-2:] == 'er'):
                        sn = sn.replace('er', 'ère')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-1:] == 'c'):
                        sn = sn.replace('c', 'che')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-1:] == 'd'):
                        sn = sn.replace('d', 'de')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-1:] == 't'):
                        sn = sn.replace('t', 'te')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-1:] == 'i'):
                        sn = sn.replace('i', 'ie')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-1:] == 'u'):
                        sn = sn.replace('u', 'ue')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-1:] == 's'):
                        sn = sn.replace('s', 'se')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue 

                    if(sn[-1:] == 'x'):
                        sn = sn.replace('x', 'se')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue

                    if(sn[-1:] == 'f'):
                        sn = sn.replace('f', 've')
                        hv = nlp(sn)
                        for v in hv:
                            if(v.has_vector):
                                s1 = s1.replace(dn, sn)
                        continue


    print(s1 + ' ' + s2)

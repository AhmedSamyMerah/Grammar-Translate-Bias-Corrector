import spacy
import spacy.attrs
import spacy.lang.fr
from spacy.tokenizer import Tokenizer
from spacy.lookups import Lookups

#Load large French model
nlp = spacy.load("fr_core_news_lg")
ennlp = spacy.load("en_core_web_sm")

#Implementation of using the decision tree built by weka
#We use a model to indentify the category of the sentence and then call correction functions based on those
def sentTagSimInt(trText, orText):
    p_s = ""
    s = ""
    d_s = ""
    a_s = ""

    doc = nlp(trText)
    
    #new
    trSents = list(doc.sents)
    trds2 = trSents[1]
    trS2 = str(trSents[1])

    orSents = list(doc.sents)
    ords2 = orSents[1]
    orS2 = str(orSents[1])

    if("elle" not in trText):
        if("her" not in orText):
            return print(trText)
    
    if("elle" in trS2):
        p_s = "elle"
        #print('wawaweewa')
    
    if("her" in orS2):
        p_s = "her"
        #print("nononeea")

    index=None

    for n in doc:
        if('subj' in n.dep_ and ('NOUN' and 'Gender=Masc' in n.tag_)):
            s = n
            index = n.i
            break
    
    for d in doc[index-1:index] or doc[index-2:index]:
        #print(d.text)
        if('DET' in d.tag_):
            d_s=d
            break
    
    for a in doc[index:index+3] or doc[index-1:index]:
        if('ADJ' in a.tag_):
            a_s = a
            break


    new_s = subjectCorrectiion(s)
    new_d = determinentCorrection(d_s)
    new_a = adjectiveCorrection(a_s)

    sents = list(doc.sents)
    s1 = str(sents[0])
    s2 = str(sents[1])

    ss = str(s)
    sd = str(d_s)
    sa = str(a_s)

    if(ss in s1):
        s1 = s1.replace(ss, new_s)
    if(sd in s1):
        s1 = s1.replace(sd, new_d)
    if(sa in s1):
        s1 = s1.replace(sa, new_a)

    print(s1 + " " + s2)

    # count = doc.count_by(spacy.attrs.IDS['POS'])
    # print(count)

    # for token in doc:
    #     print(token.text, '\t', token.pos_, '\t',token.dep_)

    # for pos, count in count.items():
    #     human_readable_tag = doc.vocab[pos].text
    #     print(human_readable_tag, count)

def subjectCorrectiion(s):
    corrected_s=""

    dn =None
    sn =None
    index =None
    hv= None

    dn = str(s)
    sn = str(s)

                #Noun endings check for replacement of suffix
    if(sn[-2:] == 'on'):
        sn = sn.replace('on', 'onne')
        hv = nlp(sn)
        #Checks if replacement is valid by looking at Vocab
        for v in hv:
            if(v.has_vector):
                corrected_s = sn
        #continue
    
    if(sn[-2:] == 'in'):
        sn = sn.replace('in', 'ine')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_s = sn
        #continue
    
    if(sn[-2:] == 'er'):
        sn = sn.replace('er', 'ère')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_s = sn
        #continue
                
    if(sn[-4:] == 'teur'):
        sn = sn.replace('teur', 'trice')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_s = sn
        #continue
                
    if(sn[-3:] == 'eur'):
        sn = sn.replace('eur', 'euse')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_s = sn
        #continue

    if(sn[-3:] == 'ien'):
        sn = sn.replace('ien', 'ienne')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_s = sn
        #continue

    #print(corrected_s)
    return corrected_s
    

def determinentCorrection(d_s):
    corrected_d_s=""

    dn =None
    sn =None
    index =None
    hv= None

    dn = str(d_s)
    sn = str(d_s)

    if(sn == 'le'):
        sn = sn.replace('le', 'la')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_d_s = sn
        #continue
        
    if(sn == 'un'):
        sn = sn.replace('un', 'une')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_d_s = sn
        #continue
    
    if(sn == 'ce'):
        sn = sn.replace('ce', 'cette')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_d_s = sn
        #continue

    if(sn == 'mon'):
        sn = sn.replace('mon', 'ma')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_d_s = sn
        #continue

    if(sn == 'ton'):
        sn = sn.replace('ton', 'ta')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_d_s = sn
        #continue

    if(sn == 'son'):
        sn = sn.replace('son', 'sa')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_d_s = sn
        #continue

    #print(corrected_d_s)
    if(corrected_d_s == ""):
        return str(d_s)

    return corrected_d_s

def adjectiveCorrection(a_s):
    corrected_a_s=""

    dn =None
    sn =None
    index =None
    hv= None

    dn = str(a_s)
    sn = str(a_s)

    if(sn[-4:] == 'teur'):
        sn = sn.replace('teur', 'trice')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-5:] == 'teurs'):
        sn = sn.replace('teurs', 'trices')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue 
    
    if(sn[-3:] == 'ien'):
        sn = sn.replace('ien', 'ienne')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-4:] == 'iens'):
        sn = sn.replace('iens', 'iennes')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue        

    if(sn[-3:] == 'eil'):
        sn = sn.replace('eil', 'eille')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue      

    if(sn[-3:] == 'eau'):
        sn = sn.replace('eau', 'elle')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue 

    if(sn[-1:] == 'x'):
        sn = sn.replace('x', 'se')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-3:] == 'eux'):
        sn = sn.replace('eux', 'eille')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-2:] == 'ai'):
        sn = sn.replace('ai', 'aie')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-2:] == 'on'):
        sn = sn.replace('on', 'onne')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-2:] == 'el'):
        sn = sn.replace('el', 'elle')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue  

    if(sn[-2:] == 'ul'):
        sn = sn.replace('ul', 'ulle')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-2:] == 'et'):
        sn = sn.replace('et', 'ette')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue 

    if(sn[-2:] == 'ot'):
        sn = sn.replace('ot', 'ote')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue   

    if(sn[-2:] == 'ou'):
        sn = sn.replace('ou', 'olle')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-2:] == 'er'):
        sn = sn.replace('er', 'ère')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-2:] == 'il'):
        sn = sn.replace('il', 'ille')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-2:] == 'it'):
        sn = sn.replace('it', 'ite')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-2:] == 'nt'):
        sn = sn.replace('nt', 'nte')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-1:] == 'c'):
        sn = sn.replace('c', 'che')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue
    
    if(sn[-1:] == 'd'):
        sn = sn.replace('d', 'de')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-1:] == 'é'):
        sn = sn.replace('é', 'ée')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-1:] == 'i'):
        sn = sn.replace('i', 'ie')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-1:] == 'u'):
        sn = sn.replace('u', 'ue')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue

    if(sn[-1:] == 's'):
        sn = sn.replace('s', 'se')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue 

    if(sn[-1:] == 'f'):
        sn = sn.replace('f', 've')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a_s=sn
        #continue
    
    if(corrected_a_s == ""):
        return str(a_s)
    #print(corrected_a_s)
    return corrected_a_s
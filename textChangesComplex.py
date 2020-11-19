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
    
    #attributes of decision tree
    p_s = None
    p_c = None
    s = ""
    c = ""
    d_s = ""
    a_s = ""
    d_c = ""
    a_c = ""
    index = None
    indexc = None

    doc = nlp(trText)
    enDoc = ennlp(orText)

    sents = list(doc.sents)
    enSents = list(enDoc.sents)
    ds2 = sents[1]
    enDs2 = enSents[1]
    parr = []

    # for ep in enDs2:
    #     if('PRON' in ep.tag_):
    #         if("her" == ep.text):
    #             parr.append(ep)
    #             #p_s = parr[0]
    #             continue
    #         elif('her' == ep.text or 'him' == ep.text):
    #             parr.append(ep)
    #             #p_c = parr[1]

    #pronoun check that appends to array
    for p in ds2:
        if('PRON' in p.tag_):
            if("elle" == p.text):
                parr.append(p)
                #p_s = parr[0]
                continue
            elif('il' == p.text or 'lui' == p.text):
                parr.append(p)
                #p_c = parr[1]

    # if(parr[0]):
    #     p_s = parr[0]

    # if(parr[1] is True):
    #     p_c = parr[1]

    print(parr)

    #First element of the array is prnoun of subject and second is pronoun of object
    if(len(parr)>1):
        p_s = parr[0]
        p_c = parr[1]
    elif(len(parr)==1):
        p_s=parr[0]

    #Getting the attributes
    for n in doc:
        if('subj' in n.dep_ and ('NOUN' and 'Gender=Masc' in n.tag_)):
            s = n
            index = n.i
            break

    for d in doc[index-1:index]:
        if('DET' in d.tag_):
            d_s=d
            break

    for a in doc[index:index+3]or doc[index-1:index]:
        if('ADJ' in a.tag_):
            a_s = a
            break

    for nc in doc:
        if(('obj' in nc.dep_ or 'obl' in nc.dep_) and ('NOUN' and 'Gender=Masc' in nc.tag_)):
            c = nc
            indexc = nc.i
            break
    
    if(indexc):
        for d in doc[indexc-3:indexc]:
            if('DET' in d.tag_):
                d_c=d
                break

    if(indexc):
        for a in doc[indexc-3:indexc+2]:
            if('ADJ' in a.tag_):
                a_c = a
                break

    print(p_s)
    print(p_c)
    print(s)
    print(c)
    print(d_s)
    print(d_c)
    print(a_s)
    print(a_c)

    s1 = str(sents[0])

    if('Gender=Fem' in p_s.tag_):
        #print('brih')
        #process s, ds, as
        new_s = subjectObjectCorrectiion(s)
        new_ds = determinentCorrection(d_s)
        new_as = adjectiveCorrection(a_s)
        
        sents = list(doc.sents)
        #s1 = str(sents[0])
        s2 = str(sents[1])

        ss = str(s)
        sd = str(d_s)
        sa = str(a_s)

        if(ss in s1):
            s1 = s1.replace(ss, new_s)
        if(sd in s1):
            s1 = s1.replace(sd, new_ds)
        if(sa in s1):
            s1 = s1.replace(sa, new_as)

        #print(s1 + " " + s2)
    
    if(p_c != None):
        if('Gender=Fem' in p_c.tag_):
            print('nuuu')
            new_c = subjectObjectCorrectiion(c)
            new_dc = determinentCorrection(d_c)
            new_ac = adjectiveCorrection(a_c)
            sents = list(doc.sents)
            #s1 = str(sents[0])
            s2 = str(sents[1])

            ss = str(c)
            sd = str(d_c)
            sa = str(a_c)

            if(ss in s1):
                s1 = s1.replace(ss, new_c)
            if(sd in s1):
                s1 = s1.replace(sd, new_dc)
            if(sa in s1):
                s1 = s1.replace(sa, new_ac)

            #print(s1 + " " + s2)
    print(s1 + " " + s2)

def subjectObjectCorrectiion(s):
    corrected=""

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
                corrected = sn
        #continue
    
    if(sn[-2:] == 'in'):
        sn = sn.replace('in', 'ine')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected = sn
        #continue
    
    if(sn[-2:] == 'er'):
        sn = sn.replace('er', 'ère')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected = sn
        #continue
                
    if(sn[-4:] == 'teur'):
        sn = sn.replace('teur', 'trice')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected = sn
        #continue
                
    if(sn[-3:] == 'eur'):
        sn = sn.replace('eur', 'euse')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected = sn
        #continue

    if(sn[-3:] == 'ien'):
        sn = sn.replace('ien', 'ienne')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected = sn
        #continue

    print(corrected)
    if(corrected == ""):
        return str(s)
    return corrected


def determinentCorrection(d_s):
    corrected_d=""

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
                corrected_d = sn
        #continue
        
    if(sn == 'un'):
        sn = sn.replace('un', 'une')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_d = sn
        #continue
    
    if(sn == 'ce'):
        sn = sn.replace('ce', 'cette')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_d = sn
        #continue

    if(sn == 'mon'):
        sn = sn.replace('mon', 'ma')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_d = sn
        #continue

    if(sn == 'ton'):
        sn = sn.replace('ton', 'ta')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_d = sn
        #continue

    if(sn == 'son'):
        sn = sn.replace('son', 'sa')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_d = sn
        #continue

    print(corrected_d)
    if(corrected_d == ""):
        return str(d_s)

    return corrected_d

def adjectiveCorrection(a_s):
    corrected_a=""

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
                corrected_a=sn
        #continue

    if(sn[-5:] == 'teurs'):
        sn = sn.replace('teurs', 'trices')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue 
    
    if(sn[-3:] == 'ien'):
        sn = sn.replace('ien', 'ienne')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-4:] == 'iens'):
        sn = sn.replace('iens', 'iennes')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue        

    if(sn[-3:] == 'eil'):
        sn = sn.replace('eil', 'eille')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue      

    if(sn[-3:] == 'eau'):
        sn = sn.replace('eau', 'elle')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue 

    if(sn[-1:] == 'x'):
        sn = sn.replace('x', 'se')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-3:] == 'eux'):
        sn = sn.replace('eux', 'eille')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-2:] == 'ai'):
        sn = sn.replace('ai', 'aie')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-2:] == 'on'):
        sn = sn.replace('on', 'onne')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-2:] == 'el'):
        sn = sn.replace('el', 'elle')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue  

    if(sn[-2:] == 'ul'):
        sn = sn.replace('ul', 'ulle')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-2:] == 'et'):
        sn = sn.replace('et', 'ette')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue 

    if(sn[-2:] == 'ot'):
        sn = sn.replace('ot', 'ote')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue   

    if(sn[-2:] == 'ou'):
        sn = sn.replace('ou', 'olle')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-2:] == 'er'):
        sn = sn.replace('er', 'ère')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-2:] == 'il'):
        sn = sn.replace('il', 'ille')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-2:] == 'it'):
        sn = sn.replace('it', 'ite')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-2:] == 'nt'):
        sn = sn.replace('nt', 'nte')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-1:] == 'c'):
        sn = sn.replace('c', 'che')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue
    
    if(sn[-1:] == 'd'):
        sn = sn.replace('d', 'de')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-1:] == 'é'):
        sn = sn.replace('é', 'ée')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-1:] == 'i'):
        sn = sn.replace('i', 'ie')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-1:] == 'u'):
        sn = sn.replace('u', 'ue')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue

    if(sn[-1:] == 's'):
        sn = sn.replace('s', 'se')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue 

    if(sn[-1:] == 'f'):
        sn = sn.replace('f', 've')
        hv = nlp(sn)
        for v in hv:
            if(v.has_vector):
                corrected_a=sn
        #continue
    
    if(corrected_a == ""):
        return str(a_s)
    print(corrected_a)
    return corrected_a
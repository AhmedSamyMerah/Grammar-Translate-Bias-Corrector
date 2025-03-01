from google.cloud import translate
from textCorrection import gender_corrector
from textChangesSimInt import sentTagSimInt
from textChangesComplex import sentTagComplex
import spacy
#import unidecode
#import unicodedata
#import numpy

#nlp = spacy.load("fr_core_news_md")

def translate_text(text="YOUR_TEXT_TO_TRANSLATE", project_id="YOUR_PROJECT_ID"):
    """Translating Text."""
    
    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": "en-US",
            "target_language_code": "fr",
        }
    )

    #Converting the Google object into a string
    trString = str(response.translations)

    #Cleaning the extra characters
    cleanStr = trString[19:-3].lower()
    
    #E accent values to be replaced
    graveE = "\\303\\250"
    aiguE = "\\303\\251"
    circE = "\\303\\252"
    tremaE = "\\303\\253"
    
    #Slash after apostrophe removal
    ap = "\\"

    #A accents
    graveA = "\\303\\240"
    circA = "\\303\\242"

    #U accents
    graveU = "\\303\\271"
    circU = "\\303\\273"
    tremaU = "\\303\\274"

    #I accents
    circI = "\\303\\256"
    tremaI = "\\303\\257"
    
    #O accents
    circO = "\\303\\264"

    #C accents
    cedi = "\\303\\247"

    if(aiguE in cleanStr or graveE in cleanStr or circE in cleanStr or ap in cleanStr or graveA in cleanStr or circA in cleanStr or graveU in cleanStr or circU in cleanStr or tremaU in cleanStr or circI in cleanStr or tremaI in cleanStr or circO in cleanStr or cedi in cleanStr or tremaE in cleanStr):
        # e decoding
        cleanStr = cleanStr.replace(aiguE, aiguE.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        cleanStr = cleanStr.replace(graveE, graveE.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        cleanStr = cleanStr.replace(circE, circE.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        cleanStr = cleanStr.replace(tremaE, tremaE.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        # a decoding
        cleanStr = cleanStr.replace(graveA, graveA.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        cleanStr = cleanStr.replace(circA, circA.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        # u decoding
        cleanStr = cleanStr.replace(graveU, graveU.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        cleanStr = cleanStr.replace(circU, circU.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        cleanStr = cleanStr.replace(tremaU, tremaU.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        # i decoding
        cleanStr = cleanStr.replace(circI, circI.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        cleanStr = cleanStr.replace(tremaI, tremaI.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        # o decoding
        cleanStr = cleanStr.replace(circO, circO.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        cleanStr = cleanStr.replace(cedi, cedi.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
        # apostrophe decoding
        cleanStr = cleanStr.replace(ap, "")

    #print(cleanStr)
    nlp = spacy.load("fr_core_news_lg")
    ennlp = spacy.load("en_core_web_sm")
    
    docFr = nlp(cleanStr)
    num_posFr = docFr.count_by(spacy.attrs.IDS['POS'])
    
    docEn = ennlp(text)
    num_depEn = docEn.count_by(spacy.attrs.IDS['DEP'])
    
    #print(num_posFr)
    #print(num_depEn)

    if(440 in num_depEn):
        if(num_depEn[440]==1):
            sentTagSimInt(cleanStr, text)
    
    if(95 in num_posFr):
        if(num_posFr[95]==1):
            sentTagSimInt(cleanStr, text)
    
    if(440 in num_depEn):
        if(num_depEn[440]>=2):
            sentTagComplex(cleanStr, text)
    
    if(95 in num_posFr):
        if(num_posFr[95]>=2):
            sentTagComplex(cleanStr, text)

    #sends for processing
    #gender_corrector(cleanStr, text)

    # doc = nlp(cleanStr)

    # for token in docFr:
    #     print(token.text, '\t', token.pos_, token.pos, token.dep_, token.dep)
    
    # for token in docEn:
    #     print(token.text, '\t', token.pos_, token.pos, token.dep_, token.dep)

    #Sentence print
    # for sent in doc.sents:
    #     print(sent)

    # Display the translation for each input text provided

    # for translation in response.translations:
    #    print("Translated text: {}".format(translation.translated_text))

# SIMPLE CASES
# translate_text(text="the player was nice. she was cool.", project_id="")
# translate_text(text="this dog is elegant. her style is good.", project_id="")
# translate_text(text="a cousin is very jealous. he holds grudges.", project_id="")
translate_text(text="that boss has many jobs. she works a lot.", project_id="")

#INTERMEDIATE
# translate_text(text="at the conference, the butcher was nervous. her work speaks to me.", project_id="")
# translate_text(text="the actor is Algerian, but the friend is tunisian. her acting skills were amazing.", project_id="")
translate_text(text="this brewer is crazy with the hard headed cousin. she was patient.", project_id="")
# translate_text(text="the driver was out of the city. he had to spend time with family.", project_id="")

#COMPLEX
#translate_text(text="the thief was really fast when trying to catch the cashier. she caught him fast.", project_id="")
translate_text(text="the doctor is kind, even when working with the baron. he fixed all the issues she was facing.", project_id="")
#translate_text(text="the wicked wolf ate the big deer. he was stuffed because he was heavy.", project_id="")
#translate_text(text="the big worker ate the explorator. she got caught by her.", project_id="")

#translate_text(text="that driver is mean with the worker. he hurt her feelings.", project_id="")
#translate_text(text="the actors are provocative. she has a good personality.", project_id="")
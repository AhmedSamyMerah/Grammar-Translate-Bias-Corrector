from google.cloud import translate
from textCorrection import gender_corrector
#import spacy
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

    print(cleanStr)
    


    # doc = nlp(cleanStr)

    # for token in doc:
    #     print(token.text, '\t', token.pos_, '\t', token.lemma_)

    #Sentence print
    # for sent in doc.sents:
    #     print(sent)

    # Display the translation for each input text provided

    # for translation in response.translations:
    #    print("Translated text: {}".format(translation.translated_text))


translate_text(text="The actor is good. She is nice.", project_id="ancient-lattice-288217")

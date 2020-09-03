from google.cloud import translate
import spacy
import unidecode
import unicodedata
import numpy

nlp = spacy.load("fr_core_news_md")

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii


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

    trString = str(response.translations)
    cleanStr = trString[19:-3]
    
    aigu = "\\303\\251"

    cleanStr = cleanStr.replace(aigu, aigu.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))
    # for c in cleanStr:
    #     if(aigu in cleanStr):
    #        cleanStr.replace(aigu, aigu.encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8'))

    print(cleanStr)
    
    #doc = nlp(cleanStr)

    # doc = nlp(str(response.translations))

    #for token in doc:
        #print(token.text)#, '\t', token.pos_, '\t', token.lemma_)

    # Display the translation for each input text provided

    # for translation in response.translations:
    #    print("Translated text: {}".format(translation.translated_text))


translate_text(text="The guardian splashed the car on the road. She is crazy.", project_id="ancient-lattice-288217")

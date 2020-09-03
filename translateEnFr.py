from google.cloud import translate
import spacy

nlp = spacy.load("fr_core_news_md")

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

    doc = nlp(str(response.translations))

    for token in doc:
        print(token.text, '\t', token.pos_, '\t', token.lemma_)

    # Display the translation for each input text provided
    #for translation in response.translations:
      # print("Translated text: {}".format(translation.translated_text))

translate_text(text="The boss ran on the road. She was terrible", project_id="ancient-lattice-288217")

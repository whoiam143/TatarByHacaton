from easygoogletranslate import EasyGoogleTranslate


def translate_to_tat(sentence):
    translator = EasyGoogleTranslate(
        source_language='ru',
        target_language='tt',
        timeout=10
    )

    result = translator.translate(sentence)
    
    return result


def translate_from_en_to_tat(sentence):
    translator = EasyGoogleTranslate(
        source_language='en',
        target_language='tt',
        timeout=10
    )

    result = translator.translate(sentence)
    
    return result
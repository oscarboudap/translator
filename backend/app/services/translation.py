import argostranslate.translate

def translate_text(text, source_lang="en", target_lang="es"):
    return argostranslate.translate.translate(text, source_lang, target_lang)
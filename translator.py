"""Translator module"""
import translators as ts

class Translator:
    """Translator class"""
    def __init__(self):
        self.__translated_text = ''

    @property
    def trasnlated_text(self):
        """Get translated text"""
        return self.__translated_text

    def translate(self, from_lang, to_lang, text):
        """Translate text"""
        return ts.translate_text(text, 'google', from_lang, to_lang)

translator = Translator()

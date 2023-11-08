"""Languages module"""

class Language:
    """Class for storing chosen voice language"""
    def __init__(self):
        self.__language_code = None
        self.__languages_dict = {
            'en': 'English',
            'uk': 'Ukrainian',
            'cs': 'Czech',
            'pl': 'Poland',
        }

    @property
    def language_code(self):
        """Language property"""
        return self.__language_code

    @property
    def language_name(self):
        """Get language name from dict"""
        return self.__languages_dict[self.language_code]

    @property
    def languages_dict(self):
        """Get languages dict"""
        return self.__languages_dict

    @language_code.setter
    def language_code(self, language_code):
        self.__language_code = language_code


lang = Language()

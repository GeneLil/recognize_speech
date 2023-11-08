"""Buttons module"""
import typing
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from language import lang

class Buttons:
    """Buttons class"""
    def __init__(self):
        self.__language_btns = {
            'en': '🇬🇧 English',
            'uk': '🇺🇦 Ukrainian',
            'cs': '🇨🇿 Czech',
            'pl': '🇵🇱 Polish'    
        }

    @property
    def language_btns(self):
        """Get language buttons"""
        return self.__language_btns

    def __draw_buttons(self, data_dict: typing.Dict):
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        for key, value in data_dict.items():
            markup.add(InlineKeyboardButton(value, callback_data=key))
        return markup

    def buttons_for_speak_language(self):
        """Draw buttons for speak languages"""        
        return self.__draw_buttons(self.language_btns)

    def buttons_for_translate_language(self):
        """Draw buttons for translate languages"""    
        btns = {}
        for key, value in self.language_btns.items():
            if key[0:2] != lang.language_code:
                btns[f'{key}_translate'] = value
        return self.__draw_buttons(btns)

    def start_buttons(self):
        """Draw buttons to start"""
        return self.__draw_buttons({
            'choose_language': 'Choose Language',
            'balance': 'Check balance'
        })

buttons = Buttons()
    
"""Telebot module"""
import re
import telebot
from audio_files import Files
from constants import API_TOKEN
from messages import messages
from language import lang
from voice_message import voice_message as vm
from translator import translator as tr
from buttons import buttons as btns
from users import users


class Telebot:
    """Class for telebot"""
    def __init__(self):
        self.__bot = telebot.TeleBot(API_TOKEN)

    @property
    def bot(self):
        """Bot property"""
        return self.__bot

    def __response_to_voice(self, message):
        """Process voice message"""    
        self.bot.send_message(message.chat.id, 'Processing your voice input...')
        audio_file = self.bot.get_file(message.voice.file_id)
        downloaded_file = self.bot.download_file(audio_file.file_path)
        new_path = Files.write_audio_file(audio_file.file_path, downloaded_file)

        self.bot.reply_to(message, Files.read_from_audio_file(new_path))
        self.bot.send_message(message.chat.id,
                              'You can translate the message into following languages:',
                              reply_markup=btns.buttons_for_translate_language())
        users.deduct_tokens_from_user(message.chat.id)

    def __send_welcome_message(self, message):
        """Send welcome message"""        
        user_data = message.chat
        self.bot.send_message(message.chat.id, messages.welcome_message(user_data),
                              reply_markup=btns.start_buttons())

    def __choose_speak_language(self, message):
        """Show choose lang menu"""
        self.bot.send_message(message.chat.id, 'Select speaking language',
                              reply_markup=btns.buttons_for_speak_language())

    def __show_balance_message(self, message):
        """Show current balance of left tokens"""        
        self.bot.send_message(message.chat.id, 
                              messages.balance_message(message.chat.id),
                              reply_markup=btns.start_buttons())

    def __get_message_processor(self, message):
        """Bot message processor"""        
        if message.text == '/start':
            return self.__send_welcome_message
        if message.content_type == 'voice':
            return self.__response_to_voice

    def __callback_handler(self, data):
        command = data.json['data']
        if command == 'choose_language':
            self.__choose_speak_language(data.message)

        if command == 'balance':  
            self.__show_balance_message(data.message)

        if command in lang.languages_dict:
            lang.language_code = command
            self.bot.send_message(data.message.chat.id,
                f'Please say the phrase in {lang.language_name} language')

        if re.match(r'[a-z]{2}_translate', command):
            from_lang = lang.language_code
            to_lang = command.split('_translate')[0]
            self.bot.send_message(data.message.chat.id,
                                  f'''Translated to {lang.languages_dict[to_lang]}:
{tr.translate(from_lang, to_lang, vm.voice_message)}''',
                                reply_markup=btns.start_buttons())

    def __echo_messages(self, *bot_messages):
        """Check and process message type"""        
        for m in bot_messages:
            message_processor = self.__get_message_processor(m[0])
            message_processor(m[0])

    def start_bot(self):
        """Start bot"""
        self.bot.set_update_listener(self.__echo_messages)
        self.bot.callback_query_handler(lambda query: query.data)(self.__callback_handler)
        self.bot.infinity_polling()


bot = Telebot()

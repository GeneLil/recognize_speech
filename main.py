"""Main module"""
from voice_bot import bot
from audio_files import Files


if __name__ == '__main__':
    Files.clear_voice_folder()
    bot.start_bot()
    
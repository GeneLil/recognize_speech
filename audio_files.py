"""Files processing module"""
import glob
import os
import re
from pydub import AudioSegment
import speech_recognition as sr
from constants import CURRENT_DIR
from language import lang
from voice_message import voice_message as vm

speech_recognizer = sr.Recognizer()

class Files:
    """Working with files"""    
    @staticmethod
    def clear_voice_folder():
        """Removes files from /voice folder"""
        files = glob.glob(f'{CURRENT_DIR}/voice/*')
        for file in files:
            os.remove(file)

    @staticmethod
    def convert_oga_to_wav(path: str):
        """Convert file"""    
        with open(path, 'rb') as audio_file:
            voice = AudioSegment.from_ogg(audio_file)
            file_name_list = re.split("voice/", path)[1].split('.')[0]
            new_path = f'voice/{file_name_list}.wav'
            voice.export(new_path, format="wav")
            return new_path

    @staticmethod
    def write_audio_file(file_path, downloaded_file):
        """Write new audio file"""
        if not os.path.exists(CURRENT_DIR + '/voice/'):
            os.mkdir('voice/')
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        return Files.convert_oga_to_wav(file_path)

    @staticmethod
    def read_from_audio_file(path: str):
        """Read from audio file"""    
        with open(path, 'rb') as audio_file:
            with sr.AudioFile(audio_file) as source:
                audio = speech_recognizer.record(source)
                try:
                    vm.voice_message = speech_recognizer.recognize_google(audio_data=audio,
language=lang.language_code)
                    return f'''You said: {vm.voice_message}'''
                except sr.UnknownValueError:
                    return ('We could not understand audio')
                except sr.RequestError as e:
                    return (f'Sphinx error; {e}')
                
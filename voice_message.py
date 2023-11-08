"""Recognized voice message module"""

class VoiceMessage:
    """Recognized voice message class"""
    def __init__(self):
        self.__voice_message = ''

    @property
    def voice_message(self):
        """Get recognized voice message"""
        return self.__voice_message

    @voice_message.setter
    def voice_message(self, message: str):
        self.__voice_message = message

voice_message = VoiceMessage()

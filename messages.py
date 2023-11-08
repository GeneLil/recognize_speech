"""Messages module"""
from constants import START_TOKENS
from user import User
from users import users

class Messages:
    """Handling text messages for replies"""

    def __welcome_to_new_user(self, user_data):
        """Welcome text for new user"""
        new_user = User.create_user(user_data, START_TOKENS)
        users.add_user(new_user)
        return f'''Welcome, {new_user.name_to_show()}!
You have received {START_TOKENS} tokens.'''

    def __welcome_to_existing_user(self, user_data):
        """Welcome text to existing user"""        
        existing_user = users.get_user_by_id(user_data.id)
        return f'Hello again, {existing_user.name_to_show()}!'

    def __welcome_message_processor(self, user_data):
        if not users.if_user_exists(user_data.id):
            return self.__welcome_to_new_user
        return self.__welcome_to_existing_user

    def balance_message(self, user_id):
        """Get balance message"""
        user = users.get_user_by_id(user_id)
        return f'You have {user.tokens} tokens left'

    def welcome_message(self, user_data):
        """Get welcome message"""
        message_processor = self.__welcome_message_processor(user_data)
        return message_processor(user_data)


messages = Messages()

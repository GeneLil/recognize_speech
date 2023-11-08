"""User module"""

COST_OF_TRANSLATE = 1

class User:
    """User class"""
    def __init__(self, user_id: int,
                 first_name: str,
                 last_name: str,
                 username: str,
                 tokens: int):
        self.__user_id = user_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__tokens = tokens

    def __eq__(self, other):
        return self.user_id == other.user_id

    @property
    def user_id(self):
        """Id field getter"""
        return self.__user_id

    @property
    def first_name(self):
        """Get first name"""
        return self.__first_name

    @property
    def last_name(self):
        """Get last name"""
        return self.__last_name

    @property
    def full_name(self):
        """Get full name"""
        return self.first_name or '' + ' ' + self.last_name or ''

    @property
    def username(self):
        """Username field getter"""
        return self.__username

    def name_to_show(self) -> str:
        """Define which name to show"""
        return self.full_name if self.__first_name or self.__last_name else self.username
    
    @staticmethod
    def create_user(user_data, tokens):
        """Create user static method"""
        return User(user_id=user_data.id,
                    first_name=user_data.first_name,
                    last_name=user_data.last_name,
                    username=user_data.username,
                    tokens=tokens)

    @property
    def tokens(self):
        """Tokens field getter"""
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens):
        """Tokens field setter"""
        self.__tokens = tokens

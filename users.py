"""Users module"""

import typing
import json
from json import JSONDecodeError
from user import User, COST_OF_TRANSLATE


class Users:
    """Users"""
    def __init__(self):
        self.__users: typing.List[User] = self.__deserialized_users()

    @property
    def users(self):
        """Get list of users"""
        return self.__users

    @users.setter
    def users(self, users_list: typing.List[User]):
        self.__users = users_list

    def __serialized_users(self):
        """Serialize users to for JSON"""
        serialized_users = []
        for user in self.users:            
            serialized_users.append({ 'id': user.user_id,
                                     'first_name': user.first_name,
                                     'last_name': user.last_name,
                                     'username': user.username,
                                     'tokens': user.tokens })
        return serialized_users

    def __deserialized_users(self):
        """Deserialize users from JSON"""
        users_from_json = self.__load_users_from_file()
        deserialized_users = []
        for user in users_from_json:
            deserialized_users.append(User(user_id=user['id'],
                                           first_name=user['first_name'],
                                           last_name=user['last_name'],
                                           username=user['username'],
                                           tokens=user['tokens']))
        return deserialized_users

    def __load_users_from_file(self):
        """Load users from JSON"""
        try:
            with open('users.json', 'r') as file:
                loaded_users = json.load(file)
        except FileNotFoundError:
            loaded_users = []
            print('file not found')
        except JSONDecodeError:
            loaded_users = []
            print('json format is wrong or the file is empty')
        return loaded_users

    def __write_all_users(self):
        """Write all users to JSON"""                
        with open('users.json', 'w') as file:            
            json.dump(self.__serialized_users(), file, indent=2)

    def get_user_by_id(self, user_id: str):
        """Returns user found by ID"""        
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def if_user_exists(self, user_id: str):
        """Check if user already in collection"""
        for user_to_check in self.users:
            if user_to_check.user_id == user_id:
                return True
        return False

    def deduct_tokens_from_user(self, user_id: str):
        """Deduct tokens for translation"""
        user = self.get_user_by_id(user_id)
        user.tokens = user.tokens - COST_OF_TRANSLATE        
        self.__write_all_users()

    def add_user(self, user: User):
        """Add user"""        
        self.users.append(user)
        self.__write_all_users()


users = Users()

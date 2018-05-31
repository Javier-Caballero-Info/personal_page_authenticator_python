from swagger_server.models import User
from swagger_server.services.firebase_service import FirebaseService


class UserService:

    _PATH = 'users'

    @staticmethod
    def get_all() -> ['User']:

        result = FirebaseService.get(UserService._PATH)

        if result is None:
            return []
        else:

            obj_result: [User] = []

            for key, val in result.items():
                val['id'] = key
                obj_result.append(User.from_dict(val))

            return obj_result

    @staticmethod
    def get_by_id(key) -> 'User':

        result = FirebaseService.get(UserService._PATH + '/' + key)
        if result:
            result['id'] = key
            return User.from_dict(result)
        else:
            return None

    @staticmethod
    def get_by_username(username) -> 'User':

        result = FirebaseService.find_equal(UserService._PATH, 'username', username)

        if result:
            return User.from_dict(result)
        else:
            return None

    @staticmethod
    def create(user: User) -> 'User':

        user.password = User.hash_password(user.password)

        return User.from_dict(FirebaseService.add(UserService._PATH, user.to_dict()))

    @staticmethod
    def edit(key, user: User) -> 'User':
               
        user_dict = user.to_dict()

        if 'password' in user_dict.keys():
            del user_dict['password']

        if 'id' in user_dict.keys():
            del user_dict['id']

        FirebaseService.edit(UserService._PATH + '/' + key, user_dict)

        return UserService.get_by_id(key)

    @staticmethod
    def change_password(key, new_pass) -> 'User':

        result: User = FirebaseService.get(UserService._PATH + '/' + key)

        if result:
            result['password'] = User.hash_password(new_pass)
            FirebaseService.edit(UserService._PATH + '/' + key, result)
            return User.from_dict(result)
        else:
            return None

    @staticmethod
    def remove(key):

        return FirebaseService.remove(UserService._PATH + '/' + key)

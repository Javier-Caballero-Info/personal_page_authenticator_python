from flask import globals


class FirebaseService:
    
    @staticmethod
    def _get_db():
        return globals.db

    @staticmethod
    def get(path):

        return FirebaseService._get_db().child(path).get()

    @staticmethod
    def find_equal(path, key, value):
        result = FirebaseService._get_db().child(path).order_by_child(key).equal_to(value).get()

        if len(result) > 0:

            key = next(iter(result))

            result = result[key]

            result['id'] = key

            return result

        else:
            return None

    @staticmethod
    def add(path, data):
        result_ref = FirebaseService._get_db().child(path).push(data)

        result = result_ref.get()

        result['id'] = result_ref.key

        return result

    @staticmethod
    def edit(path, data):
        return FirebaseService._get_db().child(path).update(data)

    @staticmethod
    def remove(path):
        FirebaseService._get_db().child(path).delete()

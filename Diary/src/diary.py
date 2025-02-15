from datetime import datetime
import bcrypt

from entry import Entry


class Diary:
    def __init__(self, username, password):
        self.__id = 1
        self._username = username
        self._password: bytes = self.__hash_password(password)
        self._is_locked = False
        self._entries = []

    @property
    def is_locked(self):
        return self._is_locked

    @property
    def username(self):
        return self._username

    def lock(self, password):
        if  self.__is_authenticated(password):
            self._is_locked = True
            return None
        raise ValueError("Password is not correct")

    def unlock(self, password):
        if  self.__is_authenticated(password):
            self._is_locked = False
            return None
        raise ValueError("Password is not correct")

    def __is_authenticated(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self._password)

    def __hash_password(self, password) -> bytes:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def total_entries(self):
        return len(self._entries)

    def add_entry(self, title, body) -> None:
        if not self.is_locked:
            current_date = datetime.today()
            current_entry = Entry(self.__id, title, body, current_date)
            self._entries.append(current_entry)
            self.__id += 1
            return None

        raise ValueError("Diary is locked")

    def delete_entry(self, entry_id, password):
        if self.is_locked: raise ValueError("Diary is locked")
        if not self.__is_authenticated(password): raise ValueError("Password is incorrect")
        entry = self.find_entry_by(entry_id)
        if entry is None: raise ValueError("Entry not found")
        self._entries.remove(entry)


    def find_entry_by(self, entry_id):
        return next(filter(lambda entry: entry.id == entry_id, self._entries))
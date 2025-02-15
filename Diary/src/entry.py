class Entry:
    def __init__(self, id, title, body, date):
        self.__id = id
        self.__title = title
        self.__body = body
        self.__date = date


    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f"ID: {self.__id}, \nTitle: {self.__title}, \nDate: {self.__date}"
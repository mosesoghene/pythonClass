from abc import ABC, abstractmethod
from address import Address

class User(ABC):
    def __init__(self, homeAdress: Address, password: str, phone: str, name: str, age: str, email: str):
        self.homeAddress = Address()
        self.password = password
        self.phone = phone
        self.name = name
        self.age = age
        self.email = email
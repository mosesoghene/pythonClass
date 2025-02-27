import os
import re
import time
from subprocess import call

import bcrypt


def validate_email(email):
    return re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[.][a-zA-Z]{2,}$", email)


def save_to_file(email, password):
    with open('users.txt', 'a') as users_file:
        user = f"{email},{password}\n"
        users_file.write(user)


def email_exists(email):
    users = load_users()
    for user in users:
        user_email, user_password = user
        if email == user_email:
            return True
    return False


def register(email, password):
    if validate_email(email):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        if email_exists(email): return False
        save_to_file(email, hashed_password)
        return True
    return False


def load_users():
    with open('users.txt', 'r') as users_file:
        users = [user.strip().split(',') for user in users_file.readlines()]
        return users


def is_authenticated(email, password):
    users = load_users()
    for user in users:
        user_email, user_password = user
        if user_email == email:
            return bcrypt.checkpw(password.encode('utf-8'), bytes(user_password, 'utf-8'))

    return False


def login(email, password):
    if validate_email(email):
        if is_authenticated(email, password):
            return True
    return False


def dashboard(email):
    print(f"Welcome {email}!")
    option = input("""
    1. Main menu
    2. Logout
    > """)
    match option:
        case '1':
            main_menu()
        case '2':
            print("User is being Logged Out ", end="")
            for _ in range(3):
                print(">", end="")
                time.sleep(1)
            print("\nLogged Out")
            main_menu()
        case _ :
            print("Invalid Option")
            dashboard(email)


def login_menu():
    email = input("""
    Login Menu
    
    Enter email: """)
    password = input("\tEnter password: ")

    if login(email, password):
        dashboard(email)


def register_menu():
    email = input("""
    Register Menu
        
    Enter email: """)
    password = input("\tEnter password: ")
    if register(email, password):
        print("Saving", end="")
        for _ in range(3):
            print(">", end="")
            time.sleep(1)
        print(f" Registered: {email}. Welcome!")
        main_menu()
    else:
        print("Invalid credentials.   Going back to main menu.")
        for _ in range(5):
            print(">", end="")
            time.sleep(1)
        main_menu()


def main_menu():
    option = input("""***Main menu***
    
    1. Register
    2. Login
    3. Exit
    > """)

    match option:
        case '1':
            register_menu()
        case '2':
            login_menu()
        case '3':
            print("Exiting", end="")
            for _ in range(5):
                print(">", end="")
                time.sleep(1)
            print("Bye")
        case _:
            print("Invalid Option")
            main_menu()

if __name__ == '__main__':
    main_menu()
"""
User interface
"""
from auth import (
    Authenticator,
    Authorizor,
    User,
    NotPermittedError,
    InvalidUsername,
    InvalidPassword,
    UsernameAlreadyExists,
    PasswordTooShort,
)

authenticator = Authenticator()
authorizor = Authorizor(authenticator)
authenticator.add_user("joe", "joepassword")
authorizor.add_permission("create notes")
authorizor.add_permission("notes")
authorizor.add_permission("all notes")
authorizor.add_permission("give permission")
authorizor.permit_user("create notes", "joe")
authorizor.permit_user("all notes", "joe")
authorizor.permit_user("notes", "joe")
authorizor.permit_user("give permission", "joe")


def possible_actions(current_user_func):
    """
    Print possible actions
    """
    actions_logged = ["notes", "create note"]
    actions_admin = ["all notes", "give permission"]
    actions_not_logged = ["login", "create account", "logout", "exit"]
    try:
        if isinstance(current_user_func, User):
            authorizor.check_permission("all notes", current_user_func.username)
            print(f"As you are admin you can {actions_admin}")
    except NotPermittedError:
        print("You are user")
    print(f"Enter ection you want to do {actions_not_logged}")
    if isinstance(current_user_func, User):
        print(f"As you are logged in you can {actions_logged}")


def get_notes(current_user_func):
    """
    Notes func
    """
    try:
        authorizor.check_permission("notes", current_user_func.username)
    except PermissionError as err:
        print(err)
    except NotPermittedError as err:
        print(err)
    if len(current_user_func.notebook.notes) == 0:
        print("No notes")
        return
    print("Input notes you want to see")
    for index, note in enumerate(current_user_func.notebook.notes):
        print(str(index + 1) + ") " + note.filename)
    file_name = input(">>> ")
    for index, note in enumerate(current_user_func.notebook.notes):
        if note.filename == file_name:
            print(note.memo)
            input("Print any to exit file >>> ")
            return
    print("No file was found")


def create_note(cucurrent_user_func):
    """
    Create note function
    """
    try:
        authorizor.check_permission("create notes", cucurrent_user_func.username)
    except PermissionError as err:
        print(err)
    except NotPermittedError as err:
        print(err)
    print("You are creating new note")
    note_name = input("Input new notename >>> ")
    notes_text = input("Input notes >>> ")
    cucurrent_user_func.notebook.new_note(note_name, notes_text)


def login():
    """
    Login function
    """
    print("You are logging in")
    username = input("input username >>> ")
    password = input("input password >>> ")
    try:
        return authenticator.login(username, password)
    except InvalidPassword as err:
        print(err)
    except InvalidUsername as err:
        print(err)


def create_account():
    """
    Create account
    """
    print("You are creating new account")
    username = input("input username >>> ")
    password = input("input password >>> ")
    try:
        authenticator.add_user(username, password)
        authorizor.permit_user("create notes", username)
        authorizor.permit_user("notes", username)
    except PasswordTooShort as err:
        print(err)
    except UsernameAlreadyExists as err:
        print(err)


def all_notes(current_user_func):
    """
    All notes
    """
    try:
        if isinstance(current_user_func, User):
            authorizor.check_permission("all notes", current_user_func.username)
    except PermissionError as err:
        print(err)
    except NotPermittedError as err:
        print(err)
    print("Whose notes you want to see")
    for i in authenticator.users:
        print(i)
    notes = input(">>> ")
    if len(authenticator.users[notes].notebook.notes) == 0:
        print("No notes")
        return
    print("What notes you want to see")
    if notes in authenticator.users:
        for i in authenticator.users[notes].notebook.notes:
            print(i.filename)
    file_name = input(">>> ")
    for note in authenticator.users[notes].notebook.notes:
        if note.filename == file_name:
            print(note.memo)
            input("Print any to exit file >>> ")
            return
    print("No notes was finded by this name.")


def give_permission(current_user_func):
    """
    This function upgrades permission
    """
    try:
        if isinstance(current_user_func, User):
            authorizor.check_permission("all notes", current_user_func.username)
    except PermissionError as err:
        print(err)
    except NotPermittedError as err:
        print(err)
    print("Whom do you want to upgrade permission")
    for i in authenticator.users:
        print(i)
    username = input(">>> ")
    if username in authenticator.users:
        authorizor.permit_user("all notes", username)
        authorizor.permit_user("give permission", username)
        print(f"Permission for {username} upgraded succesfuly")
    else:
        print("User not found")


def main():
    """
    Main Func
    """
    current_user = object
    while True:
        possible_actions(current_user)
        command = input(">>> ")
        if isinstance(current_user, User):
            if command == "notes":
                get_notes(current_user)
                continue
            if command == "create note":
                create_note(current_user)
                continue
            if command == "logout":
                authenticator.users[
                    current_user.username
                ].notebook = current_user.notebook
                current_user = object
                continue

        if command == "login":
            current_user = login()
        elif command == "create account":
            create_account()
        elif command == "all notes":
            all_notes(current_user)
        elif command == "give permission":
            give_permission(current_user)
        elif command == "exit":
            break
        else:
            print("Command is not recognized.")


main()

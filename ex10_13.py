###Sourse : Python crash course(2nd edition) by Eric Matthes###
##cp10's 13th excrcise

import json

filepath = "/storage/emulated/0/python_work/Python_work_book/File_python_work_book/username.json"


def get_stored_users():
    """Get list of stored users if available."""
    try:
        with open(filepath) as f:
            users = json.load(f)
    except FileNotFoundError:
        return []
    else:
        return users


def save_user(users):
    """Save the updated user list."""
    with open(filepath, "w") as f:
        json.dump(users, f)


def greet_user():
    """Greet existing users or add new ones."""
    users = get_stored_users()

    name = input("What is your name? ").lower()

    if name in users:
        print(f"Welcome back, {name}!")
    else:
        print(f"We'll remember you when you come back, {name}!")
        users.append(name)
        save_user(users)


greet_user()



# login.py
import json
import os

USER_DATA_FILE = 'users.json'

def load_users():
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

def authenticate(username, password):
    users = load_users()
    user = users.get(username)
    if user and user['password'] == password:
        return True
    return False

def register(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = {'password': password}
    save_users(users)
    return True

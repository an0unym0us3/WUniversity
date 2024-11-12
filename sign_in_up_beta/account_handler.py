from sqlite3 import connect
from cryptography.fernet import Fernet

# https://inloop.github.io/sqlite-viewer/

db = connect('user_acc.db')
c = db.cursor()


class User:
    def __init__(self, name, pwd, dob, email):
        self.name = name
        self.pwd = pwd
        self.dob = dob
        self.email = email


class DB_Error(Exception):
    def __init__(self, info):
        self.info = info


def encrypt(message: str, key: str) -> str:
    return Fernet(key.encode()).encrypt(message.encode()).decode()


def decrypt(token: str, key: str) -> str:
    return Fernet(key.encode()).decrypt(token.encode()).decode()


def db_sign_up(username, password):
    if not (username and password):
        raise DB_Error('Cannot leave Username/Password empty.')

    c.execute(f"select name from users where name='{username}'")
    if not c.fetchall():
        db_key = Fernet.generate_key().decode()
        db_token = encrypt(password, db_key)
        db.execute(f"insert into users(name, token, key) values('{username}', '{db_token}', '{db_key}')")
        db.commit()
    else:
        raise DB_Error('Username already taken.')


def db_sign_in(username, password):
    c.execute(f"select token, key from users where name='{username}'")
    if this := c.fetchone():
        db_token, db_key = this
    else:
        raise DB_Error('User does not exist')

    if password == decrypt(db_token, db_key):
        print('is there and welcome')
        # do account security stuff here ig
    else:
        raise DB_Error('Either username or password is incorrect')

#import mysql.connector as sql
from sqlite3 import connect
from cryptography.fernet import Fernet

# https://inloop.github.io/sqlite-viewer/

# Database/Table setup
"""
db = sql.connect(
    host='localhost',
    user='root',
    password='root')

c.execute('''create database if not exists university_application_hub;''')

c.execute('''use university_application_hub''')

Note: to convert from sqlite3 to mysql, change autoincrement to auto_increment
in decrypt convert key and token.encode to decode cause of the way sqlite and mysql store blob
"""

db = connect('data.db')
c = db.cursor()

c.execute('''
create table if not exists access(
id integer primary key autoincrement,
name varchar(30) not null,
token blob not null,
passkey blob not null);
''')

db.commit()


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

    c.execute(f"select name from access where name='{username}'")
    if not c.fetchall():
        db_key = Fernet.generate_key().decode()
        db_token = encrypt(password, db_key)
        c.execute(f"insert into access(name, token, passkey) values('{username}', '{db_token}', '{db_key}')")
        db.commit()
    else:
        raise DB_Error('Username already taken.')


def db_sign_in(username, password):
    c.execute(f"select token, passkey from access where name='{username}'")
    if this := c.fetchone():
        db_token, db_key = this
    else:
        raise DB_Error('User does not exist')

    if password == decrypt(db_token, db_key):
        print('Remember to interconnect using this line!')
        # do account security stuff here ig
    else:
        raise DB_Error('Either username or password is incorrect')

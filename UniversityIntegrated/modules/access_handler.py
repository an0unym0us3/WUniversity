from sqlite3 import connect
from cryptography.fernet import Fernet
# https://inloop.github.io/sqlite-viewer/

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


class DB_Error(Exception):
    def __init__(self, info):
        self.info = info


def encrypt(message: str, key: str) -> str:
    return Fernet(key.encode()).encrypt(message.encode()).decode()

def decrypt(token: str, key: str) -> str:
    return Fernet(key.encode()).decrypt(token.encode()).decode()

def is_exist(username):
    c.execute(f"select name from access where name='{username}'")
    return bool(c.fetchall())

def db_sign_up(username, password):
    if not (username and password):
        raise DB_Error('Cannot leave Username/Password empty.')
    
    if is_exist(username):
        raise DB_Error('Username already taken.')
    else:
        db_key = Fernet.generate_key().decode()
        db_token = encrypt(password, db_key)
        c.execute(f"insert into access(name, token, passkey) values('{username}', '{db_token}', '{db_key}')")
        db.commit()

def db_sign_in(username, password):
    c.execute(f"select token, passkey from access where name='{username}'")
    if this := c.fetchone():
        db_token, db_key = this
    else:
        raise DB_Error('User does not exist')

    if password != decrypt(db_token, db_key):
        raise DB_Error('Either username or password is incorrect')

def db_recover(username, new_password):
    db_key = Fernet.generate_key().decode()
    db_token = encrypt(new_password, db_key)
    c.execute(f'update access set token=?, passkey=? where name=?;', (db_token, db_key, username))

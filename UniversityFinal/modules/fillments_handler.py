#import mysql.connector as sql
from sqlite3 import connect
from datetime import datetime

# https://inloop.github.io/sqlite-viewer/

# Table setup
"""
db = sql.connect(
    host='localhost',
    user='root',
    password='root',
    database='university_application_hub')

Note: to convert sqlite to mysql, replace ? with %s, and autoincrement to auto_increment
"""

db = connect('data.db')
c = db.cursor()

c.execute('''
create table if not exists personal(
id integer primary key autoincrement,
first_name varchar(30) not null,
last_name varchar(30) not null,
dob date,
email varchar(30),
phone varchar(15)
);
''')


c.execute('''
create table if not exists document(
id integer primary key autoincrement,
passport_copy blob not null,
residence_card_front blob not null,
residence_card_back blob not null
);
''')


c.execute('''
create table if not exists scores(
id integer primary key autoincrement,
ielts real,
toefl integer,
sat integer,
act integer
);
''')

c.execute('''
create table if not exists uploads(
id integer primary key autoincrement,
academic_transcript blob not null,
letter_of_recommendation_1 blob not null,
letter_of_recommendation_2 blob not null,
personal_statement blob not null
);
''')

db.commit()

def dateify(date):
    return datetime.strptime(date, '%Y-%m-%d')

def blobbify(path):
    print(path)
    with open(path, 'rb') as f:
        blob_data = f.read()
        print('someblob is here' if blob_data else 'no blob')
    return blob_data


def deblobbify(blob_data, path):
    with open(path, 'wb') as f:
        f.write(blob_data)    

def db_personal(first_name, last_name, dob, email, phone):
    c.execute(f"insert into personal(first_name, last_name, dob, email, phone) values('{first_name}', '{last_name}', '{dateify(dob)}', '{email}', '{phone}');")
    db.commit()

def db_documents(passport_copy, residence_card_front, residence_card_back):
    args = [passport_copy, residence_card_front, residence_card_back]
    blobs = [blobbify(each) for each in args]
    c.execute(f"insert into document(passport_copy, residence_card_front, residence_card_back) values(?, ?, ?);", blobs)
    db.commit()

def db_scores(ielts, toefl, sat, act):
    c.execute(f"insert into scores(ielts, toefl, sat, act) values({ielts}, {toefl}, {sat}, {act});")
    db.commit()

def db_uploads(academic_transcript, letter_of_recommendation_1, letter_of_recommendation_2, personal_statement):
    args = [academic_transcript, letter_of_recommendation_1, letter_of_recommendation_2, personal_statement]
    blobs = [blobbify(each) for each in args]
    c.execute(f"insert into uploads(academic_transcript, letter_of_recommendation_1, letter_of_recommendation_2, personal_statement) values(?, ?, ?, ?);", blobs)
    db.commit()




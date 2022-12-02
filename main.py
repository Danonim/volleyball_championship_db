import pymysql.cursors
from config import host, user, password, db_name

connection = pymysql.connect(
    host=host,
    user=user,
    database=db_name,
    password=password,
    cursorclass=pymysql.cursors.DictCursor
    )

with connection:
    with connection.cursor() as cursor:
        # cursor.execute("CREATE DATABASE volleyball_championship")

        cursor.execute("CREATE TABLE Teams (id int PRIMARY KEY AUTO_INCREMENT, name varchar(30) NOT NULL, wins int NOT NULL, defeats int NOT NULL)")
        cursor.execute("INSERT INTO Teams (name, wins, defeats) VALUES (%s,%s,%s)", ("Бобри", 3, 0))
        cursor.execute("INSERT INTO Teams (name, wins, defeats) VALUES (%s,%s,%s)", ("Тюбіки", 0, 3))

        cursor.execute("CREATE TABLE Players (id int PRIMARY KEY AUTO_INCREMENT, name varchar(30) NOT NULL, age int NOT NULL, teamId int REFERENCES Teams(id))")
        cursor.execute("INSERT INTO Players (name, age, teamId) VALUES (%s,%s,%s)", ("Артем", 19, 1))
        cursor.execute("INSERT INTO Players (name, age, teamId) VALUES (%s,%s,%s)", ("Андрій", 18, 1))
        cursor.execute("INSERT INTO Players (name, age, teamId) VALUES (%s,%s,%s)", ("Даня", 17, 1))
        cursor.execute("INSERT INTO Players (name, age, teamId) VALUES (%s,%s,%s)", ("Діма", 15, 2))
        cursor.execute("INSERT INTO Players (name, age, teamId) VALUES (%s,%s,%s)", ("Льоша", 17, 2))
        cursor.execute("INSERT INTO Players (name, age, teamId) VALUES (%s,%s,%s)", ("Тімоха", 13, 2))

    connection.commit()

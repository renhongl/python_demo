


import pymysql

# db = pymysql.connect(host='localhost', user='root', password='root', port=3306)

# cursor = db.cursor()

# cursor.execute('SELECT VERSION()')

# data = cursor.fetchone()

# print('database version: ', data)

# cursor.execute('CREATE DATABASE spider DEFAULT CHARACTER SET utf8mb4')

# db.close()

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spider')

cursor = db.cursor()

# sql = 'CREATE TABLE IF NOT EXISTS student (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'

# cursor.execute(sql)

# db.close()

sql = 'INSERT INTO student(id, name, age) values(%s, %s, %s)'

try:
    cursor.execute(sql, ('2001001', 'renhong', 18))
    db.commit()
except:
    db.rollback()

db.close()


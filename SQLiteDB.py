import sqlite3

conn = sqlite3.connect("testing.db")

db = conn.cursor()
query = ("DROP TABLE user")
db.execute(query)
query = ("""CREATE TABLE 'user' (
  'id' INT(11) NOT NULL,
  'name' VARCHAR(45) NULL DEFAULT NULL UNIQUE,
  'points' INT(11) NULL DEFAULT '0',
  'ign' VARCHAR(45) NULL DEFAULT NULL,
  'is_registered' TINYINT(1) NULL DEFAULT '1',
  PRIMARY KEY ('id')
  )""")
db.execute(query)
conn.commit()
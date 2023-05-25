import sqlite3

conn = sqlite3.connect('test.db')

sql = '''
insert into saram(id, name, age)
values(?,?,?)
'''
c = conn.cursor()
c.execute(sql,('lee','qwe',34))
c.close()

conn.commit()
conn.close()
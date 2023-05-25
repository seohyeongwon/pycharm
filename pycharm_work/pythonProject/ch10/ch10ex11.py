import sqlite3

conn = sqlite3.connect('test.db')

sql = '''
    insert into saram(id, name, age)
    values("park","qwe",34)
'''

c = conn.cursor()
c.execute(sql)
c.close()

conn.commit()
conn.close()
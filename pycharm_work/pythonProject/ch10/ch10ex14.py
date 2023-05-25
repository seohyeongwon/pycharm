import sqlite3

conn = sqlite3.connect('test.db')

sql = '''
insert into saram(id, name, age)
values(?,?,?)
'''

data = [
    ('lee', 'qwe', 34),
    ('seo', 'qwe', 32),
    ('qwe', 'qwe', 14),
    ('asdas', 'qwe', 24)

]
c = conn.cursor()
c.executemany(sql, data)
c.close()

conn.commit()
conn.close()
import sqlite3

people_values = (
("Benjamin Sisko", "Human", 40),
("Jadzia Dax", "Trill", 300),
("Kira Nerys", "Bajoran", 29)
)

update_people = (
    ("Ezri Dax","Jadzia Dax")
)

add_rank = (
    ("Capatain","Benjamin Sisko"),
    ("Lieutenant","Ezri Dax"),
    ("Major","Kira Nerys")
)

with sqlite3.connect('roster.db') as conn:
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        species TEXT NOT NULL,
        age INTEGER NOT NULL
        )
        ''')
    # cursor.execute('''DROP TABLE IF EXISTS Users''')
    # Value larni kiritish
    cursor.executemany('''INSERT INTO Users (name, species, age) Values (?,?,?)''', people_values)
    # Ismga qarab ism o'zgartrish
    cursor.execute('''UPDATE Users SET name=? WHERE name=?''', update_people)
    conn.commit()

    #Bajoran ga tegishli malumotlarni qaytarish
    cursor.execute('''SELECT name, age From Users Where species=('Bajoran')''')
    for row in cursor.fetchall():
        print(row)
    # 100 dan kattalarni chopish
    cursor.execute('''DELETE FROM Users WHERE age > 100''')
    conn.commit()
    # Ranl qo'shish
    cursor.execute('''ALTER TABLE Users ADD COLUMN Rank TEXT''')
    cursor.executemany('''UPDATE Users SET Rank=? WHERE name=?''', add_rank)
    conn.commit()
    # Kamayish tartibida fetchall
    cursor.execute('''SELECT * FROM Users ORDER BY age DESC''')
    for row in cursor.fetchall():
        print(row)

import sqlite3

library = (
    ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
    ('1984', 'George Orwell', 1949, 'Dystopian'),
    ('The Great Gatsby','F. Scott Fitzgerald',	1925, 'Classic')
)

rating_library = (
    (4.8, 'To Kill a Mockingbird'),
    (4.7, '1984')
)
with sqlite3.connect('library.db') as conn:
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Library(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year_published INTEGER NOT NULL,
        genre TEXT NOT NULL)''')

    # Value larni kiritish
    cursor.executemany('''INSERT INTO Library(title, author, year_published, genre) Values (?,?,?,?)''', library)
    conn.commit()
    # 1984 ni yilini 1950 ga ozgartirish
    cursor.execute('''UPDATE Library SET year_published=? Where title=?''', (1950, '1984'))
    conn.commit()
    # Janri Dystopian bolgan kitoblarni chop etish
    cursor.execute('''SELECT title, author From Library WHERE genre = ('Dystopian')''')
    for row in cursor.fetchall():
        print(row)

    #1950 da oldin yozilgan kitoblarni chopish
    cursor.execute('''DELETE FROM Library WHERE year_published < 1950''')
    conn.commit()
    #Rating column qo'shish
    cursor.execute('''ALTER TABLE Library ADD COLUMN rating FLOAT''')
    conn.commit()
    #Rating kiritish
    cursor.executemany('''UPDATE Library SET rating=? WHERE title=?''', rating_library)
    conn.commit()
    #yozilgan yili osish tartibida chop etish
    cursor.execute('''SELECT * FROM Library ORDER BY year_published ASC''')
    for row in cursor.fetchall():
        print(row)

    # cursor.execute('''DROP TABLE IF EXISTS Library''')
    # conn.commit()

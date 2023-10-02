import sqlite3

db = sqlite3.connect('todo.db')

db.execute("""
    CREATE TABLE IF NOT EXISTS to_do (
        name TEXT NOT NULL UNIQUE
    );
""")


def first_fiche():
    return db.execute("SELECT * FROM to_do").fetchall()





def insert_todo(name):
    if name != '':
        name = name.replace(' ', '_')
        db.execute("INSERT INTO to_do (name) VALUES (?)", (name,))
        db.commit()
        return db.execute("SELECT * FROM to_do").fetchall()



def delete_todo(name):
    db.execute("DELETE FROM to_do where name = (?)", (name,))
    db.commit()
    x =  db.execute("SELECT * FROM to_do").fetchall()
    return x

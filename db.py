import sqlite3

states = ["to-do", "in progress", "done"]

def init_table():
    
    conn = sqlite3.connect('task.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT,
                 body TEXT,
                 state TEXT)
                 ''')
    conn.commit()
    conn.close()
    print("""
    Initialized the table
    """)

def insert_task(title = "", body = "", state = 0):
    
    try:
        con = sqlite3.connect('task.db')
        c = con.cursor()
        c.execute("INSERT INTO tasks (title, body, state) VALUES (?, ?, ?)", (title, body, states[state]))
        con.commit()
        con.close()
        print("""
        Inserted a task
        """)
    except Exception as e:
        print(e)
        init_table()
        insert_task(title, body, state)

def print_tasks():
    con = sqlite3.connect('task.db')
    c = con.cursor()
    c.execute("SELECT * FROM tasks")
    for row in c.fetchall():
        print(row[0], '\t', row[1], '\t', row[3], '\n\t', row[2])

def update_state_task(id, state):

    con = sqlite3.connect('task.db')
    c = con.cursor()
    c.execute("SELECT * FROM tasks WHERE id = ?", (id,))
    for row in c.fetchall():
        print(str(row[0]) + '. ' + row[1] +  ' (' + row[3] + ' -> ' + states[state] + ')')
    c.execute("UPDATE tasks SET state = ? WHERE id = ?", (states[state], id))
    con.commit()
    con.close()
    print("""
    Updated a task
    """)

def clear_table():
    con = sqlite3.connect('task.db')
    c = con.cursor()
    c.execute("DELETE FROM tasks")
    con.commit()
    con.close()
    print("""
    Cleared the table
    """)

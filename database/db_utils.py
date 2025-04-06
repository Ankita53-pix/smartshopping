def init_db(path="database/smartshop.db"):
    import sqlite3
    conn = sqlite3.connect(path)
    with open("database/schema.sql") as f:
        conn.executescript(f.read())
    conn.commit()
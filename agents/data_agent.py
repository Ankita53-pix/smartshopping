import sqlite3
import pickle

class DataAgent:
    def __init__(self, db_path="database/smartshop.db"):
        self.conn = sqlite3.connect(db_path)

    def insert_product(self, product_info, embedding):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO products (product_id, name, category, embedding) VALUES (?, ?, ?, ?)",
                       (product_info['product_id'], product_info['name'], product_info['category'], pickle.dumps(embedding)))
        self.conn.commit()

    def get_all_product_embeddings(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT product_id, embedding FROM products")
        rows = cursor.fetchall()
        return [(r[0], pickle.loads(r[1])) for r in rows]
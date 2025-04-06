-- SQLite Schema
CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    name TEXT,
    category TEXT,
    embedding BLOB
);
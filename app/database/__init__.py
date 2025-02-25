import sqlite3
from flask import

DATABASE_URL = "main.db"

def get_db():
    db = getattr(g, "_database", None)
    if not db: # if db == None
        db = g._database = sqlite3.connect(DATABASE_URL)
        return db
    

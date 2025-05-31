import sqlite3
from datetime import datetime
import os
from honeynet import config

os.makedirs("logs", exist_ok=True)

def init_db():
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            username TEXT,
            password TEXT,
            user_agent TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_attempt(ip, username, password, user_agent):
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO logins (ip, username, password, user_agent, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (ip, username, password, user_agent, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

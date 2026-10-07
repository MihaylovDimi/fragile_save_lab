"""Persistence layer for saving users. Deliberately fragile baseline (Phase 1)."""

import sqlite3

DATABASE_PATH = "/var/data/production.db"


class SaveManager:
    """Saves users directly to a hard-coded SQL database."""

    def save_user(self, username):
        connection = sqlite3.connect(DATABASE_PATH)
        connection.execute("INSERT INTO users (name) VALUES (?)", (username,))
        connection.commit()
        connection.close()
        return "User saved"
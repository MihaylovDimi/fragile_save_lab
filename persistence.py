"""Persistence layer. SaveManager delegates saving to whichever saver it is given."""

import sqlite3

DATABASE_PATH = "/var/data/production.db"


class DatabaseSaver:
    """Saves users to the SQL database."""

    def __init__(self, path=DATABASE_PATH):
        self.path = path

    def save(self, username):
        connection = sqlite3.connect(self.path)
        connection.execute("INSERT INTO users (name) VALUES (?)", (username,))
        connection.commit()
        connection.close()


class ApiSaver:
    """Saves users to a third-party API. Placeholder until the API contract is agreed."""

    def __init__(self, base_url):
        self.base_url = base_url

    def save(self, username):
        raise NotImplementedError("Third-party API integration is not built yet")


class SaveManager:
    """Saves users through an injected saver, so the storage can change freely."""

    def __init__(self, saver):
        self.saver = saver

    def save_user(self, username):
        try:
            self.saver.save(username)
        except ConnectionError:
            return "Service Unavailable"
        return "User saved"
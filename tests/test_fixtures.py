import os
import sqlite3
import pytest

from app import app_with_db


@pytest.fixture(scope='function')
def db(tmpdir):
    file = os.path.join(tmpdir.strpath, "test.db")
    conn = sqlite3.connect(file)
    conn.execute("CREATE TABLE blog (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, text TEXT)")
    yield conn
    conn.close()


def test_entry_creation(db):
    app_with_db.create_blog_entry(db=db, title="pytest", text="Pytest is awesome!")
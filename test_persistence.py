"""Unit tests for SaveManager, isolated from the real database with mocks."""

from unittest.mock import patch

from persistence import SaveManager


@patch("persistence.sqlite3.connect")
def test_save_user_writes_user_to_database(mock_connect):
    mock_connection = mock_connect.return_value

    result = SaveManager().save_user("alice")

    mock_connect.assert_called_once_with("/var/data/production.db")
    mock_connection.execute.assert_called_once_with(
        "INSERT INTO users (name) VALUES (?)", ("alice",)
    )
    mock_connection.commit.assert_called_once()
    assert result == "User saved"
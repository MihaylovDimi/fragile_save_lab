"""Unit tests for the persistence layer, isolated from real storage with mocks."""

from unittest.mock import Mock, patch

from persistence import DatabaseSaver, SaveManager


def test_save_user_passes_username_to_injected_saver():
    saver = Mock()

    result = SaveManager(saver).save_user("alice")

    saver.save.assert_called_once_with("alice")
    assert result == "User saved"


def test_save_user_returns_service_unavailable_when_saver_fails():
    saver = Mock()
    saver.save.side_effect = ConnectionError("Saver unreachable")

    result = SaveManager(saver).save_user("alice")

    assert result == "Service Unavailable"


@patch("persistence.sqlite3.connect")
def test_database_saver_inserts_user_into_users_table(mock_connect):
    mock_connection = mock_connect.return_value

    DatabaseSaver().save("alice")

    mock_connect.assert_called_once_with("/var/data/production.db")
    mock_connection.execute.assert_called_once_with(
        "INSERT INTO users (name) VALUES (?)", ("alice",)
    )
    mock_connection.commit.assert_called_once()
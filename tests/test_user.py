from gamling_machine import user
from unittest.mock import patch, mock_open


def test_read_player_stats_user_found():
    mock_file_data = "John 10 20 30\nDoe 15 25 35"
    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        with patch("os.path.dirname", return_value=""):
            result = user.read_player_stats("John")
            assert result == user.User("John", 10, 20, 30)

def test_read_player_stats_user_not_found():
    mock_file_data = "John 10 20 30\nDoe 15 25 35"
    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        with patch("os.path.dirname", request_value=""):
            result = user.read_player_stats("Anna")
            assert result is None

def test_read_player_stats_empty_file():
    mock_file_data = ""
    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        with patch("os.path.dirname", request_value=""):
            result = user.read_player_stats("John")
            assert result is None

from unittest import mock
from app import utils


def test_is_base64_valid():
    """Tests for a valid Base64 string."""
    valid_b64 = "SGVsbG8gd29ybGQh"  # Hello world!
    assert utils.is_base64(valid_b64) is True


def test_is_base64_invalid():
    """Tests invalid Base64 string."""
    invalid_b64 = "###@@@123"
    assert utils.is_base64(invalid_b64) is False


@mock.patch('app.utils.pyperclip.copy')
@mock.patch('app.utils.pyperclip.paste')
def test_copy_to_clipboard_and_paste_mocked(mock_paste, mock_copy):
    """Tests copying and pasting from clipboard (with mock)."""
    text = "Clipboard test!"

    # Set up a mock - paste will return what we copy
    def copy_side_effect(value):
        mock_paste.return_value = value

    mock_copy.side_effect = copy_side_effect

    # Call function
    utils.copy_to_clipboard(text)
    result = utils.paste_from_clipboard()

    assert result == text

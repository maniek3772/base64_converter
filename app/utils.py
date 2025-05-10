import pyperclip
import base64


def copy_to_clipboard(text: str) -> None:
    """Copy text to clipboard."""
    pyperclip.copy(text)


def paste_from_clipboard() -> str:
    """Get text from clipboard."""
    return pyperclip.paste()


def is_base64(s: str) -> bool:
    """Checks if a string looks like Base64."""
    try:
        # Check if it can be decoded correctly
        base64.b64decode(s, validate=True)
        return True
    except Exception as e:
        print(f"Exception: {e}")
        return False

import base64


def encode_text(text: str) -> str:
    """Encode text to Base64."""
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')


def encode_file(filepath: str) -> str:
    """Encode file do Base64."""
    with open(filepath, 'rb') as file:
        encoded_bytes = base64.b64encode(file.read())
    return encoded_bytes.decode('utf-8')

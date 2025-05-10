import base64


def decode_text(b64_text: str) -> str:
    """Decode Base64 to plain text."""
    return base64.b64decode(b64_text.encode('utf-8')).decode('utf-8')


def decode_to_file(b64_text: str, output_path: str) -> None:
    """Decode Base64 and write to file."""
    decoded_bytes = base64.b64decode(b64_text.encode('utf-8'))
    with open(output_path, 'wb') as file:
        file.write(decoded_bytes)

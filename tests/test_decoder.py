from app import decoder


def test_decode_text():
    """Tests decoding Base64 text to plain text."""
    encoded = "SGVsbG8gd29ybGQh"  # Base64 dla "Hello world!"
    expected = "Hello world!"
    result = decoder.decode_text(encoded)
    assert result == expected


def test_decode_to_file(tmp_path):
    """Tests Base64 decoding and writing to file."""
    encoded = "SGVsbG8gdGVzdA=="  # Base64 dla "Hello test"
    expected_content = b"Hello test"

    # Path to temporary file
    output_file = tmp_path / "output.txt"

    # Decode and save to file
    decoder.decode_to_file(encoded, str(output_file))

    # Read file and check the contents
    with open(output_file, 'rb') as f:
        content = f.read()

    assert content == expected_content

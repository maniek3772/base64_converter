from app import encoder

def test_encode_text():
    """Tests text encoding to Base64."""
    text = "Hello world!"
    expected = "SGVsbG8gd29ybGQh"
    result = encoder.encode_text(text)
    assert result == expected

def test_encode_file(tmp_path):
    """Tests text file encoding to Base64."""
    file_content = "Hello file!"
    expected_base64 = "SGVsbG8gZmlsZSE="

    # Create a temporary file with the contents
    file_path = tmp_path / "test.txt"
    file_path.write_text(file_content, encoding='utf-8')

    result = encoder.encode_file(str(file_path))
    assert result == expected_base64

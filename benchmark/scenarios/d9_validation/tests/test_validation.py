from src.validation import validate_email, validate_phone, sanitize_html


def test_valid_email():
    assert validate_email("user@example.com") is True
    assert validate_email("a.b-c@sub.domain.org") is True


def test_invalid_email():
    assert validate_email("not-an-email") is False
    assert validate_email("user@") is False
    assert validate_email("@domain.com") is False
    assert validate_email("user@domain") is False


def test_valid_phone():
    assert validate_phone("+1 555-123-4567") is True
    assert validate_phone("(555) 123-4567") is True
    assert validate_phone("5551234567") is True


def test_invalid_phone():
    assert validate_phone("123") is False
    assert validate_phone("abcdefghij") is False
    assert validate_phone("") is False


def test_sanitize_html():
    assert sanitize_html("<script>alert('x')</script>") == \
        "&lt;script&gt;alert(&#x27;x&#x27;)&lt;/script&gt;"
    assert sanitize_html("<b>hi</b>") == "&lt;b&gt;hi&lt;/b&gt;"
    assert sanitize_html("plain text") == "plain text"

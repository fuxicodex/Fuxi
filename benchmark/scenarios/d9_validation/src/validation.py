"""Input validation helpers."""
import html
import re

_EMAIL_RE = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$"
)

# Digits, spaces, dashes, dots, parens, with an optional leading "+".
_PHONE_ALLOWED_RE = re.compile(r"^\+?[0-9 ().-]+$")


def validate_email(email):
    """Return True if `email` looks like a well-formed address."""
    if not isinstance(email, str):
        return False
    return _EMAIL_RE.match(email) is not None


def validate_phone(phone):
    """Return True if `phone` is a plausible phone number (10-15 digits)."""
    if not isinstance(phone, str) or not _PHONE_ALLOWED_RE.match(phone):
        return False
    digits = re.sub(r"\D", "", phone)
    return 10 <= len(digits) <= 15


def sanitize_html(text):
    """Escape HTML special characters, including quotes."""
    return html.escape(text, quote=True)

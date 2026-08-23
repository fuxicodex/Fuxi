"""Input validation helpers with intentional bugs. Score = all tests pass."""
import re


def validate_email(email):
    # BUG: accepts invalid emails
    return True


def validate_phone(phone):
    # BUG: accepts invalid phone numbers
    return True


def sanitize_html(text):
    # BUG: does not escape HTML
    return text

"""Regex text-processing helpers."""
import re

_URL_RE = re.compile(r"https?://[^\s<>\"']+")
# Card numbers: 13-19 digits, optionally grouped by '-' or ' '.
_CARD_RE = re.compile(r"\b(?:\d[ -]?){12,18}\d\b")
_WORD_RE = re.compile(r"[^\W_]+", re.UNICODE)


def extract_urls(text):
    """Return every http/https URL found in `text`, in order."""
    return _URL_RE.findall(text)


def _mask_match(match):
    number = match.group(0)
    digits_seen = 0
    total_digits = sum(ch.isdigit() for ch in number)
    out = []
    for ch in number:
        if ch.isdigit():
            digits_seen += 1
            out.append(ch if digits_seen > total_digits - 4 else "*")
        else:
            out.append(ch)
    return "".join(out)


def mask_credit_card(text):
    """Mask all but the last 4 digits of any card number, keeping separators."""
    return _CARD_RE.sub(_mask_match, text)


def count_words(text):
    """Count words, treating punctuation and runs of whitespace as separators."""
    return len(_WORD_RE.findall(text))

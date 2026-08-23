"""Regex text-processing helpers with intentional bugs. Score = all tests pass."""
import re


def extract_urls(text):
    # BUG: returns empty list always
    return []


def mask_credit_card(text):
    # BUG: does not mask
    return text


def count_words(text):
    # BUG: naive split, mishandles punctuation/whitespace
    return len(text.split())

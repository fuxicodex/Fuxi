from src.textproc import extract_urls, mask_credit_card, count_words


def test_extract_urls():
    text = "Visit https://example.com and http://test.org/path?q=1"
    assert extract_urls(text) == ["https://example.com", "http://test.org/path?q=1"]
    assert extract_urls("no urls here") == []


def test_mask_credit_card():
    assert mask_credit_card("1234-5678-9012-3456") == "****-****-****-3456"
    assert mask_credit_card("1234567890123456") == "************3456"
    assert mask_credit_card("no card") == "no card"


def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("  spaced   out  ") == 2
    assert count_words("one,two;three") == 3
    assert count_words("") == 0

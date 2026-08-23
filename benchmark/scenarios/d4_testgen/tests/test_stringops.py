"""Tests for the StringOps class in src.stringops."""
import re

import pytest

from src.stringops import StringOps


# ---------------------------------------------------------------- word_count

class TestWordCount:
    def test_single_word(self):
        assert StringOps("hello").word_count() == 1

    def test_multiple_words(self):
        assert StringOps("the quick brown fox").word_count() == 4

    def test_empty_string(self):
        assert StringOps("").word_count() == 0

    def test_only_whitespace(self):
        assert StringOps("   ").word_count() == 0

    def test_tabs_and_newlines(self):
        assert StringOps("one\ttwo\nthree").word_count() == 3

    def test_multiple_spaces(self):
        assert StringOps("a   b    c").word_count() == 3

    def test_punctuation_without_spaces_is_one_word(self):
        # split() only splits on whitespace, so this is 2 "words"
        assert StringOps("hello,world! foo.bar").word_count() == 2

    def test_numbers_and_symbols(self):
        assert StringOps("42 3.14 $ €").word_count() == 4


# ------------------------------------------------------------------ to_title

class TestToTitle:
    def test_basic(self):
        assert StringOps("hello world").to_title() == "Hello World"

    def test_already_title(self):
        assert StringOps("Hello World").to_title() == "Hello World"

    def test_empty_string(self):
        assert StringOps("").to_title() == ""

    def test_mixed_case(self):
        assert StringOps("hELLO wORLD").to_title() == "Hello World"

    def test_apostrophe_behavior(self):
        # Python's str.title() uppercases the letter after the apostrophe
        assert StringOps("don't stop").to_title() == "Don'T Stop"

    def test_digits(self):
        assert StringOps("version 2 beta 3").to_title() == "Version 2 Beta 3"

    def test_punctuation_only(self):
        assert StringOps("!!! ???").to_title() == "!!! ???"

    def test_unicode(self):
        assert StringOps("héllo wörld").to_title() == "Héllo Wörld"


# ------------------------------------------------------------------ find_all

class TestFindAll:
    def test_simple_match(self):
        assert StringOps("abc abc abc").find_all(r"abc") == ["abc", "abc", "abc"]

    def test_no_match(self):
        assert StringOps("hello world").find_all(r"xyz") == []

    def test_empty_pattern(self):
        # An empty regex matches at every position (plus the end)
        assert StringOps("ab").find_all(r"") == ["", "", ""]

    def test_digit_pattern(self):
        assert StringOps("a1 b22 c333").find_all(r"\d+") == ["1", "22", "333"]

    def test_word_pattern(self):
        assert StringOps("foo, bar; baz").find_all(r"\w+") == ["foo", "bar", "baz"]

    def test_capturing_group_returns_groups(self):
        # With capturing groups, findall returns tuples of group contents
        assert StringOps("2024-05 06-07").find_all(r"(\d+)-(\d+)") == [
            ("2024", "05"),
            ("06", "07"),
        ]

    def test_empty_text(self):
        assert StringOps("").find_all(r"a") == []

    def test_whitespace_anchor(self):
        assert StringOps("a b  c").find_all(r"\s+") == [" ", "  "]

    def test_case_sensitive_by_default(self):
        assert StringOps("ABC abc").find_all(r"abc") == ["abc"]


# ---------------------------------------------------------------- is_anagram

class TestIsAnagram:
    def test_true_basic(self):
        assert StringOps("listen").is_anagram("silent") is True

    def test_false_different_letters(self):
        assert StringOps("hello").is_anagram("world") is False

    def test_different_lengths(self):
        assert StringOps("abc").is_anagram("abcd") is False

    def test_case_insensitive(self):
        assert StringOps("Listen").is_anagram("SILENT") is True

    def test_ignores_punctuation(self):
        assert StringOps("a gentleman").is_anagram("elegant man") is True

    def test_ignores_whitespace(self):
        assert StringOps("dormitory").is_anagram("dirty room") is True

    def test_same_word(self):
        assert StringOps("race").is_anagram("race") is True

    def test_empty_strings(self):
        assert StringOps("").is_anagram("") is True

    def test_empty_vs_punctuation_only(self):
        assert StringOps("").is_anagram("!!!") is True

    def test_anagram_with_digits(self):
        assert StringOps("123").is_anagram("321") is True

    def test_unicode_letters(self):
        assert StringOps("café").is_anagram("éfac") is True


# ---------------------------------------------------------------- snake_case

class TestSnakeCase:
    def test_basic_spaces(self):
        assert StringOps("hello world").snake_case() == "hello_world"

    def test_single_word(self):
        assert StringOps("hello").snake_case() == "hello"

    def test_empty_string(self):
        assert StringOps("").snake_case() == ""

    def test_uppercase(self):
        assert StringOps("Hello World").snake_case() == "hello_world"

    def test_underscores_collapsed(self):
        assert StringOps("hello__world").snake_case() == "hello_world"

    def test_mixed_separators(self):
        assert StringOps("hello - world / foo,bar").snake_case() == "hello_world_foo_bar"

    def test_leading_and_trailing_separators_stripped(self):
        assert StringOps("  hello world  ").snake_case() == "hello_world"

    def test_leading_underscores_stripped(self):
        assert StringOps("__hello__").snake_case() == "hello"

    def test_only_punctuation(self):
        assert StringOps("!!! ???").snake_case() == ""

    def test_keeps_camel_case_intact(self):
        # Only \W and _ are replaced; camelCase boundaries are not split
        assert StringOps("camelCase").snake_case() == "camelcase"

    def test_unicode(self):
        assert StringOps("héllo wörld").snake_case() == "héllo_wörld"

    def test_digits(self):
        assert StringOps("version 2 beta").snake_case() == "version_2_beta"

    def test_tabs_and_newlines(self):
        assert StringOps("one\ttwo\nthree").snake_case() == "one_two_three"

    def test_single_separator_only(self):
        assert StringOps("_").snake_case() == ""

    def test_internal_digits_not_separated(self):
        assert StringOps("v2").snake_case() == "v2"


# --------------------------------------------------------------- constructor

class TestInit:
    def test_stores_text_verbatim(self):
        s = StringOps("  Raw Text  ")
        assert s.text == "  Raw Text  "

    def test_text_is_mutable_and_methods_follow_it(self):
        s = StringOps("one two")
        assert s.word_count() == 2
        s.text = "one two three"
        assert s.word_count() == 3

    def test_methods_do_not_mutate_text(self):
        s = StringOps("Hello World")
        s.to_title()
        s.snake_case()
        s.is_anagram("dlrow olleh")
        assert s.text == "Hello World"

    def test_instances_are_independent(self):
        a, b = StringOps("abc"), StringOps("xyz")
        assert a.snake_case() == "abc"
        assert b.snake_case() == "xyz"


# -------------------------------------------------------------- error paths

class TestErrorHandling:
    def test_word_count_non_string_raises(self):
        with pytest.raises(AttributeError):
            StringOps(None).word_count()

    def test_to_title_non_string_raises(self):
        with pytest.raises(AttributeError):
            StringOps(123).to_title()

    def test_find_all_invalid_pattern_raises(self):
        with pytest.raises(re.error):
            StringOps("abc").find_all(r"(unclosed")

    def test_is_anagram_non_string_other_raises(self):
        with pytest.raises(AttributeError):
            StringOps("abc").is_anagram(None)

    def test_snake_case_non_string_raises(self):
        with pytest.raises(TypeError):
            StringOps(42).snake_case()

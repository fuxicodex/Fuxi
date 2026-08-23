"""Well-implemented module. Your job is to WRITE TESTS for it (test generation)."""
import re


class StringOps:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())

    def to_title(self):
        return self.text.title()

    def find_all(self, pattern):
        return re.findall(pattern, self.text)

    def is_anagram(self, other):
        a = re.sub(r"\W", "", self.text.lower())
        b = re.sub(r"\W", "", other.lower())
        return sorted(a) == sorted(b)

    def snake_case(self):
        s = re.sub(r"[\W_]+", "_", self.text).strip("_").lower()
        return s

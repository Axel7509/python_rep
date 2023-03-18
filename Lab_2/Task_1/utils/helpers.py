
import re
from utils.constants import PUNCT_MARKS, TERM_MARKS
import utils.helpers as help


def remove_punctuation(text: str) -> str:

    return "".join(list(filter(lambda x: x not in PUNCT_MARKS + TERM_MARKS, text.strip())))


def is_word(word: str) -> bool:

    return word.isalnum() and not word.isdigit()


def get_words(text: str) -> list[str]:
    text = re.sub(r"[!?.,;:-]", ' ', text)
    words = list(filter(is_word, text.split()))

    return words


def count_characters(text: str) -> int:
    """Counts amount of all characters in words only"""

    words = get_words(text)

    return sum(len(word) for word in words)





from utils.constants import PUNCT_MARKS, TERM_MARKS


def is_word(word: str) -> bool:

    return word.isalnum() and not word.isdigit()


def remove_punctuation(text: str) -> str:

    return "".join(list(filter(lambda x: x not in PUNCT_MARKS + TERM_MARKS, text.strip())))


def average_word_length(text: str) -> int:

    words = list(filter(is_word, remove_punctuation(text).split()))

    return int(sum((map(len, words))) / len(words))








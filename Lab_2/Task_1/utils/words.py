
from utils.helpers import remove_punctuation


def is_word(word: str) -> bool:

    return word.isalnum() and not word.isdigit()


def average_word_length(text: str) -> int:

    words = list(filter(is_word, remove_punctuation(text).split()))

    return int(sum((map(len, words))) / len(words))

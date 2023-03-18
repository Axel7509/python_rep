

from utils.helpers import get_words
from utils.helpers import count_characters


def average_word_length(text: str) -> float:

    words = get_words(text)
    characters = count_characters(text)

    return characters / len(words)

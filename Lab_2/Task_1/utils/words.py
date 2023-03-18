
import re
from utils.helpers import get_words
from utils.helpers import count_characters
from utils.sentences import count_sentences


def average_word_length(text: str) -> float:

    words = get_words(text)
    characters = count_characters(text)

    return characters / len(words)


def average_sentence_length(text: str) -> float:
    """Counts average sentence-length in the text"""

    return len(get_words(text)) / count_sentences(text)
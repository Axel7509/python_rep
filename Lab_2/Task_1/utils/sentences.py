from utils.helpers import remove_punctuation
from utils.helpers import is_word
from utils.constants import TERM_MARKS, PUNCT_MARKS


def is_sentence(sentence: str) -> bool:
    sentence = remove_punctuation(sentence)

    return len(list(filter(is_word, sentence))) > 0



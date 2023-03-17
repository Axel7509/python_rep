

from utils.constants import PUNCT_MARKS, TERM_MARKS


def remove_punctuation(text: str) -> str:

    return "".join(list(filter(lambda x: x not in PUNCT_MARKS + TERM_MARKS, text.strip())))











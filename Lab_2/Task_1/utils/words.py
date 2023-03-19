
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


def top_k_n_grams(text: str, n: int = 4, k: int = 10) -> list[str]:
    """Returns top-K repeated N-grams in the text"""

    text = re.sub(r"[!?.,;:-]", '', text)
    words = get_words(text)
    n_grams = tuple(
        " ".join(words[i:i+n])
        for i in range(len(words)) if i + n <= len(words)
    )
    unique_n_grams = sorted(set(n_grams), key=n_grams.count, reverse=True)

    return unique_n_grams[:k]


from utils.constants import PUNCT_MARKS, TERM_MARKS


def is_word(word: str) -> bool:

    return word.isalnum() and not word.isdigit()


def remove_punctuation(text: str) -> str:

    return "".join(list(filter(lambda x: x not in PUNCT_MARKS + TERM_MARKS, text.strip())))


def average_word_length(text: str) -> int:

    words = list(filter(is_word, remove_punctuation(text).split()))

    return int(sum((map(len, words))) / len(words))


def counter_factory(punct_marks: tuple[str]) -> object:
    def sentence_counter(text) -> int:

        text_length = len(text)
        text += " "

        return sum(
            char in punct_marks and (text[ind + 1] not in punct_marks or ind >= len(text) - 1)
            for ind, char in zip(range(text_length), list(text))
        )

    return sentence_counter


# Sentence counters (all & non-declarative)
count_sentences = counter_factory(TERM_MARKS)
count_non_declarative = counter_factory(TERM_MARKS[1:])







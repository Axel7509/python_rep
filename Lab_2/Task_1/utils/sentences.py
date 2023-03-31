from utils.helpers import remove_punctuation
from utils.helpers import is_word
import re


def is_sentence(sentence: str) -> bool:
    sentence = remove_punctuation(sentence)

    return len(list(filter(is_word, sentence))) > 0


def count_sentences(text: str) -> int:

    return len(re.findall(r'(?<=\w)+([?!.])+(?= |$)', text))


def count_non_declarative(text: str) -> int:

    all_sent = re.findall(r'(?<=\w)+([?!.])+(?= |$)', text)
    decl_sent = re.findall(r'(?<=\w)+([.])+(?= |$)', text)

    return len(all_sent) - len(decl_sent)
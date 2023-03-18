import utils.helpers as help
from utils import words, sentences


def main():
    file = open('public/text.txt', encoding='utf-8')
    text = file.read()
    print(text)
    text = text.lower().replace('\n', ' ')
    print("\n", "#"*30, "\n")
    print(f"Average word length in text = {words.average_word_length(text)}")
    #print(f"Numbers of sentences in the text = {help.count_sentences(text)}")
    #print(f"Numbers of non-declarative sentences in the text = {help.count_non_declarative(text)}")


if __name__ == '__main__':
    main()


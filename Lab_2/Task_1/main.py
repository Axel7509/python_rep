import utils.helpers as help
from utils import words, sentences



def main():
    file = open('public/text.txt', encoding='utf-8')
    text = file.read()
    print(text)

    print("\n", "#"*30, "\n")

    print(f"Numbers of sentences in the text = {sentences.count_sentences(text)}")
    print(f"Numbers of non-declarative sentences in the text = {sentences.count_non_declarative(text)}")
    print(f"Average length of the word in the text = {words.average_word_length(text)}")
    print(f"Average length of the sentence = {words.average_sentence_length(text)}")


if __name__ == '__main__':
    main()


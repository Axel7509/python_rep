import utils.helpers as help


def main():
    file = open('public/text.txt', encoding='utf-8')
    text = file.read()
    print(text)
    print(f"Average word length in text = {help.average_word_length(text)}")


if __name__ == '__main__':
    main()


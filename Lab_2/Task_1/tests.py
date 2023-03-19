import unittest

from utils.words import (
    average_word_length,
    average_sentence_length,
    top_k_n_grams
)
from utils.sentences import (
    count_sentences,
    count_non_declarative
)


class TestAverageWordLength(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(average_word_length("  .. . .. !?? !? ? !? ?! "), 0)
        self.assertEqual(average_word_length(""), 0)

    def test_one_letter(self):
        self.assertEqual(average_word_length("A"), 1)

    def test_one_word_many_letters(self):
        self.assertEqual(average_word_length(
            "COOLBUGSFACTONEDAYYOUWILLANSWERFORYO- -URACTIONS"), 22.5)

    def test_many_words_many_letters(self):
        self.assertEqual(average_word_length("abba sus 124912 imp0ster"), 5)


class TestCountSentences(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(count_sentences(" .. . .. !??-- ? !? ! ?!a wire"), 0)
        self.assertEqual(count_sentences(""), 0)

    def test_one_sentence(self):
        self.assertEqual(count_sentences("a."), 1)

    def test_one_sentence_many_words(self):
        self.assertEqual(count_sentences(
            "COOL BUGS FACT: ONE 14 YOU WILL ___`14gaAB{}0 FOR YOUR ACT."), 1)

    def test_many_sentences_many_words(self):
        self.assertEqual(count_sentences(
            "a b. c?? abba!! abba, aboba... bobA AA..?   .! ? . sjf> as."), 6)


class TestCountNonDeclarative(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(count_non_declarative(" .. . .. !??-- ? !? ! ?!a wire"), 0)
        self.assertEqual(count_non_declarative(""), 0)

    def test_one_sentence(self):
        self.assertEqual(count_non_declarative("a...!??!!??!?!"), 1)

    def test_many_non_declarative_many_signs(self):
        self.assertEqual(count_non_declarative(
            "a...!?? ----!!?? a b!? c..!"), 3)

    def test_many_sentences_many_words(self):
        self.assertEqual(count_non_declarative(
            "a b. c?? abba!! abba, aboba... bobA AA..?   .! ? . sjf> as."), 3)


class TestAverageSentenceLength(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(average_sentence_length(""), 0)
        self.assertEqual(average_sentence_length(
            "  .. . . . .. !?? !?? ? !? ! ?! "), 0)

    def test_one_char_long(self):
        self.assertEqual(average_sentence_length("a...!??!!??!?!"), 1)
        self.assertEqual(average_sentence_length(" @-@. .?.?.?!  A. 14 "), 1)

    def test_two_sentences_many_words(self):
        self.assertEqual(average_sentence_length(
            """COOL BUGS 98123749812374 FACT. ONE DAY 14 YOU WILL."""), 12.5)

    def test_many_sentences_many_words(self):
        self.assertAlmostEqual(average_sentence_length(
            "a b. c? abba!! abba, .. bobA AA..? .! . ?. sjf> as."), 3.8)


class TestTopKNGrams(unittest.TestCase):
    def test_zero_result(self):
        self.assertEqual(top_k_n_grams(''), [])
        self.assertEqual(top_k_n_grams('. - 123 123 123 123 234 234 6 !!'), [])
        self.assertEqual(top_k_n_grams('akjsdnkjansdkjnasdkjn'), [])

    def test_one_n_gram(self):
        self.assertEqual(top_k_n_grams('a b c d'), ['a b c d'])

    def test_four_n_grams(self):
        self.assertEqual(
            top_k_n_grams('a b c d a b c d')[0],
            ['a b c d', 'b c d a', 'c d a b', 'd a b c'][0]
        )
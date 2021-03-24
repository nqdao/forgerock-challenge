import unittest

def get_longest_words(word_list):
    if not word_list:
        return []

    longest_words = []
    max_len = 0
    for word in word_list:
        if len(word) > max_len:
            max_len = len(word)
            longest_words = [word]
        elif len(word) == max_len:
            longest_words.append(word)

    return longest_words

def get_word_count(word_list):
    return len(word_list)

def get_average_length(word_list):
    if not word_list:
        return 0

    word_lengths = [len(word) for word in word_list]

    return sum(word_lengths)/len(word_lengths)

def get_unique_count(word_list):
    unique_words = []
    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)

    return len(unique_words)

def get_palindrome_count(word_list):
    count = 0
    for word in word_list:
        if word == word[::-1]:
            count += 1

    return count

class UnitTest(unittest.TestCase):
    def test_get_longest_words(self):
        input = ['hello', 'my', 'world']
        output = get_longest_words(input)
        expected = ['hello', 'world']
        self.assertEqual(output, expected)

    def test_get_longest_word_empty(self):
        input = []
        output = get_longest_words(input)
        expected = []
        self.assertEqual(output, expected)

    def test_get_word_count(self):
        input = ['hello', 'my', 'world']
        output = get_word_count(input)
        expected = 3
        self.assertEqual(output, expected)

    def test_get_word_count_empty(self):
        input = []
        output = get_word_count(input)
        expected = 0
        self.assertEqual(output, expected)

    def test_average_length(self):
        input = ['I', 'am', 'god']
        output = get_average_length(input)
        expected = 2
        self.assertEqual(output, expected)

    def test_average_length_empty(self):
        input = []
        output = get_average_length(input)
        expected = 0
        self.assertEqual(output, expected)

    def test_unique_count(self):
        input = ['hello', 'hello', 'world']
        output = get_unique_count(input)
        expected = 2
        self.assertEqual(output, expected)

    def test_unique_count_empty(self):
        input = []
        output = get_unique_count(input)
        expected = 0
        self.assertEqual(output, expected)

    def test_palindrome_count(self):
        input = ['civic', 'level', 'world']
        output = get_palindrome_count(input)
        expected = 2
        self.assertEqual(output, expected)

    def test_palindrome_count_empty(self):
        input = []
        output = get_palindrome_count(input)
        expected = 0
        self.assertEqual(output, expected)

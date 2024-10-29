import unittest
from data_structures import *

# I did one test per case ill keep on adding more test cases and push them
class MyTestCase(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([14, 3, 15, 7]), 15)
        self.assertEqual(find_max([10, 56, 89, 46, 15]), 89)
        self.assertEqual(find_max([15, 26]), 26)

    def test_find_min(self):
        self.assertEqual(find_min([26, 58, 52, 14]), 14)
        self.assertEqual(find_min([15]), 15)
    def test_special_characters(self):
        input_list = ['!', '@', '#', '1', '2', '3', '$', '%', '^']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, [])
        self.assertEqual(result_numbers, [1, 2, 3])
        
        self.assertEqual(find_min([19, 18, 24]), 18)

    def test_find_average(self):
        self.assertEqual(find_average([5, 10, 15, 10]), 10)
        self.assertEqual(find_average([5, 15]), 10)
        self.assertEqual(find_average([5]), 5)

    def test_find_all_even_numbers(self):
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5, 6]), (2, 4, 6))
        self.assertEqual(find_even_numbers([10, 9, 8, 7, 6, 5]), (10, 8, 6))
        self.assertEqual(find_even_numbers([1, 53, 51]), ())

    def test_find_all_odd_numbers(self):
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5]), (1, 3, 5))
        self.assertEqual(find_odd_numbers([2, 4, 6, 8]), ())
        self.assertEqual(find_odd_numbers([3, 2]), (3,))

    def test_find_total_number_of_even_numbers(self):
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5]), 2)
        self.assertEqual(find_number_of_even_numbers([1, 3, 5]), 0)
        self.assertEqual(find_number_of_even_numbers([2, 4, 6, 5, 2]), 4)

    def test_find_total_number_of_odd_numbers(self):
        self.assertEqual(find_number_of_odd_numbers([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_number_of_odd_numbers([12, 2, 14, 4, 2]), 0)
        self.assertEqual(find_number_of_odd_numbers([7, 5, 3, 4, 7]), 4)
        
    def test_return_list_stats(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = {
            "unique_numbers": {1, 2, 3, 4, 5},
            "min": 1,
            "max": 5,
            "average": 3.0,
            "even_numbers": (2, 4),
            "odd_numbers": (1, 3, 5),
            "number_of_even_numbers": 2,
            "number_of_odd_numbers": 3
        }
        self.assertEqual(return_list_stats(input_list), expected_output)

    def test_basic(self):
        input_list = ['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(result_numbers, [1, 3, 5])

    def test_mixed_input(self):
        input_list = ['a', '1', 'b', '3', 'c', '2', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(result_numbers, [1, 2, 3, 5])

    def test_repeated_characters(self):
        input_list = ['1', 'b', 'a', 'c', 'c', 'b', 'a', '1']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['a', 'b', 'c'])
        self.assertEqual(result_numbers, [1])

    def test_special_characters(self):
        input_list = ['!', '@', '#', '1', '2', '3', '$', '%', '^']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, [])
        self.assertEqual(result_numbers, [1, 2, 3])
        

    def test_more_special_characters(self):
        input_list = ['%', '&', '*', '4', '6', '8', '(', ')', '!', 'x']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['x'])
        self.assertEqual(result_numbers, [4, 6, 8])

    def test_generate_squared_dict(self):
        self.assertEqual(generate_squared_dict(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})

    def test_convert_word_list_sentence(self):
        text = "Fear cuts deeper than swords."
        self.assertEqual(convert_to_word_list(text), ['fear', 'cuts', 'deeper', 'than', 'swords.'])

    def test_letters_count_sentence(self):
        text = "Fear cuts deeper than swords."
        expected_output = {
            'a': 1, 'b': 0, 'c': 1, 'd': 3, 'e': 5, 'f': 1, 'g': 0, 'h': 1, 'i': 0,
            'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 1, 'p': 1, 'q': 0, 'r': 3,
            's': 3, 't': 2, 'u': 1, 'v': 0, 'w': 1, 'x': 0, 'y': 0, 'z': 0
        }
        self.assertEqual(letters_count_map(text), expected_output)

    #def test_text_to_morse(self):
    #def test_text_to_morse(self):

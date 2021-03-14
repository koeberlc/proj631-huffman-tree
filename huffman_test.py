import unittest
from main_program.constant import Constant
from main_program.huffman import Huffman

class Huffman_test(unittest.TestCase):
    def setUp(self):
        constant = Constant()
        compressed_text, average_storage_bit, list_char_freq, ratio = Huffman().compress("bonjour")
        self.compressed_text = compressed_text
        self.list_char_freq = list_char_freq
        self.ratio = ratio
        self.average_storage_bit = average_storage_bit

    def test_compressed_text(self):
        self.assertEqual(self.compressed_text, "0101110111001111011100000")

    def test_list_char_freq(self):
        self.assertEqual(self.list_char_freq, [('b', 1), ('n', 1), ('j', 1), ('u', 1), ('r', 1), ('o', 2), ('!', 2)])

    def test_ratio(self):
        self.assertEqual(round(self.ratio, 2), 0.65)

    def test_average(self):
        self.assertEqual(round(self.average_storage_bit, 2), 2.86)


if __name__ == '__main__':
    unittest.main()
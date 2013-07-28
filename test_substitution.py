import os
import unittest

from substitution import find_subs


class TestSubsitutionFunctions(unittest.TestCase):
    def setUp(self):
        self.word_list = open('words').read().splitlines()
        self.sample_targets = {"sky": "", "Zyzzogeton": ""}

    def test_find_subs(self):
        """It should return a result map with word -> word + 7, wrapping around the dictionary
        if need be.
        """

        res = find_subs(self.sample_targets, self.word_list)
        self.assertEqual(res["sky"], "skylark")
        self.assertEqual(res["Zyzzogeton"], "Aani")


if __name__ == '__main__':
    unittest.main()

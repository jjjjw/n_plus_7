import os
import unittest


class TestSubsitutionFunctions(unittest.TestCase):
    def setUp(self):
        words = open('words')
        self.word_list = words.read().splitlines()
        words.close()
        self.sample_targets = set(["sky", "Zyzzogeton",])

    def test_find_subs(self):
        """It should return a result map with word -> word + 7, wrapping around the dictionary
        if need be.

        """
        from substitution import find_subs

        res_gen = find_subs(self.sample_targets, self.word_list)

        res = next(res_gen)
        self.assertEqual(res[0], "sky")
        self.assertEqual(res[1], "skylark")

        res = next(res_gen)
        self.assertEqual(res[0], "Zyzzogeton")
        self.assertEqual(res[1], "Aani")


    def test_perf_subs(self):
        """It should return a text with the appropriate replacements, and one replacement per word.

        """
        from substitution import perf_subs

        res_gen = [("sky", "skylark"), ("skylark", "skyphoi")]  # Dynamically equivalent to a generator

        res = perf_subs("The sky is a skylark", res_gen)
        self.assertEqual(res, "The skylark is a skyphoi")


if __name__ == '__main__':
    unittest.main()

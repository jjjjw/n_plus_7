from nplus7 import NPlus7
from unittest import TestCase


class TestSubsitutionFunctions(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_sentence = "The sky above the port was the color of television, tuned to a dead channel."
        cls.sample_output = "Theban skylarker abracadabra theanthropist portague washableness theanthropist colorant offcut television, tunemaker toadery aba deader channel."
        cls.nplus7 = NPlus7()

    def test_n_plus_7(self):
        res = self.nplus7(self.sample_sentence)
        self.assertEqual(res, self.sample_output)


if __name__ == '__main__':
    from unittest import main

    main()

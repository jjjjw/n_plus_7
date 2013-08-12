from substitution import find_subs
from substitution import perf_subs


class NPlus7():
    @property
    def word_list(self) -> list:
        """A sorted list of English nouns.

        """
        if not hasattr(self, '_word_list'):
            words = open('words')  # TODO: nouns only
            self._word_list = sorted(words.read().splitlines())
            words.close()

        return self._word_list


    def __call__(self, text: str, n: int = 7) -> str:
        """Given a corpus, return a new corpus with every noun replaced by the nth noun following it.

        """
        # Compute the target words.
        tokens = text.split()  # TODO: word tokenizer
        targets = set(tokens)

        # Do substitutions
        subs = find_subs(targets, self.word_list, n)
        res = perf_subs(text, subs)

        return res

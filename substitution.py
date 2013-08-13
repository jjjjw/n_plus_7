from re import sub
from string import Template


def find_subs(targets: set, words: list, n: int) -> tuple:
    """Using the provided word dictionary and target set, yields a tuple (target_word, target_word + n).

    """
    word_len = len(words)

    for target in targets:
        try:
            i = words.index(target)
        except:
            continue

        step = i + n % word_len
        replacement = words[step]

        yield (target, replacement)


def perf_subs(text: str, subs: list) -> str:
    """Performs substitutions on the text, using the listed (target, replacement) tuples,
    returns a transformed copy of the text.

    """
    tmpl_map = {}
    tmpl_text = text.strip()  # Copy the string

    for target, replacement in subs:
        r_target = r"\b{}\b".format(target)
        tmpl_target = "$" + target
        tmpl_map[target] = replacement
        tmpl_text = sub(r_target, tmpl_target, tmpl_text)

    tmpl = Template(tmpl_text)
    transformed_text = tmpl.substitute(tmpl_map)

    return transformed_text

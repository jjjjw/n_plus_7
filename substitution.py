def make_word_dict(word_list: "list"):
    """Returns a beastly alphabetically ordered dict of the words.
    TODO: rabbit hole of case insensitivity

    """
    from collections import OrderedDict

    # word_list = [w.lower() for w in word_list]
    word_list.sort()
    word_range = range(len(word_list))
    return OrderedDict(zip(word_list, word_range))


def find_subs(targets: "set", word_dict: "ordereddict", n=7):
    """Using the provided word dictionary and target set, yields a tuple (target_word, target_word + n).

    """
    from math import fmod

    words = list(word_dict)
    word_len = len(words)

    for target in targets:
        i = word_dict.get(target)
        if i is None:
            continue

        step = int(fmod(i + n, word_len))
        replacement = words[step]
        yield (target, replacement)


def perf_subs(text: "string", subs: "generator"):
    """Performs substitutions on the text, using the generated (target, replacement) tuples,
    returns a transformed copy of the text.

    """
    from string import Template
    import re

    tmpl_map = {}
    tmpl_text = text.strip()  # Copy the string

    for target, replacement in subs:
        r_target = r"\b%s\b" % target
        tmpl_target = "$" + target
        tmpl_map[target] = replacement
        tmpl_text = re.sub(r_target, tmpl_target, tmpl_text)

    tmpl = Template(tmpl_text)
    transformed_text = tmpl.substitute(tmpl_map)
    return transformed_text

def find_subs(targets: "set", words: "list", n=7):
    """Using the provided word dictionary and target set, yields a tuple (target_word, target_word + n).

    """
    from math import fmod

    word_len = len(words)

    for target in targets:
        try:
            i = words.index(target)
        except:
            continue

        step = int(fmod(i + n, word_len))
        replacement = words[step]
        yield (target, replacement)


def perf_subs(text: "string", subs: "list"):
    """Performs substitutions on the text, using the listed (target, replacement) tuples,
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

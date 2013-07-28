def find_subs(targets: "set", word_list: "list", n=7):
    """Using the provided word list and target set, yields a tuple (target_word, target_word + n).

    """
    from itertools import cycle

    subs = {}

    for i, word in enumerate(cycle(word_list)):
        if word in targets:
            subs[i + n] = word

        target = subs.get(i)
        if target is not None:
            yield (target, word)


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

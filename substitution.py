def find_subs(targets, word_list, n=7):
    """Using the provided word list, find words n steps from the target words."""
    subs = {}

    for word, i in zip(word_list, range(len(word_list))):
        if targets.get(word) is not None:
            subs[i + n] = word

        target = subs.get(i)
        if target is not None:
            targets[target] = word

    return targets

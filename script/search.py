"""Search algorithms."""


def relevance(k, pattern):
    """Assign a value to 'k' to make it sortable, according to how closely k matches pattern.

    Pass this function to sort a list of strings according to its relevance matching a pattern:

    i.e. `results.sort(key=lambda word: relevance(word, pattern))`

    You need to use lambda or define a function to pass a pattern.

    Relevance:
        0 (most relevant): k == pattern
        1 (next relevant): pattern matches a full word, separated by spaces, inside 'k'.
        2...             : pattern is part of a word in 'k'. The more letters in word not in 'k',
                           the higher the result and less relevant it is.

    Examples:

        pattern == "star"

        k = "star"    -> 0
        k = "a star"  -> 1
        k = "start"   -> 2
        k = "restart" -> 4

    """

    text = k[k.rfind("-") + 1 :].replace("_", " ")
    i = text.find(pattern)
    if i == 0:
        # Highest match, weight is 0
        if len(text) == len(pattern):
            return 0
        # First word, separated by space. Next highest match.
        elif text[len(pattern)] == " ":
            return 1
        # Partial match.
        else:
            # We should order them alphabetically, but for now:
            diff = 0
            pos = len(pattern)
            while True:
                if len(text) == pos or text[pos] == " ":
                    break
                pos += 1
                diff += 1
            return 1 + diff
    else:
        if text[i - 1] == " ":
            # Full word match, but the string contains other words.
            if len(text) == i + len(pattern) or text[i + len(pattern)] == " ":
                return 1
            # Partial match.
            else:
                # We should order them alphabetically, but for now:
                diff = 0
                pos = i + len(pattern)
                while True:
                    if len(text) == pos or text[pos] == " ":
                        break
                    pos += 1
                    diff += 1
                return 1 + diff
        # Partial match.
        else:
            # We should order them alphabetically, but for now:
            diff = 0

            pos = i - 1
            while True:
                if pos < 0 or text[pos] == " ":
                    break
                pos -= 1
                diff += 1

            pos = i + len(pattern)
            while True:
                if len(text) == pos or text[pos] == " ":
                    break
                if text[pos] == " ":
                    break
                pos += 1
                diff += 1

            return 1 + diff


def simple_search(icons, pattern, max_el):
    """Icon name contains pattern."""

    findings = []

    if len(pattern) == 0:
        return findings

    # Find matches.
    for k in icons.keys():
        # Don't search in prefixes ("nv-xxx-") and allow to search for multiple space separated words.
        text = k[k.rfind("-") + 1 :].replace("_", " ")
        if text.find(pattern) > -1:
            # Add k to findings. The value "0" will be use to "weigh" the match.
            findings.append(k)

    findings.sort(key=lambda x: relevance(x, pattern))

    # TODO: by now, I'm returning no more than the elements that fit on the screen.
    # We need to return all the matches and allow to scroll.
    return findings[:max_el]


def fuzzy_search(icons, pattern, max_el):
    """A very basic bur working fuzzy search.
    The letters of pattern should appear in order, but don't need to be
    contiguous.
    i.e. 'cirle' will match 'circle'."""

    findings = []
    for key in icons.keys():
        pos = 0
        found = False
        for letter in pattern:
            if letter == " ":
                continue
            found = False
            for i in range(pos, len(key)):
                if letter == key[i]:
                    found = True
                    pos = i + 1
                    break
            if not found:
                break
        if found:
            findings.append(key)

    # Sort: full matches first.
    ordered_findings = []
    for i in range(len(findings)):
        if findings[i].find(pattern) > 0:
            ordered_findings.insert(0, findings[i])
        else:
            ordered_findings.append(findings[i])

    return ordered_findings[:max_el]

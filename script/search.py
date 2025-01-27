"""Search algorithms."""


def simple_search(icons, pattern, max_el):
    """Icon name contains pattern."""

    findings = []
    for k in icons.keys():
        if k.find(pattern) > 0:
            findings.append(k)
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

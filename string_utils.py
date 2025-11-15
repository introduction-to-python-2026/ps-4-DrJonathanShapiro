def split_at_digit(formula):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1


def split_before_each_uppercase(formula):
    parts = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i

    if formula:          
        parts.append(formula[start:])

    return parts

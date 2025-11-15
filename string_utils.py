def split_at_digit(formula):
    prefix = ""
    digits = ""

    for ch in formula:
        if ch.isdigit():
           digits += ch
        else:
            if digits:
                break
            prefix += ch

    if digits:
        return prefix, int(digits)
    else:
        return formula, 1

def split_before_each_uppercase(formula):
    parts = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i

    parts.append(formula[start:])   # Add the last chunk
    return parts


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


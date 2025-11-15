def split_at_digit(formula):
    prefix = ""
    digits = ""

    for ch in formula:
        if ch.isdigit():
            digits += ch
        else:
            # If digits already started and we hit a non-digit, stop collecting
            if digits:
                break
            prefix += ch

    if digits:
        return prefix, int(digits)
    else:
        return formula, 1

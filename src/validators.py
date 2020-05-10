def is_valid_number(str):
    try:
        integer = int(str) # Do not typecast the age variable before this line
    except ValueError:
        return False
    return True

def is_valid_float(str):
    try:
        flt = float(str) # Do not typecast the age variable before this line
    except ValueError:
        return False

    return True

import string


def alphabet_position(character):
    return string.ascii_letters.find(character) % 26


def rotate_string_13(text):
    rotated = ''
    for char in text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + string.ascii_uppercase[rotated_idx]
        else:
            rotated = rotated + string.ascii_lowercase[rotated_idx]
    return rotated


def rotate_character(char, rot):
    rotated_idx = (alphabet_position(char) + rot) % 26
    if char.isupper():
        return string.ascii_uppercase[rotated_idx]
    else:
        return string.ascii_lowercase[rotated_idx]


def rotate_string(text, rot):
    rotated = ''
    for char in text:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char
    return rotated

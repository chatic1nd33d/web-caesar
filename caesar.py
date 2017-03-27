def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    orichar = char
    char = char.lower()
    encrypted = ''
    if char == ' ':
        encrypted = encrypted + ' '
        return encrypted
    elif char not in alphabet:
        return char
    else:
        rotated_index = alphabet.index(char) + rot
        if rotated_index < 26:
            encrypted = encrypted + alphabet[rotated_index]
            if orichar in alphabet:
                return encrypted
            else:
                return encrypted.upper()
        else:
            encrypted = encrypted + alphabet[rotated_index % 26]
            if orichar in alphabet:
                return encrypted
            else:
                return encrypted.upper()

def encrypt(text, rot):
    encrypted = ""
    for char in text:
         newtext = rotate_character(char, rot)
         encrypted = encrypted + str(newtext)
    return encrypted

def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter = letter.lower()
    position = alphabet.index(letter)
    return position

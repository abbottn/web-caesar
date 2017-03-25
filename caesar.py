def alphabet_position(letter):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z']
    letter = letter.lower()
    return alphabet.index(letter)

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    uppercase = False
    if char.isupper():
        uppercase = True
        char = char.lower()
    if not char.isalpha():
        encrypted = encrypted + char
    else:
            rotated_index = alphabet_position(char) + rot
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = encrypted + alphabet[rotated_index % 26]
    if uppercase == True:
        encrypted = encrypted.upper()
    return encrypted

def encrypt(text, rot):
    ciphertext = ''
    for letter in text:
        ciphertext = ciphertext + rotate_character(letter, rot)
    return ciphertext

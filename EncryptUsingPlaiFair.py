def prepare_input(text):
    # Preprocessing the input text: removing spaces and converting to uppercase
    text = text.replace(" ", "")
    text = text.upper()

    # If the length of the text is odd, add a dummy character ('X')
    if len(text) % 2 != 0:
        text += "X"

    return text


def generate_key_matrix(key):
    # Generating the key matrix
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Excluding 'J'
    key_matrix = []
    for char in key + alphabet:
        if char not in key_matrix:
            key_matrix.append(char)

    # Reshaping the key matrix to a 5x5 grid
    key_matrix_grid = [key_matrix[i:i + 5] for i in range(0, 25, 5)]

    return key_matrix_grid


def find_char_positions(matrix, char):
    # Finding the positions of a character in the key matrix
    for i, row in enumerate(matrix):
        if char in row:
            return (i, row.index(char))
    return None


def encrypt(message, key):
    message = prepare_input(message)
    key_matrix = generate_key_matrix(key)

    # Encrypting the message
    encrypted_text = ""
    for i in range(0, len(message), 2):
        char1, char2 = message[i], message[i + 1]

        row1, col1 = find_char_positions(key_matrix, char1)
        row2, col2 = find_char_positions(key_matrix, char2)

        if row1 == row2:
            encrypted_text += key_matrix[row1][(col1 + 1) % 5]
            encrypted_text += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += key_matrix[(row1 + 1) % 5][col1]
            encrypted_text += key_matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += key_matrix[row1][col2]
            encrypted_text += key_matrix[row2][col1]

    return encrypted_text


def decrypt(ciphertext, key):
    key_matrix = generate_key_matrix(key)

    # Decrypting the message
    decrypted_text = ""
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]

        row1, col1 = find_char_positions(key_matrix, char1)
        row2, col2 = find_char_positions(key_matrix, char2)

        if row1 == row2:
            decrypted_text += key_matrix[row1][(col1 - 1) % 5]
            decrypted_text += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += key_matrix[(row1 - 1) % 5][col1]
            decrypted_text += key_matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += key_matrix[row1][col2]
            decrypted_text += key_matrix[row2][col1]

    return decrypted_text


# Example usage
message = "hello i am sanjay"
key = "monarchy"
encrypted_message = encrypt(message, key)
print("Encrypted:", encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted:", decrypted_message)

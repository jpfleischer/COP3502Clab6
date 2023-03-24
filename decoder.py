def decoder(encrypted_password):
    # password is an eight-digit number that will be encoded
    # each digit is shifted upwards by 3

    # convert to string

    # initialize empty encoded password
    decoded_password = ''
    encrypted_password = str(encrypted_password)

    # iterate through each character in string
    for character in encrypted_password:
        digit = int(character) - 3
        # subtract 3
        if digit <= -1:
            # the digit has spilled over to 10 or above, so take the last digit
            digit += 10
        decoded_password += str(digit)

    return int(decoded_password)

print(decoder("1234555"))
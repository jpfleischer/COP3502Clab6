# Jacques Fleischer
from decoder import decoder

def encode(password: int):
    # password is an eight-digit number that will be encoded
    # each digit is shifted upwards by 3
    # convert to string
    password = str(password)

    # initialize empty encoded password
    encoded = ''

    # iterate through each character in string
    for character in password:
        character = int(character)
        # add 3
        character += 3
        if character >= 10:
            # the digit has spilled over to 10 or above, so take the last digit
            character = str(character)[-1]
        encoded += str(character)

    return int(encoded)


def show_menu():
    # show a menu and return the user's selection
    return int(input('Menu\n'
                     '-------------\n'
                     '1. Encode\n'
                     '2. Decode\n'
                     '3. Quit\n'
                     '\n'
                     'Please enter an option: '))


def main():
    # initialize a bool that continues the while loop, as well as
    # empty variables for the encoded and decoded password
    continuing = True
    encoded = None
    decoded = None

    # main loop
    while continuing:
        selection = show_menu()
        if selection == 1:
            # encode
            decoded = int(input('Please enter your password to encode: '))
            encoded = encode(decoded)
            print('Your password has been encoded and stored!\n')
        if selection == 2:
            # decode
            if encoded and decoded:
                print(f'The encoded password is {encoded}, and the original password is {decoder(encoded)}.\n')
            else:
                # encoded and decoded are none, which means that the user has not entered anything
                print('You have not yet encoded a password!')
        if selection == 3:
            # quit
            exit()


if __name__ == '__main__':
    main()


import cs50
import sys
from sys import argv


def main():

    while True:
        if len(argv) == 2:
            break
        else:
            print("Usage: python vigenre key")
            sys.exit(1)

    key = argv[1]
    key_list = []
    if key.isalpha():
        key = key.lower()

    else:
        print("Usage: python vigenre key")
        sys.exit(1)


    ptxt = cs50.get_string("plaintext: ")

    print("ciphertext: ", end="")

    j = 0
    for ch in ptxt:
        if not ch.isalpha():
            print(ch, end="")
            continue

        offset = 65 if ch.isupper() else 97

        pi = ord(ch) - offset
        kj = ord(key[j % len(key)]) - 97
        ci = (pi + kj) % 26
        j += 1

        print(chr(ci + offset), end="")

    print("")


if __name__ == "__main__":
    main()
from cs50 import get_int

def main():

    height = get_positiv_int("Height: ")


    for i in range(1, height + 1):
        print(" " * (height - i) + ("#" * i) + "  " + ("#" * (i)))

def get_positiv_int(prompt):
    while True:
        n = get_int(prompt)
        if n <= 8 and n > 0:
            break
    return n


if __name__ == "__main__":
    main()
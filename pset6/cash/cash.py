import cs50


def main():

    while True:
        change = cs50.get_float("Change owed: ")
        if change > 0:
            break

    change = round(change * 100)

    q = change // 25  # quarters
    d = (change % 25) // 10  # dimes
    n = ((change % 25) % 10) // 5  # nickles
    p = ((change % 25) % 10) % 5  # pennies

    print(f"{q + d + n + p}")


if __name__ == "__main__":
    main()
import cs50
import sys


def main():

    while True:  # get card number
        cc_num = cs50.get_int("Enter card number: ")
        if cc_num > 0:
            break

    count_digits = 0
    number_check = cc_num
    while True:
        number_check = number_check // 10
        count_digits += 1
        if number_check <= 0:
            break

    if count_digits == 13 or count_digits == 15 or count_digits == 16:

        even_num = find_even_numbers(cc_num) #  checks card number
        odd_num = find_odd_numbers(cc_num)
        zum = add_products_x2(even_num) + sum(odd_num)

    else:
        print("INVALID")
        sys.exit(0)

    if (zum % 10 == 0):
        check(count_digits, cc_num)
    else:
        print("INVALID")
        sys.exit(2)


def find_even_numbers(number):

    numbers = []
    digit = 0
    number = number // 10
    while True:
        digit = number % 10
        number = number // 100
        numbers.append(digit)
        if number <= 0:
            break
    return numbers


def find_odd_numbers(number):

    numbers = []
    digit = 0
    while True:
        digit = number % 10
        number = number // 100
        numbers.append(digit)
        if number <= 0:
            break
    return numbers


def add_products_x2(list_x):  # multiplies numbers in list by 2 and adds the products together
    new_list = [i * 2 for i in list_x]

    product_digits = [((i % 10) + (i // 10)) for i in new_list]
    return(sum(product_digits))


def check(cd, cc_num):
    if cd == 13 and (cc_num // 1000000000000) == 4:
         print("VISA")
    elif cd == 16 and (cc_num // 1000000000000000) == 4:
        print("VISA")
    elif cd == 16 and (cc_num // 100000000000000) >= 51 and (cc_num // 100000000000000) <= 55:
        print("MASTERCARD")
    elif cd == 15 and (cc_num // 10000000000000) == 34 or (cc_num // 10000000000000) == 37:
        print("AMEX")


if __name__ == "__main__":
    main()
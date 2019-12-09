import cs50


#number = cs50.get_int("number: ")

def add_odd_numbers(number):

    numbers = []
    digit = 0
    while True:
        digit = number % 10
        number = number // 100
        numbers.append(digit)
        if number <= 0:
            break
    return numbers

listx = [1, 0, 0, 0, 0, 6, 0, 4]

listy = [i * 2 for i in listx]




def add_products_x2(listx):
    new_list = [i * 2 for i in listx]

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

cd = 16
cc_num = 4012888888881881
check(cd,cc_num)
import cs50

numbers = []

number = cs50.get_int("number: ")


digit = 0
number = number // 10
while True:
    digit = number % 10
    number = number // 100
    numbers.append(digit)
    if number <= 0:
        break




for digits in numbers:
    print(digits)



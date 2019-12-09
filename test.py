
user_number  = input("Enter your number ")
if user_number.isdigit():
    user_number = int(user_number) * 2
    print("int times two is " + str(user_number))
else:
    print("User input is string ")
            

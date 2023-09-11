def ask_for_input():
    number_picked = input("Pick a number: ")
    return number_picked

def echo_user_input(x):
    print(x)

def add_two_numbers(x,y):
    z = int(x) + int(y)
    print(z)

def multiply_three_numbers(x,y,z):
        return(int(x) * int(y) * int(z))

def determine_largest(x,y):
    if int(x) > int(y):
         print(x + " is larger")
    if int(x) < int(y):
         print(y + " is larger")
    if int(x) == int(y):
        print("Bruh")

a = ask_for_input()

echo_user_input(a)

add_two_numbers(ask_for_input(),ask_for_input())

product = multiply_three_numbers(ask_for_input(),ask_for_input(),ask_for_input())
echo_user_input(product)

determine_largest(ask_for_input(),ask_for_input())
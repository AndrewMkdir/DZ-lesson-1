n = input("Enter an integer: ")

while n < '0':
    print("I've asked for number greater than 0! Please try again!")
    n = input('Please enter number greater than 0: ')

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

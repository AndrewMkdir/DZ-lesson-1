num_init = int(input("Enter a positive integer: "))
greatest_dig = 0
num = num_init

while num > 0:
    digit = num % 10
    if digit > greatest_dig:
        greatest_dig = digit
        if greatest_dig == 9:
            break
    num = num // 10

print(f"The largest digit in the number {num_init} is equal to {greatest_dig}")

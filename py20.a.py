print("Prime Number Checking")
print("---------------------")
n = int(input("Enter the number: "))
print("Result:")

count = 0
for i in range(2, n):
    if n % i == 0:
        count += 1
        break  # No need to continue if a divisor is found

if n > 1 and count == 0:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

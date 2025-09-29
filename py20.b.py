print("Prime number generation")
print("-----------------------")
SN = int(input("Enter the starting number: "))
EN = int(input("Enter the ending number: "))
print("Result:")

for n in range(SN, EN + 1):
    if n > 1:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):  
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{n} is prime")
        else:
            print(f"{n} is not prime")
    else:
        print(f"{n} is not prime")

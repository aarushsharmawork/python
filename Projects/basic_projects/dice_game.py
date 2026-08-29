import random
b = int(input("Please enter your Number"))
a = random.randint(1,6)
if a == b:
    print("Yaah you won")
else:
    print("better luck next time. The number was:", a)
n = int(input("Enter the number: "))
for i in range (1,n+1):
    if i == 1 or n:
        print ("*"*n)
    else:
        print("*"," "*(n-2), "*")
        n = int(input("Enter the number: "))
spaces = n-2
space = " "
symbol = "#" 
for i in range(1,n+1):
    if i == 1 or i == (n):
        print(f"{symbol * n}")
    else:
        print(f"{symbol}{spaces * space}{symbol}")
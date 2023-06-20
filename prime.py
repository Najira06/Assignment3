number= int(input("Enter a number: "))
number>2
for n in range(2,int(number/2)+1 ):
    if number % n == 0:
        print(number, "is not a prime number")
        break
else:
    print(number, "is a prime number")
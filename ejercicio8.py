
num=int(input("Ingrese un numero: "))

for i in range(num):
    if i % 3==0:
        print("Fizz")
    if i % 5==0:
        print("Buzz")
    if i % 3==0 and num % 5==0:
        print ("FizzBuzz")
    

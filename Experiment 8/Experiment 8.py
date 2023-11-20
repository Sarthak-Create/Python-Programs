def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius*9/5)+32
    return fahrenheit

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit*5/9)-32
    return celcius

ch = int(input("Enter the choice:"))
while True:
    if ch ==1:
        num1=float(input("Enter temp in c:"))
        result = celcius_to_fahrenheit(num1)
        print(result)

    elif ch ==2:
        num1=float(input("Enter temp in f:"))
        result = fahrenheit_to_celcius(num1)
        print(result)

    else:
        print("Invalid")

number = 1
while number <= 100:
    number = number +1
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz") 
    elif number % 5 == 0:
        print("Fizz")
    elif number % 3 == 0:
        print("Buzz")
    else:
        print(number)

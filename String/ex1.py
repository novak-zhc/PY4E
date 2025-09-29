import string
fruit = 'banana'
number = len(fruit)
print(number)
while number > 0:
    letter = fruit[number-1]
    print(letter)
    number = number - 1


numbers = []
while True:
    usr_input = input('Please Enter a nubmer:')
    if usr_input == 'done':
        break
    num =float(usr_input)
    numbers.append(usr_input)

print(max(numbers))
print(min(numbers))


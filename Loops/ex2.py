minmum = None
maxmum = None
while True:
    usr_input = input('Enter a number:')
    if usr_input == 'done':
            break
    try:
        number = int(usr_input)
        if minmum is None or minmum > number:
            minmum = number
        if maxmum is None or maxmum < number:
            maxmum = number
             
    except:
        print('Invalid input')
print('Maximum is',maxmum)
print('Minimum is',minmum)
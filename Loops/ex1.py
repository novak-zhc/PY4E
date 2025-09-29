count = 0
total = 0
while True:
    usr_input = input('Enter a number:')
    if usr_input == 'done':
            break
    try:
        number = int(usr_input)
        count = count + 1
        total = total + number       
    except:
        print('Invalid input')
print(total,count,total/count)
    




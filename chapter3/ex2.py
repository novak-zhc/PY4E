hours = input('enter your hours:\n')
rate = input('enter your rates:')
price = 0
try:
    hours =float(hours)
    rate = float(rate)
    if hours <= 40:
        price = hours * rate
    else :
        price = 40 * rate + (hours - 40) * (rate * 1.5)

    print(price)
except:
    print('enter numbers')
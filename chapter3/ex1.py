hours = float(input('enter your hours:\n'))
rate = float(input('enter your rates:'))
price = 0
if hours <= 40:
    price = hours * rate
else :
    price = 40 * rate + (hours - 40) * (rate * 1.5)

print(price)



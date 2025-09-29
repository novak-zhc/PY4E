hour = float(input('enter your hours'))
rate = float(input('enter your rates'))
def computepay(hours,rates):
    if (hours > 40):
        salary = 40 * rates + (hours - 40) * 1.5 * rates
    else :
        salary = hours * rates
    return salary
print('Pay',computepay(hour,rate))
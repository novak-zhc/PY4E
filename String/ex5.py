data ='X-DSPAM-Confidence: 0.8475'
atpos = data.find(':')

number = data[atpos+1:]
number = float(number)
print(number)
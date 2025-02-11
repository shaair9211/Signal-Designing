import random

i=0
t=0

while t<54000:
    t+=1
    if random.random() < 0.00921:
        i+=1
        print(i)

print(i)


#1939 = 0.0355
#1676 = 0.031
#508 - 501 = 0.00921
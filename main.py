#add 10 random numbers and prints the answer
import random
zulu = 0
for i in range(1,10):
    i = random.randint(1,1000)
    zulu += i
print(zulu)
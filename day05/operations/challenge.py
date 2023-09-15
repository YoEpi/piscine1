import time
startingTime = time.time()
import random


list= random.sample(range(1,10000000), 1000000)



sorted_list = sorted(list)


duration = time.time()- startingTime
print(sorted_list[:100])
print (duration)


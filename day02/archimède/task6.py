n = 1
pi = 0

for i in range(1000000):

  if i % 2 == 0:
    pi += (1 / n)
  else:
    pi -= (1 / n)
  n += 2
  if n == 6: 
    break

pi *= 4

pi_appro = round (pi, 6)
print(pi_appro)
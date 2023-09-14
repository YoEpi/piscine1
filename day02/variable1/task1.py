
def summation(n):
    sum = 0     #stocker pour la somme des termes de la serie
    j = 1        #variable sera utilisée pour générer_termes_de_la_série.
     
    for i in range(1, n + 1):
        sum = sum + j
        j = (j * 10) + 1
         
    return sum
         

n = 9
print(summation(n))



for expo in range (1,8):
	result = sum ** expo
print(f"Sum {expo}: {result}")
      
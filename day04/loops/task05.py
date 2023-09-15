n = int(input("Enter an integer (n): "))

# Loop from 2 to n/2
for i in range(2, n // 2 + 1):
    multiples = []

    # Find multiples of i strictly smaller than n
    for j in range(n - 1, 0, -1):
        if j % i == 0:
            multiples.append(j)  #ajoute les j qui respectent la condition dans le tableau 

    # Display the multiples in descending order
    if multiples:
        print(" ".join(map(str, multiples)))     #converti les int en string multiples afin de printer

# Additional case for n itself
for k in range(n - 1, 0, -1):
    if k % n == 0:                         #  ctrl+/ pour commenter plusieurs ligne
        print(k)

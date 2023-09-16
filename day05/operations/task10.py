first_name = [ " Jackie " , " Bruce " , " Arnold " , " Sylvester " ]
last_name = [ " Stallone " , " Schwarzenegger " , " Willis " , " Chan " ]
magic = [* zip ( first_name , last_name [:: -1]) ]       #inversion de la liste lastname + association des listes
print ( magic [0])
print ( magic [3])
print ( magic [1][0])   # affiche le prenom 
print ( magic [0][1])  # affiche le nom
print ( magic [2])
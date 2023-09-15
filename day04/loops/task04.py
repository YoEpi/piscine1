beverage = "age-appropriate bottles"
for i in range(99, 0, -1):
    print(f"{i} {'bottle' if i == 1 else 'bottles'} of {beverage} on the wall,")
    print(f"{i} {'bottle' if i == 1 else 'bottles'} of {beverage}!")
    print("Take one down, pass it around,")
    print(f"{i - 1} {'bottle' if i - 1 == 1 else 'bottles'} of {beverage} on the wall.\n")
print("No more bottles of age-appropriate bottles on the wall.")

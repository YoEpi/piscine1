#DECHIFFRER:::::


string_base=str(input("Write your string: "))
user_key=str(input("Write your key: "))

len_base=len(string_base)
new_string=""

for i in range(len_base):
    new_char= user_key[i%len(user_key)]
    new_string+=new_char

print(new_string)
table_base=[]
table_new_string=[]
table_transformed=[]

for char in string_base:
    table_base.append(char)

for char in new_string:
    table_new_string.append(char)

print(table_base)
print(table_new_string)
for j in range (len_base):
    if table_base[j].isalpha():
        transformed_value=(ord(table_base[j])-ord(table_new_string[j]))
        # table_transformed.append((ord(table_base[j])-ord(table_new_string[j]))-97)
        if table_base[j].islower():
            transformed_value = (transformed_value % 26) + ord('a')
        else:
            transformed_value = (transformed_value % 26) + ord('A')

        table_transformed.append(chr(transformed_value))
    else:
        table_transformed.append(table_base[j])

string_transformed="".join(table_transformed)

print(string_transformed)
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
        table_transformed.append((ord(table_base[j]) + ord(table_new_string[j])) - 97)  # inversion 
        table_transformed[j]=chr(table_transformed[j])
    else:
        table_transformed.append(table_base[j])

string_transformed="".join(table_transformed)

print(string_transformed)
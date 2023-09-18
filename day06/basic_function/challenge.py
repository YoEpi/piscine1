import time 
x = int (input("number:"))
y = int(input("power:"))

def power(x,y):
    return(x**y)


start_time = time.time()
result = power(x, y)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"{x}^{y} = {result}")
print(f"Time taken to compute: {elapsed_time} seconds")
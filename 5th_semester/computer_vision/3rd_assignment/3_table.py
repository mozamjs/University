# (c) Write a program that prints a multiplication table for the given number.

num = int(input("Enter a number:"))
print(f"Multiplication table of {num}:")

for i in range (1, 11):
    # print(f"{num} x {i} = {num*i}") 
   print(num, "x", i, "=", num * i)
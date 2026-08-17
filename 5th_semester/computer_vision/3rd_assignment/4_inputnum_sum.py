# (d) Write a program that asks the user for a number n and prints the sum of the numbers 1 to n.

num = int(input("Enter a number:"))

sum = 0 

for i in range(1, num+1):
    sum = sum + i

print("sum from 1 to ", num, "is = ", sum)


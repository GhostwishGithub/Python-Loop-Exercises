#Python if else, for loop, and range() Exercises with Solutions
#Execise 1: Print first 10 natural numbers using while loop
#Extremely simple. A good warmup.
counter = 1
while counter <=10:
    print(counter)
    counter += 1

#Exercise 2: Print the following pattern
#They then provide a picture. It shouldn't be too hard.
row = 5
for counter1 in range(1, row + 1, 1):
    for counter2 in range(1, counter1 + 1):
        print(counter2, end=' ')
    print("")

# #Exercise 3: Calculate the sum of all numbers from 1 to a given number
# #just a simple bit of math between the loop and range
# s = 0
# n = int(input("Enter a number to be added all the way from 1: "))
# for i in range(1, n + 1, 1):
#     s += i
# print("\n")
# print("Sum is:", s)
#Commented out for expediency

#Exercise 4: Write a program to print multiplication table of a given number
#They actually meant the first 10, so good thing I read ahead
n = 2
for i in range(1, 11, 1):
    product = n * i
    print(product)

#Exercise 5: Display numbers from a list using a loop
'''They then give a series of instructions:
    The number must be divisible by five
    If the number is greater than 150, then skip it and move to the next number
    If the number is greater than 500, then stop the loop
    numbers = [12, 75, 150, 180, 145, 525, 50]
'''
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)
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
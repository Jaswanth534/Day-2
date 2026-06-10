
# loops 
# for loop & while loop

# for num in range(5):
#     print(num)

# for num in range(1, 6):
#     print(num)    

for num in range(0, 13, 4):
    print(num)

# loop through a string

name = 'Python'

for letter in name:
    print(letter)

# loop through a list

fruits = ['apple', 'banana', 'manago']

for fruit in fruits:
    print(fruit)

# Real function example

def print_nums(n):
    for num in range(1, n+1):
        print(num)
print_nums(6)


# while loop

count = 1

while count <= 10:
    print(count)
    count += 1

#infinite loop - a loop that runs indefinitely until a certain condition is met


# break statement

for num in range(1,11):
    if num == 5:
        break
    print(num)

#continue statement

for num in range(1, 11):
    if num == 5:
        continue
    print(num)


# sum of numbers 

total = 0

for num in range(1,6):
    total += num
    print(total)

#reusable code -  
def sum_of_nums(n):
    total = 0
    for num in range(1, n+1):
        total += num
    return total
print(sum_of_nums(10))
def average(numbers):
    "Return the average of a list of numbers"
    # YOUR CODE HERE
    #print(f"{numbers = }")
    # A + 8.0 = 8.0
    total = 0
    for number in numbers:
        #print(f"{number = }")
        total = total + number
        #print(f"{total = }")
    #print(f"{total = }")
    #print(f"{len(numbers) = }")
    return total/ len(numbers)

print(average([32, 78, 48, 71, 93, 71, 79, 44, 5, 42])) #56.3
print(average([5, 4, 3, 2, 1])) # 3.0
print(average([8.0, 3.14159, 17])) # 9.38053
import random

numberList = [random.randint(0, 100) for _ in range(24)]

print("Generated number list:", numberList)

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print("Maximum number in the list is:", find_max(numberList))
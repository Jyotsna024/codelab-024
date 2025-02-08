"""Write a Python function called find_largest() that takes a list of numbers as input and returns the
largest number from the list. Test the function with a sample list"""

def find_largest(numbers):
    if not numbers:  
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

sample_list = [10, 45, 32, 89, 22]
print("The largest number is:", find_largest(sample_list))

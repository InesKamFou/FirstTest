
#create a function that transforms a list of numbers into a list of strings
def transform(numbers):
    strings = []
    for i in numbers:
        strings.append(str(i))
    return strings
#create a list of numbers
numbers = [1, 2, 3, 4, 5]
#call the function
print(transform(numbers))
#call the function and print the result
print(transform([1, 2, 3, 4, 5]))

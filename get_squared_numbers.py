def get_squared_number(numbers):
    squared_number = []
    for n in numbers:
        squared_number.append(n*n)
    return squared_number

number = [2, 5, 7, 8, 9, 10]
print(get_squared_number(number))

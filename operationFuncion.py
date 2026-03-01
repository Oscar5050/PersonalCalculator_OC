import numpy as np

def addition():
    print("addition:")
    while True:
        try:
            num_array = np.array(input("Enter the numbers separated by space: ").split(), dtype=float)
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    return np.sum(num_array)

def subtraction():
    print("subtraction:")
    while True:
        try:
            num_array = np.array(input("Enter the numbers separated by space: ").split(), dtype=float)
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    return np.subtract(num_array[0], np.sum(num_array[1:]))

def multiplication():
    print("multiplication:")
    while True:
        try:
            num_array = np.array(input("Enter the numbers separated by space: ").split(), dtype=float)
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    return np.prod(num_array)

def division():
    print("division:")
    while True:
        try:
            num_array = np.array(input("Enter the numbers separated by space: ").split(), dtype=float)
            if 0 in num_array[1:]:
                print("Cannot divide by zero. Please enter valid numbers.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    result = num_array[0]
    for num in num_array[1:]:
        result /= num

    return result

import numpy as np

class new_operation:
    def __init__(self):
        self.operation_value  = np.array([0.0])

    def get_operation_value(self):
        value_text = np.array2string(self.operation_value)
        for i in value_text:
            if i in "[]":
                value_text = value_text.replace(i, "")
        return value_text

    def addition(self, value):
        while True:
            try:
                num_array = np.array(input("Enter the number: "), dtype=float)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        self.operation_value= np.add(value, num_array)
        return self.operation_value

    def subtraction(self, value):
        while True:
            try:
                num_array = np.array(input("Enter the number: "), dtype=float)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        self.operation_value = np.subtract(value, num_array)
        return self.operation_value

    def multiplication(self, value):
        while True:
            try:
                num_array = np.array(input("Enter the number: "), dtype=float)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        self.operation_value = np.multiply(value, num_array)
        return self.operation_value

    def division(self, value):
        while True:
            try:
                num_array = np.array(input("Enter the number: "), dtype=float)
                if num_array == 0:
                    print("Cannot divide by zero. Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        self.operation_value = np.divide(value, num_array)
        return self.operation_value

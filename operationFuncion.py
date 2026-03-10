import numpy as np

class new_operation:
    def __init__(self):
        self.memory_value  = np.array([0.0])

# Para una futura funcionalidad +M
    def get_memory_value(self):
        value_text = np.array2string(self.memory_value)
        for i in value_text:
            if i in "[]":
                value_text = value_text.replace(i, "")
        return value_text
    
    def set_memory_value(self, value):
        self.memory_value = value

    def reset_memory_value(self):
        self.memory_value = np.array([0.0])

    def execute_operation(self, value_1, value_2, operation_type):
        match operation_type:
            case 0:
                return self.addition(value_1, value_2)
            case 1:
                return self.subtraction(value_1, value_2)
            case 2:
                return self.multiplication(value_1, value_2)
            case 3:
                return self.division(value_1, value_2)

    def addition(self, value_1, value_2):
        self.memory_value = np.add(value_1, value_2)
        return self.memory_value

    def subtraction(self, value_1, value_2):
        self.memory_value = np.subtract(value_1, value_2)
        return self.memory_value

    def multiplication(self, value_1, value_2):
        self.memory_value = np.multiply(value_1, value_2)
        return self.memory_value

    def division(self, value_1, value_2):
        if value_2 == 0:
            print("Cannot divide by zero. Please enter a valid number.")
            return value_1
        self.memory_value = np.divide(value_1, value_2)
        return self.memory_value

import operationFuncion
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class main_window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.operation = operationFuncion.new_operation()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 200)

        self.value_label = QLabel(self.operation.get_operation_value(), self)
        self.value_label.setGeometry(50, 10, 200, 20)

        self.add_button = QPushButton("Addition", self)
        self.add_button.setGeometry(50, 30, 200, 30)
        self.add_button.clicked.connect(self.perform_addition)

        self.sub_button = QPushButton("Subtraction", self)
        self.sub_button.setGeometry(50, 70, 200, 30)
        self.sub_button.clicked.connect(self.perform_subtraction)

        self.mul_button = QPushButton("Multiplication", self)
        self.mul_button.setGeometry(50, 110, 200, 30)
        self.mul_button.clicked.connect(self.perform_multiplication)

        self.div_button = QPushButton("Division", self)
        self.div_button.setGeometry(50, 150, 200, 30)
        self.div_button.clicked.connect(self.perform_division)

    def update_value_label(self):
        self.value_label.setText(self.operation.get_operation_value())

    def perform_addition(self):
        result = self.operation.addition(self.operation.operation_value)
        print(f"Result: {result}")
        self.update_value_label()

    def perform_subtraction(self):
        result = self.operation.subtraction(self.operation.operation_value)
        print(f"Result: {result}")
        self.update_value_label()

    def perform_multiplication(self):
        result = self.operation.multiplication(self.operation.operation_value)
        print(f"Result: {result}")
        self.update_value_label()

    def perform_division(self):
        result = self.operation.division(self.operation.operation_value)
        print(f"Result: {result}")
        self.update_value_label()

    def close_event(self, event):
        QApplication.quit()
        event.accept()
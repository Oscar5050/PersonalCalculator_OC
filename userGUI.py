import operationFuncion
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 200)

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

    def perform_addition(self):
        result = operationFuncion.addition()
        print(f"Result: {result}")

    def perform_subtraction(self):
        result = operationFuncion.subtraction()
        print(f"Result: {result}")

    def perform_multiplication(self):
        result = operationFuncion.multiplication()
        print(f"Result: {result}")

    def perform_division(self):
        result = operationFuncion.division()
        print(f"Result: {result}")

    def closeEvent(self, event):
        QApplication.quit()
        event.accept()
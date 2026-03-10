import operationFuncion
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox

class main_window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.operation = operationFuncion.new_operation()
        self.display_value = np.array([0.0])
        self.support_value = np.array([0.0])
        self.op_status = False
        self.operation_type = None

        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 450)

# Sección de visualización

        self.value_label = QLabel(self.display_value.astype(str)[0], self)
        self.value_label.setGeometry(50, 10, 200, 20)

        self.operation_label = QLabel(str(self.operation_type), self)
        self.operation_label.setGeometry(50, 30, 200, 20)

# Sección de botones numéricos

        button_width, button_height = 50, 30
        spacing = 10
        base_x, base_y = 50, 50
        self.num_buttons = []
        for i in range(10):
            btn = QPushButton(str(i), self)
            row = i // 3
            col = i % 3
            x = base_x + col * (button_width + spacing)
            y = base_y + row * (button_height + spacing)
            btn.setGeometry(x, y, button_width, button_height)
            btn.clicked.connect(lambda checked, n=i: self.number_pressed(n))
            self.num_buttons.append(btn)

# Sección de botones de operaciones

        ops = [
            ("Addition", self.set_addition),
            ("Subtraction", self.set_subtraction),
            ("Multiplication", self.set_multiplication),
            ("Division", self.set_division),
        ]
        button_width, button_height = 200, 30
        spacing = 40
        base_x = 50
        base_y = 210
        self.op_buttons = []
        for idx, (label, handler) in enumerate(ops):
            btn = QPushButton(label, self)
            btn.setGeometry(base_x, base_y + idx * spacing, button_width, button_height)
            btn.clicked.connect(handler)
            self.op_buttons.append(btn)

        self.exe_button = QPushButton("Execute", self)
        self.exe_button.setGeometry(50, 370, 200, 30)
        self.exe_button.clicked.connect(lambda: self.execute_operation(self.support_value, self.display_value, self.operation_type))

# Métodos para configurar las operaciones

    def update_value_label(self, value):
        try:
            self.value_label.setText(value.astype(str)[0])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def number_pressed(self, n: int):
        try:
            if self.op_status:
                self.display_value = np.array([0.0])
                self.update_value_label(self.display_value)
                self.op_status = False
            current = float(self.display_value[0])
            new_val = current * 10 + n
            self.display_value = np.array([new_val])
            self.update_value_label(self.display_value)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}")

# Métodos para operar

    def set_addition(self):
        self.support_value = self.display_value
        self.operation_label.setText("Addition")
        self.op_status = True
        self.operation_type = 0

    def set_subtraction(self):
        self.support_value = self.display_value
        self.operation_label.setText("Subtraction")
        self.op_status = True
        self.operation_type = 1

    def set_multiplication(self):
        self.support_value = self.display_value
        self.operation_label.setText("Multiplication")
        self.op_status = True
        self.operation_type = 2

    def set_division(self):
        self.support_value = self.display_value
        self.operation_label.setText("Division")
        self.op_status = True
        self.operation_type = 3
    
    def execute_operation(self, value_1, value_2, operation_type):
        try:
            self.display_value = self.operation.execute_operation(value_1, value_2, operation_type)
            self.operation_type = None
            self.update_value_label(self.display_value)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def close_event(self, event):
        QApplication.quit()
        event.accept()
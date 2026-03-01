import userGUI
from PyQt6.QtWidgets import QApplication

def main_interface():
    app = QApplication([])
    window = userGUI.MainWindow()
    window.show()
    app.exec()
    return 0

if __name__ == "__main__":
    main_interface()

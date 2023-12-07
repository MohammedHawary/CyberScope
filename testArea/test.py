import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Button Search Example")
        self.setGeometry(100, 100, 300, 200)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a layout
        layout = QVBoxLayout(central_widget)

        # Create buttons with different text values
        button1 = QPushButton("Click Me", self)
        button2 = QPushButton("Press Me", self)
        button3 = QPushButton("Another Button", self)

        # Add the buttons to the layout
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        # Find the button by text "Press Me"
        target_text = "Click Me"
        found_button = self.find_button_by_text(target_text)

        if found_button:
            print(f"Button with text '{target_text}' found!")
        else:
            print(f"No button with text '{target_text}' found.")

    def find_button_by_text(self, target_text):
        for child in self.findChildren(QPushButton):
            if child.text() == target_text:
                return child
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

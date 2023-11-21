import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QScrollArea

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QScrollArea Background Color Example')

        # Create a QTextEdit widget to be placed inside the QScrollArea
        text_edit = QTextEdit(self)
        text_edit.setPlainText("This is a QTextEdit inside a QScrollArea. Scroll down to see more text." * 10)

        # Create a QScrollArea and set the background color using a stylesheet
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)  # Ensures that the widget inside the QScrollArea can resize
        scroll_area.setWidget(text_edit)

        # Set the background color of the QScrollArea using a stylesheet
        scroll_area.setStyleSheet("background-color: red;")

        # Create a QVBoxLayout to arrange the QScrollArea
        layout = QVBoxLayout(self)
        layout.addWidget(scroll_area)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())

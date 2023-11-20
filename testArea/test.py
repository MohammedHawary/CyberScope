from PyQt5.QtWidgets import QApplication, QMainWindow, QToolButton, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        tool_button = QToolButton(self)
        tool_button.setText('Options')

        menu = QMenu(self)

        # Add items to the menu
        action1 = QAction('Item 1', self)
        action2 = QAction('Item 2', self)
        action3 = QAction('Item 3', self)

        menu.addAction(action1)
        menu.addAction(action2)
        menu.addAction(action3)

        # Connect the triggered signal to a function
        action1.triggered.connect(lambda: self.on_action_triggered(action1))
        action2.triggered.connect(lambda: self.on_action_triggered(action2))
        action3.triggered.connect(lambda: self.on_action_triggered(action3))

        # Set the menu for the tool button
        tool_button.setMenu(menu)

        # Make the tool button a menu button
        tool_button.setPopupMode(QToolButton.MenuButtonPopup)

        # Set the background color for the arrow
        arrow_background_color = '#e74c3c'  # Change this to the desired color
        tool_button.setStyleSheet(f'''
            QToolButton::menu-indicator {{
                background-color: {arrow_background_color};
                width: 40px;
                height: 100%;
            }}
            QToolButton {{
                background-color: #3498db;
                color: #ffffff;
                border: 1px solid #2980b9;
                border-radius: 4px;
                padding: 5px;
            }}
            QToolButton::menu-arrow {{
                border: none;
                image: none;
            }}
        ''')

        # Set a custom arrow icon with a width of 40px and background color
        icon = QIcon('path/to/your/arrow-image.png')  # Replace with your arrow image
        pixmap = icon.pixmap(40, 40)
        pixmap.fill(Qt.transparent)  # Set the background color to transparent
        tool_button.setIcon(QIcon(pixmap))

        # Apply styles using QSS
        self.setStyleSheet('''
            QMenu {
                background-color: #2c3e50;
                border: 1px solid #34495e;
                padding: 5px;
            }

            QMenu::item {
                color: #ecf0f1;
            }

            QMenu::item:selected {
                background-color: #2980b9;
            }
        ''')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QToolButton Example')
        self.show()

    def on_action_triggered(self, action):
        print(f'Pressed: {action.text()}')

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()

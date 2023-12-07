import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QLabel, QLineEdit, QPushButton, QStackedWidget

class StackedWidgetExample(QWidget):
    def __init__(self):
        super(StackedWidgetExample, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Stacked Widget Example')

        # Create stacked widget
        self.stackedWidget = QStackedWidget(self)

        # Page 1
        page_1 = QWidget()
        label_1 = QLabel('Page 1 Content', page_1)
        page_1_layout = QVBoxLayout(page_1)
        page_1_layout.addWidget(label_1)
        self.stackedWidget.addWidget(page_1)

        # Page 2
        page_2 = QWidget()
        label_2 = QLabel('Page 2 Content', page_2)
        page_2_layout = QVBoxLayout(page_2)
        page_2_layout.addWidget(label_2)
        self.stackedWidget.addWidget(page_2)

        # Page 3
        page_3 = QWidget()
        label_3 = QLabel('Page 3 Content', page_3)
        page_3_layout = QVBoxLayout(page_3)
        page_3_layout.addWidget(label_3)
        self.stackedWidget.addWidget(page_3)

        # Page 4 with search bar and scroll area
        page_4 = QWidget()
        search_layout = QVBoxLayout(page_4)

        # Search bar
        search_bar = QLineEdit(page_4)
        search_layout.addWidget(search_bar)

        # Scroll area
        scroll_area = QScrollArea(page_4)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # Add some content to the scroll area (adjust as needed)
        for i in range(20):
            label = QLabel(f'Scroll Item {i}')
            scroll_layout.addWidget(label)

        scroll_area.setWidget(scroll_content)
        search_layout.addWidget(scroll_area)

        self.stackedWidget.addWidget(page_4)

        # Create navigation buttons
        btn_prev = QPushButton('Previous', self)
        btn_prev.clicked.connect(self.showPrevPage)

        btn_next = QPushButton('Next', self)
        btn_next.clicked.connect(self.showNextPage)

        # Layout for main window
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.stackedWidget)
        main_layout.addWidget(btn_prev)
        main_layout.addWidget(btn_next)

        self.show()

    def showPrevPage(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index > 0:
            self.stackedWidget.setCurrentIndex(current_index - 1)

    def showNextPage(self):
        current_index = self.stackedWidget.currentIndex()
        if current_index < self.stackedWidget.count() - 1:
            self.stackedWidget.setCurrentIndex(current_index + 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StackedWidgetExample()
    sys.exit(app.exec_())

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QScrollArea, QComboBox, QToolButton, QTextEdit, QTabWidget, QDialog, QHBoxLayout, QMainWindow, QWidget, QLineEdit, QAction, QPushButton, QLabel, QVBoxLayout, QStackedWidget, QDesktopWidget, QGridLayout, QMenu
from PyQt5.QtCore import QFile, QTextStream, Qt
from PyQt5.QtGui import QIcon
import DB

class MainWindow(QMainWindow):
    x = 1
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('MainWindow.ui', self)
        self.load_stylesheet("MainWindow.qss")
        self.setGeometry(500, 500, 500, 200)
        self.center_on_screen()
                    # initialize UI elements from UI file
                            # QWidget
        self.allWidgetsScan       = self.findChild(QWidget,        "allWidgetsScan"    )
        self.seconWidgets         = self.findChild(QWidget,        "seconWidgets"      )
        self.InputsWidget         = self.findChild(QWidget,        "InputsWidget"      )
        self.underTopBar          = self.findChild(QWidget,        "underTopBar"       )
        self.sidBar               = self.findChild(QWidget,        "sidBar"            )
        self.topBar               = self.findChild(QWidget,        "topBar"            )

        self.titleOfScansWidget   = self.findChild(QWidget,        "titleOfScansWidget")
        self.scan_1_widget        = self.findChild(QWidget,        "scan_1_widget"     )
        self.scan_2_widget        = self.findChild(QWidget,        "scan_2_widget"     )
        self.scan_3_widget        = self.findChild(QWidget,        "scan_3_widget"     )
        self.scan_4_widget        = self.findChild(QWidget,        "scan_4_widget"     )
        self.scan_5_widget        = self.findChild(QWidget,        "scan_5_widget"     )
        self.scan_6_widget        = self.findChild(QWidget,        "scan_6_widget"     )
        self.scan_7_widget        = self.findChild(QWidget,        "scan_7_widget"     )
        self.scan_8_widget        = self.findChild(QWidget,        "scan_8_widget"     )
        self.scan_9_widget        = self.findChild(QWidget,        "scan_9_widget"     )
        self.scan_10_widget       = self.findChild(QWidget,        "scan_10_widget"    )
        self.scan_11_widget       = self.findChild(QWidget,        "scan_11_widget"    )
        self.scan_12_widget       = self.findChild(QWidget,        "scan_12_widget"    )
        self.scan_13_widget       = self.findChild(QWidget,        "scan_13_widget"    )
        self.scan_14_widget       = self.findChild(QWidget,        "scan_14_widget"    )
        self.scan_15_widget       = self.findChild(QWidget,        "scan_15_widget"    )
        self.scan_16_widget       = self.findChild(QWidget,        "scan_16_widget"    )
        self.scan_17_widget       = self.findChild(QWidget,        "scan_17_widget"    )
        self.scan_18_widget       = self.findChild(QWidget,        "scan_18_widget"    )
        self.scan_19_widget       = self.findChild(QWidget,        "scan_19_widget"    )
                            # QStackedWidget
        self.pagesStackedWidget   = self.findChild(QStackedWidget, "pagesStackedWidget")
                            # QLabel
        self.cyberScopeLabel      = self.findChild(QLabel,          "cyberScopeLabel"  )
        self.myScansLabel         = self.findChild(QLabel,          "myScansLabel"     )
        self.logedInUserLabel     = self.findChild(QLabel,          "logedInUserLabel" )
        self.newFolderLbel        = self.findChild(QLabel,          "newFolderLbel"    )
                            # QPushButton
        self.createNewScan_btn    = self.findChild(QPushButton,     "createNewScan_btn")
        self.scansTopBar_btn      = self.findChild(QPushButton,     "scansTopBar_btn"  )
        self.logedUser_btn        = self.findChild(QPushButton,     "logedUser_btn"    )
        self.newFolder_btn        = self.findChild(QPushButton,     "newFolder_btn"    )
        self.allScans_btn         = self.findChild(QPushButton,     "allScans_btn"     )
        self.myScans_btn          = self.findChild(QPushButton,     "myScans_btn"      )
        self.newScan_btn          = self.findChild(QPushButton,     "newScan_btn"      )
        self.OWASP_btn_1          = self.findChild(QPushButton,     "OWASP_btn_1"      )
        self.OWASP_btn_2          = self.findChild(QPushButton,     "OWASP_btn_2"      )
        self.OWASP_btn_3          = self.findChild(QPushButton,     "OWASP_btn_3"      )
        self.trash_btn            = self.findChild(QPushButton,     "trash_btn"        )
        self.cancel_btn           = self.findChild(QPushButton,     "cancel_btn"       )
        self.back_btn             = self.findChild(QPushButton,     "back_btn"         )
        self.show_btn             = self.findChild(QPushButton,     "show_btn"         )
                            # QLineEdit
        self.targetInput          = self.findChild(QLineEdit,       "targetInput"      )
        self.nameInput            = self.findChild(QLineEdit,       "nameInput"        )
        self.searchInput          = self.findChild(QLineEdit,       "searchInput"      )
                            # QGridLayout
        self.gridLayout_8         = self.findChild(QGridLayout,     "gridLayout_8"     )
                            # QTabWidget
        self.tabWidgetForInputs   = self.findChild(QTabWidget,     "tabWidgetForInputs")
                            # QTextEdit
        self.descriptionInput     = self.findChild(QTextEdit,       "descriptionInput" )
                            # QComboBox
        self.folderInput          = self.findChild(QComboBox,       "folderInput"      )
                            # QToolButton
        self.save_btn             = self.findChild(QToolButton,     "save_btn"         )
                            # QScrollArea
        self.scrollArea           = self.findChild(QScrollArea,       "scrollArea"     )
        # self.scrollArea.setStyleSheet("background-color: white;")
                            # QLabel section
        self.logedUser_btn.setIcon(QIcon("png/profile-user.png"))
        self.logedUser_btn.setIconSize(self.logedUser_btn.size())
                            # QLabel section
        self.OWASP_btn_1.setIcon(QIcon("png/OWASP_TOP_10.png"))
        self.OWASP_btn_1.setIconSize(self.OWASP_btn_1.size())

                            # QPushButton section
        self.scansTopBar_btn.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(0))
        self.createNewScan_btn.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(1))
        self.newScan_btn.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(1))
        self.OWASP_btn_1.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(2))
        self.OWASP_btn_2.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(2))
        self.OWASP_btn_3.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(2))
        # self.trash_btn.clicked.connect(lambda: self.selected_btn(self.trash_btn,2))
        self.newFolder_btn.clicked.connect(self.AddNewFolderWindow)

        self.cancel_btn.clicked.connect(self.cancel_scan)
        self.save_btn.clicked.connect(self.save_scan)


        self.CreateAllFolders()
        all_buttons = self.sidBar.findChildren(QPushButton)
        all_buttons[1].setStyleSheet('''
                    border-left: 5px solid rgb(63, 174, 73);
                    background-color: rgb(222, 222, 222);
                    color: black;
                    border-radius: 5px;
                    height: 40px;
                    font-size: 15px;
                    text-align: left;
            ''')
                            # called func section
        DB.create_table()
        self.addTabSpace()
        self.search()
        self.show()
        self.showMaximized()

                            # pages section

        self.pagesStackedWidget.setCurrentIndex(7)
        self.pagesStackedWidget.currentChanged.connect(self.on_page_changed)

                            # different sections
        menu = QMenu(self)
        # Add items to the menu
        self.launch_btn = QAction('launch', self)

        menu.addAction(self.launch_btn)
        self.save_btn.setMenu(menu)
        self.save_btn.setPopupMode(QToolButton.MenuButtonPopup)
        self.launch_btn.triggered.connect(lambda: print("launch_btn pressed"))



        self.show_btn.clicked.connect(self.showing)


    def search(self):
        self.searchInput.setPlaceholderText("Search Scans")


    def showing(self):
        self.x += 1
        widgets = {2:self.scan_1_widget, 3:self.scan_2_widget, 4:self.scan_3_widget, 5:self.scan_4_widget,6:self.scan_5_widget,7:self.scan_6_widget,8:self.scan_7_widget,9:self.scan_8_widget,10:self.scan_9_widget,11:self.scan_10_widget}
        widgets[self.x].hide()


    def cancel_scan(self):
        self.nameInput.setText("")
        self.descriptionInput.setText("")
        self.targetInput.setText("")
        self.pagesStackedWidget.setCurrentIndex(1)

    def save_scan(self):
        print(f'name   => {self.nameInput.text()}')
        print(f'desc   => {self.descriptionInput.toPlainText()}')
        print(f'folder => {self.folderInput.currentText()}')
        print(f'target => {self.targetInput.text()}')

    def on_page_changed(self, index):
        if index == 0:
            self.back_btn.setText("")
            self.myScansLabel.setText(f"{DB.get_first_id_and_name()[1]}")
            self.back_btn.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(0))
        elif index == 1:
            self.back_btn.setText(f"< back to {DB.get_first_id_and_name()[1]}")
            self.myScansLabel.setText("Scan Templates")
            self.back_btn.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(DB.get_first_id_and_name()[0]))
        elif index == 2:
            self.back_btn.setText(f"< back to Scan Templates")
            self.myScansLabel.setText("New Scan / Web Application Test")
            self.back_btn.clicked.connect(lambda: self.pagesStackedWidget.setCurrentIndex(1))
    def AddNewFolderWindow(self):
        self.addNewFolderWindow = QDialog(self)
        self.addNewFolderWindow.setWindowTitle("Add New Folder")
        uic.loadUi('Dialog.ui',self.addNewFolderWindow)
        self.addNewFolderWindow.setWindowFlags(Qt.FramelessWindowHint)
        self.newFolderNameInput = self.addNewFolderWindow.findChild(QLineEdit,"newFolderNameInput")
        self.title_bar_widget   = self.addNewFolderWindow.findChild(QWidget,"title_bar_widget")
        self.create_btn         = self.addNewFolderWindow.findChild(QPushButton,"create_btn")
        self.warmingLabel       = self.addNewFolderWindow.findChild(QLabel,"warmingLabel")
        self.x_btn              = self.addNewFolderWindow.findChild(QPushButton,"x_btn")
        self.x_btn.clicked.connect(self.addNewFolderWindow.close)
        self.newFolderNameInput.setPlaceholderText("Enter new folder name")
        self.newFolderNameInput.setStyleSheet("font-size: 15px")

        self.x_btn.setStyleSheet('''
            #x_btn{
                text-align: right;
                background-color: rgb(58, 85, 108);
                border:none;
                height: 24px;
            }
            #x_btn:hover{
                color:red;
            }
            ''') 
        self.create_btn.setStyleSheet('''
                #create_btn{
                    background-color:rgb(37, 90, 136);
                    color:white;
                    font-size: 15px;
                    border-radius: 5px;
                }
                #create_btn:hover{
                    background-color:rgb(27, 65, 98);
                    font-size: 15px;
                }
            ''')      
        self.title_bar_widget.setStyleSheet('''
            #title_bar_widget{
                border-top: none;
                border: 2px solid rgb(229, 229, 229);
                border-radius: 5px;
            } 
            ''')

        screen_geometry = QDesktopWidget().screenGeometry()
        new_window_width = 613
        new_window_height = 121
        self.addNewFolderWindow.setGeometry(
            screen_geometry.width() // 2 - new_window_width // 2,
            screen_geometry.height() // 2 - new_window_height // 2,
            new_window_width,
            new_window_height
        )

        self.warmingLabel.setText("")
        self.warmingLabel.setStyleSheet("color:red;")
        self.newFolderNameInput.setFocus()

        self.newFolderNameInput.returnPressed.connect(lambda: self.create_new_button(self.newFolderNameInput.text()))
        self.create_btn.clicked.connect(lambda: self.create_new_button(self.newFolderNameInput.text()))
        self.addNewFolderWindow.exec_()
    def create_new_button(self,text):
        if not text.lstrip():
            self.warmingLabel.setText("Please Enter valid Name!")
            return
        elif len(text) > 20:
            self.warmingLabel.setText("Please Enter folder name between (_1 and 19_) charcter!")
            return

        newId = DB.get_last_element_id() + 1
        status_code = DB.insert_folder_data_if_not_exists(newId,text)
        if hasattr(self, 'addNewFolderWindow') and self.addNewFolderWindow is not None:        
            print(status_code)
            if status_code:
                self.warmingLabel.setText("Folder name already exists try another name!")
                return


        if hasattr(self, 'addNewFolderWindow') and self.addNewFolderWindow is not None:
            new_button = QPushButton(f'        {text.strip()}', self)
        else:
            new_button = QPushButton(f'{text.strip()}', self)

        context_menu = QMenu(self)
        delete_action = QAction("Delete", self)
        delete_action.triggered.connect(lambda _, button=new_button: self.deleteButton(button))
        context_menu.addAction(delete_action)
        new_button.setContextMenuPolicy(3)
        new_button.customContextMenuRequested.connect(
            lambda pos, button=new_button, menu=context_menu: self.showContextMenu(pos, button, menu)
        )


        last_row = self.gridLayout_8.rowCount()
        last_col = self.gridLayout_8.columnCount() - 1
        self.gridLayout_8.addWidget(new_button, last_row, last_col)
        new_button.setStyleSheet('''
            QPushButton{height: 40px;
            font-size: 15px;
            border: none;
            text-align: left;
            }
            QPushButton:hover{
                background-color: rgb(38, 55, 70);
                color: rgb(255, 255, 255);
            }
            ''')
        new_button.clicked.connect(self.LinkedAllFolders)

        if hasattr(self, 'addNewFolderWindow') and self.addNewFolderWindow is not None:
            # The variable has been initialized
            print("addNewFolderWindow is initialized.")
            self.addNewFolderWindow.close()

        new_button.setObjectName(text)
    def CreateAllFolders(self):
        data = DB.select_all_data()
        for row in data:
            self.create_new_button(row[1])
            if not row[1] == "All Scans":
                self.folderInput.addItem(row[1])


    def LinkedAllFolders(self,button):
        sender_button = self.sender()
        print(f"{sender_button.objectName()} pressed!")

        # if sender_button.objectName() == 


        all_buttons = self.sidBar.findChildren(QPushButton)

        for button in all_buttons:
            button.setStyleSheet('''
                    QPushButton{height: 40px;
                    font-size: 15px;
                    border: none;
                    text-align: left;
                    }
                    QPushButton:hover{
                        background-color: rgb(38, 55, 70);
                        color: rgb(255, 255, 255);
                    }
                ''')

        sender_button.setStyleSheet('''
                    border-left: 5px solid rgb(63, 174, 73);
                    background-color: rgb(222, 222, 222);
                    color: black;
                    border-radius: 5px;
                    height: 40px;
                    font-size: 15px;
                    text-align: left;
                ''')
        data = DB.select_all_data()

        for row in data:
            if row[1] == sender_button.objectName():
                self.pagesStackedWidget.setCurrentIndex(row[0])
    def deleteButton(self, button):
        button.deleteLater()
        DB.delete_folder_by_name(button.objectName())
    def showContextMenu(self, pos, button, menu):
        global_pos = button.mapToGlobal(pos)
        menu.exec_(global_pos)
    def addTabSpace(self):
        all_buttons = self.sidBar.findChildren(QPushButton)
        for button in all_buttons:
            button.setText(f"        {button.text()}")
            button.setContextMenuPolicy(3)
    def load_stylesheet(self, filename):
        style_file = QFile(filename)
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            content = stream.readAll()
            style_file.close()
            self.setStyleSheet(content)
        else:
            print(f"Failed to open {filename}")

    def center_on_screen(self):
        screen_geo = QDesktopWidget().screenGeometry()
        widget_geo = self.geometry()
        x = (screen_geo.width() - widget_geo.width()) // 5
        y = (screen_geo.height() - widget_geo.height()) // 3
        self.move(x, y)

app = QApplication([])
UiWindow = MainWindow()
app.exec_()
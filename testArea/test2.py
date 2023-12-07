        h_layout = QHBoxLayout()
        checkbox = QCheckBox()
        label_1 = QLabel("Label 1")
        h_layout.addWidget(checkbox, 1)
        h_layout.addWidget(label_1, 14)
        h_layout.setSpacing(20)

        h_layout2 = QHBoxLayout()
        label_2 = QLabel("Label 1")
        label_3 = QLabel("Label 1")
        h_layout2.addWidget(label_2, 7)
        h_layout2.addWidget(label_3, 2)

        main_layout = QGridLayout()
        btn1 = QPushButton("x")
        btn2 = QPushButton("/")
        main_layout.addWidget(btn2, 0, 2)
        main_layout.addWidget(btn1, 0, 3)
        main_layout.addLayout(h_layout, 0, 0)
        main_layout.addLayout(h_layout2, 0, 1)
            ####################################################
            #############                           ############
            #############        main_layout        ############
            #############                           ############
            ####################################################
        w_h_layout = QHBoxLayout()
        w_checkbox = QCheckBox()
        w_label_1 = QLabel("Label 1")
        w_h_layout.addWidget(w_checkbox, 1)
        w_h_layout.addWidget(w_label_1, 14)
        w_h_layout.setSpacing(20)

        w_h_layout2 = QHBoxLayout()
        w_label_2 = QLabel("Label 1")
        w_label_3 = QLabel("Label 1")
        w_h_layout2.addWidget(w_label_2, 7)
        w_h_layout2.addWidget(w_label_3, 2)

        w_main_layout = QGridLayout()
        w_btn1 = QPushButton("x")
        w_btn2 = QPushButton("/")
        w_main_layout.addWidget(w_btn2, 0, 2)
        w_main_layout.addWidget(w_btn1, 0, 3)
        w_main_layout.addLayout(w_h_layout, 0, 0)
        w_main_layout.addLayout(w_h_layout2, 0, 1)
            ####################################################
            #############                           ############
            #############       w_main_layout       ############
            #############                           ############
            ####################################################

        ParintLayout = QGridLayout()         #######> this is the main layout that all windget inside it 

        self.widget_2 = QWidget(self)
        self.widget_2.setStyleSheet('background-color: white;')
        self.widget_2.setLayout(w_main_layout)  # set layout of widget_2 with his elements


        self.widget_2w = QWidget(self)
        self.widget_2w.setStyleSheet('background-color: yellow;')
        self.widget_2w.setLayout(main_layout)  # set layout of widget_2w with his elements

                            # add widget will all element to main Virtival layout 
        main_v_layout.addWidget(self.widget_2)    
        main_v_layout.addWidget(self.widget_2w)


        main_v_layout = QVBoxLayout()  # create virtival layout to add all widget virticaly and set it as main layout for main widget 
        main_v_layout.addLayout(ParintLayout)

        self.MainWidget = QWidget(self) # Create Main widget 
        self.MainWidget.setLayout(main_v_layout) # add the main Virtical layout that contain all widget with his elements 
        self.MainWidget.setStyleSheet('background-color: red;')

        self.scrollArea.setWidget(self.MainWidget)

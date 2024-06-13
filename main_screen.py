from PyQt5 import QtCore, QtGui, QtWidgets
from operations import Operations

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.edit_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.edit_text.setGeometry(QtCore.QRect(10, 110, 761, 121))
        self.edit_text.setObjectName("edit_text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.cbox_operations = QtWidgets.QComboBox(self.centralwidget)
        self.cbox_operations.setGeometry(QtCore.QRect(180, 240, 300, 22))
        self.cbox_operations.setObjectName("cbox_operations")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 290, 1000, 400))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 769, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(800, 30, 181, 100))
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10) 
        self.gridLayout.setObjectName("gridLayout")

        self.label_varr1 = QtWidgets.QLabel(self.widget)
        self.label_varr1.setObjectName("label_varr1")
        self.label_varr1.setText("Word 1")
        self.gridLayout.addWidget(self.label_varr1, 0, 0, 1, 1)

        self.textbox_varr1 = QtWidgets.QLineEdit(self.widget)
        self.textbox_varr1.setObjectName("textbox_varr1")
        self.gridLayout.addWidget(self.textbox_varr1, 0, 1, 1, 1)

        self.label_varr2 = QtWidgets.QLabel(self.widget)
        self.label_varr2.setObjectName("label_varr2")
        self.label_varr2.setText("Word 2")
        self.gridLayout.addWidget(self.label_varr2, 1, 0, 1, 1)

        self.textbox_varr2 = QtWidgets.QLineEdit(self.widget)
        self.textbox_varr2.setObjectName("textbox_varr2")
        self.gridLayout.addWidget(self.textbox_varr2, 1, 1, 1, 1)

        self.gridLayout.setVerticalSpacing(0)

    
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.tableWidget)

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btnGet = QtWidgets.QPushButton(self.centralwidget)
        self.btnGet.setGeometry(QtCore.QRect(500, 240, 75, 23))
        self.btnGet.setObjectName("btnGet")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        Operations.getComboboxItem(self.cbox_operations)
        self.selected_item = 'Tokenize'
        Operations.labelNameInputs(self=self,selected_item=self.selected_item)

        self.btnGet.clicked.connect(self.returnResultButton)
        self.cbox_operations.currentIndexChanged.connect(self.handle_combobox_selection)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ana Sayfa"))
        self.label.setText(_translate("MainWindow", "Natural Language Processing Operations"))
        self.label_2.setText(_translate("MainWindow", "Text:"))
        self.btnGet.setText(_translate("MainWindow", "Return Result"))

    def returnResultButton(self):
        result = Operations.getSelectedItemToModel(self=self,selected_item=self.selected_item)
        self.display_result(result)

    def handle_combobox_selection(self):
        self.selected_item = self.cbox_operations.currentText()
        Operations.labelNameInputs(self=self,selected_item=self.selected_item)
    
    def display_result(self, result):
        if self.selected_item == 'Part of Speech Tagging':
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Word", "Tag"])
            
            for i, (word, tag) in enumerate(result):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(word))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(tag))
            
            self.tableWidget.resizeColumnsToContents()
        
        elif self.selected_item == 'Word Relationships in Text':
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(3)
            self.tableWidget.setHorizontalHeaderLabels(["Word 1", "Word 2", "Similarity"])

            for i, (word1, word2, similarity) in enumerate(result):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(word1))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(word2))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(similarity)))
            
            self.tableWidget.resizeColumnsToContents()

        elif self.selected_item == 'Finding Relationships Between Structures (WordNet)':
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(["Synset1 Name", "Synset1 Definition","Synset2 Name", "Synset2 Definition","Similarity"])

            for i, (syn1Name, syn1Def, syn2Name,syn2Def,Similarity) in enumerate(result):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(syn1Name))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(syn1Def))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(syn2Name))
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(syn2Def))
                self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(Similarity)))
            
            self.tableWidget.resizeColumnsToContents()

        elif self.selected_item == 'Word Density':
            self.tableWidget.setRowCount(len(result[2]))  
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Unique Word", "Frequency"])

            for i, (word, freq) in enumerate(result[2]):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(word))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(freq)))

        elif self.selected_item == 'Identify Phrases':
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Phrase", "Type"])

            for i, (phrase, phrase_type) in enumerate(result):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(phrase))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(phrase_type))

        elif self.selected_item == 'Identify Structural Elements':
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Element Type", "Content"])
            self.tableWidget.setRowCount(len(result))

            for i, (element_type, content) in enumerate(result):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(element_type))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(content))
        elif self.selected_item == 'Word Distribution':
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Word", "Following Words"])
            
            row = 0
            for word, freq_dist in result.items():
                most_common_following = ', '.join([f"{fw} ({f})" for fw, f in freq_dist.most_common(5)])
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(word))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(most_common_following))
                row += 1
        
        elif self.selected_item == 'Trigram Analysis':
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(["Trigram", "Frequency"])

            for row, (trigram, freq) in enumerate(result):
                trigram_str = ' '.join(trigram)
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(trigram_str))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(freq)))

        else:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setHorizontalHeaderLabels(["Result"])
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(result)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

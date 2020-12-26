import sys
import json
import time
import class_searchbar as sb
from app_modules import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QCompleter
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont


class AppDemo(QWidget):
    def __init__(self, for_people = True):
        super().__init__()
        self.list_ = []
        self.ui = Ui_MainWindow()
        self.for_people = for_people
        self.entryItem = 'l'
        self.input_search = []
        self.resize(600, 100)
        with open('test_database.json') as f:
        	data = json.load(f)
        
        if self.for_people:
            list_name = []
            for name in data['people']:
                list_name.append(name['nom'])
                list_name.append(name['prenom'])
        else:
        	list_name = []
        	for name in data['depliant']:
        		list_name.append(name['Prestation'])
        fnt = QFont('Open Sans', 12)
 
        mainLayout = QVBoxLayout()
 
        # input field
        self.input = QLineEdit()
        self.input.setFixedHeight(50)
        self.input.setFont(fnt)
        self.input.editingFinished.connect(self.addEntry)
        mainLayout.addWidget(self.input)
 
        self.model = QStandardItemModel()
        completer = QCompleter(self.model, self)
        self.input.setCompleter(completer)
 
        self.setLayout(mainLayout)

        for i in list_name:
        	if not self.model.findItems(i):
        		self.model.appendRow(QStandardItem(i.lower()))
        	else:
        		pass

    def addEntry(self):
        self.list_ = []
        self.entryItem = self.input.text()
        self.list_.append(self.entryItem)
        self.input.clear()
        self.close()



    def Show_wind(self, for_people):
        self.__init__(for_people)
        self.show()


# def launch_search_bar(for_people):
#     app = QApplication(sys.argv)
#     demo = AppDemo(for_people)
#     demo.Show_wind()
#     app.exec_()
#     print(list_[0])
#     return list_[0]

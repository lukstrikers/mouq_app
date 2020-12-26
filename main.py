################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

import sys
import platform
import time
import class_searchbar as sb
import test as t
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QStandardItem, QStandardItemModel)
from PySide2.QtWidgets import *

# GUI FILE
from app_modules import *

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.searcWindow = sb.AppDemo()
		self.ui.setupUi(self)

	        ## PRINT ==> SYSTEM
		print('System: ' + platform.system())
		print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
		UIFunctions.load_file(self)
		UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
		self.setWindowTitle('Main Window - Python Base')
		UIFunctions.labelTitle(self, 'Main Window - Python Base')
		UIFunctions.labelDescription(self, 'Set text')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
		startSize = QSize(1200, 800)
		self.resize(startSize)
		self.setMinimumSize(startSize)
		#UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
		self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
		self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.Update_nbr_client(self))

		self.ui.btn_add.clicked.connect(lambda: UIFunctions.button_LoginClicked(self))
		self.ui.btn_add.clicked.connect(lambda: UIFunctions.Update_nbr_client(self))

		self.ui.btn_modify.clicked.connect(lambda: UIFunctions.apply_modif_client(self))
		self.ui.btn_modify.clicked.connect(lambda: UIFunctions.Update_nbr_client(self))

		self.ui.pushButton_3.clicked.connect(lambda: UIFunctions.show_no_passeport_names(self))
		self.ui.pushButton_3.clicked.connect(lambda: UIFunctions.show_red_page(self))

		self.ui.pushButton_4.clicked.connect(lambda: UIFunctions.show_near_passeport_names(self))
		self.ui.pushButton_4.clicked.connect(lambda: UIFunctions.show_orange_page(self))


        ## ==> END ##

		UIFunctions.launch_combo_completion(self)

		self.ui.comboBox_16.currentIndexChanged[str].connect(lambda: UIFunctions.check_current_combobox_add(self))
		self.ui.comboBox_39.currentIndexChanged[str].connect(lambda: UIFunctions.check_current_combobox_mod(self))

		self.ui.comboBox_16.currentIndexChanged[str].connect(lambda: UIFunctions.change_name_presta_from_add(self))
		self.ui.comboBox_2.currentIndexChanged[str].connect(lambda: UIFunctions.change_name_presta_from_add(self))
		self.ui.comboBox_11.currentIndexChanged[str].connect(lambda: UIFunctions.change_name_presta_from_add(self))
		self.ui.comboBox_13.currentIndexChanged[str].connect(lambda: UIFunctions.change_name_presta_from_add(self))
		self.ui.comboBox_20.currentIndexChanged[str].connect(lambda: UIFunctions.change_name_presta_from_add(self))
		self.ui.comboBox_22.currentIndexChanged[str].connect(lambda: UIFunctions.change_name_presta_from_add(self))

		self.ui.comboBox_4.currentIndexChanged[str].connect(lambda: UIFunctions.change_name_presta_from_mod(self))
		self.ui.comboBox_31.currentIndexChanged[str].connect(lambda: UIFunctions.change_name_presta_from_mod(self))
		self.ui.comboBox_33.currentIndexChanged[str].connect(lambda: UIFunctions.change_name_presta_from_mod(self))
		self.ui.comboBox_35.currentIndexChanged[str].connect(lambda: UIFunctions.change_name_presta_from_mod(self))
		self.ui.comboBox_37.currentIndexChanged[str].connect(lambda: UIFunctions.change_name_presta_from_mod(self))
        ## ==> ADD CUSTOM MENUS
		self.ui.stackedWidget.setMinimumWidth(20)
		UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
		UIFunctions.addNewMenu(self, "Recherche client", "btn_search_client", "url(:/16x16/icons/16x16/cil-magnifying-glass.png)", True)
		UIFunctions.addNewMenu(self, "Ajouter client", "btn_add_client", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
		UIFunctions.addNewMenu(self, "Supprimer client", "btn_suppr_client", "url(:/16x16/icons/16x16/cil-remove.png)", True)
		UIFunctions.addNewMenu(self, "Modifier client", "btn_modify_client", "url(:/16x16/icons/16x16/cil-keyboard.png)", True)
		UIFunctions.addNewMenu(self, "Rechercher prestation", "btn_search_presta", "url(:/16x16/icons/16x16/cil-zoom-in.png)", True)
		UIFunctions.addNewMenu(self, "Voir prestations", "btn_see_presta", "url(:/16x16/icons/16x16/cil-options-horizontal.png)", True)
		UIFunctions.addNewMenu(self, "Custom Widgets", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
		UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
		self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
		UIFunctions.userIcon(self, "PB", "", True)
        ## ==> END ##

		self.ui.frame_18.hide()
		self.ui.frame_19.hide()
		self.ui.frame_20.hide()
		self.ui.frame_23.hide()
		self.ui.frame_24.hide()

		self.ui.frame_25.hide()
		self.ui.frame_32.hide()
		self.ui.frame_33.hide()
		self.ui.frame_34.hide()
		self.ui.frame_35.hide()

		self.ui.frame_17.hide()
		self.ui.frame_26.hide()
		self.ui.frame_27.hide()
		self.ui.frame_28.hide()
		self.ui.frame_29.hide()


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
		def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
			if UIFunctions.returStatus() == 1:
			    UIFunctions.maximize_restore(self)

            # MOVE WINDOW
			if event.buttons() == Qt.LeftButton:
			    self.move(self.pos() + event.globalPos() - self.dragPos)
			    self.dragPos = event.globalPos()
			    event.accept()

        # WIDGET TO MOVE
		self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
		UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################


		self.ui.label_url.setText('<a href="https://www.lebienetre.fr/mouquet-s-ethique/wasquehal/fiche/lille/6106/FR"> Le Bien Être</a>')
		UIFunctions.Update_nbr_client(self)

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
		self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
		self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
	def Button(self):
        # GET BT CLICKED
		btnWidget = self.sender()

        # PAGE HOME
		if btnWidget.objectName() == "btn_home":
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
			UIFunctions.resetStyle(self, "btn_home")
			UIFunctions.labelPage(self, "Home")
			btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
			UIFunctions.Update_nbr_client(self)

        # PAGE SEARCH CLIENT
		if btnWidget.objectName() == "btn_search_client":
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_client)
			UIFunctions.resetStyle(self, "btn_search_client")
			UIFunctions.labelPage(self, "Recherche client")
			btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
			UIFunctions.searchBar(self, True, True, False, False)
			UIFunctions.Update_nbr_client(self)


 		# PAGE ADD CLIENT
		if btnWidget.objectName() == "btn_add_client":
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_add_client)
			UIFunctions.resetStyle(self, "btn_add_client")
			UIFunctions.labelPage(self, "Ajouter client")
			btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
			UIFunctions.Update_nbr_client(self)


        # PAGE SUPPR CLIENT
		if btnWidget.objectName() == "btn_suppr_client":
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_suppr_client)
			UIFunctions.resetStyle(self, "btn_suppr_client")
			UIFunctions.labelPage(self, "Supprimer client")
			btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
			UIFunctions.searchBar(self, True, False, True, False)
			UIFunctions.Update_nbr_client(self)


		# PAGE MODIFY CLIENT
		if btnWidget.objectName() == "btn_modify_client":
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_modif_client)
			UIFunctions.resetStyle(self, "btn_suppr_client")
			UIFunctions.labelPage(self, "Mofifier client")
			btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
			UIFunctions.searchBar(self, True, False, False, True)
			UIFunctions.Update_nbr_client(self)


		# PAGE SEARCH PRESTA
		if btnWidget.objectName() == "btn_search_presta":
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_search_presta)
			UIFunctions.resetStyle(self, "btn_search_presta")
			UIFunctions.labelPage(self, "Rechercher prestation")
			btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
			UIFunctions.searchBar(self, False, False, False, False)
			UIFunctions.Update_nbr_client(self)


		# PAGE SEE PRESTA
		if btnWidget.objectName() == "btn_see_presta":
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_see_presta)
			UIFunctions.resetStyle(self, "btn_see_presta")
			UIFunctions.labelPage(self, "Voir prestation")
			btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
			UIFunctions.Update_nbr_client(self)

            

        # PAGE WIDGETS
		if btnWidget.objectName() == "btn_widgets":
			self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
			UIFunctions.resetStyle(self, "btn_widgets")
			UIFunctions.labelPage(self, "Custom Widgets")
			btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
			UIFunctions.Update_nbr_client(self)


    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
	#def eventFilter(self, watched, event):
		# if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
		# 	print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
	def mousePressEvent(self, event):
		self.ui.label_27.setText("")
		self.dragPos = event.globalPos()
		# if event.buttons() == Qt.LeftButton:
		# 	print('Mouse click: LEFT CLICK')
		# if event.buttons() == Qt.RightButton:
		# 	print('Mouse click: RIGHT CLICK')
		# if event.buttons() == Qt.MidButton:
		# 	print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################

	def keyPressEvent(self, event):
		#print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
		if event.key() == 16777220 and self.ui.stackedWidget.currentWidget().objectName() == 'page_client':
			UIFunctions.searchBar(self, True, True, False, False)

		elif event.key() == 16777220 and self.ui.stackedWidget.currentWidget().objectName() == 'page_suppr_client':
			UIFunctions.searchBar(self, True, False, True, False)
			UIFunctions.apply_modif_client(self)

			self.ui.label_27.setText("Le client à bien été supprimé")

		elif event.key() == 16777220 and self.ui.stackedWidget.currentWidget().objectName() == 'page_modif_client':
			UIFunctions.modify_client(self, t.get_info(UIFunctions.searchBar(self, True, False, False, True))[0])
		elif event.key() == 16777220 and self.ui.stackedWidget.currentWidget().objectName() == 'page_search_presta':
			UIFunctions.searchBar(self, False, False, False, False)
		# elif event.key() == 16777220 and self.ui.stackedWidget.currentWidget().objectName() == 'page_test':
		# 	UIFunctions.check_current_comboboxes(self)
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
	def resizeEvent(self, event):
		self.resizeFunction()
		return super(MainWindow, self).resizeEvent(event)

	def resizeFunction(self):
		print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())

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

## ==> GUI FILE
from main import *
import test as t
import json
import shutil

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1

class UIFunctions(MainWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True
    def __init__(self):
        self.name_info = ''

    ########################################################################
    ## START - GUI FUNCTIONS
    ########################################################################

    ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(110, 95, 96)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(110, 95, 96, 200)")
            self.ui.frame_size_grip.show()

    ## ==> RETURN STATUS
    def returStatus():
        return GLOBAL_STATE

    ## ==> SET STATUS
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## ==> ENABLE MAXIMUM SIZE
    ########################################################################
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()


    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    ## ==> HEADER TEXTS
    ########################################################################
    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    ## ==> DYNAMIC MENUS
    ########################################################################
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(count),self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    ## ==> SELECT/DESELECT MENU
    ########################################################################
    ## ==> SELECT
    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(110, 95, 96); }")
        return select

    ## ==> DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(110, 95, 96); }", "")
        return deselect

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    ## ==> CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    ## ==> USER ICON
    ########################################################################
    def userIcon(self, initialsTooltip, icon, showHide):
        if showHide:
            # SET TEXT
            self.ui.label_user_icon.setText(initialsTooltip)

            # SET ICON
            if icon:
                style = self.ui.label_user_icon.styleSheet()
                setIcon = "QLabel { background-image: " + icon + "; }"
                self.ui.label_user_icon.setStyleSheet(style + setIcon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initialsTooltip)
        else:
            self.ui.label_user_icon.hide()

    ########################################################################
    ## END - GUI FUNCTIONS
    def button_LoginClicked(self): 
        nom = (self.ui.lineEdit_22.text())
        prenom = (self.ui.lineEdit_24.text())
        birthdate = (self.ui.lineEdit_28.text())
        tel = (self.ui.lineEdit_25.text())
        adresse = (self.ui.lineEdit_23.text())
        mail = (self.ui.lineEdit_31.text())
        id_bien_etre = (UIFunctions.clear_comboBox(self))
        mode_regl = (self.ui.lineEdit_26.text())
        date_regl = (self.ui.lineEdit_27.text())
        reste_payer = (self.ui.lineEdit_30.text())
        divers = (UIFunctions.get_reste_presta(self))
        list_com = [self.ui.comboBox_16.currentIndex(),
                    self.ui.comboBox_2.currentIndex(),
                    self.ui.comboBox_10.currentIndex(),
                    self.ui.comboBox_11.currentIndex(),
                    self.ui.comboBox_12.currentIndex(),
                    self.ui.comboBox_13.currentIndex(),
                    self.ui.comboBox_14.currentIndex(),
                    self.ui.comboBox_20.currentIndex(),
                    self.ui.comboBox_21.currentIndex(),
                    self.ui.comboBox_22.currentIndex(),
                    self.ui.comboBox_23.currentIndex(),
                    [self.ui.label_17.text(), self.ui.comboBox_3.currentIndex(), self.ui.textEdit_3.toPlainText()],
                    [self.ui.label_21.text(), self.ui.comboBox_5.currentIndex(), self.ui.textEdit_2.toPlainText()],
                    [self.ui.label_32.text(), self.ui.comboBox_6.currentIndex(), self.ui.textEdit.toPlainText()],
                    [self.ui.label_35.text(), self.ui.comboBox_7.currentIndex(), self.ui.textEdit_4.toPlainText()],
                    [self.ui.label_49.text(), self.ui.comboBox_8.currentIndex(), self.ui.textEdit_5.toPlainText()]]
        real_divers = self.ui.lineEdit_21.toPlainText()
        if prenom =='':
            return
        else:
            t.add_person(nom, prenom, birthdate, tel, adresse, mail, id_bien_etre, mode_regl, date_regl, reste_payer, divers, list_com, real_divers)
            self.ui.lineEdit_22.setText("")
            self.ui.lineEdit_24.setText("")
            self.ui.lineEdit_28.setText("")
            self.ui.lineEdit_25.setText("")
            self.ui.lineEdit_23.setText("")
            self.ui.lineEdit_31.setText("")
            UIFunctions.clear_comboBoxes(self)
            self.ui.lineEdit_26.setText("")
            self.ui.lineEdit_27.setText("")
            self.ui.lineEdit_30.setText("")
            self.ui.lineEdit_21.setText("")

    def modify_client(self, json_file_list):
        count = 1
        for i in json_file_list:
            for key in i.keys():
                if key == 'nom':
                    self.ui.lineEdit_35.setText(i[key])
                    self.name_info = i[key]
                elif key == 'prenom':
                    self.ui.lineEdit_39.setText(i[key])
                elif key == 'date de naissance':
                    self.ui.lineEdit_42.setText(i[key])
                elif key == 'Num Tel':
                    self.ui.lineEdit_32.setText(i[key])
                elif key == 'Adresse':
                    self.ui.lineEdit_41.setText(i[key])
                elif key == 'Mail':
                    self.ui.lineEdit_36.setText(i[key])
                elif key == 'Identifiant Bien Etre':
                    self.ui.comboBox_39.setCurrentIndex(i['list com'][0])
                    self.ui.comboBox_4.setCurrentIndex(i['list com'][1])
                    self.ui.comboBox_30.setCurrentIndex(i['list com'][2])
                    self.ui.comboBox_31.setCurrentIndex(i['list com'][3])
                    self.ui.comboBox_32.setCurrentIndex(i['list com'][4])
                    self.ui.comboBox_33.setCurrentIndex(i['list com'][5])
                    self.ui.comboBox_34.setCurrentIndex(i['list com'][6])
                    self.ui.comboBox_35.setCurrentIndex(i['list com'][7])
                    self.ui.comboBox_36.setCurrentIndex(i['list com'][8])
                    self.ui.comboBox_37.setCurrentIndex(i['list com'][9])
                    self.ui.comboBox_38.setCurrentIndex(i['list com'][10])
                elif key == 'mode de reglement':
                    self.ui.lineEdit_33.setText(i[key])
                elif key == 'date de reglement':
                    self.ui.lineEdit_38.setText(i[key])
                elif key == 'reste a payer':
                    self.ui.lineEdit_37.setText(i[key])
                elif key == 'divers infos':
                    self.ui.label_52.setText(i['list com'][11][0])
                    self.ui.comboBox_9.setCurrentIndex(i['list com'][11][1])
                    self.ui.textEdit_6.setText(i['list com'][11][2])

                    self.ui.label_55.setText(i['list com'][12][0])
                    self.ui.comboBox_15.setCurrentIndex(i['list com'][12][1])
                    self.ui.textEdit_7.setText(i['list com'][12][2])

                    self.ui.label_64.setText(i['list com'][13][0])
                    self.ui.comboBox_19.setCurrentIndex(i['list com'][13][1])
                    self.ui.textEdit_10.setText(i['list com'][13][2])

                    self.ui.label_61.setText(i['list com'][14][0])
                    self.ui.comboBox_18.setCurrentIndex(i['list com'][14][1])
                    self.ui.textEdit_9.setText(i['list com'][14][2])

                    self.ui.label_58.setText(i['list com'][15][0])
                    self.ui.comboBox_17.setCurrentIndex(i['list com'][15][1])
                    self.ui.textEdit_8.setText(i['list com'][15][2])
                elif key =='divers':
                    self.ui.lineEdit_34.setText(i[key])


    def apply_modif_client(self):
        t.delete_person(self.name_info)
        nom = (self.ui.lineEdit_35.text())
        prenom = (self.ui.lineEdit_39.text())
        birthdate = (self.ui.lineEdit_42.text())
        tel = (self.ui.lineEdit_32.text())
        adresse = (self.ui.lineEdit_41.text())
        mail = (self.ui.lineEdit_36.text())
        id_bien_etre = (UIFunctions.clear_comboBox_mod(self))
        mode_regl = (self.ui.lineEdit_33.text())
        date_regl = (self.ui.lineEdit_38.text())
        reste_payer = (self.ui.lineEdit_37.text())
        divers = (UIFunctions.get_reste_presta_mod(self))
        list_com = [self.ui.comboBox_39.currentIndex(),
                    self.ui.comboBox_4.currentIndex(),
                    self.ui.comboBox_30.currentIndex(),
                    self.ui.comboBox_31.currentIndex(),
                    self.ui.comboBox_32.currentIndex(),
                    self.ui.comboBox_33.currentIndex(),
                    self.ui.comboBox_34.currentIndex(),
                    self.ui.comboBox_35.currentIndex(),
                    self.ui.comboBox_36.currentIndex(),
                    self.ui.comboBox_37.currentIndex(),
                    self.ui.comboBox_38.currentIndex(),
                    [self.ui.label_52.text(), self.ui.comboBox_9.currentIndex(), self.ui.textEdit_6.toPlainText()],
                    [self.ui.label_55.text(), self.ui.comboBox_15.currentIndex(), self.ui.textEdit_7.toPlainText()],
                    [self.ui.label_64.text(), self.ui.comboBox_19.currentIndex(), self.ui.textEdit_10.toPlainText()],
                    [self.ui.label_61.text(), self.ui.comboBox_18.currentIndex(), self.ui.textEdit_9.toPlainText()],
                    [self.ui.label_58.text(), self.ui.comboBox_17.currentIndex(), self.ui.textEdit_8.toPlainText()]]
        real_divers = self.ui.lineEdit_34.toPlainText()
        if prenom =='':
            return
        else:
            t.modif_person(nom, prenom, birthdate, tel, adresse, mail, id_bien_etre, mode_regl, date_regl, reste_payer, divers, list_com, real_divers)
            self.ui.lineEdit_35.setText("")
            self.ui.lineEdit_39.setText("")
            self.ui.lineEdit_42.setText("")
            self.ui.lineEdit_32.setText("")
            self.ui.lineEdit_41.setText("")
            self.ui.lineEdit_36.setText("")
            UIFunctions.clear_comboBoxes(self)
            self.ui.lineEdit_33.setText("")
            self.ui.lineEdit_38.setText("")
            self.ui.lineEdit_37.setText("")
            self.ui.lineEdit_34.setText("")


    def searchBar(self, for_people, isSearchPeople, isSupprPeople, isModifyPeople):
        with open('test_database.json') as f:
            data = json.load(f)
        
        if for_people:
            list_name = []
            for name in data['people']:
                list_name.append(name['nom'])
                list_name.append(name['prenom'])
        else:
            list_name = []
            for name in data['depliant']:
                list_name.append(name['Prestation'])

        if isSearchPeople:
            self.ui.lineEdit_search_client.editingFinished.connect(self.ui.lineEdit_search_client.text())
            self.model = QStandardItemModel()
            completer = QCompleter(self.model, self)
            self.ui.lineEdit_search_client.setCompleter(completer)
            for i in list_name:
                if not self.model.findItems(i):
                    self.model.appendRow(QStandardItem(i.lower()))
                else:
                    pass

            json_output_list = t.get_info(self.ui.lineEdit_search_client.text())[0]
            for i in json_output_list:
                    for key in i.keys():
                        if key == 'nom':
                            self.ui.lineEdit_10.setText(i[key])
                        elif key == 'prenom':
                            self.ui.lineEdit_11.setText(i[key])
                        elif key == 'date de naissance':
                            self.ui.lineEdit_12.setText(i[key])
                        elif key == 'Num Tel':
                            self.ui.lineEdit_13.setText(i[key])
                        elif key == 'Adresse':
                            self.ui.lineEdit_14.setText(i[key])
                        elif key == 'Mail':
                            self.ui.lineEdit_15.setText(i[key])
                        elif key == 'Identifiant Bien Etre':
                            self.ui.lineEdit_16.setText(i[key])
                        elif key == 'mode de reglement':
                            self.ui.lineEdit_17.setText(i[key])
                        elif key == 'date de reglement':
                            self.ui.lineEdit_18.setText(i[key])
                        elif key == 'reste a payer':
                            self.ui.lineEdit_19.setText(i[key])
                        elif key == 'divers infos':
                            self.ui.lineEdit_20.setText(i[key])
                        elif key == 'divers':
                            self.ui.lineEdit_29.setText(i[key])
        elif isSupprPeople:
            self.ui.lineEdit_suppr_client.editingFinished.connect(self.ui.lineEdit_suppr_client.text())
            self.model = QStandardItemModel()
            completer = QCompleter(self.model, self)
            self.ui.lineEdit_suppr_client.setCompleter(completer)
            for i in list_name:
                if not self.model.findItems(i):
                    self.model.appendRow(QStandardItem(i.lower()))
                else:
                    pass
            t.delete_person(self.ui.lineEdit_suppr_client.text())

        elif isModifyPeople:
            self.ui.lineEdit_modify_client.editingFinished.connect(self.ui.lineEdit_modify_client.text())
            self.model = QStandardItemModel()
            completer = QCompleter(self.model, self)
            self.ui.lineEdit_modify_client.setCompleter(completer)
            for i in list_name:
                if not self.model.findItems(i):
                    self.model.appendRow(QStandardItem(i.lower()))
                else:
                    pass

            return self.ui.lineEdit_modify_client.text()

        elif not for_people:
            self.ui.lineEdit_search_presta.editingFinished.connect(self.ui.lineEdit_search_presta.text())
            self.model = QStandardItemModel()
            completer = QCompleter(self.model, self)
            self.ui.lineEdit_search_presta.setCompleter(completer)
            for i in list_name:
                if not self.model.findItems(i):
                    self.model.appendRow(QStandardItem(i.lower()))
                else:
                    pass
                    
            json_output_list = t.get_info(self.ui.lineEdit_search_presta.text(), False)[0]
            for i in json_output_list:
                for key in i.keys():
                    if key == 'Prestation':
                        self.ui.label_name_presta.setText(i[key])
                    elif key == 'prix':
                        self.ui.label_prix_presta_2.setText(i[key])

    def check_current_combobox_add(self):
        for i in self.ui.comboBox_16.currentText():
            print(i)
            if i == '0':
                self.ui.frame_18.hide()
                self.ui.frame_19.hide()
                self.ui.frame_20.hide()
                self.ui.frame_23.hide()
                self.ui.frame_24.hide()

                self.ui.frame_17.hide()
                self.ui.frame_26.hide()
                self.ui.frame_27.hide()
                self.ui.frame_28.hide()
                self.ui.frame_29.hide()
            elif i == '1':
                self.ui.frame_18.show()
                self.ui.frame_19.hide()
                self.ui.frame_20.hide()
                self.ui.frame_23.hide()
                self.ui.frame_24.hide()

                self.ui.frame_17.show()
                self.ui.frame_26.hide()
                self.ui.frame_27.hide()
                self.ui.frame_28.hide()
                self.ui.frame_29.hide()
            elif i == '2':
                self.ui.frame_18.show()
                self.ui.frame_19.show()
                self.ui.frame_20.hide()
                self.ui.frame_23.hide()
                self.ui.frame_24.hide()

                self.ui.frame_17.show()
                self.ui.frame_26.show()
                self.ui.frame_27.hide()
                self.ui.frame_28.hide()
                self.ui.frame_29.hide()
            elif i == '3':
                self.ui.frame_18.show()
                self.ui.frame_19.show()
                self.ui.frame_20.show()
                self.ui.frame_23.hide()
                self.ui.frame_24.hide()

                self.ui.frame_17.show()
                self.ui.frame_26.show()
                self.ui.frame_27.show()
                self.ui.frame_28.hide()
                self.ui.frame_29.hide()
            elif i == '4':
                self.ui.frame_18.show()
                self.ui.frame_19.show()
                self.ui.frame_20.show()
                self.ui.frame_23.show()
                self.ui.frame_24.hide()

                self.ui.frame_17.show()
                self.ui.frame_26.show()
                self.ui.frame_27.show()
                self.ui.frame_28.show()
                self.ui.frame_29.hide()
            elif i == '5':
                self.ui.frame_18.show()
                self.ui.frame_19.show()
                self.ui.frame_20.show()
                self.ui.frame_23.show()
                self.ui.frame_24.show()

                self.ui.frame_17.show()
                self.ui.frame_26.show()
                self.ui.frame_27.show()
                self.ui.frame_28.show()
                self.ui.frame_29.show()

    def check_current_combobox_mod(self):
        for i in self.ui.comboBox_39.currentText():
            print(i)
            if i == '0':
                self.ui.frame_25.hide()
                self.ui.frame_32.hide()
                self.ui.frame_33.hide()
                self.ui.frame_34.hide()
                self.ui.frame_35.hide()

                self.ui.frame_31.hide()
                self.ui.frame_37.hide()
                self.ui.frame_38.hide()
                self.ui.frame_39.hide()
                self.ui.frame_40.hide()
            elif i == '1':
                self.ui.frame_25.show()
                self.ui.frame_32.hide()
                self.ui.frame_33.hide()
                self.ui.frame_34.hide()
                self.ui.frame_35.hide()

                self.ui.frame_31.show()
                self.ui.frame_37.hide()
                self.ui.frame_40.hide()
                self.ui.frame_39.hide()
                self.ui.frame_38.hide()
            elif i == '2':
                self.ui.frame_25.show()
                self.ui.frame_32.show()
                self.ui.frame_33.hide()
                self.ui.frame_34.hide()
                self.ui.frame_35.hide()

                self.ui.frame_31.show()
                self.ui.frame_37.show()
                self.ui.frame_40.hide()
                self.ui.frame_39.hide()
                self.ui.frame_38.hide()
            elif i == '3':
                self.ui.frame_25.show()
                self.ui.frame_32.show()
                self.ui.frame_33.show()
                self.ui.frame_34.hide()
                self.ui.frame_35.hide()

                self.ui.frame_31.show()
                self.ui.frame_37.show()
                self.ui.frame_40.show()
                self.ui.frame_39.hide()
                self.ui.frame_38.hide()
            elif i == '4':
                self.ui.frame_25.show()
                self.ui.frame_32.show()
                self.ui.frame_33.show()
                self.ui.frame_34.show()
                self.ui.frame_35.hide()

                self.ui.frame_31.show()
                self.ui.frame_37.show()
                self.ui.frame_40.show()
                self.ui.frame_39.show()
                self.ui.frame_38.hide()
            elif i == '5':
                self.ui.frame_25.show()
                self.ui.frame_32.show()
                self.ui.frame_33.show()
                self.ui.frame_34.show()
                self.ui.frame_35.show()

                self.ui.frame_31.show()
                self.ui.frame_37.show()
                self.ui.frame_40.show()
                self.ui.frame_39.show()
                self.ui.frame_38.show()

    def clear_comboBox(self):
        output = ''
        nbr_presta_tt = self.ui.comboBox_16.currentText()
        type_presta_1 = self.ui.comboBox_2.currentText()
        nbr_presta_1 = self.ui.comboBox_10.currentText()
        type_presta_2 = self.ui.comboBox_11.currentText()
        nbr_presta_2 = self.ui.comboBox_12.currentText()
        type_presta_3 = self.ui.comboBox_13.currentText()
        nbr_presta_3 = self.ui.comboBox_14.currentText()
        type_presta_4 = self.ui.comboBox_20.currentText()
        nbr_presta_4 = self.ui.comboBox_21.currentText()
        type_presta_5 = self.ui.comboBox_22.currentText()
        nbr_presta_5 = self.ui.comboBox_23.currentText()

        if self.ui.comboBox_16.currentText() == '1':
            output += 'Passeport : ' + '\n' + '     ' + nbr_presta_tt + ' Prestation :' + '\n' +  '         -' + nbr_presta_1 + ' ' + type_presta_1
        elif self.ui.comboBox_16.currentText() == '2':
            output += 'Passeport : ' + '\n' + '     ' + nbr_presta_tt + ' Prestation :' + '\n' +  '         -' + nbr_presta_1 + ' ' + type_presta_1 + '\n' +  '         -' + nbr_presta_2 + ' ' + type_presta_2
        elif self.ui.comboBox_16.currentText() == '3':
            output += ('Passeport : ' + '\n' + '     ' + nbr_presta_tt + ' Prestation :' + '\n' +  '         -' + nbr_presta_1 + ' ' 
                + type_presta_1 + '\n' +  '         -' + nbr_presta_2 + ' ' + type_presta_2 + '\n' +  '         -' + nbr_presta_3 + ' ' + type_presta_3)
        elif self.ui.comboBox_16.currentText() == '4':
            output += ('Passeport : ' + '\n' + '     ' + nbr_presta_tt + ' Prestation :' + '\n' +  '         -' + nbr_presta_1 + ' ' 
                + type_presta_1 + '\n' +  '         -' + nbr_presta_2 + ' ' + type_presta_2 + '\n' +  '         -' + nbr_presta_3 + ' ' + type_presta_3
                 + '\n' +  '         -' + nbr_presta_4 + ' ' + type_presta_4)
        elif self.ui.comboBox_16.currentText() == '5':
            output += ('Passeport : ' + '\n' + '     ' + nbr_presta_tt + ' Prestation :' + '\n' +  '         -' + nbr_presta_1 + ' ' 
                + type_presta_1 + '\n' +  '         -' + nbr_presta_2 + ' ' + type_presta_2 + '\n' +  '         -' + nbr_presta_3 + ' ' + type_presta_3
                 + '\n' +  '         -' + nbr_presta_4 + ' ' + type_presta_4 + '\n' +  '         -' + nbr_presta_5 + ' ' + type_presta_5)
        return output

    def clear_comboBox_mod(self):
        output = ''
        nbr_presta_tt = self.ui.comboBox_39.currentText()
        type_presta_1 = self.ui.comboBox_4.currentText()
        nbr_presta_1 = self.ui.comboBox_30.currentText()
        type_presta_2 = self.ui.comboBox_31.currentText()
        nbr_presta_2 = self.ui.comboBox_32.currentText()
        type_presta_3 = self.ui.comboBox_33.currentText()
        nbr_presta_3 = self.ui.comboBox_34.currentText()
        type_presta_4 = self.ui.comboBox_35.currentText()
        nbr_presta_4 = self.ui.comboBox_36.currentText()
        type_presta_5 = self.ui.comboBox_37.currentText()
        nbr_presta_5 = self.ui.comboBox_38.currentText()

        if self.ui.comboBox_39.currentText() == '1':
            output += 'Passeport : ' + '\n' + '     ' + nbr_presta_tt + ' Prestation :' + '\n' +  '         -' + nbr_presta_1 + ' ' + type_presta_1
        elif self.ui.comboBox_39.currentText() == '2':
            output += 'Passeport : ' + '\n' + '     ' + nbr_presta_tt + ' Prestation :' + '\n' +  '         -' + nbr_presta_1 + ' ' + type_presta_1 + '\n' +  '         -' + nbr_presta_2 + ' ' + type_presta_2
        elif self.ui.comboBox_39.currentText() == '3':
            output += ('Passeport : ' + '\n' + '     ' + nbr_presta_tt + ' Prestation :' + '\n' +  '         -' + nbr_presta_1 + ' ' 
                + type_presta_1 + '\n' +  '         -' + nbr_presta_2 + ' ' + type_presta_2 + '\n' +  '         -' + nbr_presta_3 + ' ' + type_presta_3)
        elif self.ui.comboBox_39.currentText() == '4':
            output += ('Passeport : ' + '\n' + '     ' + nbr_presta_tt + ' Prestation :' + '\n' +  '         -' + nbr_presta_1 + ' ' 
                + type_presta_1 + '\n' +  '         -' + nbr_presta_2 + ' ' + type_presta_2 + '\n' +  '         -' + nbr_presta_3 + ' ' + type_presta_3
                 + '\n' +  '         -' + nbr_presta_4 + ' ' + type_presta_4)
        elif self.ui.comboBox_39.currentText() == '5':
            output += ('Passeport : ' + '\n' + '     ' + nbr_presta_tt + ' Prestation :' + '\n' +  '         -' + nbr_presta_1 + ' ' 
                + type_presta_1 + '\n' +  '         -' + nbr_presta_2 + ' ' + type_presta_2 + '\n' +  '         -' + nbr_presta_3 + ' ' + type_presta_3
                 + '\n' +  '         -' + nbr_presta_4 + ' ' + type_presta_4 + '\n' +  '         -' + nbr_presta_5 + ' ' + type_presta_5)
        return output

    def get_reste_presta(self):
        output = ''
        type_presta_1 = self.ui.label_17.text()
        nbr_reste_presta_1 = self.ui.comboBox_3.currentText()
        date_presta_1 = self.ui.textEdit_3.toPlainText()

        type_presta_2 = self.ui.label_21.text()
        nbr_reste_presta_2 = self.ui.comboBox_5.currentText()
        date_presta_2 = self.ui.textEdit_2.toPlainText()

        type_presta_3 = self.ui.label_32.text()
        nbr_reste_presta_3 = self.ui.comboBox_6.currentText()
        date_presta_3 = self.ui.textEdit.toPlainText()

        type_presta_4 = self.ui.label_35.text()
        nbr_reste_presta_4 = self.ui.comboBox_7.currentText()
        date_presta_4 = self.ui.textEdit_4.toPlainText()

        type_presta_5 = self.ui.label_49.text()
        nbr_reste_presta_5 = self.ui.comboBox_8.currentText()
        date_presta_5 = self.ui.textEdit_5.toPlainText()

        if self.ui.comboBox_16.currentText() == '1':
            output += ' Prestation :' + '\n' +  '         - il reste : ' + nbr_reste_presta_1 + ' ' + type_presta_1 + '\n' + '          -Faite le : ' + date_presta_1
        elif self.ui.comboBox_16.currentText() == '2':
            output += (' Prestation :' + '\n' +  '         - il reste : ' + nbr_reste_presta_1 + ' ' + type_presta_1 + '\n' + '          -Faite le : ' + date_presta_1
                    + '\n' +  '         - il reste : ' + nbr_reste_presta_2 + ' ' + type_presta_2 + '\n' + '          -Faite le : ' + date_presta_2
                        )
        elif self.ui.comboBox_16.currentText() == '3':
            output += (' Prestation :' + '\n' +  '         - il reste : ' + nbr_reste_presta_1 + ' ' + type_presta_1 + '\n' + '          -Faite le : ' + date_presta_1
                    + '\n' +  '         - il reste : ' + nbr_reste_presta_2 + ' ' + type_presta_2 + '\n' + '          -Faite le : ' + date_presta_2
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_3 + ' ' + type_presta_3 + '\n' + '          -Faite le : ' + date_presta_3)
        elif self.ui.comboBox_16.currentText() == '4':
            output += (' Prestation :' + '\n' +  '         - il reste : ' + nbr_reste_presta_1 + ' ' + type_presta_1 + '\n' + '          -Faite le : ' + date_presta_1
                    + '\n' +  '         - il reste : ' + nbr_reste_presta_2 + ' ' + type_presta_2 + '\n' + '          -Faite le : ' + date_presta_2
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_3 + ' ' + type_presta_3 + '\n' + '          -Faite le : ' + date_presta_3
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_4 + ' ' + type_presta_4 + '\n' + '          -Faite le : ' + date_presta_4)
        elif self.ui.comboBox_16.currentText() == '5':
            output += (' Prestation :' + '\n' +  '         - il reste : ' + nbr_reste_presta_1 + ' ' + type_presta_1 + '\n' + '          -Faite le : ' + date_presta_1
                    + '\n' +  '         - il reste : ' + nbr_reste_presta_2 + ' ' + type_presta_2 + '\n' + '          -Faite le : ' + date_presta_2
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_3 + ' ' + type_presta_3 + '\n' + '          -Faite le : ' + date_presta_3
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_4 + ' ' + type_presta_4 + '\n' + '          -Faite le : ' + date_presta_4
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_5 + ' ' + type_presta_5 + '\n' + '          -Faite le : ' + date_presta_5)
        return output

    def get_reste_presta_mod(self):
        output = ''
        type_presta_1 = self.ui.label_52.text()
        nbr_reste_presta_1 = self.ui.comboBox_9.currentText()
        date_presta_1 = self.ui.textEdit_6.toPlainText()

        type_presta_2 = self.ui.label_55.text()
        nbr_reste_presta_2 = self.ui.comboBox_15.currentText()
        date_presta_2 = self.ui.textEdit_7.toPlainText()

        type_presta_3 = self.ui.label_64.text()
        nbr_reste_presta_3 = self.ui.comboBox_19.currentText()
        date_presta_3 = self.ui.textEdit_10.toPlainText()

        type_presta_4 = self.ui.label_61.text()
        nbr_reste_presta_4 = self.ui.comboBox_18.currentText()
        date_presta_4 = self.ui.textEdit_9.toPlainText()

        type_presta_5 = self.ui.label_58.text()
        nbr_reste_presta_5 = self.ui.comboBox_17.currentText()
        date_presta_5 = self.ui.textEdit_8.toPlainText()

        if self.ui.comboBox_39.currentText() == '1':
            output += ' Prestation :' + '\n' +  '         - il reste : ' + nbr_reste_presta_1 + ' ' + type_presta_1 + '\n' + '                  -Faite le : ' + date_presta_1
        elif self.ui.comboBox_39.currentText() == '2':
            output += (' Prestation :' + '\n' +  '         - il reste : ' + nbr_reste_presta_1 + ' ' + type_presta_1 + '\n' + '                 -Faite le : ' + date_presta_1
                    + '\n' +  '         - il reste : ' + nbr_reste_presta_2 + ' ' + type_presta_2 + '\n' + '                -Faite le : ' + date_presta_2
                        )
        elif self.ui.comboBox_39.currentText() == '3':
            output += (' Prestation :' + '\n' +  '         - il reste : ' + nbr_reste_presta_1 + ' ' + type_presta_1 + '\n' + '                 -Faite le : ' + date_presta_1
                    + '\n' +  '         - il reste : ' + nbr_reste_presta_2 + ' ' + type_presta_2 + '\n' + '                -Faite le : ' + date_presta_2
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_3 + ' ' + type_presta_3 + '\n' + '                -Faite le : ' + date_presta_3)
        elif self.ui.comboBox_39.currentText() == '4':
            output += (' Prestation :' + '\n' +  '         - il reste : ' + nbr_reste_presta_1 + ' ' + type_presta_1 + '\n' + '                 -Faite le : ' + date_presta_1
                    + '\n' +  '         - il reste : ' + nbr_reste_presta_2 + ' ' + type_presta_2 + '\n' + '                -Faite le : ' + date_presta_2
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_3 + ' ' + type_presta_3 + '\n' + '                -Faite le : ' + date_presta_3
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_4 + ' ' + type_presta_4 + '\n' + '                -Faite le : ' + date_presta_4)
        elif self.ui.comboBox_39.currentText() == '5':
            output += (' Prestation :' + '\n' +  '         - il reste : ' + nbr_reste_presta_1 + ' ' + type_presta_1 + '\n' + '                 -Faite le : ' + date_presta_1
                    + '\n' +  '         - il reste : ' + nbr_reste_presta_2 + ' ' + type_presta_2 + '\n' + '                -Faite le : ' + date_presta_2
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_3 + ' ' + type_presta_3 + '\n' + '                -Faite le : ' + date_presta_3
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_4 + ' ' + type_presta_4 + '\n' + '                -Faite le : ' + date_presta_4
                        + '\n' +  '         - il reste : ' + nbr_reste_presta_5 + ' ' + type_presta_5 + '\n' + '                -Faite le : ' + date_presta_5)
        return output

    def clear_comboBoxes(self):
        self.ui.comboBox_16.setCurrentIndex(0)
        self.ui.comboBox_2.setCurrentIndex(0)
        self.ui.comboBox_10.setCurrentIndex(0)
        self.ui.comboBox_11.setCurrentIndex(0)
        self.ui.comboBox_12.setCurrentIndex(0)
        self.ui.comboBox_13.setCurrentIndex(0)
        self.ui.comboBox_14.setCurrentIndex(0)
        self.ui.comboBox_20.setCurrentIndex(0)
        self.ui.comboBox_21.setCurrentIndex(0)
        self.ui.comboBox_22.setCurrentIndex(0)
        self.ui.comboBox_23.setCurrentIndex(0)
        self.ui.comboBox_39.setCurrentIndex(0)
        self.ui.comboBox_4.setCurrentIndex(0)
        self.ui.comboBox_30.setCurrentIndex(0)
        self.ui.comboBox_31.setCurrentIndex(0)
        self.ui.comboBox_32.setCurrentIndex(0)
        self.ui.comboBox_33.setCurrentIndex(0)
        self.ui.comboBox_35.setCurrentIndex(0)
        self.ui.comboBox_36.setCurrentIndex(0)
        self.ui.comboBox_37.setCurrentIndex(0)
        self.ui.comboBox_38.setCurrentIndex(0)
        self.ui.comboBox_3.setCurrentIndex(0)
        self.ui.comboBox_5.setCurrentIndex(0)
        self.ui.comboBox_6.setCurrentIndex(0)
        self.ui.comboBox_7.setCurrentIndex(0)
        self.ui.comboBox_8.setCurrentIndex(0)

        self.ui.label_17.setText("Nom de la prestation")
        self.ui.label_21.setText("Nom de la prestation")
        self.ui.label_32.setText("Nom de la prestation")
        self.ui.label_35.setText("Nom de la prestation")
        self.ui.label_49.setText("Nom de la prestation")

        self.ui.textEdit_3.setText('')
        self.ui.textEdit_2.setText('')
        self.ui.textEdit.setText('')
        self.ui.textEdit_4.setText('')
        self.ui.textEdit_5.setText('')
        self.ui.textEdit_6.setText('')
        self.ui.textEdit_7.setText('')
        self.ui.textEdit_10.setText('')
        self.ui.textEdit_9.setText('')
        self.ui.textEdit_8.setText('')

    def Update_nbr_client(self):
        with open('test_database.json') as f:
            data = json.load(f)
            count = 0
            count_2 = 0
            for i in range(len(data['people'])+1):
                self.ui.label_top_info_1.setText('Nombre de clients : ' + str(i))
            for name in data['people']:
                if name['Identifiant Bien Etre'] != '':
                    count +=1
                for y in range(0, name['list com'][0]):
                    if int(name['list com'][(11 + y)][1]) <= 2:
                        count_2 += 1
                        break
            self.ui.label_top_info_3.setText('Dont ' + str(count) + ' sous passeport')
            self.ui.pushButton_2.setText(str(count))
            self.ui.pushButton_3.setText(str(len(data['people']) - count))
            self.ui.pushButton_4.setText(str(count_2))

    def show_no_passeport_names(self):
        list_nom_no_passeport = []
        with open('test_database.json') as f:
            data = json.load(f)
            for name in data['people']:
                if name['Identifiant Bien Etre'] == '':
                    list_nom_no_passeport.append([name['nom'], name['prenom']])
        return list_nom_no_passeport

    def show_near_passeport_names(self):
        list_nom_near_passeport = []
        with open('test_database.json') as f:
            data = json.load(f)
            for name in data['people']:
                for y in range(0, name['list com'][0]):
                    if int(name['list com'][(11 + y)][1]) <= 2:
                        list_nom_near_passeport.append([name['nom'], name['prenom'], name['list com'][(11 + y)][0]])
        return list_nom_near_passeport


    def launch_combo_completion(self):
        with open('test_database.json') as f:
            data = json.load(f)
            for i in data['depliant']:
                self.ui.comboBox_2.addItem(i['Prestation'])
                self.ui.comboBox_11.addItem(i['Prestation'])
                self.ui.comboBox_13.addItem(i['Prestation'])
                self.ui.comboBox_20.addItem(i['Prestation'])
                self.ui.comboBox_22.addItem(i['Prestation'])

                self.ui.comboBox_4.addItem(i['Prestation'])
                self.ui.comboBox_31.addItem(i['Prestation'])
                self.ui.comboBox_33.addItem(i['Prestation'])
                self.ui.comboBox_35.addItem(i['Prestation'])
                self.ui.comboBox_37.addItem(i['Prestation'])

        for integer in range(0, 21):
            self.ui.comboBox_3.addItem(str(integer))
            self.ui.comboBox_5.addItem(str(integer))
            self.ui.comboBox_6.addItem(str(integer))
            self.ui.comboBox_7.addItem(str(integer))
            self.ui.comboBox_8.addItem(str(integer))

            self.ui.comboBox_9.addItem(str(integer))
            self.ui.comboBox_15.addItem(str(integer))
            self.ui.comboBox_19.addItem(str(integer))
            self.ui.comboBox_18.addItem(str(integer))
            self.ui.comboBox_17.addItem(str(integer))

    def change_name_presta_from_add(self):
        self.ui.label_17.setText(self.ui.comboBox_2.currentText())
        self.ui.label_21.setText(self.ui.comboBox_11.currentText())
        self.ui.label_32.setText(self.ui.comboBox_13.currentText())
        self.ui.label_35.setText(self.ui.comboBox_20.currentText())
        self.ui.label_49.setText(self.ui.comboBox_22.currentText())

    def change_name_presta_from_mod(self):
        self.ui.label_52.setText(self.ui.comboBox_4.currentText())
        self.ui.label_55.setText(self.ui.comboBox_31.currentText())
        self.ui.label_64.setText(self.ui.comboBox_33.currentText())
        self.ui.label_61.setText(self.ui.comboBox_35.currentText())
        self.ui.label_58.setText(self.ui.comboBox_37.currentText())

    def show_orange_page(self):
        out = ''
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_orange_client)
        for i in UIFunctions.show_near_passeport_names(self):
            out += '\n' + i[0] + ' ' + i[1] + ' sur la prestation ' + i[2] + '\n'
        self.ui.textEdit_11.setText(out)

    def show_red_page(self):
        out = ''
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_red_client)
        for i in UIFunctions.show_no_passeport_names(self):
            out += '\n' + i[0] + ' ' + i[1] + '\n'
        self.ui.textEdit_12.setText(out)

    def save_file(self):
        shutil.copyfile(r"C:/Users/Lucas M/Documents/Python Logiciel/Mouquet's_app_v1.0.4/test_database.json", r"C:/Users/Lucas M/OneDrive - ESME/test_database.json")

    def load_file(self):
        shutil.copyfile(r"C:/Users/Lucas M/OneDrive - ESME/test_database.json", r"C:/Users/Lucas M/Documents/Python Logiciel/Mouquet's_app_v1.0.4/test_database.json")

    # def save_file(self):
    #     shutil.copyfile(r"C:/Users/Lucas M/Documents/Python Logiciel/Mouquet's_app_v1.0.4/test_database.json", r"C:/Users/Lucas M/OneDrive - ESME/test_database.json")

    # def load_file(self):
    #     shutil.copyfile(r"C:/Users/Lucas M/OneDrive - ESME/test_database.json", r"C:/Users/Lucas M/Documents/Python Logiciel/Mouquet's_app_v1.0.4/test_database.json")
    ########################################################################


    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        ## REMOVE ==> STANDARD TITLE BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()


        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        ## SHOW ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: UIFunctions.save_file(self))
        self.ui.btn_close.clicked.connect(lambda: self.close())


    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################

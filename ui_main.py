# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE_v2DTxkUb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1165, 936)
        MainWindow.setMinimumSize(QSize(100, 100))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgb(110, 95, 96);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout = QGridLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(100, 109, 100);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(50, 50, 50);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(250, 250, 250);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color"
                        ": rgb(85, 170, 255);	\n"
"	background-color: rgb(250, 250, 250);\n"
"	padding: 15px;\n"
"	selection-background-color: rgb(255, 170, 255);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::"
                        "handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: rgb(137, 118, 120);")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(134, 115, 117);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	\n"
"	background-color: rgb(117, 102, 103);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgb(139, 120, 122);")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(113, 97, 99);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(255, 255, 255); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_3 = QLabel(self.frame_top_info)
        self.label_top_info_3.setObjectName(u"label_top_info_3")
        self.label_top_info_3.setFont(font2)
        self.label_top_info_3.setStyleSheet(u"color: rgb(255, 255, 255); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_3)

        self.label_url = QLabel(self.frame_top_info)
        self.label_url.setObjectName(u"label_url")
        self.label_url.setStyleSheet(u"color: rgb(255, 170, 255);")
        self.label_url.setInputMethodHints(Qt.ImhNone)
        self.label_url.setTextFormat(Qt.RichText)
        self.label_url.setOpenExternalLinks(True)
        self.label_url.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout_8.addWidget(self.label_url)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(250, 250, 250);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(185, 143, 140);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        font4 = QFont()
        font4.setPointSize(14)
        self.frame_left_menu.setFont(font4)
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(110, 95, 96);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setStyleSheet(u"background-color: rgb(110, 95, 96);")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setStyleSheet(u"background-color: rgb(110, 95, 96);")
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        self.label_user_icon.setFont(font5)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(185, 143, 140);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_content)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(40)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.frame_41 = QFrame(self.page_home)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.frame_41)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.pushButton_4 = QPushButton(self.frame_41)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(125, 150))
        self.pushButton_4.setMaximumSize(QSize(150, 150))
        font7 = QFont()
        font7.setFamily(u"Meloriac")
        font7.setPointSize(20)
        self.pushButton_4.setFont(font7)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 75px;\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255,100,0,150);\n"
"}")

        self.gridLayout_47.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_41)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(125, 150))
        self.pushButton_2.setMaximumSize(QSize(150, 150))
        self.pushButton_2.setFont(font7)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 75px;\n"
"	background-color: rgb(85,255,125);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85,255,127,150);\n"
"}")

        self.gridLayout_47.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.label_70 = QLabel(self.frame_41)
        self.label_70.setObjectName(u"label_70")
        font8 = QFont()
        font8.setFamily(u"3ds")
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_70.setFont(font8)
        self.label_70.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_47.addWidget(self.label_70, 1, 0, 1, 1)

        self.label_71 = QLabel(self.frame_41)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font8)
        self.label_71.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_47.addWidget(self.label_71, 1, 1, 1, 1)

        self.label_72 = QLabel(self.frame_41)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font8)
        self.label_72.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_47.addWidget(self.label_72, 1, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_41)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(125, 150))
        self.pushButton_3.setMaximumSize(QSize(150, 150))
        self.pushButton_3.setFont(font7)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 75px;\n"
"	background-color: rgb(255,85,85);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255,35,35,150);\n"
"}")

        self.gridLayout_47.addWidget(self.pushButton_3, 0, 2, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_41)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(14)
        self.label.setFont(font9)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_home)
        self.page_orange_client = QWidget()
        self.page_orange_client.setObjectName(u"page_orange_client")
        self.verticalLayout_21 = QVBoxLayout(self.page_orange_client)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_68 = QLabel(self.page_orange_client)
        self.label_68.setObjectName(u"label_68")
        font10 = QFont()
        font10.setFamily(u"3ds")
        font10.setPointSize(28)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_68.setFont(font10)
        self.label_68.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_68)

        self.textEdit_11 = QTextEdit(self.page_orange_client)
        self.textEdit_11.setObjectName(u"textEdit_11")
        font11 = QFont()
        font11.setFamily(u"3ds")
        font11.setPointSize(24)
        self.textEdit_11.setFont(font11)
        self.textEdit_11.setStyleSheet(u"background-color: rgb(185, 143, 140);")
        self.textEdit_11.setFrameShape(QFrame.NoFrame)
        self.textEdit_11.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_21.addWidget(self.textEdit_11)

        self.stackedWidget.addWidget(self.page_orange_client)
        self.page_red_client = QWidget()
        self.page_red_client.setObjectName(u"page_red_client")
        self.page_red_client.setStyleSheet(u"background-color: rgb(185, 143, 140);")
        self.verticalLayout_22 = QVBoxLayout(self.page_red_client)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_69 = QLabel(self.page_red_client)
        self.label_69.setObjectName(u"label_69")
        font12 = QFont()
        font12.setFamily(u"3ds")
        font12.setPointSize(24)
        font12.setBold(True)
        font12.setWeight(75)
        self.label_69.setFont(font12)
        self.label_69.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_69)

        self.textEdit_12 = QTextEdit(self.page_red_client)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setFont(font11)
        self.textEdit_12.setFrameShape(QFrame.NoFrame)
        self.textEdit_12.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_22.addWidget(self.textEdit_12)

        self.stackedWidget.addWidget(self.page_red_client)
        self.page_client = QWidget()
        self.page_client.setObjectName(u"page_client")
        self.gridLayout_6 = QGridLayout(self.page_client)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.scrollArea_3 = QScrollArea(self.page_client)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1025, 2378))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(100)
        self.lineEdit_18 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        font13 = QFont()
        font13.setFamily(u"3ds")
        font13.setPointSize(20)
        self.lineEdit_18.setFont(font13)

        self.gridLayout_15.addWidget(self.lineEdit_18, 8, 1, 1, 1)

        self.label_client_2 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_client_2.setObjectName(u"label_client_2")
        font14 = QFont()
        font14.setFamily(u"3ds")
        font14.setPointSize(20)
        font14.setBold(True)
        font14.setWeight(75)
        self.label_client_2.setFont(font14)
        self.label_client_2.setStyleSheet(u"")
        self.label_client_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_client_2, 1, 0, 1, 1)

        self.label_client_1 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_client_1.setObjectName(u"label_client_1")
        self.label_client_1.setBaseSize(QSize(0, 0))
        self.label_client_1.setFont(font14)
        self.label_client_1.setStyleSheet(u"")
        self.label_client_1.setAlignment(Qt.AlignCenter)
        self.label_client_1.setMargin(0)

        self.gridLayout_15.addWidget(self.label_client_1, 0, 0, 1, 1)

        self.lineEdit_20 = QTextEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(0, 300))
        self.lineEdit_20.setFont(font13)
        self.lineEdit_20.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_15.addWidget(self.lineEdit_20, 10, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setFont(font13)

        self.gridLayout_15.addWidget(self.lineEdit_14, 4, 1, 1, 1)

        self.label_client_5 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_client_5.setObjectName(u"label_client_5")
        self.label_client_5.setFont(font14)
        self.label_client_5.setStyleSheet(u"")
        self.label_client_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_client_5, 4, 0, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font14)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_9, 10, 0, 1, 1)

        self.label_client_3 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_client_3.setObjectName(u"label_client_3")
        self.label_client_3.setFont(font14)
        self.label_client_3.setStyleSheet(u"")
        self.label_client_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_client_3, 2, 0, 1, 1)

        self.label_client_8 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_client_8.setObjectName(u"label_client_8")
        self.label_client_8.setFont(font14)
        self.label_client_8.setStyleSheet(u"")
        self.label_client_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_client_8, 7, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setFont(font13)

        self.gridLayout_15.addWidget(self.lineEdit_13, 3, 1, 1, 1)

        self.lineEdit_17 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setFont(font13)

        self.gridLayout_15.addWidget(self.lineEdit_17, 7, 1, 1, 1)

        self.lineEdit_12 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setFont(font13)

        self.gridLayout_15.addWidget(self.lineEdit_12, 2, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 40))
        font15 = QFont()
        font15.setFamily(u"3ds")
        font15.setPointSize(16)
        self.lineEdit_10.setFont(font15)

        self.gridLayout_15.addWidget(self.lineEdit_10, 0, 1, 1, 1)

        self.label_client_4 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_client_4.setObjectName(u"label_client_4")
        self.label_client_4.setFont(font14)
        self.label_client_4.setStyleSheet(u"")
        self.label_client_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_client_4, 3, 0, 1, 1)

        self.label_client_7 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_client_7.setObjectName(u"label_client_7")
        self.label_client_7.setFont(font14)
        self.label_client_7.setStyleSheet(u"")
        self.label_client_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_client_7, 6, 0, 1, 1)

        self.lineEdit_16 = QTextEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 300))
        self.lineEdit_16.setFont(font13)
        self.lineEdit_16.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_15.addWidget(self.lineEdit_16, 6, 1, 1, 1)

        self.lineEdit_19 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setFont(font13)

        self.gridLayout_15.addWidget(self.lineEdit_19, 9, 1, 1, 1)

        self.lineEdit_15 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setFont(font13)

        self.gridLayout_15.addWidget(self.lineEdit_15, 5, 1, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font14)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_3, 8, 0, 1, 1)

        self.label_client_6 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_client_6.setObjectName(u"label_client_6")
        self.label_client_6.setFont(font14)
        self.label_client_6.setStyleSheet(u"")
        self.label_client_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_client_6, 5, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setFont(font13)

        self.gridLayout_15.addWidget(self.lineEdit_11, 1, 1, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font14)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_7, 9, 0, 1, 1)

        self.label_67 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font14)
        self.label_67.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_67, 11, 0, 1, 1)

        self.lineEdit_29 = QTextEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setMinimumSize(QSize(0, 300))
        self.lineEdit_29.setFont(font13)
        self.lineEdit_29.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_15.addWidget(self.lineEdit_29, 11, 1, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_6.addWidget(self.scrollArea_3, 10, 0, 1, 1)

        self.label_8 = QLabel(self.page_client)
        self.label_8.setObjectName(u"label_8")
        font16 = QFont()
        font16.setFamily(u"Meloriac")
        font16.setPointSize(28)
        self.label_8.setFont(font16)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setStyleSheet(u"")
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_8, 6, 0, 1, 2)

        self.frame_9 = QFrame(self.page_client)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 50))
        self.frame_9.setMaximumSize(QSize(2000, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(300, 50, 300, 25)
        self.lineEdit_search_client = QLineEdit(self.frame_9)
        self.lineEdit_search_client.setObjectName(u"lineEdit_search_client")
        self.lineEdit_search_client.setMinimumSize(QSize(0, 50))
        self.lineEdit_search_client.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.lineEdit_search_client.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.lineEdit_search_client, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_9, 7, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_client)
        self.page_add_client = QWidget()
        self.page_add_client.setObjectName(u"page_add_client")
        self.verticalLayout_9 = QVBoxLayout(self.page_add_client)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.page_add_client)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font16)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setStyleSheet(u"")
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_10)

        self.scrollArea_4 = QScrollArea(self.page_add_client)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setFont(font13)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, -2040, 1031, 3330))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setVerticalSpacing(100)
        self.gridLayout_10.setContentsMargins(100, 50, 100, 30)
        self.lineEdit_22 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(500, 50))
        self.lineEdit_22.setFont(font15)
        self.lineEdit_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_22, 0, 1, 1, 1)

        self.lineEdit_26 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMinimumSize(QSize(500, 50))
        self.lineEdit_26.setFont(font13)
        self.lineEdit_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_26, 7, 0, 1, 2)

        self.lineEdit_27 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setMinimumSize(QSize(500, 50))
        self.lineEdit_27.setFont(font13)
        self.lineEdit_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_27, 8, 0, 1, 2)

        self.lineEdit_25 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setMinimumSize(QSize(500, 50))
        self.lineEdit_25.setFont(font13)
        self.lineEdit_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_25, 3, 1, 1, 1)

        self.lineEdit_23 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMinimumSize(QSize(500, 50))
        self.lineEdit_23.setFont(font13)
        self.lineEdit_23.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_23, 4, 1, 1, 1)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 600))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_21)
        self.verticalLayout_17.setSpacing(50)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_22)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.label_18 = QLabel(self.frame_22)
        self.label_18.setObjectName(u"label_18")
        font17 = QFont()
        font17.setFamily(u"3ds")
        font17.setPointSize(14)
        self.label_18.setFont(font17)

        self.gridLayout_29.addWidget(self.label_18, 0, 0, 1, 1)

        self.comboBox_16 = QComboBox(self.frame_22)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_29.addWidget(self.comboBox_16, 0, 1, 1, 1)


        self.verticalLayout_17.addWidget(self.frame_22)

        self.scrollArea_7 = QScrollArea(self.frame_21)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setMinimumSize(QSize(0, 500))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 785, 692))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_18 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 130))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_18)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_5 = QLabel(self.frame_18)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font17)

        self.gridLayout_26.addWidget(self.label_5, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_18)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_26.addWidget(self.comboBox_2, 0, 1, 1, 1)

        self.label_12 = QLabel(self.frame_18)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font17)

        self.gridLayout_26.addWidget(self.label_12, 1, 0, 1, 1)

        self.comboBox_10 = QComboBox(self.frame_18)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_26.addWidget(self.comboBox_10, 1, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 130))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_19)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.label_13 = QLabel(self.frame_19)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font17)

        self.gridLayout_27.addWidget(self.label_13, 0, 0, 1, 1)

        self.comboBox_11 = QComboBox(self.frame_19)
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_27.addWidget(self.comboBox_11, 0, 1, 1, 1)

        self.label_14 = QLabel(self.frame_19)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font17)

        self.gridLayout_27.addWidget(self.label_14, 1, 0, 1, 1)

        self.comboBox_12 = QComboBox(self.frame_19)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_27.addWidget(self.comboBox_12, 1, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 130))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_20)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_15 = QLabel(self.frame_20)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font17)

        self.gridLayout_28.addWidget(self.label_15, 0, 0, 1, 1)

        self.comboBox_13 = QComboBox(self.frame_20)
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_28.addWidget(self.comboBox_13, 0, 1, 1, 1)

        self.label_16 = QLabel(self.frame_20)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font17)

        self.gridLayout_28.addWidget(self.label_16, 1, 0, 1, 1)

        self.comboBox_14 = QComboBox(self.frame_20)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_28.addWidget(self.comboBox_14, 1, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.frame_20)

        self.frame_23 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 130))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_23)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_22 = QLabel(self.frame_23)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font17)

        self.gridLayout_32.addWidget(self.label_22, 0, 0, 1, 1)

        self.comboBox_20 = QComboBox(self.frame_23)
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_32.addWidget(self.comboBox_20, 0, 1, 1, 1)

        self.label_23 = QLabel(self.frame_23)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font17)

        self.gridLayout_32.addWidget(self.label_23, 1, 0, 1, 1)

        self.comboBox_21 = QComboBox(self.frame_23)
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_32.addWidget(self.comboBox_21, 1, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 130))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_24)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.label_24 = QLabel(self.frame_24)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font17)

        self.gridLayout_33.addWidget(self.label_24, 0, 0, 1, 1)

        self.comboBox_22 = QComboBox(self.frame_24)
        self.comboBox_22.setObjectName(u"comboBox_22")
        self.comboBox_22.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_33.addWidget(self.comboBox_22, 0, 1, 1, 1)

        self.label_25 = QLabel(self.frame_24)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font17)

        self.gridLayout_33.addWidget(self.label_25, 1, 0, 1, 1)

        self.comboBox_23 = QComboBox(self.frame_24)
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.setObjectName(u"comboBox_23")
        self.comboBox_23.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_33.addWidget(self.comboBox_23, 1, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.frame_24)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_17.addWidget(self.scrollArea_7)


        self.gridLayout_10.addWidget(self.frame_21, 6, 1, 1, 1)

        self.lineEdit_31 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setMinimumSize(QSize(500, 50))
        self.lineEdit_31.setFont(font13)
        self.lineEdit_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_31, 5, 1, 1, 1)

        self.lineEdit_30 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setMinimumSize(QSize(500, 50))
        self.lineEdit_30.setFont(font13)
        self.lineEdit_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_30, 9, 0, 1, 2)

        self.lineEdit_24 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setMinimumSize(QSize(500, 50))
        self.lineEdit_24.setFont(font13)
        self.lineEdit_24.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_24, 1, 1, 1, 1)

        self.lineEdit_21 = QTextEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(0, 300))
        self.lineEdit_21.setFont(font13)
        self.lineEdit_21.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_21.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)

        self.gridLayout_10.addWidget(self.lineEdit_21, 11, 0, 1, 2)

        self.lineEdit_28 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setMinimumSize(QSize(500, 50))
        self.lineEdit_28.setFont(font13)
        self.lineEdit_28.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.lineEdit_28, 2, 0, 1, 2)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 100))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.btn_add = QPushButton(self.frame_4)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setEnabled(True)
        self.btn_add.setMinimumSize(QSize(0, 50))
        font18 = QFont()
        font18.setFamily(u"Segoe UI")
        font18.setPointSize(12)
        font18.setBold(False)
        font18.setItalic(False)
        font18.setWeight(50)
        self.btn_add.setFont(font18)
        self.btn_add.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_add.setMouseTracking(False)
        self.btn_add.setLayoutDirection(Qt.LeftToRight)
        self.btn_add.setAutoFillBackground(False)
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"   background-color: rgb(53, 50, 67);\n"
"   color: rgb(208, 208, 208);\n"
"   font: 12pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	\n"
"	background-color: rgb(55, 52, 70);\n"
"\n"
"}")
        self.btn_add.setCheckable(False)
        self.btn_add.setAutoRepeat(False)
        self.btn_add.setAutoExclusive(False)
        self.btn_add.setAutoDefault(True)
        self.btn_add.setFlat(False)

        self.gridLayout_12.addWidget(self.btn_add, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_4, 12, 0, 1, 2)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 600))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_16)
        self.verticalLayout_18.setSpacing(9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.scrollArea_6 = QScrollArea(self.frame_16)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, -540, 791, 1203))
        self.gridLayout_22 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setVerticalSpacing(100)
        self.frame_17 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_17)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_17 = QLabel(self.frame_17)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font13)

        self.gridLayout_23.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_19 = QLabel(self.frame_17)
        self.label_19.setObjectName(u"label_19")
        font19 = QFont()
        font19.setFamily(u"3ds")
        font19.setPointSize(12)
        self.label_19.setFont(font19)
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_23.addWidget(self.label_19, 0, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.frame_17)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(180, 0))
        self.comboBox_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_23.addWidget(self.comboBox_3, 0, 2, 1, 1)

        self.label_20 = QLabel(self.frame_17)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 50))
        self.label_20.setFont(font13)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_23.addWidget(self.label_20, 1, 0, 1, 1)

        self.textEdit_3 = QTextEdit(self.frame_17)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setFont(font17)
        self.textEdit_3.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_23.addWidget(self.textEdit_3, 1, 1, 1, 2)


        self.gridLayout_22.addWidget(self.frame_17, 0, 0, 1, 1)

        self.frame_26 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_26)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_21 = QLabel(self.frame_26)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font13)

        self.gridLayout_24.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_28 = QLabel(self.frame_26)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font19)
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_24.addWidget(self.label_28, 0, 1, 1, 1)

        self.comboBox_5 = QComboBox(self.frame_26)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(180, 0))
        self.comboBox_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_24.addWidget(self.comboBox_5, 0, 2, 1, 1)

        self.label_31 = QLabel(self.frame_26)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 50))
        self.label_31.setFont(font13)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.label_31, 1, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.frame_26)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setFont(font17)
        self.textEdit_2.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_24.addWidget(self.textEdit_2, 1, 1, 1, 2)


        self.gridLayout_22.addWidget(self.frame_26, 1, 0, 1, 1)

        self.frame_29 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_29)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_49 = QLabel(self.frame_29)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font13)

        self.gridLayout_31.addWidget(self.label_49, 0, 0, 1, 1)

        self.label_50 = QLabel(self.frame_29)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font19)
        self.label_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_31.addWidget(self.label_50, 0, 1, 1, 1)

        self.comboBox_8 = QComboBox(self.frame_29)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMinimumSize(QSize(180, 0))
        self.comboBox_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_31.addWidget(self.comboBox_8, 0, 2, 1, 1)

        self.label_51 = QLabel(self.frame_29)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(16777215, 50))
        self.label_51.setFont(font13)
        self.label_51.setAlignment(Qt.AlignCenter)

        self.gridLayout_31.addWidget(self.label_51, 1, 0, 1, 1)

        self.textEdit_5 = QTextEdit(self.frame_29)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setFont(font17)
        self.textEdit_5.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_31.addWidget(self.textEdit_5, 1, 1, 1, 2)


        self.gridLayout_22.addWidget(self.frame_29, 4, 0, 1, 1)

        self.frame_28 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_28)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_35 = QLabel(self.frame_28)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font13)

        self.gridLayout_30.addWidget(self.label_35, 0, 0, 1, 1)

        self.label_36 = QLabel(self.frame_28)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font19)
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_30.addWidget(self.label_36, 0, 1, 1, 1)

        self.comboBox_7 = QComboBox(self.frame_28)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMinimumSize(QSize(180, 0))
        self.comboBox_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_30.addWidget(self.comboBox_7, 0, 2, 1, 1)

        self.label_48 = QLabel(self.frame_28)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(16777215, 50))
        self.label_48.setFont(font13)
        self.label_48.setAlignment(Qt.AlignCenter)

        self.gridLayout_30.addWidget(self.label_48, 1, 0, 1, 1)

        self.textEdit_4 = QTextEdit(self.frame_28)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setFont(font17)
        self.textEdit_4.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_30.addWidget(self.textEdit_4, 1, 1, 1, 2)


        self.gridLayout_22.addWidget(self.frame_28, 3, 0, 1, 1)

        self.frame_27 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_27)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.label_32 = QLabel(self.frame_27)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font13)

        self.gridLayout_25.addWidget(self.label_32, 0, 0, 1, 1)

        self.label_33 = QLabel(self.frame_27)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font19)
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_33, 0, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.frame_27)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(180, 0))
        self.comboBox_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_25.addWidget(self.comboBox_6, 0, 2, 1, 1)

        self.label_34 = QLabel(self.frame_27)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(16777215, 50))
        self.label_34.setFont(font13)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.gridLayout_25.addWidget(self.label_34, 1, 0, 1, 1)

        self.textEdit = QTextEdit(self.frame_27)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font17)
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_25.addWidget(self.textEdit, 1, 1, 1, 2)


        self.gridLayout_22.addWidget(self.frame_27, 2, 0, 1, 1)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_18.addWidget(self.scrollArea_6)


        self.gridLayout_10.addWidget(self.frame_16, 10, 0, 1, 2)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_9.addWidget(self.scrollArea_4)

        self.stackedWidget.addWidget(self.page_add_client)
        self.page_suppr_client = QWidget()
        self.page_suppr_client.setObjectName(u"page_suppr_client")
        self.gridLayout_8 = QGridLayout(self.page_suppr_client)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_7 = QFrame(self.page_suppr_client)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_26 = QLabel(self.frame_7)
        self.label_26.setObjectName(u"label_26")
        font20 = QFont()
        font20.setFamily(u"Meloriac")
        font20.setPointSize(40)
        self.label_26.setFont(font20)
        self.label_26.setLayoutDirection(Qt.LeftToRight)
        self.label_26.setStyleSheet(u"")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_26, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.page_suppr_client)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_8)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_27 = QLabel(self.frame_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setEnabled(False)
        self.label_27.setFont(font15)
        self.label_27.setLayoutDirection(Qt.LeftToRight)
        self.label_27.setStyleSheet(u"")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.label_27, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_8, 2, 0, 1, 1)

        self.frame_10 = QFrame(self.page_suppr_client)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(300, -1, 300, -1)
        self.lineEdit_suppr_client = QLineEdit(self.frame_10)
        self.lineEdit_suppr_client.setObjectName(u"lineEdit_suppr_client")
        self.lineEdit_suppr_client.setMinimumSize(QSize(0, 50))
        self.lineEdit_suppr_client.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.lineEdit_suppr_client.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.lineEdit_suppr_client, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_10, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_suppr_client)
        self.page_modif_client = QWidget()
        self.page_modif_client.setObjectName(u"page_modif_client")
        self.verticalLayout_13 = QVBoxLayout(self.page_modif_client)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_11 = QLabel(self.page_modif_client)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font16)
        self.label_11.setLayoutDirection(Qt.LeftToRight)
        self.label_11.setStyleSheet(u"")
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_11)

        self.frame_12 = QFrame(self.page_modif_client)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 50))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_12)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(300, 50, 300, -1)
        self.lineEdit_modify_client = QLineEdit(self.frame_12)
        self.lineEdit_modify_client.setObjectName(u"lineEdit_modify_client")
        self.lineEdit_modify_client.setMinimumSize(QSize(0, 50))
        self.lineEdit_modify_client.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.lineEdit_modify_client.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.lineEdit_modify_client, 0, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_12)

        self.scrollArea_5 = QScrollArea(self.page_modif_client)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, -2160, 1031, 3450))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(100)
        self.gridLayout_7.setContentsMargins(50, 100, 50, 100)
        self.lineEdit_34 = QTextEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setMinimumSize(QSize(0, 300))
        self.lineEdit_34.setFont(font13)
        self.lineEdit_34.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_7.addWidget(self.lineEdit_34, 11, 0, 1, 1)

        self.lineEdit_42 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setMinimumSize(QSize(500, 50))
        self.lineEdit_42.setFont(font13)
        self.lineEdit_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_42, 2, 0, 1, 1)

        self.lineEdit_38 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setMinimumSize(QSize(500, 50))
        self.lineEdit_38.setFont(font13)
        self.lineEdit_38.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_38, 8, 0, 1, 1)

        self.lineEdit_37 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setMinimumSize(QSize(500, 50))
        self.lineEdit_37.setFont(font13)
        self.lineEdit_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_37, 9, 0, 1, 1)

        self.lineEdit_32 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setMinimumSize(QSize(500, 50))
        self.lineEdit_32.setFont(font13)
        self.lineEdit_32.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_32, 3, 0, 1, 1)

        self.lineEdit_35 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setMinimumSize(QSize(500, 50))
        self.lineEdit_35.setFont(font15)
        self.lineEdit_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_35, 0, 0, 1, 1)

        self.lineEdit_36 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setMinimumSize(QSize(500, 50))
        self.lineEdit_36.setFont(font13)
        self.lineEdit_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_36, 5, 0, 1, 1)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 100))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.btn_modify = QPushButton(self.frame_5)
        self.btn_modify.setObjectName(u"btn_modify")
        self.btn_modify.setEnabled(True)
        self.btn_modify.setMinimumSize(QSize(0, 50))
        self.btn_modify.setFont(font18)
        self.btn_modify.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_modify.setMouseTracking(False)
        self.btn_modify.setLayoutDirection(Qt.LeftToRight)
        self.btn_modify.setAutoFillBackground(False)
        self.btn_modify.setStyleSheet(u"QPushButton {\n"
"   background-color: rgb(53, 50, 67);\n"
"   color: rgb(208, 208, 208);\n"
"   font: 12pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	\n"
"	background-color: rgb(55, 52, 70);\n"
"\n"
"}")
        self.btn_modify.setCheckable(False)
        self.btn_modify.setAutoRepeat(False)
        self.btn_modify.setAutoExclusive(False)
        self.btn_modify.setAutoDefault(True)
        self.btn_modify.setFlat(False)

        self.gridLayout_13.addWidget(self.btn_modify, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_5, 12, 0, 1, 1)

        self.lineEdit_33 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setMinimumSize(QSize(500, 50))
        self.lineEdit_33.setFont(font13)
        self.lineEdit_33.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_33, 7, 0, 1, 1)

        self.lineEdit_41 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setMinimumSize(QSize(500, 50))
        self.lineEdit_41.setFont(font13)
        self.lineEdit_41.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_41, 4, 0, 1, 1)

        self.lineEdit_39 = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setMinimumSize(QSize(500, 50))
        self.lineEdit_39.setFont(font13)
        self.lineEdit_39.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_39, 1, 0, 1, 1)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 600))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_36 = QFrame(self.frame_15)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_36)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.label_47 = QLabel(self.frame_36)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font17)

        self.gridLayout_43.addWidget(self.label_47, 0, 0, 1, 1)

        self.comboBox_39 = QComboBox(self.frame_36)
        self.comboBox_39.addItem("")
        self.comboBox_39.addItem("")
        self.comboBox_39.addItem("")
        self.comboBox_39.addItem("")
        self.comboBox_39.addItem("")
        self.comboBox_39.addItem("")
        self.comboBox_39.setObjectName(u"comboBox_39")
        self.comboBox_39.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_43.addWidget(self.comboBox_39, 0, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_36)

        self.scrollArea_9 = QScrollArea(self.frame_15)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setMinimumSize(QSize(0, 500))
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 891, 1109))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_20.setSpacing(100)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 50, -1, -1)
        self.frame_25 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 130))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_25)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.label_37 = QLabel(self.frame_25)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font17)

        self.gridLayout_38.addWidget(self.label_37, 0, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.frame_25)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_38.addWidget(self.comboBox_4, 0, 1, 1, 1)

        self.label_38 = QLabel(self.frame_25)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font17)

        self.gridLayout_38.addWidget(self.label_38, 1, 0, 1, 1)

        self.comboBox_30 = QComboBox(self.frame_25)
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.addItem("")
        self.comboBox_30.setObjectName(u"comboBox_30")
        self.comboBox_30.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_38.addWidget(self.comboBox_30, 1, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_25)

        self.frame_32 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 130))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_32)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.label_39 = QLabel(self.frame_32)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font17)

        self.gridLayout_39.addWidget(self.label_39, 0, 0, 1, 1)

        self.comboBox_31 = QComboBox(self.frame_32)
        self.comboBox_31.setObjectName(u"comboBox_31")
        self.comboBox_31.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_39.addWidget(self.comboBox_31, 0, 1, 1, 1)

        self.label_40 = QLabel(self.frame_32)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font17)

        self.gridLayout_39.addWidget(self.label_40, 1, 0, 1, 1)

        self.comboBox_32 = QComboBox(self.frame_32)
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.addItem("")
        self.comboBox_32.setObjectName(u"comboBox_32")
        self.comboBox_32.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_39.addWidget(self.comboBox_32, 1, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 130))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_33)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.label_41 = QLabel(self.frame_33)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font17)

        self.gridLayout_40.addWidget(self.label_41, 0, 0, 1, 1)

        self.comboBox_33 = QComboBox(self.frame_33)
        self.comboBox_33.setObjectName(u"comboBox_33")
        self.comboBox_33.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_40.addWidget(self.comboBox_33, 0, 1, 1, 1)

        self.label_42 = QLabel(self.frame_33)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font17)

        self.gridLayout_40.addWidget(self.label_42, 1, 0, 1, 1)

        self.comboBox_34 = QComboBox(self.frame_33)
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.addItem("")
        self.comboBox_34.setObjectName(u"comboBox_34")
        self.comboBox_34.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_40.addWidget(self.comboBox_34, 1, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 130))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_34)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.label_43 = QLabel(self.frame_34)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font17)

        self.gridLayout_41.addWidget(self.label_43, 0, 0, 1, 1)

        self.comboBox_35 = QComboBox(self.frame_34)
        self.comboBox_35.setObjectName(u"comboBox_35")
        self.comboBox_35.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_41.addWidget(self.comboBox_35, 0, 1, 1, 1)

        self.label_44 = QLabel(self.frame_34)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font17)

        self.gridLayout_41.addWidget(self.label_44, 1, 0, 1, 1)

        self.comboBox_36 = QComboBox(self.frame_34)
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.addItem("")
        self.comboBox_36.setObjectName(u"comboBox_36")
        self.comboBox_36.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_41.addWidget(self.comboBox_36, 1, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.scrollAreaWidgetContents_9)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 130))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_35)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.label_45 = QLabel(self.frame_35)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font17)

        self.gridLayout_42.addWidget(self.label_45, 0, 0, 1, 1)

        self.comboBox_37 = QComboBox(self.frame_35)
        self.comboBox_37.setObjectName(u"comboBox_37")
        self.comboBox_37.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_42.addWidget(self.comboBox_37, 0, 1, 1, 1)

        self.label_46 = QLabel(self.frame_35)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font17)

        self.gridLayout_42.addWidget(self.label_46, 1, 0, 1, 1)

        self.comboBox_38 = QComboBox(self.frame_35)
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.addItem("")
        self.comboBox_38.setObjectName(u"comboBox_38")
        self.comboBox_38.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_42.addWidget(self.comboBox_38, 1, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_35)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_14.addWidget(self.scrollArea_9)


        self.gridLayout_7.addWidget(self.frame_15, 6, 0, 1, 1)

        self.frame_30 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 600))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_30)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.scrollArea_8 = QScrollArea(self.frame_30)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, -540, 891, 1203))
        self.gridLayout_34 = QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setVerticalSpacing(100)
        self.frame_31 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_31)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_52 = QLabel(self.frame_31)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font13)

        self.gridLayout_35.addWidget(self.label_52, 0, 0, 1, 1)

        self.label_53 = QLabel(self.frame_31)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font19)
        self.label_53.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_35.addWidget(self.label_53, 0, 1, 1, 1)

        self.comboBox_9 = QComboBox(self.frame_31)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMinimumSize(QSize(180, 0))
        self.comboBox_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_35.addWidget(self.comboBox_9, 0, 2, 1, 1)

        self.label_54 = QLabel(self.frame_31)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(16777215, 50))
        self.label_54.setFont(font13)
        self.label_54.setAlignment(Qt.AlignCenter)

        self.gridLayout_35.addWidget(self.label_54, 1, 0, 1, 1)

        self.textEdit_6 = QTextEdit(self.frame_31)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setFont(font17)
        self.textEdit_6.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_35.addWidget(self.textEdit_6, 1, 1, 1, 2)


        self.gridLayout_34.addWidget(self.frame_31, 0, 0, 1, 1)

        self.frame_37 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_37)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_55 = QLabel(self.frame_37)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font13)

        self.gridLayout_36.addWidget(self.label_55, 0, 0, 1, 1)

        self.label_56 = QLabel(self.frame_37)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font19)
        self.label_56.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_36.addWidget(self.label_56, 0, 1, 1, 1)

        self.comboBox_15 = QComboBox(self.frame_37)
        self.comboBox_15.setObjectName(u"comboBox_15")
        self.comboBox_15.setMinimumSize(QSize(180, 0))
        self.comboBox_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_36.addWidget(self.comboBox_15, 0, 2, 1, 1)

        self.label_57 = QLabel(self.frame_37)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(16777215, 50))
        self.label_57.setFont(font13)
        self.label_57.setAlignment(Qt.AlignCenter)

        self.gridLayout_36.addWidget(self.label_57, 1, 0, 1, 1)

        self.textEdit_7 = QTextEdit(self.frame_37)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setFont(font17)
        self.textEdit_7.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_36.addWidget(self.textEdit_7, 1, 1, 1, 2)


        self.gridLayout_34.addWidget(self.frame_37, 1, 0, 1, 1)

        self.frame_38 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_38)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.label_58 = QLabel(self.frame_38)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font13)

        self.gridLayout_37.addWidget(self.label_58, 0, 0, 1, 1)

        self.label_59 = QLabel(self.frame_38)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font19)
        self.label_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_37.addWidget(self.label_59, 0, 1, 1, 1)

        self.comboBox_17 = QComboBox(self.frame_38)
        self.comboBox_17.setObjectName(u"comboBox_17")
        self.comboBox_17.setMinimumSize(QSize(180, 0))
        self.comboBox_17.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_37.addWidget(self.comboBox_17, 0, 2, 1, 1)

        self.label_60 = QLabel(self.frame_38)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(16777215, 50))
        self.label_60.setFont(font13)
        self.label_60.setAlignment(Qt.AlignCenter)

        self.gridLayout_37.addWidget(self.label_60, 1, 0, 1, 1)

        self.textEdit_8 = QTextEdit(self.frame_38)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setFont(font17)
        self.textEdit_8.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_37.addWidget(self.textEdit_8, 1, 1, 1, 2)


        self.gridLayout_34.addWidget(self.frame_38, 4, 0, 1, 1)

        self.frame_39 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_39)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.label_61 = QLabel(self.frame_39)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font13)

        self.gridLayout_44.addWidget(self.label_61, 0, 0, 1, 1)

        self.label_62 = QLabel(self.frame_39)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font19)
        self.label_62.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_44.addWidget(self.label_62, 0, 1, 1, 1)

        self.comboBox_18 = QComboBox(self.frame_39)
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setMinimumSize(QSize(180, 0))
        self.comboBox_18.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_44.addWidget(self.comboBox_18, 0, 2, 1, 1)

        self.label_63 = QLabel(self.frame_39)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(16777215, 50))
        self.label_63.setFont(font13)
        self.label_63.setAlignment(Qt.AlignCenter)

        self.gridLayout_44.addWidget(self.label_63, 1, 0, 1, 1)

        self.textEdit_9 = QTextEdit(self.frame_39)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setFont(font17)
        self.textEdit_9.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_44.addWidget(self.textEdit_9, 1, 1, 1, 2)


        self.gridLayout_34.addWidget(self.frame_39, 3, 0, 1, 1)

        self.frame_40 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_40)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.label_64 = QLabel(self.frame_40)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font13)

        self.gridLayout_45.addWidget(self.label_64, 0, 0, 1, 1)

        self.label_65 = QLabel(self.frame_40)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font19)
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_45.addWidget(self.label_65, 0, 1, 1, 1)

        self.comboBox_19 = QComboBox(self.frame_40)
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setMinimumSize(QSize(180, 0))
        self.comboBox_19.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 14pt \"3ds\";")

        self.gridLayout_45.addWidget(self.comboBox_19, 0, 2, 1, 1)

        self.label_66 = QLabel(self.frame_40)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMaximumSize(QSize(16777215, 50))
        self.label_66.setFont(font13)
        self.label_66.setAlignment(Qt.AlignCenter)

        self.gridLayout_45.addWidget(self.label_66, 1, 0, 1, 1)

        self.textEdit_10 = QTextEdit(self.frame_40)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setFont(font17)
        self.textEdit_10.setStyleSheet(u"QTextEdit {\n"
"	background-color: transparent;\n"
"	border: 2px solid rgb(30, 30, 50);\n"
"	padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_45.addWidget(self.textEdit_10, 1, 1, 1, 2)


        self.gridLayout_34.addWidget(self.frame_40, 2, 0, 1, 1)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_19.addWidget(self.scrollArea_8)


        self.gridLayout_7.addWidget(self.frame_30, 10, 0, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_13.addWidget(self.scrollArea_5)

        self.stackedWidget.addWidget(self.page_modif_client)
        self.page_search_presta = QWidget()
        self.page_search_presta.setObjectName(u"page_search_presta")
        self.gridLayout_11 = QGridLayout(self.page_search_presta)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_6 = QFrame(self.page_search_presta)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(5)
        self.formLayout_2.setVerticalSpacing(50)
        self.formLayout_2.setContentsMargins(10, 50, 10, -1)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        font21 = QFont()
        font21.setFamily(u"3ds")
        font21.setPointSize(16)
        font21.setBold(True)
        font21.setWeight(75)
        self.label_2.setFont(font21)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_name_presta = QLabel(self.frame_6)
        self.label_name_presta.setObjectName(u"label_name_presta")
        self.label_name_presta.setFont(font17)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_name_presta)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font21)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_prix_presta_2 = QLabel(self.frame_6)
        self.label_prix_presta_2.setObjectName(u"label_prix_presta_2")
        self.label_prix_presta_2.setFont(font17)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_prix_presta_2)


        self.gridLayout_14.addLayout(self.formLayout_2, 2, 0, 1, 1)

        self.label_29 = QLabel(self.frame_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 50))
        font22 = QFont()
        font22.setFamily(u"Meloriac")
        font22.setPointSize(26)
        self.label_29.setFont(font22)
        self.label_29.setLayoutDirection(Qt.LeftToRight)
        self.label_29.setStyleSheet(u"")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.label_29, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_13)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 50))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_14)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(300, 50, 300, -1)
        self.lineEdit_search_presta = QLineEdit(self.frame_14)
        self.lineEdit_search_presta.setObjectName(u"lineEdit_search_presta")
        self.lineEdit_search_presta.setMinimumSize(QSize(0, 50))
        self.lineEdit_search_presta.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.lineEdit_search_presta.setAlignment(Qt.AlignCenter)

        self.gridLayout_20.addWidget(self.lineEdit_search_presta, 0, 0, 1, 1)


        self.gridLayout_21.addWidget(self.frame_14, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_13, 1, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_search_presta)
        self.page_see_presta = QWidget()
        self.page_see_presta.setObjectName(u"page_see_presta")
        self.gridLayout_3 = QGridLayout(self.page_see_presta)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_11 = QFrame(self.page_see_presta)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_30 = QLabel(self.frame_11)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font22)
        self.label_30.setLayoutDirection(Qt.LeftToRight)
        self.label_30.setStyleSheet(u"")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_30, 0, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.frame_11)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 344, 82))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_5.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_5.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label_prix_see = QLabel(self.scrollAreaWidgetContents_2)
        self.label_prix_see.setObjectName(u"label_prix_see")
        font23 = QFont()
        font23.setFamily(u"3ds")
        font23.setPointSize(18)
        font23.setBold(True)
        font23.setWeight(75)
        self.label_prix_see.setFont(font23)

        self.gridLayout_5.addWidget(self.label_prix_see, 1, 0, 1, 1)

        self.label_name_see = QLabel(self.scrollAreaWidgetContents_2)
        self.label_name_see.setObjectName(u"label_name_see")
        self.label_name_see.setFont(font23)

        self.gridLayout_5.addWidget(self.label_name_see, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_4.addWidget(self.scrollArea_2, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_11, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_see_presta)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        font24 = QFont()
        font24.setFamily(u"Segoe UI")
        font24.setPointSize(9)
        self.pushButton.setFont(font24)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.frame_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font24)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy5)
        self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon4)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(255, 255, 255, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(255, 255, 255, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(255, 255, 255, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_12.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(250, 250, 250);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.commandLinkButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.btn_add.setDefault(False)
        self.btn_modify.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_3.setText("")
        self.label_url.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"WM", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"AVEC PASSEPORT", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"FIN DE PASSEPORT", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"SANS PASSEPORT", None))
        self.pushButton_3.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"MOUQUET'S ETHIQUE\u00ae Tous droits r\u00e9serv\u00e9s", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"CLIENT SOUS PASSEPORT BIEN\u00d4T TERMINE", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"CLIENT SANS PASSEPORT :", None))
        self.label_client_2.setText(QCoreApplication.translate("MainWindow", u"PRENOM : ", None))
        self.label_client_1.setText(QCoreApplication.translate("MainWindow", u"NOM : ", None))
        self.label_client_5.setText(QCoreApplication.translate("MainWindow", u"ADRESSE : ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"PASSEPORT :", None))
        self.label_client_3.setText(QCoreApplication.translate("MainWindow", u"DATE de NAISSANCE : ", None))
        self.label_client_8.setText(QCoreApplication.translate("MainWindow", u"MODE DE REGLEMENT : ", None))
        self.label_client_4.setText(QCoreApplication.translate("MainWindow", u"TEL : ", None))
        self.label_client_7.setText(QCoreApplication.translate("MainWindow", u"ID bien \u00eatre : ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DATE DE REGLEMENT : ", None))
        self.label_client_6.setText(QCoreApplication.translate("MainWindow", u"MAIL : ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u" RESTE A PAYER ? : ", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"DIVERS :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"RECHERCHER UN CLIENT", None))
        self.lineEdit_search_client.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENTREZ LE NOM / PRENOM", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"AJOUTER UN CLIENT", None))
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nom", None))
        self.lineEdit_26.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mode de r\u00e9glement", None))
        self.lineEdit_27.setPlaceholderText(QCoreApplication.translate("MainWindow", u"date de reglement", None))
        self.lineEdit_25.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Num Tel", None))
        self.lineEdit_23.setPlaceholderText(QCoreApplication.translate("MainWindow", u"adresse", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DE PRESTATION", None))
        self.comboBox_16.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_16.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_16.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_16.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_16.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TYPE DE PRESTATION", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_10.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_10.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_10.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_10.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_10.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_10.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_10.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_10.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_10.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_10.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_10.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_10.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_10.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_10.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_10.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_10.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_10.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TYPE DE PRESTATION", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_12.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_12.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_12.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_12.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_12.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_12.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_12.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_12.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_12.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_12.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_12.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_12.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_12.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_12.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_12.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_12.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_12.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TYPE DE PRESTATION", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_14.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_14.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_14.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_14.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_14.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_14.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_14.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_14.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_14.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_14.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_14.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_14.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_14.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_14.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_14.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_14.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_14.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_14.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TYPE DE PRESTATION", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.comboBox_21.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_21.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_21.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_21.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_21.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_21.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_21.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_21.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_21.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_21.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_21.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_21.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_21.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_21.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_21.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_21.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_21.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_21.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_21.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_21.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"TYPE DE PRESTATION", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.comboBox_23.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_23.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_23.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_23.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_23.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_23.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_23.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_23.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_23.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_23.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_23.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_23.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_23.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_23.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_23.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_23.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_23.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_23.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_23.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_23.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.lineEdit_31.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mail", None))
        self.lineEdit_30.setPlaceholderText(QCoreApplication.translate("MainWindow", u"reste \u00e0 payer", None))
        self.lineEdit_24.setPlaceholderText(QCoreApplication.translate("MainWindow", u"pr\u00e9nom", None))
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIVERS", None))
        self.lineEdit_28.setPlaceholderText(QCoreApplication.translate("MainWindow", u"date de naissance", None))
#if QT_CONFIG(tooltip)
        self.btn_add.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">LOGIN SYSTEM</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"AJOUTER", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Nom de la prestation", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"RESTE A FAIRE : ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"FAIT LE : ", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Nom de la prestation", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"RESTE A FAIRE : ", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"FAIT LE : ", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Nom de la prestation", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"RESTE A FAIRE : ", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"FAIT LE : ", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Nom de la prestation", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"RESTE A FAIRE : ", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"FAIT LE : ", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Nom de la prestation", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"RESTE A FAIRE : ", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"FAIT LE : ", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"SUPPRIMER UN CLIENT", None))
        self.label_27.setText("")
        self.lineEdit_suppr_client.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENTRE LE NOM / PRENOM", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"MODIFIER UN CLIENT", None))
        self.lineEdit_modify_client.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENTREZ LE NOM / PRENOM", None))
        self.lineEdit_34.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DIVERS", None))
        self.lineEdit_42.setPlaceholderText(QCoreApplication.translate("MainWindow", u"date de naissance", None))
        self.lineEdit_38.setPlaceholderText(QCoreApplication.translate("MainWindow", u"date de reglement", None))
        self.lineEdit_37.setPlaceholderText(QCoreApplication.translate("MainWindow", u"reste \u00e0 payer", None))
        self.lineEdit_32.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Num Tel", None))
        self.lineEdit_35.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nom", None))
        self.lineEdit_36.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mail", None))
#if QT_CONFIG(tooltip)
        self.btn_modify.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">LOGIN SYSTEM</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_modify.setText(QCoreApplication.translate("MainWindow", u"SAUVEGARDER LES CHANGMENTS", None))
        self.lineEdit_33.setPlaceholderText(QCoreApplication.translate("MainWindow", u"mode de r\u00e9glement", None))
        self.lineEdit_41.setPlaceholderText(QCoreApplication.translate("MainWindow", u"adresse", None))
        self.lineEdit_39.setPlaceholderText(QCoreApplication.translate("MainWindow", u"pr\u00e9nom", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"NOMBRE DE PRESTATION", None))
        self.comboBox_39.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_39.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_39.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_39.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_39.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_39.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))

        self.label_37.setText(QCoreApplication.translate("MainWindow", u"TYPE DE PRESTATION", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.comboBox_30.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_30.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_30.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_30.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_30.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_30.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_30.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_30.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_30.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_30.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_30.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_30.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_30.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_30.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_30.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_30.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_30.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_30.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_30.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_30.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TYPE DE PRESTATION", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.comboBox_32.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_32.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_32.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_32.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_32.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_32.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_32.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_32.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_32.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_32.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_32.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_32.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_32.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_32.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_32.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_32.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_32.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_32.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_32.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_32.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_41.setText(QCoreApplication.translate("MainWindow", u"TYPE DE PRESTATION", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.comboBox_34.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_34.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_34.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_34.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_34.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_34.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_34.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_34.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_34.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_34.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_34.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_34.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_34.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_34.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_34.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_34.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_34.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_34.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_34.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_34.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_43.setText(QCoreApplication.translate("MainWindow", u"TYPE DE PRESTATION", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.comboBox_36.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_36.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_36.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_36.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_36.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_36.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_36.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_36.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_36.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_36.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_36.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_36.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_36.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_36.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_36.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_36.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_36.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_36.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_36.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_36.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_45.setText(QCoreApplication.translate("MainWindow", u"TYPE DE PRESTATION", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None))
        self.comboBox_38.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_38.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_38.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_38.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_38.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_38.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_38.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_38.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_38.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_38.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_38.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_38.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_38.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_38.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_38.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_38.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_38.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_38.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_38.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_38.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Nom de la prestation", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"RESTE A FAIRE : ", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"FAIT LE : ", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Nom de la prestation", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"RESTE A FAIRE : ", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"FAIT LE : ", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Nom de la prestation", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"RESTE A FAIRE : ", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"FAIT LE : ", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Nom de la prestation", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"RESTE A FAIRE : ", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"FAIT LE : ", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Nom de la prestation", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"RESTE A FAIRE : ", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"FAIT LE : ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NOM DE LA PRESTATION : ", None))
        self.label_name_presta.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PRIX DE LA PRESTATION", None))
        self.label_prix_presta_2.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"RECHERCHER UNE PRESTATION", None))
        self.lineEdit_search_presta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENTREZ LE NOM / PRENOM", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"VOIR LES PRESTATION", None))
        self.label_prix_see.setText(QCoreApplication.translate("MainWindow", u"PRIX DE LA PRESTATION", None))
        self.label_name_see.setText(QCoreApplication.translate("MainWindow", u"NOM DE LA PRESTATION", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"BLENDER INSTALLATION", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Blender", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"D\u00e9velopp\u00e9 par: Mouquet Lucas", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi


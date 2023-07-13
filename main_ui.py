# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(852, 572)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.picLabel = QLabel(self.centralwidget)
        self.picLabel.setObjectName(u"picLabel")

        self.gridLayout.addWidget(self.picLabel, 0, 0, 1, 1)

        self.browseButton = QPushButton(self.centralwidget)
        self.browseButton.setObjectName(u"browseButton")

        self.gridLayout.addWidget(self.browseButton, 1, 0, 1, 1)


        self.DiagnoseButton = QPushButton(self.centralwidget)
        self.DiagnoseButton.setObjectName(u"DiagnoseButton")

        self.gridLayout.addWidget(self.DiagnoseButton, 2, 0, 1, 1)

        
        self.DbackBut = QPushButton(self.centralwidget)
        self.DbackBut.setObjectName(u"DbackBut")
        self.gridLayout.addWidget(self.DbackBut, 3, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.picLabel.setText(QCoreApplication.translate("MainWindow", u"Pic", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.DiagnoseButton.setText(QCoreApplication.translate("MainWindow", u"Diagnose", None))
        self.DbackBut.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi


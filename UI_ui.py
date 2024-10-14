# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(737, 539)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.txtInput = QLineEdit(self.tab_2)
        self.txtInput.setObjectName(u"txtInput")
        self.txtInput.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.txtInput)

        self.btnOpen = QPushButton(self.tab_2)
        self.btnOpen.setObjectName(u"btnOpen")

        self.horizontalLayout_2.addWidget(self.btnOpen)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.txtOutput = QLineEdit(self.tab_2)
        self.txtOutput.setObjectName(u"txtOutput")
        self.txtOutput.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.txtOutput)

        self.btnSetLocation = QPushButton(self.tab_2)
        self.btnSetLocation.setObjectName(u"btnSetLocation")

        self.horizontalLayout_4.addWidget(self.btnSetLocation)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.cmbColumns = QComboBox(self.tab_2)
        self.cmbColumns.setObjectName(u"cmbColumns")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbColumns.sizePolicy().hasHeightForWidth())
        self.cmbColumns.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.cmbColumns)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.txtCKIPOutputColumn = QLineEdit(self.tab_2)
        self.txtCKIPOutputColumn.setObjectName(u"txtCKIPOutputColumn")

        self.horizontalLayout_10.addWidget(self.txtCKIPOutputColumn)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.txtLongWord = QLineEdit(self.tab_2)
        self.txtLongWord.setObjectName(u"txtLongWord")

        self.verticalLayout.addWidget(self.txtLongWord)

        self.lstLongWord = QListView(self.tab_2)
        self.lstLongWord.setObjectName(u"lstLongWord")

        self.verticalLayout.addWidget(self.lstLongWord)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.txtSameWord = QLineEdit(self.tab_2)
        self.txtSameWord.setObjectName(u"txtSameWord")
        self.txtSameWord.setMaxLength(32767)

        self.verticalLayout_2.addWidget(self.txtSameWord)

        self.lstSameWord = QListView(self.tab_2)
        self.lstSameWord.setObjectName(u"lstSameWord")

        self.verticalLayout_2.addWidget(self.lstSameWord)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.txtResult = QPlainTextEdit(self.tab_2)
        self.txtResult.setObjectName(u"txtResult")

        self.verticalLayout_3.addWidget(self.txtResult)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.btnStartCKIP = QPushButton(self.tab_2)
        self.btnStartCKIP.setObjectName(u"btnStartCKIP")

        self.verticalLayout_4.addWidget(self.btnStartCKIP)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.txtInputCKIPedFile = QLineEdit(self.tab)
        self.txtInputCKIPedFile.setObjectName(u"txtInputCKIPedFile")
        self.txtInputCKIPedFile.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.txtInputCKIPedFile)

        self.btnOpenCKIPed = QPushButton(self.tab)
        self.btnOpenCKIPed.setObjectName(u"btnOpenCKIPed")

        self.horizontalLayout_6.addWidget(self.btnOpenCKIPed)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.cmbCKIPDataColumn = QComboBox(self.tab)
        self.cmbCKIPDataColumn.setObjectName(u"cmbCKIPDataColumn")
        sizePolicy.setHeightForWidth(self.cmbCKIPDataColumn.sizePolicy().hasHeightForWidth())
        self.cmbCKIPDataColumn.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.cmbCKIPDataColumn)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.sbTopWordCount = QSpinBox(self.tab)
        self.sbTopWordCount.setObjectName(u"sbTopWordCount")
        sizePolicy.setHeightForWidth(self.sbTopWordCount.sizePolicy().hasHeightForWidth())
        self.sbTopWordCount.setSizePolicy(sizePolicy)
        self.sbTopWordCount.setMinimum(1)
        self.sbTopWordCount.setMaximum(10000)
        self.sbTopWordCount.setValue(70)

        self.horizontalLayout_8.addWidget(self.sbTopWordCount)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_5.addWidget(self.label_13)

        self.txtStopWord = QLineEdit(self.tab)
        self.txtStopWord.setObjectName(u"txtStopWord")
        self.txtStopWord.setMaxLength(32767)

        self.verticalLayout_5.addWidget(self.txtStopWord)

        self.lstStopWord = QListView(self.tab)
        self.lstStopWord.setObjectName(u"lstStopWord")

        self.verticalLayout_5.addWidget(self.lstStopWord)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.txtCooccurrenceFilePath = QLineEdit(self.tab)
        self.txtCooccurrenceFilePath.setObjectName(u"txtCooccurrenceFilePath")
        self.txtCooccurrenceFilePath.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.txtCooccurrenceFilePath)

        self.btnSaveCooccurrence = QPushButton(self.tab)
        self.btnSaveCooccurrence.setObjectName(u"btnSaveCooccurrence")

        self.horizontalLayout_9.addWidget(self.btnSaveCooccurrence)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6a94\u6848\uff1a", None))
        self.btnOpen.setText(QCoreApplication.translate("MainWindow", u"\u958b\u555f\u6a94\u6848", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u6a94\u6848\uff1a", None))
        self.btnSetLocation.setText(QCoreApplication.translate("MainWindow", u"\u8a2d\u5b9a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8981\u65b7\u8a5e\u7684\u6b04\u4f4d\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u65b7\u8a5e\u8f38\u51fa\u6b04\u4f4d\uff1a", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u9577\u8a5e\uff0c\u7a0b\u5f0f\u9000\u51fa\u6642\u6703\u81ea\u52d5\u5132\u5b58", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u9577\u8a5e", None))
#if QT_CONFIG(tooltip)
        self.txtLongWord.setToolTip(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u9577\u8a5e\uff0c\u7a0b\u5f0f\u9000\u51fa\u6642\u6703\u81ea\u52d5\u5132\u5b58", None))
#endif // QT_CONFIG(tooltip)
        self.txtLongWord.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f38\u5165\u65b0\u9577\u8a5e\u5f8c\u6309Enter", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u540c\u7fa9\u8a5e\u4e26\u4f7f\u7528\u9017\u865f\u5206\u9694\uff0c\u7b2c1\u500b\u8a5e\u6703\u53d6\u4ee3\u4e4b\u5f8c\u7684\u8a5e\u3002\u7a0b\u5f0f\u9000\u51fa\u6642\u6703\u81ea\u52d5\u5132\u5b58", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u540c\u7fa9\u8a5e", None))
        self.txtSameWord.setText("")
        self.txtSameWord.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f38\u5165\u65b0\u540c\u7fa9\u8a5e\u5f8c\u6309Enter", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7d50\u679c", None))
        self.btnStartCKIP.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb\u65b7\u8a5e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u65b7\u8a5e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u65b7\u8a5e\u597d\u7684\u6a94\u6848\uff1a", None))
        self.btnOpenCKIPed.setText(QCoreApplication.translate("MainWindow", u"\u958b\u555f\u6a94\u6848", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5b58\u653e\u65b7\u8a5e\u7684\u6b04\u4f4d\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u524d", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u540d\u5171\u73fe", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u505c\u7528\u8a5e\u3002\u7a0b\u5f0f\u9000\u51fa\u6642\u6703\u81ea\u52d5\u5132\u5b58", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u505c\u7528\u8a5e", None))
#if QT_CONFIG(tooltip)
        self.txtStopWord.setToolTip(QCoreApplication.translate("MainWindow", u"\u8acb\u8f38\u5165\u505c\u7528\u8a5e\u3002\u7a0b\u5f0f\u9000\u51fa\u6642\u6703\u81ea\u52d5\u5132\u5b58", None))
#endif // QT_CONFIG(tooltip)
        self.txtStopWord.setText("")
        self.txtStopWord.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f38\u5165\u65b0\u505c\u7528\u8a5e\u5f8c\u6309Enter", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51fa\u6a94\u6848\uff1a", None))
        self.btnSaveCooccurrence.setText(QCoreApplication.translate("MainWindow", u"\u8a08\u7b97\u8a5e\u5f59\u5171\u73fe\u4e26\u5132\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u8a5e\u983b\u5206\u6790", None))
    # retranslateUi


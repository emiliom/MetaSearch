# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cswsearchdialogbase.ui'
#
# Created: Tue Oct  5 22:21:10 2010
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CSWSearchDialog(object):
    def setupUi(self, CSWSearchDialog):
        CSWSearchDialog.setObjectName("CSWSearchDialog")
        CSWSearchDialog.resize(438, 573)
        self.verticalLayout = QtGui.QVBoxLayout(CSWSearchDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(CSWSearchDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.leKeywords = QtGui.QLineEdit(CSWSearchDialog)
        self.leKeywords.setObjectName("leKeywords")
        self.horizontalLayout.addWidget(self.leKeywords)
        self.label_5 = QtGui.QLabel(CSWSearchDialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.spnRecords = QtGui.QSpinBox(CSWSearchDialog)
        self.spnRecords.setMaximum(100)
        self.spnRecords.setProperty("value", QtCore.QVariant(10))
        self.spnRecords.setObjectName("spnRecords")
        self.horizontalLayout.addWidget(self.spnRecords)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btnSearch = QtGui.QPushButton(CSWSearchDialog)
        self.btnSearch.setObjectName("btnSearch")
        self.verticalLayout.addWidget(self.btnSearch)
        self.groupBox = QtGui.QGroupBox(CSWSearchDialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.leNorth = QtGui.QLineEdit(self.groupBox)
        self.leNorth.setAlignment(QtCore.Qt.AlignCenter)
        self.leNorth.setObjectName("leNorth")
        self.gridLayout.addWidget(self.leNorth, 0, 1, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.leWest = QtGui.QLineEdit(self.groupBox)
        self.leWest.setAlignment(QtCore.Qt.AlignCenter)
        self.leWest.setObjectName("leWest")
        self.gridLayout.addWidget(self.leWest, 1, 0, 1, 2)
        self.leEast = QtGui.QLineEdit(self.groupBox)
        self.leEast.setAlignment(QtCore.Qt.AlignCenter)
        self.leEast.setObjectName("leEast")
        self.gridLayout.addWidget(self.leEast, 1, 2, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.leSouth = QtGui.QLineEdit(self.groupBox)
        self.leSouth.setAlignment(QtCore.Qt.AlignCenter)
        self.leSouth.setObjectName("leSouth")
        self.gridLayout.addWidget(self.leSouth, 2, 1, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 1)
        self.btnDefaultBbox = QtGui.QPushButton(self.groupBox)
        self.btnDefaultBbox.setObjectName("btnDefaultBbox")
        self.gridLayout_2.addWidget(self.btnDefaultBbox, 1, 1, 1, 1)
        self.btnCanvasBbox = QtGui.QPushButton(self.groupBox)
        self.btnCanvasBbox.setObjectName("btnCanvasBbox")
        self.gridLayout_2.addWidget(self.btnCanvasBbox, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lblResults = QtGui.QLabel(CSWSearchDialog)
        self.lblResults.setObjectName("lblResults")
        self.gridLayout_3.addWidget(self.lblResults, 0, 0, 1, 3)
        self.treeRecords = QtGui.QTreeWidget(CSWSearchDialog)
        self.treeRecords.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeRecords.setAlternatingRowColors(True)
        self.treeRecords.setRootIsDecorated(False)
        self.treeRecords.setItemsExpandable(False)
        self.treeRecords.setAllColumnsShowFocus(True)
        self.treeRecords.setObjectName("treeRecords")
        self.treeRecords.header().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.treeRecords, 1, 0, 1, 4)
        self.label_6 = QtGui.QLabel(CSWSearchDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.txtAbstract = QtGui.QTextEdit(CSWSearchDialog)
        self.txtAbstract.setObjectName("txtAbstract")
        self.gridLayout_3.addWidget(self.txtAbstract, 4, 0, 1, 4)
        self.btnAddToMap = QtGui.QPushButton(CSWSearchDialog)
        self.btnAddToMap.setObjectName("btnAddToMap")
        self.gridLayout_3.addWidget(self.btnAddToMap, 5, 0, 1, 1)
        self.btnDownload = QtGui.QPushButton(CSWSearchDialog)
        self.btnDownload.setObjectName("btnDownload")
        self.gridLayout_3.addWidget(self.btnDownload, 5, 1, 1, 1)
        self.btnMetadata = QtGui.QPushButton(CSWSearchDialog)
        self.btnMetadata.setObjectName("btnMetadata")
        self.gridLayout_3.addWidget(self.btnMetadata, 5, 2, 1, 1)
        self.btnShowXML = QtGui.QPushButton(CSWSearchDialog)
        self.btnShowXML.setObjectName("btnShowXML")
        self.gridLayout_3.addWidget(self.btnShowXML, 5, 3, 1, 1)
        self.btnFirst = QtGui.QPushButton(CSWSearchDialog)
        self.btnFirst.setObjectName("btnFirst")
        self.gridLayout_3.addWidget(self.btnFirst, 2, 0, 1, 1)
        self.btnPrev = QtGui.QPushButton(CSWSearchDialog)
        self.btnPrev.setObjectName("btnPrev")
        self.gridLayout_3.addWidget(self.btnPrev, 2, 1, 1, 1)
        self.btnNext = QtGui.QPushButton(CSWSearchDialog)
        self.btnNext.setObjectName("btnNext")
        self.gridLayout_3.addWidget(self.btnNext, 2, 2, 1, 1)
        self.btnLast = QtGui.QPushButton(CSWSearchDialog)
        self.btnLast.setObjectName("btnLast")
        self.gridLayout_3.addWidget(self.btnLast, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(CSWSearchDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CSWSearchDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CSWSearchDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CSWSearchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CSWSearchDialog)

    def retranslateUi(self, CSWSearchDialog):
        CSWSearchDialog.setWindowTitle(QtGui.QApplication.translate("CSWSearchDialog", "Search in catalog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CSWSearchDialog", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CSWSearchDialog", "Return records", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSearch.setText(QtGui.QApplication.translate("CSWSearchDialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("CSWSearchDialog", "Bounding box", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDefaultBbox.setText(QtGui.QApplication.translate("CSWSearchDialog", "Set global", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCanvasBbox.setText(QtGui.QApplication.translate("CSWSearchDialog", "From map canvas", None, QtGui.QApplication.UnicodeUTF8))
        self.treeRecords.setSortingEnabled(True)
        self.treeRecords.headerItem().setText(0, QtGui.QApplication.translate("CSWSearchDialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.treeRecords.headerItem().setText(1, QtGui.QApplication.translate("CSWSearchDialog", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.treeRecords.headerItem().setText(2, QtGui.QApplication.translate("CSWSearchDialog", "Identifier", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("CSWSearchDialog", "Abstract", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddToMap.setText(QtGui.QApplication.translate("CSWSearchDialog", "Add to map", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDownload.setText(QtGui.QApplication.translate("CSWSearchDialog", "Download", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMetadata.setText(QtGui.QApplication.translate("CSWSearchDialog", "Full metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.btnShowXML.setText(QtGui.QApplication.translate("CSWSearchDialog", "View XML", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFirst.setText(QtGui.QApplication.translate("CSWSearchDialog", "First", None, QtGui.QApplication.UnicodeUTF8))
        self.btnPrev.setText(QtGui.QApplication.translate("CSWSearchDialog", "Prev", None, QtGui.QApplication.UnicodeUTF8))
        self.btnNext.setText(QtGui.QApplication.translate("CSWSearchDialog", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLast.setText(QtGui.QApplication.translate("CSWSearchDialog", "Last", None, QtGui.QApplication.UnicodeUTF8))


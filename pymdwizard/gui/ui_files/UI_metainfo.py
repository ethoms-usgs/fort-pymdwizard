# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metainfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fgdc_metainfo(object):
    def setupUi(self, fgdc_metainfo):
        fgdc_metainfo.setObjectName("fgdc_metainfo")
        fgdc_metainfo.resize(858, 578)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(fgdc_metainfo)
        self.verticalLayout_2.setContentsMargins(0, 3, 0, 3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(fgdc_metainfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(10, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(15, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget1 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setMinimumSize(QtCore.QSize(100, 0))
        self.widget1.setObjectName("widget1")
        self.layoutWidget = QtWidgets.QWidget(self.widget1)
        self.layoutWidget.setGeometry(QtCore.QRect(3, 1, 110, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(15, 0))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(79, 0))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.widget1)
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.idinfo_scroll_area = QtWidgets.QScrollArea(fgdc_metainfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idinfo_scroll_area.sizePolicy().hasHeightForWidth())
        self.idinfo_scroll_area.setSizePolicy(sizePolicy)
        self.idinfo_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.idinfo_scroll_area.setFrameShadow(QtWidgets.QFrame.Plain)
        self.idinfo_scroll_area.setWidgetResizable(True)
        self.idinfo_scroll_area.setObjectName("idinfo_scroll_area")
        self.idinfo_main_widget = QtWidgets.QWidget()
        self.idinfo_main_widget.setGeometry(QtCore.QRect(0, 0, 854, 543))
        self.idinfo_main_widget.setObjectName("idinfo_main_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.idinfo_main_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.two_column = QtWidgets.QWidget(self.idinfo_main_widget)
        self.two_column.setObjectName("two_column")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.two_column)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.two_column_left = QtWidgets.QWidget(self.two_column)
        self.two_column_left.setObjectName("two_column_left")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.two_column_left)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.fgdc_metc = QtWidgets.QGroupBox(self.two_column_left)
        self.fgdc_metc.setObjectName("fgdc_metc")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.fgdc_metc)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.fgdc_metc)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setStyleSheet("font: italic;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(6, -1, -1, -1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.fgdc_metc)
        self.label_6.setMinimumSize(QtCore.QSize(0, 20))
        self.label_6.setStyleSheet("font: italic;")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.button_use_dataset = QtWidgets.QPushButton(self.fgdc_metc)
        self.button_use_dataset.setMinimumSize(QtCore.QSize(150, 0))
        self.button_use_dataset.setObjectName("button_use_dataset")
        self.horizontalLayout_5.addWidget(self.button_use_dataset)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addWidget(self.fgdc_metc)
        spacerItem3 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_4.addWidget(self.two_column_left)
        self.two_column_right = QtWidgets.QWidget(self.two_column)
        self.two_column_right.setObjectName("two_column_right")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.two_column_right)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.help_metstdv = QtWidgets.QGroupBox(self.two_column_right)
        self.help_metstdv.setObjectName("help_metstdv")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.help_metstdv)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.help_metstdv)
        self.label_9.setMinimumSize(QtCore.QSize(0, 20))
        self.label_9.setStyleSheet("font: italic;")
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fgdc_metstdv = QtWidgets.QComboBox(self.help_metstdv)
        self.fgdc_metstdv.setEditable(True)
        self.fgdc_metstdv.setObjectName("fgdc_metstdv")
        self.fgdc_metstdv.addItem("")
        self.fgdc_metstdv.addItem("")
        self.horizontalLayout_6.addWidget(self.fgdc_metstdv)
        self.label_7 = QtWidgets.QLabel(self.help_metstdv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(15, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_7.setIndent(0)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.help_metstdv)
        self.help_metstdn = QtWidgets.QGroupBox(self.two_column_right)
        self.help_metstdn.setObjectName("help_metstdn")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.help_metstdn)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.help_metstdn)
        self.label_10.setMinimumSize(QtCore.QSize(0, 20))
        self.label_10.setStyleSheet("font: italic;")
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.fgdc_metstdn = QtWidgets.QComboBox(self.help_metstdn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_metstdn.sizePolicy().hasHeightForWidth())
        self.fgdc_metstdn.setSizePolicy(sizePolicy)
        self.fgdc_metstdn.setMinimumSize(QtCore.QSize(375, 0))
        self.fgdc_metstdn.setEditable(True)
        self.fgdc_metstdn.setObjectName("fgdc_metstdn")
        self.fgdc_metstdn.addItem("")
        self.fgdc_metstdn.addItem("")
        self.horizontalLayout_7.addWidget(self.fgdc_metstdn)
        self.label_8 = QtWidgets.QLabel(self.help_metstdn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(15, 0))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_8.setIndent(0)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addWidget(self.help_metstdn)
        self.help_metd = QtWidgets.QGroupBox(self.two_column_right)
        self.help_metd.setObjectName("help_metd")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.help_metd)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_4.addWidget(self.help_metd)
        spacerItem4 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_4.addWidget(self.two_column_right)
        self.verticalLayout_3.addWidget(self.two_column)
        self.idinfo_scroll_area.setWidget(self.idinfo_main_widget)
        self.horizontalLayout_2.addWidget(self.idinfo_scroll_area)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(fgdc_metainfo)
        self.fgdc_metstdv.setCurrentIndex(1)
        self.fgdc_metstdn.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(fgdc_metainfo)

    def retranslateUi(self, fgdc_metainfo):
        _translate = QtCore.QCoreApplication.translate
        fgdc_metainfo.setWindowTitle(_translate("fgdc_metainfo", "Form"))
        self.label_5.setToolTip(_translate("fgdc_metainfo", "Required"))
        self.label_5.setText(_translate("fgdc_metainfo", "<html><head/><body><p><span style=\" font-style:italic; color:#55aaff;\">Provide information about the individual who wrote the metadata for the data set.  This is usually YOUR information</span></p><p><br/></p></body></html>"))
        self.label_4.setToolTip(_translate("fgdc_metainfo", "Required"))
        self.label_4.setText(_translate("fgdc_metainfo", "<html><head/><body><p><span style=\" font-size:15pt; color:#55aaff;\">*</span></p></body></html>"))
        self.label_3.setToolTip(_translate("fgdc_metainfo", "Required"))
        self.label_3.setText(_translate("fgdc_metainfo", "<html><head/><body><p><span style=\" font-size:9pt; font-style:italic; color:#55aaff;\">= Required</span></p></body></html>"))
        self.fgdc_metc.setTitle(_translate("fgdc_metainfo", "Metadata Contact"))
        self.label_2.setText(_translate("fgdc_metainfo", "Who wrote the metadata?  Alternatively, who can be contacted for questions pertaining to the metadata?"))
        self.label_6.setText(_translate("fgdc_metainfo", "Is the Metadata Contact the same as the Data Set Contact?"))
        self.button_use_dataset.setText(_translate("fgdc_metainfo", "Use Dataset Contact Info"))
        self.help_metstdv.setTitle(_translate("fgdc_metainfo", "Metadata Standard Version"))
        self.label_9.setText(_translate("fgdc_metainfo", "You probably won\'t have a need to change this value"))
        self.fgdc_metstdv.setItemText(0, _translate("fgdc_metainfo", "FGDC-STD-001-1998"))
        self.fgdc_metstdv.setItemText(1, _translate("fgdc_metainfo", "FGDC-STD-001.1-1999"))
        self.label_7.setToolTip(_translate("fgdc_metainfo", "Required"))
        self.label_7.setText(_translate("fgdc_metainfo", "<html><head/><body><p><span style=\" font-size:18pt; color:#55aaff;\">*</span></p></body></html>"))
        self.help_metstdn.setTitle(_translate("fgdc_metainfo", "Metadata Standard Name"))
        self.label_10.setText(_translate("fgdc_metainfo", "Select \'FGDC Biological Data Profile of the CDGSM\' if your data contains information about a species"))
        self.fgdc_metstdn.setItemText(0, _translate("fgdc_metainfo", "FGDC CSDGM"))
        self.fgdc_metstdn.setItemText(1, _translate("fgdc_metainfo", "FGDC Biological Data Profile of the CDGSM"))
        self.label_8.setToolTip(_translate("fgdc_metainfo", "Required"))
        self.label_8.setText(_translate("fgdc_metainfo", "<html><head/><body><p><span style=\" font-size:18pt; color:#55aaff;\">*</span></p></body></html>"))
        self.help_metd.setTitle(_translate("fgdc_metainfo", "Metadata Date"))


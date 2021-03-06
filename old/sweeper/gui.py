# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sweepergui(object):
    def setupUi(self, sweepergui):
        sweepergui.setObjectName("sweepergui")
        sweepergui.resize(900, 663)
        sweepergui.setMinimumSize(QtCore.QSize(900, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo_crop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sweepergui.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(sweepergui)
        self.gridLayout.setObjectName("gridLayout")
        self.bigProgBar = QtWidgets.QProgressBar(sweepergui)
        self.bigProgBar.setMaximum(1)
        self.bigProgBar.setProperty("value", 0)
        self.bigProgBar.setObjectName("bigProgBar")
        self.gridLayout.addWidget(self.bigProgBar, 7, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(sweepergui)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 1)
        self.exportButton = QtWidgets.QPushButton(sweepergui)
        self.exportButton.setObjectName("exportButton")
        self.gridLayout.addWidget(self.exportButton, 8, 2, 1, 1)
        self.mplwindow = QtWidgets.QWidget(sweepergui)
        self.mplwindow.setMinimumSize(QtCore.QSize(0, 0))
        self.mplwindow.setBaseSize(QtCore.QSize(0, 0))
        self.mplwindow.setObjectName("mplwindow")
        self.mplvl = QtWidgets.QVBoxLayout(self.mplwindow)
        self.mplvl.setContentsMargins(0, 0, 0, 0)
        self.mplvl.setObjectName("mplvl")
        self.gridLayout.addWidget(self.mplwindow, 0, 0, 9, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(sweepergui)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.startEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.startEdit.setObjectName("startEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startEdit)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.endEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.endEdit.setObjectName("endEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.endEdit)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.stepEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.stepEdit.setEnabled(False)
        self.stepEdit.setObjectName("stepEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stepEdit)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.delaySpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.delaySpinBox.setMaximum(65000)
        self.delaySpinBox.setProperty("value", 10)
        self.delaySpinBox.setObjectName("delaySpinBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.delaySpinBox)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.decadeComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.decadeComboBox.setObjectName("decadeComboBox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.decadeComboBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logRadioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.logRadioButton.setChecked(True)
        self.logRadioButton.setObjectName("logRadioButton")
        self.verticalLayout.addWidget(self.logRadioButton)
        self.linRadioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.linRadioButton.setEnabled(True)
        self.linRadioButton.setObjectName("linRadioButton")
        self.verticalLayout.addWidget(self.linRadioButton)
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.groupBox_4)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.senseLocalRadioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.senseLocalRadioButton.setEnabled(True)
        self.senseLocalRadioButton.setObjectName("senseLocalRadioButton")
        self.verticalLayout_3.addWidget(self.senseLocalRadioButton)
        self.senseRemoteRadioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.senseRemoteRadioButton.setEnabled(True)
        self.senseRemoteRadioButton.setChecked(True)
        self.senseRemoteRadioButton.setObjectName("senseRemoteRadioButton")
        self.verticalLayout_3.addWidget(self.senseRemoteRadioButton)
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.groupBox_5)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(sweepergui)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pocetMereniBox = QtWidgets.QSpinBox(self.groupBox)
        self.pocetMereniBox.setMinimum(1)
        self.pocetMereniBox.setMaximum(9999)
        self.pocetMereniBox.setObjectName("pocetMereniBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pocetMereniBox)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sourceCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.sourceCheckBox.setEnabled(False)
        self.sourceCheckBox.setCheckable(True)
        self.sourceCheckBox.setChecked(True)
        self.sourceCheckBox.setObjectName("sourceCheckBox")
        self.verticalLayout_2.addWidget(self.sourceCheckBox)
        self.measureCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.measureCheckBox.setEnabled(False)
        self.measureCheckBox.setChecked(True)
        self.measureCheckBox.setObjectName("measureCheckBox")
        self.verticalLayout_2.addWidget(self.measureCheckBox)
        self.delayCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.delayCheckBox.setObjectName("delayCheckBox")
        self.verticalLayout_2.addWidget(self.delayCheckBox)
        self.timeCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.timeCheckBox.setObjectName("timeCheckBox")
        self.verticalLayout_2.addWidget(self.timeCheckBox)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.groupBox_3)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.stableSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.stableSpinBox.setMaximum(9999)
        self.stableSpinBox.setProperty("value", 5)
        self.stableSpinBox.setObjectName("stableSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stableSpinBox)
        self.sleepSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.sleepSpinBox.setProperty("value", 3)
        self.sleepSpinBox.setObjectName("sleepSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sleepSpinBox)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 2)
        self.littleProgBar = QtWidgets.QProgressBar(sweepergui)
        self.littleProgBar.setProperty("value", 0)
        self.littleProgBar.setObjectName("littleProgBar")
        self.gridLayout.addWidget(self.littleProgBar, 5, 1, 1, 2)
        self.startBtn = QtWidgets.QPushButton(sweepergui)
        self.startBtn.setObjectName("startBtn")
        self.gridLayout.addWidget(self.startBtn, 8, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(sweepergui)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 1)

        self.retranslateUi(sweepergui)
        QtCore.QMetaObject.connectSlotsByName(sweepergui)

    def retranslateUi(self, sweepergui):
        _translate = QtCore.QCoreApplication.translate
        sweepergui.setWindowTitle(_translate("sweepergui", "Sweeper"))
        self.bigProgBar.setFormat(_translate("sweepergui", "%v/%m"))
        self.label_9.setText(_translate("sweepergui", "Aktuální sweep:"))
        self.exportButton.setText(_translate("sweepergui", "Export"))
        self.groupBox_2.setTitle(_translate("sweepergui", "Parametry sweepu"))
        self.label_3.setText(_translate("sweepergui", "Start [A]"))
        self.startEdit.setText(_translate("sweepergui", "1e-10"))
        self.label_4.setText(_translate("sweepergui", "End [A]"))
        self.endEdit.setText(_translate("sweepergui", "1e-12"))
        self.label_11.setText(_translate("sweepergui", "Step [A]"))
        self.stepEdit.setText(_translate("sweepergui", "1e-12"))
        self.label_5.setText(_translate("sweepergui", "Delay [ms]"))
        self.label_6.setText(_translate("sweepergui", "Bodů/dekádu"))
        self.logRadioButton.setText(_translate("sweepergui", "Logaritmický"))
        self.linRadioButton.setText(_translate("sweepergui", "Lineární"))
        self.label.setText(_translate("sweepergui", "Druh sweepu"))
        self.label_12.setText(_translate("sweepergui", "Sense"))
        self.senseLocalRadioButton.setText(_translate("sweepergui", "Local"))
        self.senseRemoteRadioButton.setText(_translate("sweepergui", "Remote"))
        self.groupBox.setTitle(_translate("sweepergui", "Ostatní parametry"))
        self.label_2.setText(_translate("sweepergui", "Počet charakteristik"))
        self.label_7.setText(_translate("sweepergui", "Sloupce dat"))
        self.sourceCheckBox.setText(_translate("sweepergui", "Source"))
        self.measureCheckBox.setText(_translate("sweepergui", "Measure"))
        self.delayCheckBox.setText(_translate("sweepergui", "Delay"))
        self.timeCheckBox.setText(_translate("sweepergui", "Time"))
        self.label_8.setText(_translate("sweepergui", "Úvodní DC mód [s]"))
        self.label_13.setText(_translate("sweepergui", "Stabilizace [s]"))
        self.startBtn.setText(_translate("sweepergui", "Start"))
        self.label_10.setText(_translate("sweepergui", "Všechny sweepy:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sweepergui = QtWidgets.QDialog()
    ui = Ui_sweepergui()
    ui.setupUi(sweepergui)
    sweepergui.show()
    sys.exit(app.exec_())


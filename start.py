# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GetRich(object):
    def setupUi(self, GetRich):
        GetRich.setObjectName("GetRich")
        GetRich.resize(872, 547)
        self.label = QtWidgets.QLabel(GetRich)
        self.label.setGeometry(QtCore.QRect(270, 200, 301, 121))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(GetRich)
        self.label_2.setGeometry(QtCore.QRect(320, -10, 191, 201))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(GetRich)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1001, 601))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(GetRich)
        self.label_4.setGeometry(QtCore.QRect(270, 360, 371, 111))
        self.label_4.setObjectName("label_4")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()

        self.retranslateUi(GetRich)
        QtCore.QMetaObject.connectSlotsByName(GetRich)

    def retranslateUi(self, GetRich):
        _translate = QtCore.QCoreApplication.translate
        GetRich.setWindowTitle(_translate("GetRich", "Dialog"))
        self.label.setText(_translate("GetRich", "<html><head/><body><p><span style=\" font-size:48pt;\">GetRich©</span></p></body></html>"))
        self.label_2.setText(_translate("GetRich", "<html><head/><body><p><img src=\":/newPrefix/logo.png\"/></p></body></html>"))
        self.label_3.setText(_translate("GetRich", "<html><head/><body><p><img src=\":/newPrefix/backgrund.jpg\"/></p></body></html>"))
        self.label_4.setText(_translate("GetRich", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600;\">Loading...</span></p></body></html>"))
import background_rc
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GetRich = QtWidgets.QDialog()
    ui = Ui_GetRich()
    ui.setupUi(GetRich)
    GetRich.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MissionOverview(object):
    def setupUi(self, MissionOverview):
        MissionOverview.setObjectName(_fromUtf8("MissionOverview"))
        MissionOverview.resize(987, 704)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/img/cranfield_logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MissionOverview.setWindowIcon(icon)
        self.logo = QtGui.QLabel(MissionOverview)
        self.logo.setGeometry(QtCore.QRect(0, 10, 201, 201))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.label_bae = QtGui.QLabel(MissionOverview)
        self.label_bae.setGeometry(QtCore.QRect(780, 10, 201, 91))
        self.label_bae.setObjectName(_fromUtf8("label_bae"))
        self.lineEdit_TID_A1 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_TID_A1.setGeometry(QtCore.QRect(80, 270, 113, 25))
        self.lineEdit_TID_A1.setObjectName(_fromUtf8("lineEdit_TID_A1"))
        self.lineEdit_TID_A2 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_TID_A2.setGeometry(QtCore.QRect(80, 320, 113, 25))
        self.lineEdit_TID_A2.setObjectName(_fromUtf8("lineEdit_TID_A2"))
        self.lineEdit_TS_A1 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_TS_A1.setGeometry(QtCore.QRect(224, 270, 113, 25))
        self.lineEdit_TS_A1.setObjectName(_fromUtf8("lineEdit_TS_A1"))
        self.lineEdit_TS_A2 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_TS_A2.setGeometry(QtCore.QRect(224, 320, 113, 25))
        self.lineEdit_TS_A2.setObjectName(_fromUtf8("lineEdit_TS_A2"))
        self.lineEdit_WS_A1 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_WS_A1.setGeometry(QtCore.QRect(374, 270, 113, 25))
        self.lineEdit_WS_A1.setObjectName(_fromUtf8("lineEdit_WS_A1"))
        self.lineEdit_WS_A2 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_WS_A2.setGeometry(QtCore.QRect(374, 320, 113, 25))
        self.lineEdit_WS_A2.setObjectName(_fromUtf8("lineEdit_WS_A2"))
        self.lineEdit_Pos_A1 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Pos_A1.setGeometry(QtCore.QRect(520, 270, 113, 25))
        self.lineEdit_Pos_A1.setObjectName(_fromUtf8("lineEdit_Pos_A1"))
        self.lineEdit_Pos_A2 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Pos_A2.setGeometry(QtCore.QRect(520, 320, 113, 25))
        self.lineEdit_Pos_A2.setObjectName(_fromUtf8("lineEdit_Pos_A2"))
        self.lineEdit_TID_A3 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_TID_A3.setGeometry(QtCore.QRect(80, 370, 113, 25))
        self.lineEdit_TID_A3.setObjectName(_fromUtf8("lineEdit_TID_A3"))
        self.lineEdit_Pos_A3 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Pos_A3.setGeometry(QtCore.QRect(520, 370, 113, 25))
        self.lineEdit_Pos_A3.setObjectName(_fromUtf8("lineEdit_Pos_A3"))
        self.lineEdit_TS_A3 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_TS_A3.setGeometry(QtCore.QRect(224, 370, 113, 25))
        self.lineEdit_TS_A3.setObjectName(_fromUtf8("lineEdit_TS_A3"))
        self.lineEdit_WS_A3 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_WS_A3.setGeometry(QtCore.QRect(374, 370, 113, 25))
        self.lineEdit_WS_A3.setObjectName(_fromUtf8("lineEdit_WS_A3"))
        self.lineEdit_TID_A4 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_TID_A4.setGeometry(QtCore.QRect(80, 420, 113, 25))
        self.lineEdit_TID_A4.setObjectName(_fromUtf8("lineEdit_TID_A4"))
        self.lineEdit_Pos_A4 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Pos_A4.setGeometry(QtCore.QRect(520, 420, 113, 25))
        self.lineEdit_Pos_A4.setObjectName(_fromUtf8("lineEdit_Pos_A4"))
        self.lineEdit_TS_A4 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_TS_A4.setGeometry(QtCore.QRect(224, 420, 113, 25))
        self.lineEdit_TS_A4.setObjectName(_fromUtf8("lineEdit_TS_A4"))
        self.lineEdit_WS_A4 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_WS_A4.setGeometry(QtCore.QRect(374, 420, 113, 25))
        self.lineEdit_WS_A4.setObjectName(_fromUtf8("lineEdit_WS_A4"))
        self.label_friend = QtGui.QLabel(MissionOverview)
        self.label_friend.setGeometry(QtCore.QRect(0, 220, 241, 17))
        self.label_friend.setObjectName(_fromUtf8("label_friend"))
        self.label_a1 = QtGui.QLabel(MissionOverview)
        self.label_a1.setGeometry(QtCore.QRect(0, 270, 67, 17))
        self.label_a1.setObjectName(_fromUtf8("label_a1"))
        self.label_a2 = QtGui.QLabel(MissionOverview)
        self.label_a2.setGeometry(QtCore.QRect(0, 320, 67, 17))
        self.label_a2.setObjectName(_fromUtf8("label_a2"))
        self.label_a3 = QtGui.QLabel(MissionOverview)
        self.label_a3.setGeometry(QtCore.QRect(0, 370, 67, 17))
        self.label_a3.setObjectName(_fromUtf8("label_a3"))
        self.label_a4 = QtGui.QLabel(MissionOverview)
        self.label_a4.setGeometry(QtCore.QRect(0, 420, 67, 17))
        self.label_a4.setObjectName(_fromUtf8("label_a4"))
        self.label_task = QtGui.QLabel(MissionOverview)
        self.label_task.setGeometry(QtCore.QRect(100, 250, 67, 17))
        self.label_task.setObjectName(_fromUtf8("label_task"))
        self.label_tasSta = QtGui.QLabel(MissionOverview)
        self.label_tasSta.setGeometry(QtCore.QRect(230, 250, 91, 20))
        self.label_tasSta.setObjectName(_fromUtf8("label_tasSta"))
        self.label_working = QtGui.QLabel(MissionOverview)
        self.label_working.setGeometry(QtCore.QRect(380, 250, 101, 20))
        self.label_working.setObjectName(_fromUtf8("label_working"))
        self.label_position = QtGui.QLabel(MissionOverview)
        self.label_position.setGeometry(QtCore.QRect(540, 250, 67, 17))
        self.label_position.setObjectName(_fromUtf8("label_position"))
        self.label_title = QtGui.QLabel(MissionOverview)
        self.label_title.setGeometry(QtCore.QRect(330, 10, 291, 41))
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.label_enem = QtGui.QLabel(MissionOverview)
        self.label_enem.setGeometry(QtCore.QRect(0, 470, 201, 17))
        self.label_enem.setObjectName(_fromUtf8("label_enem"))
        self.lineEdit_Bat_A2 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Bat_A2.setGeometry(QtCore.QRect(680, 320, 113, 25))
        self.lineEdit_Bat_A2.setObjectName(_fromUtf8("lineEdit_Bat_A2"))
        self.lineEdit_Bat_A1 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Bat_A1.setGeometry(QtCore.QRect(680, 270, 113, 25))
        self.lineEdit_Bat_A1.setObjectName(_fromUtf8("lineEdit_Bat_A1"))
        self.lineEdit_Bat_A4 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Bat_A4.setGeometry(QtCore.QRect(680, 420, 113, 25))
        self.lineEdit_Bat_A4.setObjectName(_fromUtf8("lineEdit_Bat_A4"))
        self.label_batter = QtGui.QLabel(MissionOverview)
        self.label_batter.setGeometry(QtCore.QRect(700, 250, 67, 17))
        self.label_batter.setObjectName(_fromUtf8("label_batter"))
        self.lineEdit_Bat_A3 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Bat_A3.setGeometry(QtCore.QRect(680, 370, 113, 25))
        self.lineEdit_Bat_A3.setObjectName(_fromUtf8("lineEdit_Bat_A3"))
        self.lineEdit_Pay_A2 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Pay_A2.setGeometry(QtCore.QRect(840, 320, 113, 25))
        self.lineEdit_Pay_A2.setObjectName(_fromUtf8("lineEdit_Pay_A2"))
        self.lineEdit_Pay_A1 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Pay_A1.setGeometry(QtCore.QRect(840, 270, 113, 25))
        self.lineEdit_Pay_A1.setObjectName(_fromUtf8("lineEdit_Pay_A1"))
        self.lineEdit_Pay_A4 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Pay_A4.setGeometry(QtCore.QRect(840, 420, 113, 25))
        self.lineEdit_Pay_A4.setObjectName(_fromUtf8("lineEdit_Pay_A4"))
        self.label_pay = QtGui.QLabel(MissionOverview)
        self.label_pay.setGeometry(QtCore.QRect(860, 250, 67, 17))
        self.label_pay.setObjectName(_fromUtf8("label_pay"))
        self.lineEdit_Pay_A3 = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_Pay_A3.setGeometry(QtCore.QRect(840, 370, 113, 25))
        self.lineEdit_Pay_A3.setObjectName(_fromUtf8("lineEdit_Pay_A3"))
        self.label_enemies = QtGui.QLabel(MissionOverview)
        self.label_enemies.setGeometry(QtCore.QRect(10, 500, 591, 181))
        self.label_enemies.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_enemies.setText(_fromUtf8(""))
        self.label_enemies.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_enemies.setObjectName(_fromUtf8("label_enemies"))
        self.label_ti_title = QtGui.QLabel(MissionOverview)
        self.label_ti_title.setGeometry(QtCore.QRect(700, 110, 111, 17))
        self.label_ti_title.setObjectName(_fromUtf8("label_ti_title"))
        self.lineEdit_time = QtGui.QLineEdit(MissionOverview)
        self.lineEdit_time.setGeometry(QtCore.QRect(820, 110, 161, 31))
        self.lineEdit_time.setObjectName(_fromUtf8("lineEdit_time"))
        self.label_ti_title_2 = QtGui.QLabel(MissionOverview)
        self.label_ti_title_2.setGeometry(QtCore.QRect(670, 160, 131, 20))
        self.label_ti_title_2.setObjectName(_fromUtf8("label_ti_title_2"))
        self.label_progress = QtGui.QLabel(MissionOverview)
        self.label_progress.setGeometry(QtCore.QRect(820, 160, 161, 21))
        self.label_progress.setText(_fromUtf8(""))
        self.label_progress.setObjectName(_fromUtf8("label_progress"))
        self.label_title_task = QtGui.QLabel(MissionOverview)
        self.label_title_task.setGeometry(QtCore.QRect(230, 120, 201, 17))
        self.label_title_task.setObjectName(_fromUtf8("label_title_task"))
        self.label_task_histo = QtGui.QLabel(MissionOverview)
        self.label_task_histo.setGeometry(QtCore.QRect(230, 150, 361, 41))
        self.label_task_histo.setFrameShape(QtGui.QFrame.WinPanel)
        self.label_task_histo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_task_histo.setObjectName(_fromUtf8("label_task_histo"))
        self.logo_2 = QtGui.QLabel(MissionOverview)
        self.logo_2.setGeometry(QtCore.QRect(620, 460, 341, 221))
        self.logo_2.setObjectName(_fromUtf8("logo_2"))

        self.retranslateUi(MissionOverview)
        QtCore.QMetaObject.connectSlotsByName(MissionOverview)

    def retranslateUi(self, MissionOverview):
        MissionOverview.setWindowTitle(_translate("MissionOverview", "Mission Overview", None))
        MissionOverview.setWhatsThis(_translate("MissionOverview", "<html><head/><body><p><img src=\":/newPrefix/img/Cranfield-Logo_Colour-2.png\"/></p></body></html>", None))
        self.logo.setText(_translate("MissionOverview", "<html><head/><body><p><img src=\":/newPrefix/img/cranfield_logo.png\"/></p></body></html>", None))
        self.label_bae.setText(_translate("MissionOverview", "<html><head/><body><p><img src=\":/newPrefix/img/baesystems_logo.png\"/></p></body></html>", None))
        self.label_friend.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Friendly Agents Information</span></p></body></html>", None))
        self.label_a1.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600;\">Agent 1:</span></p></body></html>", None))
        self.label_a2.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600;\">Agent 2:</span></p></body></html>", None))
        self.label_a3.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600;\">Agent 3:</span></p></body></html>", None))
        self.label_a4.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600;\">Agent 4:</span></p></body></html>", None))
        self.label_task.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600;\">Task-ID</span></p></body></html>", None))
        self.label_tasSta.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600;\">Task Status</span></p></body></html>", None))
        self.label_working.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600;\">WorkingStatus</span></p></body></html>", None))
        self.label_position.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600;\">Position</span></p></body></html>", None))
        self.label_title.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; text-decoration: underline;\">Mission Overview</span></p></body></html>", None))
        self.label_enem.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Enemy Agents Information</span></p></body></html>", None))
        self.label_batter.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600;\">Battery</span></p><p><br/></p><p><br/></p><p><br/></p></body></html>", None))
        self.label_pay.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600;\">Payload?</span></p></body></html>", None))
        self.label_ti_title.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Mission Time:</span></p></body></html>", None))
        self.label_ti_title_2.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Mission Progress:</span></p></body></html>", None))
        self.label_title_task.setText(_translate("MissionOverview", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Last Task Assignment</span></p></body></html>", None))
        self.label_task_histo.setText(_translate("MissionOverview", "<html><head/><body><p><br/></p></body></html>", None))
        self.logo_2.setText(_translate("MissionOverview", "<html><head/><body><p><img src=\":/newPrefix/img/capure.png\"/></p></body></html>", None))

import app_rc

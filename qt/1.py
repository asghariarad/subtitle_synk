# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

subbtitles = list()
movies = list()


class Ui_synksubwithmovie(object):
    def setupUi(self, synksubwithmovie):
        synksubwithmovie.setObjectName("synksubwithmovie")
        synksubwithmovie.setEnabled(True)
        synksubwithmovie.resize(897, 850)
        self.progressBar = QtWidgets.QProgressBar(synksubwithmovie)
        self.progressBar.setGeometry(QtCore.QRect(180, 620, 521, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.start = QtWidgets.QPushButton(synksubwithmovie)
        self.start.setGeometry(QtCore.QRect(40, 618, 131, 23))
        self.start.setObjectName("start")
        self.browse = QtWidgets.QToolButton(synksubwithmovie)
        self.browse.setGeometry(QtCore.QRect(560, 80, 131, 31))
        self.browse.setObjectName("browse")
        self.widget = QtWidgets.QWidget(synksubwithmovie)
        self.widget.setGeometry(QtCore.QRect(40, 80, 501, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.path_box = QtWidgets.QTextEdit(self.widget)
        self.path_box.setObjectName("path_box")
        self.horizontalLayout.addWidget(self.path_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.splitter = QtWidgets.QSplitter(synksubwithmovie)
        self.splitter.setGeometry(QtCore.QRect(44, 128, 651, 461))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.movies_list = QtWidgets.QListWidget(self.widget1)
        self.movies_list.setObjectName("movies_list")
        self.verticalLayout.addWidget(self.movies_list)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.subs_list = QtWidgets.QListWidget(self.layoutWidget)
        self.subs_list.setObjectName("subs_list")
        self.verticalLayout_2.addWidget(self.subs_list)

        self.retranslateUi(synksubwithmovie)
        self.start.clicked.connect(self.synk)
        self.browse.clicked.connect(self.select_path)
        QtCore.QMetaObject.connectSlotsByName(synksubwithmovie)

    def select_path(self):

        folder_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.path_box.setText(folder_path)
        self.Grouping()
        self.start.setText("start")
        self.start.setEnabled(True)

    def Grouping(self):
        global subbtitles
        global movies

        SUBTITLES_FORMAT = [".srt", ".ass", ".xml", ".vss"]
        MOVIES_FORMAT = [".mkv", ".wav", ".mp4"]
        folder_path = self.path_box.toPlainText()

        entries_names = os.listdir(folder_path)
        for entry in entries_names:
            file_format = os.path.splitext(entry)[1]
            if file_format in SUBTITLES_FORMAT:
                subbtitles.append(entry)
            elif file_format in MOVIES_FORMAT:
                movies.append(entry)
        self.movies_list.addItems(movies)
        self.subs_list.addItems(subbtitles)

    def synk(self):
        path = self.path_box.toPlainText()
        Progress = 100 / len(subbtitles)
        value = 0
        for i in range(len(subbtitles)):
            subbtitle_name = os.path.splitext(subbtitles[i])[0]
            subbtitle_format = os.path.splitext(subbtitles[i])[1]

            movie_name = os.path.splitext(movies[i])[0]

            os.rename(
                path + "\\" + subbtitle_name + subbtitle_format,
                path + "\\" + movie_name + subbtitle_format,
            )
            value += Progress
            self.progressBar.setValue(value)
        self.progressBar.setValue(100)
        self.movies_list.clear()
        self.subs_list.clear()
        movies.clear()
        subbtitles.clear()
        self.Grouping()
        self.start.setText("Finished")
        self.start.setEnabled(False)

    def retranslateUi(self, synksubwithmovie):
        _translate = QtCore.QCoreApplication.translate
        synksubwithmovie.setWindowTitle(_translate("synksubwithmovie", "synk sub"))
        self.start.setText(_translate("synksubwithmovie", "start"))
        self.browse.setText(_translate("synksubwithmovie", "browse"))
        self.label_3.setText(_translate("synksubwithmovie", "path"))
        self.label.setText(_translate("synksubwithmovie", "movies"))
        self.label_2.setText(_translate("synksubwithmovie", "subtitles"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    synksubwithmovie = QtWidgets.QDialog()
    ui = Ui_synksubwithmovie()
    ui.setupUi(synksubwithmovie)
    synksubwithmovie.show()
    sys.exit(app.exec_())

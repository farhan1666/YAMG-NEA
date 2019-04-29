from PyQt5 import QtCore, QtGui, QtWidgets
import MazeGraphics

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainImage = QtWidgets.QLabel(self.centralwidget)
        self.mainImage.setText("")
        self.mainImage.setPixmap(QtGui.QPixmap("placeholder.png"))
        self.mainImage.setObjectName("mainImage")
        self.verticalLayout_2.addWidget(self.mainImage)
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setObjectName("playButton")
        self.verticalLayout_2.addWidget(self.playButton)
        self.widthLabel = QtWidgets.QLabel(self.centralwidget)
        self.widthLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.widthLabel.setObjectName("widthLabel")
        self.verticalLayout_2.addWidget(self.widthLabel)
        self.widthSlider = QtWidgets.QSlider(self.centralwidget)
        self.widthSlider.setMinimum(2)
        self.widthSlider.setMaximum(50)
        self.widthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.widthSlider.setObjectName("widthSlider")
        self.verticalLayout_2.addWidget(self.widthSlider)
        self.heightLabel = QtWidgets.QLabel(self.centralwidget)
        self.heightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.heightLabel.setObjectName("heightLabel")
        self.verticalLayout_2.addWidget(self.heightLabel)
        self.heightSlider = QtWidgets.QSlider(self.centralwidget)
        self.heightSlider.setMinimum(2)
        self.heightSlider.setMaximum(50)
        self.heightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.heightSlider.setObjectName("heightSlider")
        self.verticalLayout_2.addWidget(self.heightSlider)
        self.wallsLabel = QtWidgets.QLabel(self.centralwidget)
        self.wallsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.wallsLabel.setObjectName("wallsLabel")
        self.verticalLayout_2.addWidget(self.wallsLabel)
        self.wallsSlider = QtWidgets.QSlider(self.centralwidget)
        self.wallsSlider.setMaximum(100)
        self.wallsSlider.setOrientation(QtCore.Qt.Horizontal)
        self.wallsSlider.setObjectName("wallsSlider")
        self.verticalLayout_2.addWidget(self.wallsSlider)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.playButton.clicked.connect(self.StartGame)
        self.widthSlider.valueChanged.connect(self.updateWidth)
        self.heightSlider.valueChanged.connect(self.updateHeight)
        self.wallsSlider.valueChanged.connect(self.updateWalls)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yet Another Maze Game"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.widthLabel.setText(_translate("MainWindow", str("Maze Width:" + str(self.widthSlider.value()))))
        self.heightLabel.setText(_translate("MainWindow", str("Maze Height:" + str(self.heightSlider.value()))))
        self.wallsLabel.setText(_translate("MainWindow", str("Broken Walls:" + str(self.wallsSlider.value()))))
        self.menuTest.setTitle(_translate("MainWindow", "Test"))

    def StartGame(self):
        MazeGraphics.main(self.widthSlider.value(), self.heightSlider.value(), self.wallsSlider.value())

    def updateWidth(self):
        self.widthLabel.setText(str("Maze Width:" + str(self.widthSlider.value())))

    def updateHeight(self):
        self.heightLabel.setText(str("Maze Height:" + str(self.heightSlider.value())))

    def updateWalls(self):
        self.wallsLabel.setText(str("Broken Walls:" + str(self.wallsSlider.value())))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit = app.exec_()
    sys.exit(exit)


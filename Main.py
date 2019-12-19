
import Regression3D
import Regression2D
from PyQt5.QtWidgets import (QApplication, QMessageBox, QMainWindow, QVBoxLayout, QAction, QFileDialog, QDialog)
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUiType
from os.path import dirname, realpath, join
from sys import argv
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import axis3d ,axes3d
import matplotlib.pyplot as plt

scriptDir = dirname(realpath(__file__))
FROM_MAIN, _ = loadUiType(join(dirname(__file__), "icons/mainwindow.ui"))


class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent = FROM_MAIN):

        super(Main, self).__init__()

        QMainWindow.__init__(self)
        self.setupUi(self)
        self.toolbare()
        self.creatTab()
        self.menubar()
        self.listWidget.addItem("Add data file")
        self.sc = myCanvas()
        self.l = QVBoxLayout(self.frame)
        self.l.addWidget(self.sc)
        self.Qe = 0
        self.quit = 0
        self.p = 0

    def Quit(self):
        self.quit = 1
        self.MessageSave()

    def creatTab(self):
        self.tabWidget.addTab(self.tab, "Results")
        self.tabWidget.addTab(self.tab_2, "Info")

    def menubar(self):

        self.actionSave_2.setShortcut('Ctrl+S')
        self.actionSave_2.setStatusTip('Save')
        self.actionSave_2.triggered.connect(self.SaveFile)

        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Quit')
        self.actionExit.triggered.connect(self.Quit)

        self.actionNew.setShortcut('Ctrl+D')
        self.actionNew.setStatusTip('Add File')
        self.actionNew.triggered.connect(self.browse_folder)

        self.actionHelp.setShortcut('Ctrl+H')
        self.actionHelp.setStatusTip('Help')
        self.actionHelp.triggered.connect(self.help)

    def help(self):
        QMessageBox.critical(self, 'Aide', "Hello This is PyQt5 Gui and Matplotlib ")

    def toolbare(self):
        AddFile = QAction(QIcon('icons/images.png'), 'A', self)  #
        AddFile.setShortcut('Ctrl+N')
        AddFile.triggered.connect(self.browse_folder)

        self.scatter3D = QAction(QIcon('icons/cupe.PNG'), 'Scatter 3D', self)
        self.scatter3D.setShortcut('Ctrl+L')
        self.scatter3D.setEnabled(1)
        self.scatter3D.triggered.connect(self.Plot3D)

        self.regression3D = QAction(QIcon('icons/cupe_plan.PNG'), 'Regression 3D', self)
        self.regression3D.setShortcut('Ctrl+r')
        self.regression3D.setEnabled(1)
        self.regression3D.triggered.connect(self.Resression3d)

        self.scatter2D = QAction(QIcon('icons/scatter.PNG'), 'Scatter 2D', self)
        self.scatter2D.setShortcut('Ctrl+L')
        self.scatter2D.setEnabled(1)
        self.scatter2D.triggered.connect(self.Plot2D)

        self.regression2D = QAction(QIcon('icons/fitted.PNG'), 'Regression 2D', self)
        self.regression2D.setShortcut('Ctrl+K')
        self.regression2D.setEnabled(1)
        self.regression2D.triggered.connect(self.Regression2d)

        self.toolbar = self.addToolBar('Add data file')
        self.toolbar.addAction(AddFile)

        self.toolbar.addAction(self.scatter2D)
        self.toolbar.addAction(self.regression2D)
        self.toolbar.addAction(self.scatter3D)
        self.toolbar.addAction(self.regression3D)
    def SaveFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Save", self.name,
                                                  "Text Files (*.txt);;All Files (*)")
        f = open(fileName, 'w')
        f.write(self.name)
        f.write('\n')
        f.write('Some results')
        f.write('\n')
        f.write('Some results ')
        f.write('\n')
        self.Qe = 0

    def MessageSave(self):
        buttonReply = QMessageBox.question(self, 'Soft', "  Save ?",
                                           QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel,
                                           QMessageBox.Cancel)
        if buttonReply == QMessageBox.Save:
            self.SaveFile()
        elif buttonReply == QMessageBox.No:
            if self.quit == 1:
                self.close()

            else:
                self.Qe = 0
                self.browse_folder()

    def browse_folder(self):
        global filename

        if self.Qe == 1:
            self.MessageSave()
        else:
            # options = QFileDialog.Options()
            # options |= QFileDialog.DontUseNativeDialog
            filename, _ = QFileDialog.getOpenFileName(self, "Open", "", "Text Files (*.txt);;All Files (*)")
            if filename:
                self.listWidget.clear()
                self.listWidget.addItem(filename)

    def Plot3D(self):
        n = ""
        try:
            n = Regression3D.getNe(filename)
            if n < 4:
                QMessageBox.warning(self, 'Error!', "Number  of points < 4 !")
                return
        except:
            QMessageBox.critical(self, 'Erorre', "   No data File !")
        if n != "":
            a, b, c, xarray, yarray, zarray, za = Regression3D.Regresion3D(filename)
            self.label_7.setText('C')
            self.lineEdit.setText(str(c))
            self.lineEdit_2.setText(str(b))
            self.lineEdit_3.setText(str(a))
            self.reg.setText(" Z = Ax + By + C ")

            self.Qe = 1
            try:
                self.sc.plot1(xarray, yarray, zarray)
            except:
                QMessageBox.critical(self, 'Erorre', "   Erore Plot")


    def Resression3d(self):
        n=""
        try:
            n = Regression3D.getNe(filename)
            if n < 4:
                QMessageBox.warning(self, 'Error!', "Number  of points < 4 !")
                return
        except:
            QMessageBox.critical(self, 'Erorre', "   No data File !")

        if  n != "":
            a, b, c, xarray, yarray, zarray, za = Regression3D.Regresion3D(filename)
            self.label_7.setText('C')
            self.lineEdit.setText(str(c))
            self.lineEdit_2.setText(str(b))
            self.lineEdit_3.setText(str(a))
            self.reg.setText(" Z = Ax + By + C ")

            self.Qe = 1
            try:
                self.sc.plot2(xarray, yarray, zarray, za)
            except:
                 QMessageBox.critical(self, 'Erorre', "   Erore Plot")

    def Plot2D(self):
        n = ""
        try:
            n = Regression2D.getNe(filename)

            if n < 4:
                QMessageBox.warning(self, 'Error!', "Number  of points < 4 !")
                return
        except:
            QMessageBox.critical(self, 'Erorre', "   No data File !")

        if n != "":
            a, b, xarray, zarray, za = Regression2D.Regression2d(filename)

            self.lineEdit.setText(str(a))
            self.lineEdit_2.setText(str(b))
            self.lineEdit_3.setText(' ')
            self.label_7.setText(' ')
            self.reg.setText(" Z = Ax + B")

            self.Qe = 1
            try:
                self.sc.plot2D(xarray,  zarray)
            except:
                QMessageBox.critical(self, 'Erorre', "   Erore Plot")

    def Regression2d(self):
        n = ""
        try:
            n = Regression2D.getNe(filename)

            if n < 4:
                QMessageBox.warning(self, 'Error!', "Number  of points < 4 !")
                return
        except:
            QMessageBox.critical(self, 'Erorre', "   No data File !")

        if n != "":
            a, b, xarray, zarray, za = Regression2D.Regression2d(filename)
            self.lineEdit.setText(str(a))
            self.lineEdit_2.setText(str(b))
            self.lineEdit_3.setText(' ')
            self.label_7.setText(' ')
            self.reg.setText(" Z = Ax + B")

            self.Qe = 1
            try:
                self.sc.plot2DM(xarray, zarray,za)
            except:
                QMessageBox.critical(self, 'Erorre', "   Erore Plot")


class myCanvas(FigureCanvas):

    def __init__(self):
        self.fig = Figure()
        FigureCanvas.__init__(self, self.fig)

    def plot2(self, xarray, yarray, zarray, za):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111, projection = '3d')

        self.ax.mouse_init(rotate_btn = 1, zoom_btn = 3)

        self.ax.plot_trisurf(xarray, yarray, za, color = 'red', alpha = 0.6, edgecolor = 'red', linewidth = 0.1,
                             antialiased = True, shade = 1)

        self.ax.plot(xarray, yarray, zarray, 'ok')
        self.ax.set_xlabel('X ')
        self.ax.set_ylabel('Y ')
        self.ax.set_zlabel('Z ')
        
        self.draw()

    def plot1(self, xarray, yarray, zarray):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111, projection = '3d')
        self.ax.mouse_init(rotate_btn = 1, zoom_btn = 3)
        self.ax.plot(xarray, yarray, zarray, 'ok')
        self.ax.set_xlabel('X ')
        self.ax.set_ylabel('Y ')
        self.ax.set_zlabel('Z ')
        self.draw()

    def plot2D(self, xarray, zarray):
        self.fig.clear()
        self.axe = self.fig.add_subplot(111)
        self.axe.plot(xarray, zarray, 'ok')
        self.axe.set_xlabel('X ')
        self.axe.set_ylabel('Y ')
        self.draw()

    def plot2DM(self, xarray, zarray, za):
        self.fig.clear()
        self.axe = self.fig.add_subplot(111)
        self.axe.plot(xarray, zarray, "ok")
        self.axe.plot(xarray, za, 'r-')
        self.axe.set_xlabel('X ')
        self.axe.set_ylabel('Y ')
        self.draw()


def main():
    app = QApplication(argv)
    window = Main()
    # window.showFullScreen() # Start at position full screen
    window.showMaximized()  # Start position max screen
    app.exec_()


if __name__ == '__main__':
    main()
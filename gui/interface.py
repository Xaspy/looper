import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QSlider, QDial, QAction, QMenuBar, QGridLayout, QGroupBox)
from PyQt5.QtGui import QFont, QIcon


class LooperGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(800, 300, 625, 600)
        self.setWindowTitle('LoopeR')
        self.setWindowIcon(QIcon('pics/looper_icon.png'))
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        groupbox = QGroupBox("GroupBox Example", self)
        groupbox.move(20, 0)

        self._set_menu_bar()

        self.show()

    def _set_menu_bar(self):
        menubar = QMenuBar()
        self.layout.addWidget(menubar, 0, 0)
        action_file = menubar.addMenu("File")
        action_file.addAction("New")
        action_file.addAction("Open")
        action_file.addAction("Save")
        action_file.addSeparator()
        action_file.addAction("Quit")
        action_edit = menubar.addMenu("Edit")
        action_edit.addAction("Add")
        action_edit.addSeparator()
        action_edit.addAction("Undo")
        action_edit.addAction("Redo")
        action_help = menubar.addMenu("Help")
        action_help.addAction("Information")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LooperGUI()
    sys.exit(app.exec_())

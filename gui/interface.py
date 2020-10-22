import sys

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QSlider, QDial, QAction)
from PyQt5.QtGui import QFont, QIcon


class LooperGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(800, 300, 625, 600)
        self.setWindowTitle('LoopeR')
        self.setWindowIcon(QIcon('pics/looper_icon.png'))
        pads = self._set_pads(4, 4)
        manage_pads = self._set_man_pads(1, 5, 40, 535, 300)
        dial = self._set_vol_dial()

        self.show()

    def _set_vol_dial(self, size=75, x=500, y=125):
        x_coord = x
        y_coord = y

        dial = QDial(self)
        dial.move(x_coord, y_coord)
        dial.setValue(20)
        dial.resize(size + 25, size + 25)

        return dial

    def _set_pads(self, on_vertical: int,
                  on_horizontal: int,
                  size=100, x=50, y=125) -> list:
        result = []
        x_coord = x
        y_coord = y
        for i in range(on_horizontal):
            for j in range(on_vertical):
                button = QPushButton('', self)
                button.resize(size, size)
                button.move(x_coord, y_coord)
                result.append(button)
                x_coord += size + 10
            x_coord -= on_vertical * (size + 10)
            y_coord += size + 10

    def _set_man_pads(self, on_vertical: int,
                      on_horizontal: int,
                      size=40, x=50, y=125) -> list:
        result = []
        x_coord = x
        y_coord = y
        for i in range(on_horizontal):
            button = QPushButton('TAP', self)
            for j in range(on_vertical):
                button.resize(size, size)
                button.move(x_coord, y_coord)
                result.append(button)
                x_coord += size + 10
            x_coord -= on_vertical * (size + 10)
            y_coord += size + 10

        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LooperGUI()
    sys.exit(app.exec_())

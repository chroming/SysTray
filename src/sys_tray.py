

import sys

from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon

from actions import get_actions


class Tray(object):
    def __init__(self):
        super(Tray, self).__init__()
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon('demo.png'))
        self._set_menu()

    def _set_menu(self):
        self.tray_menu = QMenu()
        for action in get_actions(self.tray):
            self.tray_menu.addAction(action)
        self.tray.setContextMenu(self.tray_menu)

    def show(self):
        self.tray.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Tray()
    t.show()
    sys.exit(app.exec_())
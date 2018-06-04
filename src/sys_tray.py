

import sys

from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

from actions import *


class BaseTray(object):
    def __init__(self, icon_path):
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(icon_path))
        self.tray_menu = QMenu()
        self._set_menu()

    def _set_menu(self):
        pass

    def show_message(self, text):
        icon = self.tray.MessageIcon()
        self.tray.showMessage('message', text, icon, 1000)

    def show(self):
        self.tray.show()

    def quit(self):
        self.tray.hide()
        sys.exit()


class Tray(BaseTray):
    def __init__(self, icon_path='demo.png'):
        super(Tray, self).__init__(icon_path)

    def _set_menu(self):
        self._set_customer_menu()
        self._set_sys_menu()

        self.tray.setContextMenu(self.tray_menu)

    def _get_actions(self):
        for a in ACTION_LIST:
            action = QAction(a[0], self.tray, triggered=lambda _: self._with_message(a[1]))
            yield action

        for c in CHECKABLE_LIST:
            action = QAction(c[0], self.tray, checkable=True, triggered=lambda x: self._with_message(c[1], x))
            yield action

    def _set_customer_menu(self):
        for action in self._get_actions():
            self.tray_menu.addAction(action)

    def _set_sys_menu(self):
        self.tray_menu.addAction(QAction('EXIT', self.tray, triggered=self.quit))

    def _with_message(self, func, *args):
        self.show_message(func(*args))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Tray()
    t.show()
    sys.exit(app.exec_())
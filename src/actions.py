
from PyQt5.QtWidgets import QAction


def exit_action():
    print("EXIT")


def check_action():
    print("CHECK")


ACTION_LIST = [['exit', exit_action]]
CHECKABLE_LIST = [['check', check_action]]


def get_actions(parent):
    for a in ACTION_LIST:
        action = QAction(a[0], parent, triggered=a[1])
        yield action

    for c in CHECKABLE_LIST:
        action = QAction(c[0], parent, checkable=True, triggered=c[1])
        yield action

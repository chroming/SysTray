
from PyQt5.QtWidgets import QAction
from web_api import *


def exit_action():
    print("EXIT")


def check_action(*args):
    print("CHECKED") if args[0] else print("UNCHECKED")


ACTION_LIST = [['status', get_ss_status]]
CHECKABLE_LIST = [['check', check_action]]


def get_actions(parent):
    for a in ACTION_LIST:
        action = QAction(a[0], parent, triggered=a[1])
        yield action

    for c in CHECKABLE_LIST:
        action = QAction(c[0], parent, checkable=True, toggled=c[1])
        yield action

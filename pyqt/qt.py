import sys

if 'PyQt6' in sys.modules:
    # PyQt6
    from PyQt6 import QtGui, QtWidgets, QtCore, uic
    from PyQt6.QtCore import pyqtSignal as Signal, pyqtSlot as Slot, Qt
    from PyQt6.QtWidgets import *
    from PyQt6.QtGui import *
    from PyQt6.QtQuick import QQuickView
    from PyQt6.QtCore import *

    def load_ui(ui_file):
        return uic.loadUi(ui_file)


else:
    # PySide6
    from PySide6 import QtGui, QtWidgets, QtCore
    from PySide6.QtCore import Signal, Slot, Qt
    from PySide6.QtWidgets import *
    from PySide6.QtGui import *
    from PySide6.QtUiTools import QUiLoader
    from PySide6.QtQuick import QQuickView
    from PySide6.QtCore import *

    loader = None


    def load_ui(ui_file):
        global loader
        if loader is None:
            loader = QUiLoader()
        return loader.load(ui_file, None)


def run_ui(setup_widget):
    app = QApplication(sys.argv)
    w = setup_widget(app)
    w.show()
    sys.exit(app.exec())
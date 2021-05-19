import sys

from PySide6.QtWidgets import *


def run_ui(app):
    """
        clicked is signal
        on_button_clicked is slot
    """
    button = QPushButton('Click')
    button.clicked.connect(on_button_clicked)
    button.show()
    sys.exit(app.exec())


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()


if __name__ == '__main__':
    app = QApplication([])
    run_ui(app)

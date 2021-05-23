import sys

from qt import *


def setup_ui(app):
    """
        clicked is signal
        on_button_clicked is slot
    """
    button = QPushButton('Click')
    button.clicked.connect(on_button_clicked)
    return button


@Slot()  # @Slot() is a decorator that identifies a function as a slot. It is not important to understand why for now, but use it always to avoid unexpected behavior.
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()


if __name__ == '__main__':
    run_ui(setup_ui)

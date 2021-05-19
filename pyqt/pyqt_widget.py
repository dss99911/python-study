import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QMessageBox


def run_label(app):
    # label = QLabel('Hello World!')
    label = QLabel('Hello World!', alignment=Qt.AlignCenter)
    label.show()
    app.exec()


def run_button(app):
    button = QPushButton('Click')
    button.show()
    app.exec()


def run_message_box(app):
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()  # pause here until user close the message box
    sys.exit(app.exec())


if __name__ == '__main__':
    app = QApplication([])
    run_message_box(app)

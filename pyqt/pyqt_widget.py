from qt import *


def setup_label(app):
    # label = QLabel('Hello World!')
    return QLabel('Hello World!', alignment=Qt.AlignCenter)


def setup_button(app):
    return QPushButton('Click')


def setup_message_box(app):
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    # alert.exec()  # pause here until user close the message box
    return alert


if __name__ == '__main__':
    run_ui(setup_message_box)

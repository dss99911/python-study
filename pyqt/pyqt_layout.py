from qt import *


def vertical_layout(app):
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    return window


if __name__ == '__main__':
    run_ui(vertical_layout)

import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


def vertical_layout():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    vertical_layout()

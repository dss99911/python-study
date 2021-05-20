from qt import *


def run_ui():
    app = QApplication(sys.argv)
    window = load_ui("pyqt_ui.ui")
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    run_ui()

from qt import *


def run_ui():
    app = QApplication(sys.argv)
    window = load_ui("ui/main_dialog.ui")
    setup_ui(window)
    window.show()
    sys.exit(app.exec())


def setup_ui(window):
    window.pushButton.clicked.connect(click_test)


@Slot()
def click_test():
    print("test")


if __name__ == '__main__':
    run_ui()

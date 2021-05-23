from qt import *


def setup_ui(app):
    window = load_ui("ui/main_dialog.ui")
    window.pushButton.clicked.connect(click_test)
    return window


@Slot()
def click_test():
    print("test")


if __name__ == '__main__':
    run_ui(setup_ui)

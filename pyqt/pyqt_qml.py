from qt import *


def get_qml(app):
    view = QQuickView()
    url = QUrl("ui/view.qml")

    view.setSource(url)
    return view


if __name__ == '__main__':
    run_ui(get_qml)

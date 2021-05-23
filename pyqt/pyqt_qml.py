from qt import *

app = QApplication([])
view = QQuickView()
url = QUrl("view.qml")

view.setSource(url)
view.show()
sys.exit(app.exec())

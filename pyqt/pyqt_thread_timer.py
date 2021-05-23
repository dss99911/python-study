from qt import *


class Worker(QThread):
    finished = Signal(int)
    count2 = 1

    def run(self):
        while True:
            self.count2 += 1
            self.finished.emit(self.count2)
            self.msleep(500)


class MyWidget(QWidget):
    count = 1

    def __init__(self):
        super().__init__()

        self.text = QLabel("Hello World", alignment=Qt.AlignCenter)
        self.text2 = QLabel("Hello World2", alignment=Qt.AlignCenter)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.text2)

        self.start_timer()
        self.start_thread()

    def start_timer(self):
        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

    def start_thread(self):
        self.worker = Worker()
        self.worker.finished.connect(self.timeout2)
        self.worker.start()

    @Slot()
    def timeout(self):
        self.count += 1
        self.text.setText(str(self.count))

    @Slot(int)
    def timeout2(self, num):
        self.text2.setText(str(num))


def setup_widget(app):
    widget = MyWidget()
    widget.resize(800, 600)
    return widget


if __name__ == "__main__":
    run_ui(setup_widget)

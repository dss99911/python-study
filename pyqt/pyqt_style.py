from qt import *

# style doc : https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# 'Fusion', 'Windows', 'WindowsVista' (Windows only) and 'Macintosh' (Mac only).

def set_style(app):
    app.setStyle('Fusion')


def set_palette(app):
    palette = QPalette()
    palette.setColor(QPalette.ButtonText, Qt.red)
    app.setPalette(palette)


def set_stylesheet(app):
    """https://doc.qt.io/qt-5/stylesheet-syntax.html"""
    app.setStyleSheet("QPushButton { margin: 10ex; }")


def style_dark_fusion(app):
    app.setStyle("Fusion")

    dark_palette = QPalette()

    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)

    app.setPalette(dark_palette)

    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")


def setup_ui(app):
    style_dark_fusion(app)
    button = QPushButton('Hello World')
    return button



if __name__ == '__main__':
    run_ui(setup_ui)

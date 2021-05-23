from qt import *

data = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
        "Project B": ["file_b.csv", "photo.jpg"],
        "Project C": []}


def setup_ui(app):
    tree = QTreeWidget()
    tree.setColumnCount(2)
    tree.setHeaderLabels(["Name", "Type"])

    items = []
    for key, values in data.items():
        item = QTreeWidgetItem([key])
        for value in values:
            ext = value.split(".")[-1].upper()
            child = QTreeWidgetItem([value, ext])
            item.addChild(child)
        items.append(item)

    tree.insertTopLevelItems(0, items)
    return tree


if __name__ == '__main__':
    run_ui(setup_ui)

import sys
import os

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout

from PyQt5.QtWidgets import QAction, qApp, QMainWindow


class Notepad(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_area = QTextEdit()

        self.clear = QPushButton("Clear")

        self.open = QPushButton("Open File")

        self.save = QPushButton("Save")

        horizontal_box = QHBoxLayout()

        horizontal_box.addWidget(self.clear)
        horizontal_box.addWidget(self.open)
        horizontal_box.addWidget(self.save)

        vertical_box = QVBoxLayout()

        vertical_box.addWidget(self.text_area)

        vertical_box.addLayout(horizontal_box)

        self.setLayout(vertical_box)

        self.setWindowTitle("My Notepad")

        self.clear.clicked.connect(self.clear_text)
        self.open.clicked.connect(self.open_file)
        self.save.clicked.connect(self.save_file)



    def clear_text(self):
        self.text_area.clear()

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File", os.getenv("HOME"))

        with open(file_name[0], "r") as file:
            self.text_area.setText(file.read())

    def save_file(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File", os.getenv("HOME"))

        with open(file_name[0], "w") as file:
            file.write(self.text_area.toPlainText())

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = Notepad()

        self.setCentralWidget(self.window)

        self.create_menus()

    def create_menus(self):
        menubar = self.menuBar()

        file = menubar.addMenu("File")

        open_file = QAction("Open File", self)

        open_file.setShortcut("Ctrl+O")

        save_file = QAction("Save File", self)

        save_file.setShortcut("Ctrl+S")

        clear = QAction("Clear", self)

        clear.setShortcut("Ctrl+D")

        exit = QAction("Exit", self)

        exit.setShortcut("Ctrl+Q")

        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(clear)
        file.addAction(exit)

        file.triggered.connect(self.response)



        self.setWindowTitle("Text Editor")

        self.show()

    def response(self, action):
        if action.text() == "Open File":
            self.window.open_file()
        elif action.text() == "Save File":
            self.window.save_file()
        elif action.text() == "Clear":
            self.window.clear_text()
        elif action.text() == "Exit":
            qApp.quit()


application = QApplication(sys.argv)

menu = Menu()

sys.exit(application.exec_())


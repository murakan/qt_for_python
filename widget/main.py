#!/usr/bin/env python
# -*- mode: python; coding: utf-8 -*-

import sys
import random
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide2.QtCore    import Qt, Slot

def make_str(str):
    return '<h1><font color="blue">' + str + '</font></h1>'

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # Create widges
        self.label_ = QLabel(make_str('I am a sample.'))
        self.label_.setAlignment(Qt.AlignCenter)
        self.button_ = QPushButton('Click me!')
        # Layout widgets
        self.layout_ = QVBoxLayout()
        self.layout_.addWidget(self.label_)
        self.layout_.addWidget(self.button_)
        self.setLayout(self.layout_)
        # signal & slot connection
        self.button_.clicked.connect(self.clicked)

    @Slot()
    def clicked(self):
        self.label_.setText(make_str('Hello world!'))

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.resize(800, 600)
    main.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python
# -*- mode: python; coding: utf-8 -*-

import sys
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

def main():
    # Prepare application
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    # Load main QML and launch application
    engine.load('main.qml')
    if not engine.rootObjects():
        sys.exit(-1)
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())

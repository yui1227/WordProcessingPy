from PySide6.QtWidgets import QApplication
from UI_func import MainWindow
import sys
import os
os.environ["TF_USE_LEGACY_KERAS"] = '1'


def main():
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
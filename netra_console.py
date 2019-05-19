import sys
import logging
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QStyle
from netra.ui.main_window import MainWindow

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)-30.30s] [%(levelname)-5.5s]  %(message)s",
        handlers=[
            logging.FileHandler("{0}/{1}.log".format("log", "netra-ai")),
            logging.StreamHandler()
        ])
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.setGeometry(
        QStyle.alignedRect(
            Qt.LeftToRight,
            Qt.AlignCenter,
            mainWindow.size(),
            app.desktop().availableGeometry()
        )  
    )
    mainWindow.show()
    sys.exit(app.exec())

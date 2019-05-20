import sys
import dlib
import logging
from PyQt5.QtCore import Qt, QPoint, QRect, pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QMouseEvent, QColor

log = logging.getLogger(__name__)

class NetraImageWidget(QLabel):
    mouseMoved = pyqtSignal(QMouseEvent)
    newRectangle = pyqtSignal(QRect)

    def __init__(self, parent):
        super(NetraImageWidget, self).__init__(parent=parent)
        
        self._drawing = False
        self._lastPoint = QPoint() 
        self._currentPoint = QPoint()
        self._drawColor = QColor(255, 0, 0)

    def paintEvent(self, event):
        super(NetraImageWidget, self).paintEvent(event)

        painter = QPainter(self)
        painter.setPen(QPen(self._drawColor, 3, Qt.SolidLine))
        
        if self._drawing:
            painter.drawRect(QRect(self._lastPoint, self._currentPoint))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drawing = True
            self._lastPoint = event.pos()
            event.accept()
            super(NetraImageWidget, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self._drawing:
            self._currentPoint = event.pos()
            self.update()
            self.mouseMoved.emit(event)
            event.accept()
            super(NetraImageWidget, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self._drawing = False
            self.newRectangle.emit(QRect(self._lastPoint, self._currentPoint))
            log.info("Release mouse...")
            event.accept()
            super(NetraImageWidget, self).mouseReleaseEvent(event)

    def selectedRect(self):
        return QRect(self._lastPoint, self._currentPoint)

    def drawColor(self):
        return self._drawColor

    def setDrawColor(self, color):
        self._drawColor = color
# internal
from widgets import ModelViewWidget
# pyqt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout


class UI(QMainWindow):
    """User Interfaces"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bootstrap()

    def _bootstrap(self):
        self._createUI()
        self._addWidgets()
        self._connectSignals()

    def _createUI(self):
        self.centWidget = QWidget(self)
        self.setCentralWidget(self.centWidget)
        self.generalLayout = QVBoxLayout()
        self.centWidget.setLayout(self.generalLayout)

    def _addWidgets(self):
        self.mv = ModelViewWidget()
        self.generalLayout.addWidget(self.mv)

    def _connectSignals(self):
        pass

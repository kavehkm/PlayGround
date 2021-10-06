# pyqt
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QAbstractListModel, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListView


class BaseWidget(QWidget):
    """Base Widget"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bootstrap()

    def _bootstrap(self):
        self._createWidget()
        self._connectSignals()
        self._setStyles()

    def _createWidget(self):
        self.generalLayout = QVBoxLayout()
        self.setLayout(self.generalLayout)

    def _connectSignals(self):
        pass

    def _setStyles(self):
        pass


##############
# Model/View #
##############
class OrderModel(QAbstractListModel):
    """Order Model"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orders = list()

    def data(self, index, role):
        row = index.row()
        orderno, customer, status = self.orders[row]
        if role == Qt.DisplayRole:
            return '{}) {}[{}]'.format(orderno, customer, status)
        elif role == Qt.BackgroundRole:
            if status == 'completed':
                return QColor(215, 228, 188)
            else:
                return QColor(230, 185, 184)

    def rowCount(self, index):
        return len(self.orders)


class ModelViewWidget(BaseWidget):
    """Model/View Widget"""
    def _createWidget(self):
        super()._createWidget()
        # orders list
        self.ordersList = QListView()
        self.generalLayout.addWidget(self.ordersList)
        # orders model
        self.model = OrderModel()
        self.ordersList.setModel(self.model)
        # add form layout
        self.addLayout = QHBoxLayout()
        self.generalLayout.addLayout(self.addLayout)
        self.orderNo = QLineEdit()
        self.customer = QLineEdit()
        self.status = QLineEdit()
        self.btnAdd = QPushButton('Add')
        self.addLayout.addWidget(self.orderNo)
        self.addLayout.addWidget(self.customer)
        self.addLayout.addWidget(self.status)
        self.addLayout.addWidget(self.btnAdd)

    def _connectSignals(self):
        super()._connectSignals()
        self.btnAdd.clicked.connect(self.addHandler)

    def _setStyles(self):
        self.setStyleSheet("""
            QListView::item{
                min-height: 50px;
            }
        """)

    def addHandler(self):
        self.model.orders.append([self.orderNo.text(), self.customer.text(), self.status.text()])
        self.model.layoutChanged.emit()

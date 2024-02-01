
from PyQt6.QtWidgets import QWidget, QStackedLayout

from ChartView import ChartView


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QStackedLayout(self)

        chartView = ChartView(parent)

        layout.addWidget(chartView)

        self.setLayout(layout)
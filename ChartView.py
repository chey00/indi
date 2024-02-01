from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QSplineSeries, QValueAxis, QAbstractAxis
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget

# Package: PyQt6-Charts
# https://github.com/chey00/qchart
class ChartView(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)

        series = QSplineSeries()

        chart = QChart()
        chart.setTitle("Die wunderbare Welt der Mathematik")
        chart.addSeries(series)

        axis_x = QValueAxis()
        axis_x.setRange(1, 4)

        axis_y = QValueAxis()
        axis_y.setRange(0, 10)

        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignTop)
        series.attachAxis(axis_x)

        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        series.setName("Parabel")
        series.append(0, 0)
        series.append(1, 1)
        series.append(2, 4)
        series.append(3, 9)
        series.append(4, 16)
        series.append(5, 25)

        self.setChart(chart)

import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui
import PyQt5.QtCore as core


class ViewWin(widgets.QWidget):

    def __init__(self, points):
        super().__init__()

        self.points = points

        self.setWindowTitle('Bez curve')
        canvas = gui.QPixmap(1800, 800)
        canvas.fill(gui.QColor("white"))

        self.label = widgets.QLabel()
        self.label.setPixmap(canvas)

        vbox = widgets.QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.prev_poly = gui.QPolygon([core.QPoint(0, 0),core.QPoint(0, 0)])

        self.draw()

    def draw(self):
        with gui.QPainter(self.label.pixmap()) as painter:
            prev = self.points[0]
            for point in self.points[1:]:
                painter.drawLine(
                    core.QPoint(*prev),
                    core.QPoint(*point)
                )
                prev = point

            pen = gui.QPen()
            pen.setColor(gui.QColor(255, 0, 0, 127))
            pen.setWidth(10)
            painter.setPen(pen)

            curve = self.curve(self.points[:4])
            painter.drawPoints(gui.QPolygon([core.QPoint(*point) for point in curve]))

            curve = self.curve(self.points[3:7])
            painter.drawPoints(gui.QPolygon([core.QPoint(*point) for point in curve]))

            curve = self.curve(self.points[6:])
            painter.drawPoints(gui.QPolygon([core.QPoint(*point) for point in curve]))

    def curve(self, dots):
        curve = []
        for i in map(lambda x: x/100.0, range(100)):
            x = (1.0-i)**3*dots[0][0] + 3*(1.0-i)**2*i*dots[1][0] + 3*(1.0-i)*i**2*dots[2][0] + i**3*dots[3][0]
            y = (1.0-i)**3*dots[0][1] + 3*(1.0-i)**2*i*dots[1][1] + 3*(1.0-i)*i**2*dots[2][1] + i**3*dots[3][1]
            curve.append([int(x), int(y)])

        return curve
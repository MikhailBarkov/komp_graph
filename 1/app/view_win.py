from math import sqrt, acos, atan2, cos, sin

import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui
import PyQt5.QtCore as core


class ViewWin(widgets.QWidget):

    def __init__(self, cycle, radius, point):
        super().__init__()

        self.xc, self.yc = cycle
        self.xp, self.yp = point
        self.radius = radius

        self.setWindowTitle('')
        canvas = gui.QPixmap(800, 800)
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
            painter.drawEllipse(
                core.QPoint(self.xc, self.yc),
                self.radius,
                self.radius
            )

            x2, y2 = self.tanget()

            print(x2, y2)

            painter.drawLine(
                core.QPoint(self.xp, self.yp),
                core.QPoint(int(x2), int(y2))
            )

    def tanget(self):
        P1x = self.xc
        P1y = self.yc

        P2x = (self.xc + self.xp) / 2
        P2y = (self.yc + self.yp) / 2

        R1 = self.radius
        R2 = sqrt((self.xp - P2x)**2 + (self.yp - P2y)**2)

        d = R2

        b = (R2**2 - R1**2 + d**2) / (2*d)

        a = d - b

        P0x = P1x + (P2x - P1x) * a / d
        P0y = P1y + (P2y - P1y) * a / d

        h = sqrt(R1**2 - a**2)

        P3x = P0x + (P2y - P1y) * h / d
        P3y = P0y - (P2x - P1x) * h / d

        return P3x, P3y

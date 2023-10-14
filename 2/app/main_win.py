from random import randint

import PyQt5.QtWidgets as widgets

from view_win import ViewWin


class MainWindow(widgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Параметры')
        self.setGeometry(100, 100, 600, 700)

        layout = widgets.QGridLayout()
        self.setLayout(layout)

        self.start_btn = widgets.QPushButton('Start')
        self.start_btn.clicked.connect(self.start)

        self.err_msg = widgets.QLabel(self)

        self.points_labels = []
        self.points_flds = []
        for i in range(1, 11):
            self.points_labels.append(widgets.QLabel(f'Координаты точки {i}'))
            self.points_flds.append(widgets.QLineEdit(f'{i*150}, {randint(100, 500)}'))

            layout.addWidget(self.points_flds[-1], i, 1)
            layout.addWidget(self.points_labels[-1], i, 0)

        layout.addWidget(self.err_msg, 0, 0)

        layout.addWidget(self.start_btn, 11, 0)

        self.start()

    def start(self):
        points = []
        for i in range(10):
            try:
                points.append(
                    tuple(int(p) for p in self.points_flds[i].text().strip().split(', '))
                )
            except BaseException:
                self.err_msg.setText('Некорректно заданы Координаты точки!')
                return

        try:
            self.view_win = ViewWin(points)
            self.view_win.show()
        except ValueError as e:
            self.err_msg.setText(e.args[0])


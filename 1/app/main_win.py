import PyQt5.QtWidgets as widgets

from view_win import ViewWin


class MainWindow(widgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Параметры круга')
        self.setGeometry(100, 100, 500, 550)

        layout = widgets.QGridLayout()
        self.setLayout(layout)

        self.start_btn = widgets.QPushButton('Start')
        self.start_btn.clicked.connect(self.start)

        self.err_msg = widgets.QLabel(self)

        self.cycle_center_label = widgets.QLabel('Центр круга')
        self.cycle_center_fld = widgets.QLineEdit('400, 400')

        self.cycle_radius_label = widgets.QLabel('Радиус круга')
        self.cycle_radius_fld = widgets.QLineEdit('100')

        self.point_label = widgets.QLabel('Координаты точки')
        self.point_fld = widgets.QLineEdit('40, 20')

        layout.addWidget(self.err_msg, 0, 0)
        layout.addWidget(self.cycle_center_fld, 1, 1)
        layout.addWidget(self.cycle_center_label, 1, 0)

        layout.addWidget(self.cycle_radius_fld, 2, 1)
        layout.addWidget(self.cycle_radius_label, 2, 0)

        layout.addWidget(self.point_fld, 4, 1)
        layout.addWidget(self.point_label, 4, 0)

        layout.addWidget(self.start_btn, 6, 0)

        self.start()

    def start(self):
        try:
            cycle_x, cycle_y = [
                int(p) for p in self.cycle_center_fld.text().strip().split(', ')
            ]
        except BaseException as e:
            raise e
            self.err_msg.setText('Некорректно заданы Координаты Центра окружности!')

        try:
            radius = int(self.cycle_radius_fld.text().strip())
        except ValueError as e:
            raise e
            self.err_msg.setText('Некорректно задан Радиус окружности!')

        try:
            point_x, point_y = [
                int(p) for p in self.point_fld.text().strip().split(', ')
            ]
        except BaseException:
            self.err_msg.setText('Некорректно заданы Координаты точки!')


        try:
            self.view_win = ViewWin((cycle_x, cycle_y), radius, (point_x, point_y))
            self.view_win.show()
        except ValueError as e:
            self.err_msg.setText(e.args[0])


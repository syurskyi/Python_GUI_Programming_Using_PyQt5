from PyQt5.QtWidgets import *
import sys


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Employees")
        self.setGeometry(450, 150, 750, 600)
        self.ui()
        self.show()

    def ui(self):
        self.main_design()
        self.layout()

    def main_design(self):
        self.employee_list = QListWidget()
        self.btn_new = QPushButton("New")
        self.btn_update = QPushButton("Update")
        self.btn_delete = QPushButton("Delete")

    def layout(self):
        # ###############################Layouts#####################################################################

        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_bottom_layout = QHBoxLayout()

        # ###############################Adding child layouts to main layout#########################################

        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)
        self.main_layout.addLayout(self.left_layout, 40)
        self.main_layout.addLayout(self.right_main_layout, 60)

        # ###############################adding widgets to layouts###################################################

        self.right_top_layout.addWidget(self.employee_list)
        self.right_bottom_layout.addWidget(self.btn_new)
        self.right_bottom_layout.addWidget(self.btn_update)
        self.right_bottom_layout.addWidget(self.btn_delete)

        # ###############################Setting main window layout##################################################

        self.setLayout(self.main_layout)


def main():
    APP = QApplication(sys.argv)
    window = Main()
    sys.exit(APP.exec_())


if __name__ == '__main__':
    main()
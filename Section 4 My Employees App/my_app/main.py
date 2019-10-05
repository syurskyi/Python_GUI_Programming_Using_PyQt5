from PyQt5.QtWidgets import *
import sys
import sqlite3


connection = sqlite3.connect('employees.db')
cursor = connection.cursor()


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Employees")
        self.setGeometry(450, 150, 750, 600)
        self.ui()
        self.show()

    def ui(self):
        self.main_design()
        self.layouts()

    def main_design(self):
        self.employee_list = QListWidget()
        self.btn_new = QPushButton("New")
        self.btn_new.clicked.connect(self.add_employee)
        self.btn_update = QPushButton("Update")
        self.btn_delete = QPushButton("Delete")

    def layouts(self):
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

    def add_employee(self):
        self.new_employee = AddEmployer()
        self.close()


class AddEmployer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employee")
        self.setGeometry(450, 150, 350, 600)
        self.ui()
        self.show()

    def ui(self):
        self.main_design()
        self.layouts()

    def main_design(self):
        pass

    def layouts(self):
        # #########################creating main layout########################################################

        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()

        # #########################adding child layoutd to main layout#########################################

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout((self.bottom_layout))

        # #########################setting main layout for window##############################################
        self.setLayout(self.main_layout)


def main():
    APP = QApplication(sys.argv)
    window = Main()
    sys.exit(APP.exec_())


if __name__ == '__main__':
    main()
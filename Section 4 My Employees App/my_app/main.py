from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
import sys
import os
import sqlite3
from PIL import Image


connection = sqlite3.connect('employees.db')
cursor = connection.cursor()
default_image = "person.png"


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

    def closeEvent(self, event):
        self.main = Main()


    def main_design(self):

        # ##############Top Layout widgets#######################

        self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        self.title = QLabel("Add Person")
        self.title.setStyleSheet("font-size: 24pt; font-family; Arial Bold;")
        self.img_add = QLabel()
        self.img_add.setPixmap(QPixmap("icons/person.png"))

        # ##################Bottom Layout Widgets#####################

        self.name_lbl = QLabel("Name :")
        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText("Enter Employee Name")
        self.surname_lbl = QLabel("Surname :")
        self.surname_entry = QLineEdit()
        self.surname_entry.setPlaceholderText("Enter Employee Surname")
        self.phone_lbl = QLabel("Phone :")
        self.phone_entry = QLineEdit()
        self.phone_entry.setPlaceholderText("Enter Employee Phone Number")
        self.email_lbl = QLabel("Email :")
        self.email_entry = QLineEdit()
        self.email_entry.setPlaceholderText("Enter Employee Email")
        self.img_lbl = QLabel("Picture: ")
        self.img_button = QPushButton("Browse")
        self.img_button.setStyleSheet("background-color:orange;font-size:10pt")
        self.img_button.clicked.connect(self.upload_image)
        self.address_lbl = QLabel("Address: ")
        self.address_editor = QTextEdit()
        self.add_button = QPushButton("Add")
        self.add_button.setStyleSheet("background-color:orange;font-size:10pt")
        self.add_button.clicked.connect(self.add_employee)

    def layouts(self):

        # #########################creating main layout########################################################

        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()

        # #########################adding child layoutd to main layout#########################################

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout((self.bottom_layout))

        # #########################adding widget to layout#####################################################
        # #########################top layout################

        self.top_layout.addStretch()
        self.top_layout.addWidget(self.title)
        self.top_layout.addWidget((self.img_add))
        self.top_layout.addStretch()
        self.top_layout.setContentsMargins(110, 20, 10, 30)

        # #########################bottom layout################

        self.bottom_layout.addRow(self.name_lbl, self.name_entry)
        self.bottom_layout.addRow(self.surname_lbl, self.surname_entry)
        self.bottom_layout.addRow(self.phone_lbl, self.phone_entry)
        self.bottom_layout.addRow(self.email_lbl, self.email_entry)
        self.bottom_layout.addRow(self.img_lbl, self.img_button)
        self.bottom_layout.addRow(self.address_lbl, self.address_editor)
        self.bottom_layout.addRow("", self.add_button)

        # #########################setting main layout for window##############################################

        self.setLayout(self.main_layout)

    def upload_image(self):
        global default_image
        size = (128, 128)
        self.file_name, ok = QFileDialog.getOpenFileName(self, "Upload Image", '', "Image Files(*.jpg *.png)")

        if ok:
            print(self.file_name)
            default_image = os.path.basename(self.file_name)
            print(default_image)
            image = Image.open(self.file_name)
            image = image.resize(size)
            image.save("images/{}".format(default_image))

    def add_employee(self):
        global default_image
        name = self.name_entry.text()
        surname = self.surname_entry.text()
        phone = self.phone_entry.text()
        email = self.email_entry.text()
        image = default_image
        address = self.address_editor.toPlainText()

        if (name and surname and phone != ""):
            try:
                query = "INSERT INTO employees(name, surname, phone, email, image, address) VALUES(?, ? , ? , ? , ? ,?)"
                cursor.execute(query, (name, surname, phone, email, image, address))
                connection.commit()
                QMessageBox.information(self, "Success", "Person has been added")
                self.close()
                self.main = Main()
            except:
                QMessageBox.information(self, "Warning", "Person has not been added")
        else:
            QMessageBox.information(self, "Warning", "Fields can not be empty")


def main():
    APP = QApplication(sys.argv)
    window = Main()
    sys.exit(APP.exec_())


if __name__ == '__main__':
    main()

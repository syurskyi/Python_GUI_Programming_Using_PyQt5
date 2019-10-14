import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
from PIL import Image

connect = sqlite3.connect('products.db')
cursor = connect.cursor

class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Product")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.ui()
        self.show()

    def ui(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # ##################widgets of top layout##########
        self.add_product_image = QLabel()
        self.image = QPixmap('icons/addproduct.png')
        self.add_product_image.setPixmap(self.img)
        self.title_text = QLabel("Add Product")
        # ################widgets of bottom layot###########
        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText("Enter name of product")
        self.manufacturer_entry = QLineEdit()
        self.manufacturer_entry.setPlaceholderText("Enter name of manufacturer")
        self.price_entry = QLineEdit()
        self.price_entry.setPlaceholderText("Enter price of product")
        self.qouta_entry = QLineEdit()
        self.qouta_entry.setPlaceholderText("Enter qouta of product")
        self.upload_button = QPushButton("Upload")
        # self.upload_button.clicked.connect(self.upload_image)
        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.addProduct)

    def layouts(self):
        pass

    def upload_image(self):
        pass

    def add_product(self):
        pass
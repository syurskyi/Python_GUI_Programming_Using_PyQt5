import sys
from PyQt5.QtWidgets import *


class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Player')
        self.setGeometry(450, 150, 480, 700)
        self.ui()
        self.show()

    def ui(self):
        self.widgets()
        self.layout()

    def widgets(self):
        ####################################Progress Bar#######################################################
        self.progress_bar = QProgressBar()
        ####################################Buttons#######################################################

    def layouts(self):
        ####################################Creating Layouts#######################################################
        self.main_layout = QVBoxLayout()
        self.top_main_layout = QVBoxLayout()
        self.top_groupbox = QGroupBox('Music Player', self)
        self.top_groupbox.setStyleSheet('background-color:#fcc324')
        self.top_layout = QHBoxLayout()
        self.middle_layout = QHBoxLayout()
        self.bottom_layout = QVBoxLayout()

        ####################################Adding Widgets#######################################################
        ####################################Top Layouts Widgets##################################################
        self.top_layout.addWidget(self.progress_bar)
        self.top_main_layout.addLayout(self.top_layout)
        self.top_main_layout.addLayout(self.middle_layout)
        self.top_groupbox.setLayout(self.top_main_layout)
        self.main_layout.addWidget(self.top_groupbox)
        self.main_layout.addWidget(self.bottom_layout)
        self.setLayout(self.main_layout)


def main():
    App = QApplication(sys.argv)
    window = Player()
    sys.exit(App.exec_())

if __name__ =='__main':
    main()
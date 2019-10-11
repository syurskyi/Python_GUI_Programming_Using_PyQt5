import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize,Qt,QTimer


class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Player')
        self.setGeometry(450, 150, 480, 700)
        self.ui()
        self.show()

    def ui(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # ###################################Progress Bar#######################################################
        self.progress_bar = QProgressBar()
        # ###################################Buttons#######################################################
        self.add_button = QToolButton()
        self.add_button.setIcon(QIcon("icons/add.png"))
        self.add_button.setIconSize(QSize(48, 48))
        self.add_button.setToolTip("Add a Song")

        self.shuffle_button = QToolButton()
        self.shuffle_button.setIcon(QIcon("icons/shuffle.png"))
        self.shuffle_button.setIconSize(QSize(48, 48))
        self.shuffle_button.setToolTip("Shuffle The list")
        # self.shuffle_button.clicked.connect(self.shuffle_play_list)

        self.previous_button = QToolButton()
        self.previous_button.setIcon(QIcon("icons/previous.png"))
        self.previous_button.setIconSize(QSize(48, 48))
        self.previous_button.setToolTip("Play Previous")
        # self.previous_button.clicked.connect(self.play_previous)

        self.play_button = QToolButton()
        self.play_button.setIcon(QIcon("icons/play.png"))
        self.play_button.setIconSize(QSize(64, 64))
        self.play_button.setToolTip("Play")
        # self.play_button.clicked.connect(self.play_sounds)

        self.next_button = QToolButton()
        self.next_button.setIcon(QIcon("icons/next.png"))
        self.next_button.setIconSize(QSize(48, 48))
        self.next_button.setToolTip("Play Next")
        # self.next_button.clicked.connect(self.play_next)

        self.mute_button = QToolButton()
        self.mute_button.setIcon(QIcon("icons/mute.png"))
        self.mute_button.setIconSize(QSize(24, 24))
        self.mute_button.setToolTip("Mute")
        # self.mute_button.clicked.connect(self.mute_sound)

    def layouts(self):
        # ###################################Creating Layouts#######################################################
        self.main_layout = QVBoxLayout()
        self.top_main_layout = QVBoxLayout()
        self.top_groupbox = QGroupBox('Music Player')
        self.top_groupbox.setStyleSheet('background-color:#fcc324')
        self.top_layout = QHBoxLayout()
        self.middle_layout = QHBoxLayout()
        self.bottom_layout = QVBoxLayout()

        # ###################################Adding Widgets#######################################################
        # ###################################Top Layouts Widgets##################################################
        self.top_layout.addWidget(self.progress_bar)

        # #################Middle layout Widget#################
        self.middle_layout.addStretch()
        self.middle_layout.addWidget(self.add_button)
        self.middle_layout.addWidget(self.shuffle_button)
        self.middle_layout.addWidget(self.play_button)
        self.middle_layout.addWidget(self.previous_button)
        self.middle_layout.addWidget(self.next_button)
        # self.middle_layout.addWidget(self.volume_slider)
        self.middle_layout.addWidget(self.mute_button)
        self.middle_layout.addStretch()

        self.top_main_layout.addLayout(self.top_layout)
        self.top_main_layout.addLayout(self.middle_layout)
        self.top_groupbox.setLayout(self.top_main_layout)
        self.main_layout.addWidget(self.top_groupbox)
        self.main_layout.addLayout(self.bottom_layout)
        self.setLayout(self.main_layout)


def main():
    App = QApplication(sys.argv)
    window = Player()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
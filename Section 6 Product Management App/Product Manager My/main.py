import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Product Manager')
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 1350, 750)
        self.setFixedSize(self.size())

        self.ui()
        self.show()

    def ui(self):
        self.toolbar()
        self.tab_widget()

    def toolbar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # ####################Toolbar Buttons############
        # ###################Add Product#################
        self.add_product = QAction(QIcon('icons/add.png'), 'Add Product', self)
        self.tb.addAction(self.add_product)
        self.tb.addSeparator()

        # #####################Add Member################
        self.add_member = QAction(QIcon('icons/users.png'), "Add Member", self)
        self.tb.addAction(self.add_member)
        # self.add_member.trigger.connect()
        self.tb.addSeparator()

        # #####################Sell Products###############
        self.sell_product = QAction(QIcon('icons/sell.png'), "Sell Product", self)
        self.tb.addAction(self.sell_product)
        # self.sellProduct.triggered.connect(self.funcSellProducts)
        self.tb.addSeparator()

    def tab_widget(self):
        self.tabs = QTabWidget()
        # self.tabs.blockSignals(True)
        self.setCentralWidget(self.tabs)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "Products")
        self.tabs.addTab(self.tab2, "Members")
        self.tabs.addTab(self.tab3, "Statistics")


def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

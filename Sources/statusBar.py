import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("状态栏例子")
        self.resize(400,200)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("show")
        file.triggered.connect(self.processTrigger)

        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)


        tb1 = self.addToolBar("File")
        new = QAction(QIcon("../Images/Avatar.jpg"),"new",self)
        tb1.addAction(new)

        tb1.setToolButtonStyle(Qt.ToolButtonFollowStyle)#设置图标与文本显示方式

    def processTrigger(self,q):
        if q.text() == "show":
            self.statusBar.showMessage(q.text() + "菜单被点击", 5000) #显示5秒钟自动关闭



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = StatusBar()
    w.show()
    sys.exit(app.exec_())








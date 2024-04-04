#Press Alt+Shift+M
import maya.cmds as mc

from PySide2.QtWidgets import QWidget,QLabel, QVBoxLayout, QPushButton


class CreateLimbControl:
    def __init__(self):
        self.root = ""
        self.mid = ""
        self.end = ""

    def FindJntBasedOnRootSel(self):
        self.root = mc.ls(sl=True, type = "joint") [0]
        self.mid - mc.listRelatives(self.root, c=True, type="joint") [0]
        self.end = mc.listRelatives(self.mid, c=True, type="joint")[0]

class CreateLimbControllerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create IkFk Limnb")
        self.setGeometry(100,100,300,300)
        self.masterlayout = QVBoxLayout()
        self.setLayout(self.masterlayout)
        
        hintLabel = QLabel("Please Select the root of the Limb: ")
        self.masterlayout.addWidget(hintLabel)

        findJntsButton = QPushButton("Find Jnts")
        findJntsButton.clicked.connect(self.FindJntBtnClicked)

        self.masterlayout.addWidget(findJntsButton)
        
        self.autoFindJntDisplay = QLabel("")
        self.masterlayout.addWidget(self.autoFindJntDisplay)
        self.adjustSize()

        self.createLimbCtrl = CreateLimbControl()

    def FindJntBtnClicked(self):
        self.createLimbCtrl.FindJntBasedOnRootSel()
        self.autoFindJntDisplay.setText(f"{self.createLimbCtrl.root},{self.createLimbCtrl.mid},{self.createLimbCtrl.end}")


ControllerWidget = CreateLimbControllerWidget()
ControllerWidget.show()
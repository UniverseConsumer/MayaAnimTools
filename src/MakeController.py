#Press Alt+Shift+M
import maya.cmds as mc

from PySide2.QtWidgets import QWidget,QLabel, QVBoxLayout, QPushButton


class CreateControllerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create IkFk Limnb")
        self.setGeometry(100,100,300,300)
        self.masterlayout = QVBoxLayout()
        self.setLayout(self.masterlayout)
        
        hintLabel = QLabel("Please Select the root of the Limb: ")
        self.masterlayout.addWidget(hintLabel)

        findJntsButton = QPushButton("Find Jnts")
        findJntsButton.clicked.connect(self,FindJntBtnClicked)

        self.masterlayout.addWidget(findJntsButton)
        self.adjustSize()

        def FindJntBtnClicked(self):
            print ("I am clicked.")


ControllerWidget = CreateControllerWidget()
ControllerWidget.show()
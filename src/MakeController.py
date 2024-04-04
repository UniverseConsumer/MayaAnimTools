#Press Alt+Shift+M
import maya.cmds as mc

from PySide2.QtWidgets import QWidget,QLabel, QVBoxLayout


class CreateControllerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create IkFk Limnb")


ControllerWidget = CreateControllerWidget()
ControllerWidget.show()
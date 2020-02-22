import sys
from mainwindow import Ui_MainWindow
from setting_dialog import Ui_Dialog
from PyQt5 import QtWidgets, QtCore

class SettingDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def plane_text(self):
        result = self.exec()
        plane_text = self.ui.textEdit.toPlainText()
        return (plane_text, result == QtWidgets.QDialog.Accepted)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionSetting.triggered.connect(self.show_setting_dialog)

    def show_setting_dialog(self):
        plane_text, result = SettingDialog(self).plane_text()
        if result:
            self.ui.textBrowser.setPlainText(plane_text)
 
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(app)
    window.show()
    app.exec_()
 
if __name__ == '__main__':
    main()

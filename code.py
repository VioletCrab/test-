from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLayout, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap, QIcon

win_width, win_hight = 500, 300
win_x, win_y = 200, 200
txt_title = "Десктопное приложение для проведения расчета чистой приведенной прибыли денежного потока"
txt_send = "Рассчитать"
txt_line = "Ставка в %"
txt_line1 = "Первоначальный вклад"
txt_line2 = "Переод начисления %"
txt_line3 = "Срок"

class MainWindow(QWidget):
    def __init__(self, parent = None, flags = Qt.WindowFlags()):
        super().__init__(parent = parent, flags = flags)
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    def initUI(self):
        self.btn_send = QPushButton(txt_send, self)
        self.line = QLineEdit(txt_line)
        self.line1 = QLineEdit(txt_line1)
        self.line2 = QLineEdit(txt_line2)
        self.line3 = QLineEdit(txt_line3)
        self.lable_finish = QLabel()
        self.txt_line_opr = QLabel("% по вкладу")
        self.txt_line1_opr = QLabel("начальная сумма вклада")
        self.txt_line2_opr = QLabel("частота начисления %")
        self.txt_line3_opr = QLabel("период, который внесенные денежные средства будут храниться на депозитном счету в банке.")
        

        #self.pixmap = QPixmap("card1.png")
        #self.pixmap = self.pixmap.scaledToWidth(64)
        #self.pixmap = self.pixmap.scaledToHeight(256)
        #картинка
        #self.lbl = QLabel(self)
        #self.lbl.setPixmap(self.pixmap)

        self.layoutV = QVBoxLayout()
        self.layoutH1 = QHBoxLayout()
        self.layoutH2 = QHBoxLayout()
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutH1.addWidget(self.line1, alignment = Qt.AlignLeft)
        self.layoutH1.addWidget(self.txt_line1_opr, alignment = Qt.AlignLeft)
        self.layoutH1.addWidget(self.line2, alignment = Qt.AlignCenter)
        self.layoutH1.addWidget(self.txt_line2_opr, alignment = Qt.AlignCenter)
        self.layoutH1.addWidget(self.line3, alignment = Qt.AlignRight)
        self.layoutH1.addWidget(self.txt_line3_opr, alignment = Qt.AlignRight)
        self.layoutH2.addWidget(self.line, alignment = Qt.AlignLeft)
        self.layoutH2.addWidget(self.txt_line_opr,alignment = Qt.AlignLeft)
        self.layoutH2.addWidget(self.btn_send, alignment = Qt.AlignCenter)
        self.layoutH2.addWidget(self.lable_finish, alignment = Qt.AlignRight)
        self.setLayout(self.layoutV)



    def scet(self):
        return (int(self.line1.text()) * int(self.line.text()) * int(self.line2.text()) / (int(self.line3.text()) * 365))//100


    def next_click(self):
        self.lable_finish.setText(str(self.scet()) + " руб.")

    def connects(self):
        self.btn_send.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_hight)
        self.move(win_x, win_y)

def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()

main()
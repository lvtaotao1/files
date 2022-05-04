from PyQt5.Qt import *
import sys
class TextQPlain(QPlainTextEdit):
    def __init__(self,tttt):
        super().__init__()  # 调用父类QWidget中的init方法
        self.scrollbar1 = tttt

    def wheelEvent(self, evt):
        print(type(evt.angleDelta()))
        if evt.angleDelta().y() > 0:
            self.sliderup()
        if evt.angleDelta().y()<0:
            self.sliderdown()

    def sliderdown(self):
        value = self.scrollbar1.value()
        print(value)
        self.scrollbar1.setValue(value+1)

    def sliderup(self):
        value = self.scrollbar1.value()
        print(value)
        self.scrollbar1.setValue(value-1)

class Window(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类QWidget中的init方法
        self.setWindowTitle("软件名称")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        self.scrollbar1 = QScrollBar()
        self.text1 = TextQPlain(self.scrollbar1)
        self.data=[]
        for i in range(10000):
            self.data.append('''第{}行\n'''.format(str(i)))
        text = ''.join(self.data)
        self.text1.setPlainText(text)
        self.text1.setReadOnly(True)
        a = self.text1.verticalScrollBar()

        self.text1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        print("文本框大小",self.text1.size())

        self.scrollbar1.setFixedSize(30,1000)
        self.scrollbar1.setMaximum(len(self.data)-62)
        self.scrollbar1.valueChanged.connect(self.sliderMoved)
        self.vbox = QHBoxLayout()

        self.vbox.addWidget(self.text1)
        self.vbox.addWidget(self.scrollbar1)
        self.setLayout(self.vbox)

    def sliderMoved(self):
        tt = ''.join(self.data[self.scrollbar1.value():self.scrollbar1.value()+63])
        self.text1.setPlainText(tt)
        print(self.scrollbar1.value())



if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用程序对象
    window = Window()
    window.show()
    sys.exit(app.exec_())  # 0是正常退出

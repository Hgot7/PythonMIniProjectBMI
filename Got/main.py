import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog


class Screen2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Screen2,self).__init__()
        loadUi("BMI.ui",self)    
        
class Main_frame(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main_frame, self).__init__()
        uic.loadUi("home.ui", self)
        self.button = self.findChild(QtWidgets.QPushButton, 'BMI_bt') # Find the button
        self.button.clicked.connect(self.gotoScreen2) # Remember to pass the definition/method, not the return value!
    def gotoScreen2(self):
        screen2 =Screen2()
        Widget.addWidget(screen2)
        Widget.show()
   
    

app = QApplication(sys.argv)
Uic = Main_frame()

Widget = QtWidgets.QStackedWidget()

Widget.addWidget(Uic)

Widget.show()

try:
  sys.exit(app.exec_())
except:
     print('Exiting')
     
# if __name__ == "__main__":
#     import sys
#     myApp = QtWidgets.QApplication(sys.argv)
#     # window = Main_frame()
#     sys.exit(app.exec_())





# class Main_frame(QDialog):
#     def __init__(self):
#         super(Main_frame, self).__init__()
#         uic.loadUi("home.ui", self)
#         self.show()


        
# class Screen2(QDialog):
#     def __init__(self):
#         super(Screen2,self).__init__()
#         loadUi("BMI.ui",self)

# app = QApplication(sys.argv)
# Uic = Main_frame()
# Widget = QtWidgets.QStackedWidget()
# screen2 =Screen2()
# Widget.addWidget(Uic)
# Widget.add(screen2)
# Widget.setFixedHeight(300)
# Widget.setFixedWidth(400)
# Widget.show()
# sys.exit(app.exec_())
# # try:
 
# # except:
# #     print('Exiting')
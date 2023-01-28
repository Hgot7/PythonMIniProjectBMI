from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import os
import pymysql
con = pymysql.connect(host="localhost", database="project", user="root", password="Mysql_1234")


bmi_ui, _ = loadUiType(os.path.join('Got/BMI.ui'))
home_ui, _ = loadUiType(os.path.join('Got/home.ui'))
success_ui, _ = loadUiType(os.path.join('Got/success.ui'))
Advice_ui, _ = loadUiType(os.path.join('Nut/Advice.ui'))
Developer_ui, _ = loadUiType(os.path.join('None/developer.ui'))
Obese_ui, _ = loadUiType(os.path.join('Nut/Obese.ui'))
Overweight_ui, _ = loadUiType(os.path.join('Nut/Overweight.ui'))
Normal_ui, _ = loadUiType(os.path.join('Nut/Normal.ui'))
Underweight_ui, _ = loadUiType(os.path.join('Nut/Underweight.ui'))


class Home_In(QMainWindow, home_ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button = self.findChild(QPushButton, 'BMI_bt') # Find the button
        self.button.clicked.connect(self.to_bmi) # Remember to pass the definition/method, not the return value!
        
        self.button = self.findChild(QPushButton, 'healtcare_bt') # Find the button
        self.button.clicked.connect(self.to_HealthCareGuide_click) # Remember to pass the definition/method, not the return value! 
        
        self.button = self.findChild(QPushButton, 'About_bt') # Find the button
        self.button.clicked.connect(self.to_Developer) # Remember to pass the definition/method, not the return value! 
        
        self.button = self.findChild(QPushButton, 'Search_bt') # Find the button
        self.button.clicked.connect(self.to_search) # Remember to pass the definition/method, not the return value! 
    
    def to_Developer(self):
        self.to_developer = Developer_In()
        self.to_developer.show()
        self.close()
    
    
        
    def to_HealthCareGuide_click(self):
        self.health = Advice_In()
        self.health.show()
        self.close()

    def to_bmi(self):
        self.to_bmi = BMI_In()
        self.to_bmi.show()
        self.close()
    
    def to_search(self):
        self.to_search = Search_ui()
        self.to_search.show()
        self.close()
  

class BMI_In(QMainWindow, bmi_ui):
    
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button = self.findChild(QPushButton, 'Home_bt') # Find the button
        self.button.clicked.connect(self.home_click) # Remember to pass the definition/method, not the return value!
        self.button = self.findChild(QPushButton, 'Submit_ok') # Find the button
        self.button.clicked.connect(self.ok_click) # Remember to pass the definition/method, not the return value!
        
        self.inputWeight = self.findChild(QLineEdit, 'Weight_input')
        self.inputHeight = self.findChild(QLineEdit, 'Height_input')
        self.inputAge = self.findChild(QLineEdit, 'Age_input')
        
    def home_click(self):
        self.home = Home_In()
        self.home.show()
      
        self.close()
 
          
    def ok_click(self):        #check subsit inofonmation weight and height   
      try:
        global Your_BMI 
        global Your_Age
        global avg12,avg20,avg60,avg60up
        
    
        Your_Age = int(self.inputAge.text())
        Height = (int(self.inputHeight.text())/100)*(int(self.inputHeight.text())/100)
        Weight = int(self.inputWeight.text())

        buffer = float(Weight/Height)                        
        Bmi_butter = round(buffer,2)           #แปลงตำแหน่ง
        Your_BMI = str(Bmi_butter)
        try :        
          cur = con.cursor()
         # cur.execute("INSERT INTO bmi (Age,Bmi) VALUES (2,3)")
          sql = "INSERT INTO bmi (Age,Bmi) VALUES (%s, %s)"
          val = (Your_Age,Bmi_butter)
          cur.execute(sql, val)
          cur.execute('SELECT avg(Bmi) FROM project.bmi WHERE (Age>=0) and (Age<12);')
          avg12  = cur.fetchall()
          cur.execute('SELECT avg(Bmi) FROM project.bmi WHERE (Age>=12) and (Age<20);')
          avg20 = cur.fetchall()
          cur.execute('SELECT avg(Bmi) FROM project.bmi WHERE (Age>=20) and (Age<=60);')
          avg60 = cur.fetchall()
          cur.execute('SELECT avg(Bmi) FROM project.bmi WHERE (Age>60);')
          avg60up = cur.fetchall()
          con.commit()
          cur.close()
        except :
          con.rollback() # ยกเลิกการทำคำสั่ง sql และดึงข้อมูลเดิมกลับมา
          print("ไม่สามารถเรียกดึงข้อมูลจากฐานข้อมูลได้")
        

                
            
        self.ok = Success_In()
        self.ok.show()
        self.close()
      except:
          print('You must input Weight and Height and Age is Number')
       
class Success_In(QMainWindow, success_ui):   
   
    def __init__(self):
       
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button = self.findChild(QPushButton, 'Home_bt') # Find the button
        self.button.clicked.connect(self.home_click) # Remember to pass the definition/method, not the return value!   
        self.button = self.findChild(QPushButton, 'Healthcare_bt') # Find the button
        self.button.clicked.connect(self.HealthCareGuide_click) # Remember to pass the definition/method, not the return value!  
        
        
        self.labelAge12 = self.findChild(QLabel, 'label_age12')
        self.labelAge12.setText(str(round(avg12[0][0],2)))
        
        self.labelAge20 = self.findChild(QLabel, 'label_age20')
        self.labelAge20.setText(str(round(avg20[0][0],2)))
        
        self.labelAge60 = self.findChild(QLabel, 'label_age60')
        self.labelAge60.setText(str(round(avg60[0][0],2)))
        
        self.labelAgemore = self.findChild(QLabel, 'label_agemore')
        self.labelAgemore.setText(str(str(round(avg60up[0][0],2))))
        
        self.labelResult = self.findChild(QLabel, 'label_number')
        self.labelResult.setText(Your_BMI) 
       
        
           
    def HealthCareGuide_click(self):
        self.health = Advice_In()
        self.health.show()
        self.close()

    def home_click(self):
        self.home = Home_In()
        self.home.show()
        self.close()
    
        
 
class Advice_In(QMainWindow, Advice_ui):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button = self.findChild(QPushButton, 'HomeButton') # Find the button
        self.button.clicked.connect(self.home_click) # Remember to pass the definition/method, not the return value!
        
        try:   
          self.labelResult = self.findChild(QLabel, 'label_ShowBMI')
          self.labelResult.setText(Your_BMI) 
        except:
         self.labelResult = self.findChild(QLabel, 'label_ShowBMI')
         self.labelResult.setText('0') 
         
       
        self.button = self.findChild(QPushButton, 'Bt_Obese') # Find the button
        self.button.clicked.connect(self.Obese_click) # Remember to pass the definition/method, not the return value!
        
        self.button = self.findChild(QPushButton, 'Bt_Overweight') # Find the button
        self.button.clicked.connect(self.Overweight_click) # Remember to pass the definition/method, not the return value!
        
        self.button = self.findChild(QPushButton, 'Bt_Normal') # Find the button
        self.button.clicked.connect(self.Normal_click) # Remember to pass the definition/method, not the return value!
        
        self.button = self.findChild(QPushButton, 'Bt_Underweight') # Find the button
        self.button.clicked.connect(self.Underweight_click) # Remember to pass the definition/method, not the return value!
                
   
    def home_click(self):
        self.home = Home_In()
        self.home.show()
        self.close()
    def Obese_click(self):
        self.obese = Obese_In()
        self.obese.show()
        self.close()
    def Overweight_click(self):
        self.Overweight = Overweight_In()
        self.Overweight.show()
        self.close()
    def Normal_click(self):
        self.normal = Normal_In()
        self.normal.show()
        self.close()
    def Underweight_click(self):
        self.underweight = Underweight_In()
        self.underweight.show()
        self.close()
    

class Developer_In(QMainWindow, Developer_ui):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button = self.findChild(QPushButton, 'Home') # Find the button
        self.button.clicked.connect(self.home_click) # Remember to pass the definition/method, not the return value!     
   
    def home_click(self):
        self.home = Home_In()
        self.home.show()
        self.close()
        
        
        
class Obese_In(QMainWindow, Obese_ui):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button = self.findChild(QPushButton, 'HomeButton') # Find the button
        self.button.clicked.connect(self.home_click) # Remember to pass the definition/method, not the return value!
        
        self.button = self.findChild(QPushButton, 'BackButton') # Find the button
        self.button.clicked.connect(self.back_click) # Remember to pass the definition/method, not the return value!     
   
    def home_click(self):
        self.home = Home_In()
        self.home.show()
        self.close()
    def back_click(self):
        self.back = Advice_In()
        self.back.show()
        self.close()
                
class Overweight_In(QMainWindow, Overweight_ui):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button = self.findChild(QPushButton, 'HomeButton') # Find the button
        self.button.clicked.connect(self.home_click) # Remember to pass the definition/method, not the return value!
        
        self.button = self.findChild(QPushButton, 'BackButton') # Find the button
        self.button.clicked.connect(self.back_click) # Remember to pass the definition/method, not the return value!     
   
    def home_click(self):
        self.home = Home_In()
        self.home.show()
        self.close()
    def back_click(self):
        self.back = Advice_In()
        self.back.show()
        self.close()
        
class Normal_In(QMainWindow, Normal_ui):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button = self.findChild(QPushButton, 'HomeButton') # Find the button
        self.button.clicked.connect(self.home_click) # Remember to pass the definition/method, not the return value!
        
        self.button = self.findChild(QPushButton, 'BackButton') # Find the button
        self.button.clicked.connect(self.back_click) # Remember to pass the definition/method, not the return value!     
   
    def home_click(self):
        self.home = Home_In()
        self.home.show()
        self.close()
    def back_click(self):
        self.back = Advice_In()
        self.back.show()
        self.close()
        
class Underweight_In(QMainWindow, Underweight_ui):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button = self.findChild(QPushButton, 'HomeButton') # Find the button
        self.button.clicked.connect(self.home_click) # Remember to pass the definition/method, not the return value!
        
        self.button = self.findChild(QPushButton, 'BackButton') # Find the button
        self.button.clicked.connect(self.back_click) # Remember to pass the definition/method, not the return value!     
   
    def home_click(self):
        self.home = Home_In()
        self.home.show()
        self.close()
    def back_click(self):
        self.back = Advice_In()
        self.back.show()
        self.close()    
        
        
    
class Search_ui(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        title = "Search healthy food"
        self.setWindowTitle(title)
    
        mainLayout = QVBoxLayout()
      
       
        companies = ('น้ำพริกหนุ่ม ผักต้ม และไข่ต้มยางมะตูม', 'สุกี้แห้งทะเล', 'ผัดผักรวมมิตรกุ้ง', 'ข้าวผัดไข่ ซาบะย่าง และผักสลัด', 'ผัดถั่วงอกใส่เต้าหู้', 'เมี่ยงปลาดอลลี่ + น้ำจิ้มซีฟู้ด'
                     , 'สลัดอกไก่โรยงา กินคู่กับน้ำสลัดญี่ปุ่น', 'เพนเน่ซุปไก่คลีนๆ', 'อกไก่ลวกกับผักต่างๆ กินคู่กับน้ำจิ้มสุกี้'
                     , 'เมี่ยงปลาเผา', 'แกงจืดไก่ก้อนเต้าหู้ไข่', 'กรีกโยเกิร์ตแช่เย็น กินคู่กับผลไม้หลากชนิด', 'ขนมปังโฮลวีตโปะอะโวคาโดและไข่กวน', 'แกงเลียงกุ้งสด', 'ข้าว (ไม่) มันไก่นึ่งสมุนไพร'
                     , 'ไข่คน ขนมปังโฮลวีตปิ้ง และสลัด', 'สลัดผักปลาย่าง', 'ต้มจืดฟักหมูสับเห็ดหอม', 'ไข่กวนฟอง ขนมปังปิ้ง อะโวคาโด้ราดน้ำผึ้ง', 'รวมมิตรผักลวก สันในไก่ต้ม เสิร์ฟพร้อมน้ำจิ้มสุกี้'
                     , 'ข้าวกล้อง อกไก่ย่าง และไข่ต้ม น้ำจิ้มแจ่ว', 'น้ำพริกกุ้งสด + ผักกูดและไข่ต้ม', 'ลาบอกไก่', 'ไแซนด์วิชอกไก่ไข่ดาว', 'ต้มยำกุ้งและเห็ดน้ำใส'
                     , 'ส้มตำผลไม้กุ้งสุก', 'ซาชิมิแซลมอน', 'ปลาซาบะย่างเกลือ', 'สาหร่ายพวงองุ่น แซลมอน น้ำจิ้มซีฟู้ดใส่อัลมอนด์', 'แตงกวาผัดไข่และกุ้ง')
        model = QStandardItemModel(len(companies), 1)
        model.setHorizontalHeaderLabels(['เมนูอาหารเพื่อสุขภาพ'])

        for row, company in enumerate(companies):
            item = QStandardItem(company)
            model.setItem(row, 0, item)

        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filter_proxy_model.setFilterKeyColumn(0)

        search_field = QLineEdit()         
        search_field.setStyleSheet('font-size: 35px; height: 60px;')
        search_field.textChanged.connect(filter_proxy_model.setFilterRegExp)
        mainLayout.addWidget(search_field)

        table = QTableView()
        table.setStyleSheet('font-size: 35px;')
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setModel(filter_proxy_model)
        mainLayout.addWidget(table)

        home = QPushButton()
        home.setText('Home')
        home.setStyleSheet('font-size: 35px; height: 60px;') 
        home.clicked.connect(self.home_click)   
         
        mainLayout.addWidget(home) 


        self.setLayout(mainLayout)
    def home_click(self):
        self.home = Home_In()
        self.home.show()
        self.close()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Home_In()
    window.show()
    app.exec_()
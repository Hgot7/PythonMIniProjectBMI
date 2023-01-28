import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout,QMainWindow,QPushButton
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
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
        search_field.setFixedWidth(600)          
        search_field.setStyleSheet('font-size: 35px; height: 60px;')
        search_field.textChanged.connect(filter_proxy_model.setFilterRegExp)
        mainLayout.addWidget(search_field)

        table = QTableView()
        table.setStyleSheet('font-size: 35px;')
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setModel(filter_proxy_model)
        mainLayout.addWidget(table)

        self.setLayout(mainLayout)

app = QApplication(sys.argv)
demo = AppDemo()
btn1 = QPushButton(demo)
btn1.setText('Home')
btn1.move(650, 30)
demo.show()

sys.exit(app.exec_())       
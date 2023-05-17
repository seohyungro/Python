from PyQt5.QtWidgets import * 
import sys , pickle

from PyQt5 import uic, QtWidgets , QtCore, QtGui
import data_visualize

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("./mainwindow.ui", self)
        
        global data
        data  = data_visualize.data_()
        self.show()
        
        self.Browse = self.findChild( QPushButton, "Browse" )
        self.column_list = self.findChild( QListWidget, "column_list" )
        self.Submit_btn = self.findChild( QPushButton, "Submit" )
        self.target_col = self.findChild( QLabel, "target_col" )
        self.table = self.findChild( QTableView, "tableView" )
        

        self.scaler = self.findChild( QComboBox, "scaler" )
        self.scale_btn = self.findChild( QPushButton, "scale_btn" )
        
        self.cat_column = self.findChild( QComboBox, "cat_column" )
        self.convert_btn = self.findChild( QPushButton, "convert_btn" )
        
        self.drop_column = self.findChild( QComboBox, "drop_column" )
        self.drop_btn = self.findChild( QPushButton, "drop_btn" )
        
        self.empty_column = self.findChild( QComboBox, "empty_column" )
        self.fillmean_btn = self.findChild( QPushButton, "fillmean_btn" )
        self.fillna_btn = self.findChild( QPushButton, "fillna_btn" )


        self.Browse.clicked.connect(self.getCSV)
        self.Submit_btn.clicked.connect(self.set_target)
        self.column_list.clicked.connect(self.target)
    
    def set_target(self):
        self.target_value = str(self.item).split()[0]
        print(self.target_value)
        self.target_col.setText(self.target_value)
        
        
        
        
    def target(self):
        self.item = self.column_list.currentItem().text()
        print(self.item)
        
    def getCSV(self):
        self.filepath , _ = QFileDialog.getOpenFileName(self,"Open File", "C:/apps/ml_7/datasets","csv(*.csv)" )
        # print(self.filepath)
        # self.column_list.addItems(["브라우져", '브라우승', "브라질"])
        self.filldetails(0)
    
    
    def fill_combo_box(self):
        x = table_display.DataFrameModel(self.df)
        self.table.setModel(x)

    def filldetails(self , flag=1):
        if (flag==0):
            self.df = data.read_file(self.filepath)
            print(self.df)
        self.column_list.clear()
        
        if len(self.df)==0:
            pass
            
        else:
            
            self.column_arr = data.get_column_list(self.df)
            # print(self.column_arr)
            for i , j in enumerate(self.column_arr):
                stri = f'{j} ------- {str(self.df[j].dtype)}'
                self.column_list.insertItem(i, stri)
        
        self.fill_combo_box
        
        

if __name__ == '__main__':       
    app = QApplication(sys.argv)
    window = UI()
    app.exec_()
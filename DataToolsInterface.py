from os import name
from threading import local
from Datasplict import *
from checkcls import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import Interface_ui as ui
from selectpath import *
from Rename import *
import time
from ToTxtList import *



class Main(QMainWindow, ui.Ui_Dialog):
    def __init__(self):
         super().__init__()
         self.setupUi(self)
         self.Ds_pushButton.clicked.connect(self.ImagePath)
         self.Ds_pushButton_2.clicked.connect(self.SavePath)
         self.Ds_pushButton_3.clicked.connect(self.StartDatasplict)
         self.Ds_pushButton_4.clicked.connect(self.LabelsPath)
         self.Re_pushButton.clicked.connect(self.Rename_Path)
         self.Re_pushButton2.clicked.connect(self.StartRename)
         self.RC_pushButton.clicked.connect(self.RC_path)
         self.RC_pushButton2.clicked.connect(self.StartReplace)
         self.FT_pushButton_1.clicked.connect(self.FT_selectpath)
         self.FT_pushButton_2.clicked.connect(self.FT_savepath)
         self.FT_pushButton_3.clicked.connect(self.FT_start)
         self.listWidget.itemSelectionChanged.connect(self.itemActivated_event)
         self.Folderpath = None
         self.Imagepath = None
         self.savefolderpath = None
         self.Selectitem = None
         self.Rename_ =None
         self.Labelspath = None
    def ImagePath(self):
        self.Imagepath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        print(self.Imagepath)
        self.textEdit.setPlainText(self.Imagepath)
    
    def LabelsPath(self):
        self.Labelspath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.textEdit_4.setPlainText(self.Labelspath)
    def SavePath(self):
        self.savefolderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        print(self.savefolderpath)
        self.textEdit_2.setPlainText(self.savefolderpath)

    def StartDatasplict(self):
        try:
            value1 = self.spinBox.value()
            value2 = self.spinBox_2.value()
            value3 = self.spinBox_3.value()
            Total_cls_numbs = self.spinBox_6.value()
            if  not self.Imagepath or not self.Imagepath :
                self.local__time()
                self.textEdit_6.append("error check Root path or Save path")
            elif value1 == 0 or value2 == 0 or value3 == 0 :
                self.local__time()
                self.textEdit_6.append("error check Start End Iteration")
            else:
                
                for _ in range(value1,value2+1,value3):
                    cls0 ,cls1,cls2= 0,0,0
                    Create_savefolderpath = self.savefolderpath+ str(_)
                    if not os.path.isdir(Create_savefolderpath):
                        os.mkdir(Create_savefolderpath)
                        Create_images_path = Create_savefolderpath+'/images'
                        Create_labels_path = Create_savefolderpath+'/labels'
                        if not os.path.isdir(Create_images_path):
                            os.mkdir(Create_images_path)
                        if not os.path.isdir(Create_labels_path):
                            os.mkdir(Create_labels_path)
                        cls0 ,cls1 ,cls2 = cpfile(_,cls0,cls1,cls2,Create_labels_path,self.Labelspath,Total_cls_numbs)
                        checkcontent(Create_labels_path)
                        cpimages(self.Imagepath,Create_images_path,Create_labels_path)
                    self.local__time()
                    self.textEdit_6.append(f'log : class 0  {cls0}.  class 1  {cls1}.  class 2  {cls2}. ')
        except Exception as e: 
            print(e)
            self.textEdit_6.append(f'Error {e}.')

    
    def Rename_Path(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.textEdit_3.setPlainText(self.folderpath)
    def StartRename(self):
        try:
            if  not self.folderpath :self.textEdit_6.append("error check Path and Newname and Filetype")
            self.rename_ = self.lineEdit.text()
            NewNameList = Rename().renameImage(self.folderpath,self.rename_,self.selectitem)
            for _ in NewNameList:
                self.textBrowser.append(f'New file name {_}')
        except Exception as e: 
            self.textBrowser.append(f'Error {e}')
            print(e)
    def itemActivated_event(self):
        try:
            for item in self.listWidget.selectedItems():
                self.selectitem = item.text()
        except Exception as e:
            self.textBrowser_3.append(e)
    def RC_path(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')       
        self.textEdit_5.setPlainText(self.folderpath)
        

    def StartReplace(self):
        try:
            Orinignalvalue0 = self.spinBox_4.value()
            Replacevalue1 = self.spinBox_5.value()
            print(Orinignalvalue0,Replacevalue1)
            if Orinignalvalue0 == 0 or Replacevalue1 == 0 : self.textBrowser_3.append("error check Orinignal class number and Replace class")
            else:
                check().checkcls(self.folderpath,str(Orinignalvalue0),str(Replacevalue1))
                showtime= self.local__time()
                self.textBrowser_3.append(showtime)
                self.textBrowser_3.append("Compelete !")
        except Exception as e :
            print(e)
            self.textBrowser_3.append(showtime)
            self.textBrowser_3.append(e)        

    def local__time(self):
        localtime = time.localtime()
        result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
        return result
    
    def FT_selectpath(self):
        try:
            showtime= self.local__time()
            selectpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
            self.FT_textEdit_1.setPlainText(f'{selectpath}')
            path_filelist = os.listdir(selectpath)
            count = 0
            for _ in path_filelist:
                count+=1
                self.textBrowser_5.append(f'{count}.{_}')
            self.textBrowser_5.append(f'{showtime}       Total number is {count} ......')
        except Exception as e :
            print(e)
            self.textBrowser_5.append(self.local__time())
            self.textBrowser_5.append(f'Error {e}.')  

    def FT_savepath(self):
        showtime= self.local__time()
        try:
            savepath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
            self.FT_textEdit_2.setPlainText(f'{savepath}/Train.txt') 
        except Exception as e :
            print(e)
            self.textBrowser_5.append(f'{showtime}     Error     {e}.')  

    def FT_start(self):
        showtime= self.local__time()
        try:
            Conversion_Txt(self.FT_textEdit_1.toPlainText(),self.FT_textEdit_2.toPlainText())
            self.textBrowser_5.append(f'Complete ! ..check {self.FT_textEdit_2.toPlainText()}') 
        except Exception as e :
            print(e)
            self.textBrowser_5.append(f'{showtime}     Error     {e}.')  

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


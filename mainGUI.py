import sys
import os
from subprocess import *

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QDialog, QFileDialog, QTabWidget
from PySide6.QtCore import QFile, QTimer, QDate, Qt
from PySide6.QtGui import QPixmap
from datetime import date, datetime
import sys
import torch
from main_ui import Ui_MainWindow
from pathlib import *
import shutil
import keyboard
import cv2
import pydicom as dicom
from pydicom.encoders import *
import seaborn as sns


class MainWindow(QMainWindow):
    #setup gui
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.browseButton.clicked.connect(self.browseImage) #browse image from folder
        self.ui.DiagnoseButton.clicked.connect(self.run) #to detect pneumonia

        #get current directory of the .py file
        self.p = os.getcwd()
        print("Path= ",self.p)

    def browseImage(self):
        #open file explorer
        self.img = QFileDialog.getOpenFileName(self, "Open File", "..\\", "Image files (*.jpg *.jpeg *.dcm *.svg)")
        self.test_src_path = self.img[0] #get the directory name from selected file

        print(self.test_src_path)

        #get file extension
        file_name, file_extension = os.path.splitext(self.test_src_path)
        print(file_extension)

        #if image is DCM format, convert into jpg format
        if(file_extension == '.dcm'):
            ds = dicom.dcmread(self.test_src_path)
            pixel_array_numpy = ds.pixel_array
            image = self.test_src_path.replace('.dcm', '.jpg')
            print("Current Image Name ",image)

            cv2.imwrite(os.path.join(self.p, image), pixel_array_numpy)
            print("Image Format Converted")
            self.test_src_path = image

        #display image selected
        self.ui.picLabel.setScaledContents(True) #fix pic size to frame size
        self.pixmap = QPixmap(self.test_src_path)
        self.pixmap = self.pixmap.scaled(1000,600)
        self.ui.picLabel.setPixmap(QPixmap(self.pixmap))
        self.ui.picLabel.resize(1000,600)
        self.ui.picLabel.repaint()




    def run(self):

        #YoloV5 custom trained model
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='{}'.format(self.p+'/best.pt'), _verbose=True)
        
        #Declare output name with current date&time
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d%m%Y%H%M%S")
        self.output_name = self.dt_string
        print(self.output_name)

        img = self.test_src_path

        results = model(img)
        results.print()

        #obtain classified class
        df = results.pandas().xyxy[0].value_counts('name')

        diagnosis = ""

        for i in df.index:
            diagnosis = i

        if diagnosis == "":
            self.msgBox.setText("Please select valid Chest X-ray image")
            self.msgBox.exec()

        else:
            results.save(save_dir = 'output/'+self.output_name) #save output imge to desired directory as desired folder name


            self.img_name = os.path.basename(self.test_src_path) 

            filename, file_ext = os.path.splitext(self.img_name)

            print('filename: ',filename)


            self.detected_img = "{}/output/{}/{}.jpg".format(self.p, self.output_name, filename)

            print("display output image path")
            print(self.detected_img)
            
            #output image
            self.ui.picLabel.setScaledContents(True)
            self.pixmap2 = QPixmap(self.detected_img)
            self.pixmap2 = self.pixmap2.scaled(1000,600)
            self.ui.picLabel.setPixmap(QPixmap(self.pixmap2))
            self.ui.picLabel.resize(1000,600)
            self.ui.picLabel.repaint()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)  

    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
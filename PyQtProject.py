# -*- coding: utf-8 -*-
"""
@file PyQtProject.py
@brief Uses GUI to prompt user input to create montages
@author: Olivia Leu

This file contains classes that create a GUI which connects user input to functions
that create montages.
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QInputDialog, QVBoxLayout, QFileDialog, QDialog
from PyQt4.QtGui import QFont
import sys
import os
from montage_manager import Montages
  
## @class Error
#  @brief Prints error window
#
#  This class prints error window asking for valid directories.
class Error(QDialog):
    def __init__(self, parent = None):
        super(Error,self).__init__(parent)
        self.message = QLabel("Please input valid directories.")
        self.btn = QPushButton("OK")
        QPushButtonStyleStr = 'QPushButton{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eafaf1, stop: 1 #d5f5e3); } \
            QPushButton:hover{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #a6e3ec); } \
            QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #60c1dc);}'
        self.btn.setStyleSheet(QPushButtonStyleStr)
        self.btn.clicked.connect(self.close)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.btn)
        self.setWindowTitle("Error")
  
## @class MontageDir
#  @brief Creates new window for creating montages from directory
#
#  This class implements the functions neeeded to create montages from directory
#  provided by the user.
class MontageDir(QDialog):
    def __init__(self, parent = None): #Constructor
        super(MontageDir,self).__init__(parent)
        self.montage = Montages()
        self.error = Error(self)
        self.createLabel = QPushButton('Provide full path to directory to create montages', self)
        QPushButtonStyleStr = 'QPushButton{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eafaf1, stop: 1 #d5f5e3); } \
            QPushButton:hover{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #a6e3ec); } \
            QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #60c1dc);}'
        self.createLabel.setStyleSheet(QPushButtonStyleStr)
        self.createLabel.setFixedWidth(310)
        self.createLabel.clicked.connect(self.showPathToCreate)
        self.orLabel1 = QLabel("or",self)
        self.orLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.browse1 = QPushButton("Browse",self)
        self.browse1.setStyleSheet(QPushButtonStyleStr)
        self.browse1.clicked.connect(self.getInputPath)
        self.createPath = QLabel("Path: ",self)      
        self.saveLabel = QPushButton('Provide full path to valid directory to save montages', self)
        self.saveLabel.setStyleSheet(QPushButtonStyleStr)
        self.saveLabel.setFixedWidth(310)
        self.saveLabel.clicked.connect(self.showPathToSave)
        self.orLabel2 = QLabel("or",self)
        self.orLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.browse2 = QPushButton("Browse",self)
        self.browse2.setStyleSheet(QPushButtonStyleStr)
        self.browse2.clicked.connect(self.getOutputPath)

        self.savePath = QLabel("Path: ",self)
        self.spacer = QLabel("",self)
        self.apply = QPushButton("Apply",self)
        self.apply.setStyleSheet(QPushButtonStyleStr)
        self.apply.setFixedWidth(200)
        self.apply.clicked.connect(self.createMontage)
        self.backToMenu = QPushButton("Back To Menu",self)
        self.backToMenu.setStyleSheet(QPushButtonStyleStr)
        self.backToMenu.setFixedWidth(200)
        self.backToMenu.clicked.connect(self.close)

        self.message = QLabel(self)
        self.layout1 = QVBoxLayout(self)
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        

        layout2.addWidget(self.createLabel)
        layout2.addWidget(self.orLabel1)
        layout2.addWidget(self.browse1)
        self.layout1.addLayout(layout2)
        self.layout1.addWidget(self.createPath)
        layout3.addWidget(self.saveLabel)
        layout3.addWidget(self.orLabel2)
        layout3.addWidget(self.browse2)
        self.layout1.addLayout(layout3)
        self.layout1.addWidget(self.savePath)
        self.layout1.addWidget(self.spacer)
        layout4.addWidget(self.apply)
        layout4.addWidget(self.backToMenu)
        self.layout1.addLayout(layout4)
        self.layout1.addWidget(self.message)
        
        self.setGeometry(600, 500, 350, 150)
        self.setWindowTitle('Option 1')
        
        self.inputPath = ""
        self.outputPath = ""        
    
    ## @function showPathToCreate 
    #  @brief Member function that gets input path to create montage from user-written path 
    def showPathToCreate(self):
        text, ok = QInputDialog.getText(self, 'Input Path to Create Montage', 
            'Enter path to directory:')
        QPushButtonStyleStr = 'QPushButton{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eafaf1, stop: 1 #d5f5e3); } \
            QPushButton:hover{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #a6e3ec); } \
            QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #60c1dc);}'
        ok.setStyleSheet(QPushButtonStyleStr)
        if ok:
            if os.path.isdir(str(text)):  
                self.createPath.clear
                self.createPath.setText("Path: " + str(text))
                self.inputPath = str(text)
            else:
                self.createPath.clear
                self.createPath.setText("Given directory is not valid: " + str(text))

    ## @function showPathToSave
    #  @brief Member function that gets path to save montage from user-written path
    def showPathToSave(self):
        text, ok = QInputDialog.getText(self, 'Input Path to Save Montage', 
            'Enter path to directory:')
        if ok:
            if os.path.isdir(str(text)):
                self.savePath.clear
                self.savePath.setText("Path: " + str(text)) 
                self.outputPath = str(text)
            else:
                self.savePath.clear
                self.savePath.setText("Given directory is not valid: " + str(text))

    ## @function getInputPath
    #  @brief Member function that gets input path to create montage from user-chosen folder 
    #  using browse
    def getInputPath(self):
        text = QFileDialog.getExistingDirectory(self, 'Select Folder', 'C:\\', QFileDialog.ShowDirsOnly)        
        self.createPath.clear
        self.createPath.setText("Path: " + str(text))        
        self.inputPath = str(text)
    
    ## @function getOutputPath
    #  @brief Member function that gets path to save montage from user-chosen folder using browse
    def getOutputPath(self):
        text = QFileDialog.getExistingDirectory(self, 'Select Folder', 'C:\\', QFileDialog.ShowDirsOnly)
        self.savePath.clear
        self.savePath.setText("Path: " + str(text))        
        self.outputPath = str(text)
      
    ## @function createMontage
    #  @brief Member function that given valid path directories creates the montage
    def createMontage(self):
        if self.inputPath == "" or self.outputPath == "":
            self.error.exec_()
        else:
            self.montage.input_data(src_path = self.inputPath, dest_path = self.outputPath)
            self.montage.montages_from_directory()
            self.message.setText("Montages created and saved.")
    
## @class MontageFromCSV
#  @brief Creates new window for creating montages from csv file      
#
#  This class implements the functions needed to create montages from CSV
#  files provided by the user.       
class MontageFromCSV(QDialog):
    def __init__(self, parent = None): #Constructor
        super(MontageFromCSV,self).__init__(parent)
        self.montage = Montages()
        self.error = Error(self)
        self.CSVLabel = QPushButton('Provide full path to csv file for creating montages', self)
        QPushButtonStyleStr = 'QPushButton{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eafaf1, stop: 1 #d5f5e3); } \
            QPushButton:hover{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #a6e3ec); } \
            QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #60c1dc);}'
        self.CSVLabel.setStyleSheet(QPushButtonStyleStr)
        self.CSVLabel.setFixedWidth(310)
        self.CSVLabel.clicked.connect(self.showPathToCSV)
        self.orLabel1 = QLabel("or",self)
        self.orLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.browse1 = QPushButton("Browse",self)
        self.browse1.setStyleSheet(QPushButtonStyleStr)
        self.browse1.clicked.connect(self.getCSVPath)
        self.CSVPathName = QLabel("Path: ",self)   
        self.imageLabel = QPushButton('Provide path to where images are located', self)
        self.imageLabel.setStyleSheet(QPushButtonStyleStr)
        self.imageLabel.setFixedWidth(310)
        self.imageLabel.clicked.connect(self.showPathToImage)
        self.orLabel2 = QLabel("or",self)
        self.orLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.browse2 = QPushButton("Browse",self)
        self.browse2.setStyleSheet(QPushButtonStyleStr)
        self.browse2.clicked.connect(self.getImagePath)
        self.imagePathName = QLabel("Path: ",self)
        self.saveLabel = QPushButton('Provide full path to valid directory to save montages', self)
        self.saveLabel.setStyleSheet(QPushButtonStyleStr)
        self.saveLabel.setFixedWidth(310)
        self.saveLabel.clicked.connect(self.showPathToSave)
        self.orLabel3 = QLabel("or",self)
        self.orLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.browse3 = QPushButton("Browse",self)
        self.browse3.setStyleSheet(QPushButtonStyleStr)
        self.browse3.clicked.connect(self.getOutputPath)
        self.savePath = QLabel("Path: ",self)
        self.spacer = QLabel("",self)
        self.apply = QPushButton("Apply",self)
        self.apply.setStyleSheet(QPushButtonStyleStr)
        self.apply.setFixedWidth(200)
        self.apply.clicked.connect(self.createMontage)
        self.backToMenu = QPushButton("Back To Menu",self)
        self.backToMenu.setStyleSheet(QPushButtonStyleStr)
        self.backToMenu.setFixedWidth(200)
        self.backToMenu.clicked.connect(self.close)
        self.message = QLabel(self)
        self.layout1 = QVBoxLayout(self)
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()
        
        layout2.addWidget(self.CSVLabel)
        layout2.addWidget(self.orLabel1)
        layout2.addWidget(self.browse1)
        self.layout1.addLayout(layout2)
        self.layout1.addWidget(self.CSVPathName)
        layout3.addWidget(self.imageLabel)
        layout3.addWidget(self.orLabel2)
        layout3.addWidget(self.browse2)
        self.layout1.addLayout(layout3)
        self.layout1.addWidget(self.imagePathName)
        layout4.addWidget(self.saveLabel)
        layout4.addWidget(self.orLabel3)
        layout4.addWidget(self.browse3)
        self.layout1.addLayout(layout4)
        self.layout1.addWidget(self.savePath)
        self.layout1.addWidget(self.spacer)
        layout5.addWidget(self.apply)
        layout5.addWidget(self.backToMenu)
        self.layout1.addLayout(layout5)
        self.layout1.addWidget(self.message)
        
        self.setGeometry(590, 475, 350, 150)
        self.setWindowTitle('Option 2')
        
        self.CSVPath = ""
        self.imagePath = ""
        self.outputPath = ""
    
    ## @function showPathToCSV
    #  @brief Member function that gets input path to CSV file from user-written path    
    def showPathToCSV(self):
        text, ok = QInputDialog.getText(self, 'Input Path to CSV File', 
            'Enter path to valid CSV File:')
        if ok:
            if os.path.isfile(str(text)):
                self.CSVPathName.clear
                self.CSVPathName.setText("Path: " + str(text))
                self.CSVPath = str(text)
            else:
                self.CSVPathName.clear
                self.CSVPathName.setText("Given file is not valid: " + str(text))
    
    ## @function showPathToImage
    #  @brief Member function that gets path to images from user-written path   
    def showPathToImage(self):
        text, ok = QInputDialog.getText(self, 'Input Path to Images', 
            'Enter path to location of images:')
        if ok:
            if os.path.isdir(str(text)):  
                self.imagePathName.clear
                self.imagePathName.setText("Path: " + str(text))
                self.imagePath = str(text)
            else:
                self.imagePathName.clear
                self.imagePathName.setText("Given directory is not valid: " + str(text))

    ## @function showPathToSave
    #  @brief Member function that gets path to save montages from user-written path
    def showPathToSave(self):
        text, ok = QInputDialog.getText(self, 'Input Path to Save Montage', 
            'Enter path to directory:')
        if ok:
            if os.path.isdir(str(text)):
                self.savePath.clear
                self.savePath.setText("Path: " + str(text)) 
                self.outputPath = str(text)
            else:
                self.savePath.clear
                self.savePath.setText("Given directory is not valid: " + str(text))
    
    ## @function getCSVPath
    #  @brief Member function that gets path to CSV files from user-chosen folder using browse            
    def getCSVPath(self):
        text = QFileDialog.getOpenFileName(self, 'Select File', 'C:\\', "CSV files (*.csv)")
        self.CSVPathName.clear
        self.CSVPathName.setText("Path: " + str(text))
        self.CSVPath = str(text)
    
    ## @function getImagePath
    #  @brief Member function that gets path to images from user-chosen folder using browse    
    def getImagePath(self):
        text = QFileDialog.getExistingDirectory(self, 'Select Folder', 'C:\\', QFileDialog.ShowDirsOnly)        
        self.imagePathName.clear
        self.imagePathName.setText("Path: " + str(text))        
        self.imagePath = str(text)
    
    ## @function getOutputPath
    #  @brief Member function that gets path to save montages from user-chosen folder using browse
    def getOutputPath(self):
        text = QFileDialog.getExistingDirectory(self, 'Select Folder', 'C:\\', QFileDialog.ShowDirsOnly)
        self.savePath.clear
        self.savePath.setText("Path: " + str(text))        
        self.outputPath = str(text)
    
    ## @function createMontage
    #  @brief Member function that given valid directories creates the montage
    def createMontage(self):
        if self.CSVPath == "" or self.imagePath == "" or self.outPath == "":
            self.error.exec_()
        else:
            self.montage.input_data(src_path = self.CSVPath, dest_path = self.outputPath, image_src_path = self.imagePath)
            self.montage.montages_from_csv_binned()
            self.message.setText("Montages created and saved.")

## @class VerticalMontageFromCSV
#  @brief Creates new window for creating vertical montages from csv files
#
#  This class implements the functions needed to create vertical montages from
#  CSV files provided by the user.            
class VerticalMontageFromCSV(QDialog):
    def __init__(self, parent = None): #Constructor
        super(VerticalMontageFromCSV,self).__init__(parent)
        self.montage = Montages()
        self.error = Error(self)
        self.CSVLabel = QPushButton('Provide full path to CSV file for creating montages', self)
        QPushButtonStyleStr = 'QPushButton{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eafaf1, stop: 1 #d5f5e3); } \
            QPushButton:hover{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #a6e3ec); } \
            QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #60c1dc);}'
        self.CSVLabel.setStyleSheet(QPushButtonStyleStr)
        self.CSVLabel.setFixedWidth(310)                                    
        self.CSVLabel.clicked.connect(self.showPathToCSV)
        self.orLabel1 = QLabel("or",self)
        self.orLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.browse1 = QPushButton("Browse",self)
        self.browse1.setStyleSheet(QPushButtonStyleStr)
        self.browse1.clicked.connect(self.getCSVPath)        
        self.CSVPathName = QLabel("Path: ",self)   
        self.imageLabel = QPushButton('Provide path to where images are located', self)
        self.imageLabel.setStyleSheet(QPushButtonStyleStr)
        self.imageLabel.setFixedWidth(310)
        self.imageLabel.clicked.connect(self.showPathToImage)
        self.orLabel2 = QLabel("or",self)
        self.orLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.browse2 = QPushButton("Browse",self)
        self.browse2.setStyleSheet(QPushButtonStyleStr)
        self.browse2.clicked.connect(self.getImagePath)
        self.imagePathName = QLabel("Path: ",self)
        self.saveLabel = QPushButton('Provide full path to valid directory to save montages', self)
        self.saveLabel.setStyleSheet(QPushButtonStyleStr)
        self.saveLabel.setFixedWidth(310)
        self.saveLabel.clicked.connect(self.showPathToSave)
        self.orLabel3 = QLabel("or",self)
        self.orLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.browse3 = QPushButton("Browse",self)
        self.browse3.setStyleSheet(QPushButtonStyleStr)
        self.browse3.clicked.connect(self.getOutputPath)
        self.savePath = QLabel("Path: ",self)
        self.spacer = QLabel("",self)
        self.apply = QPushButton("Apply",self)
        self.apply.setStyleSheet(QPushButtonStyleStr)
        self.apply.clicked.connect(self.createMontage)
        self.backToMenu = QPushButton("Back To Menu",self)
        self.backToMenu.setStyleSheet(QPushButtonStyleStr)
        self.backToMenu.clicked.connect(self.close)
        self.message = QLabel(self)
        self.layout1 = QVBoxLayout(self)
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()
        

        layout2.addWidget(self.CSVLabel)
        layout2.addWidget(self.orLabel1)
        layout2.addWidget(self.browse1)
        self.layout1.addLayout(layout2)
        self.layout1.addWidget(self.CSVPathName)
        layout3.addWidget(self.imageLabel)
        layout3.addWidget(self.orLabel2)
        layout3.addWidget(self.browse2)
        self.layout1.addLayout(layout3)
        self.layout1.addWidget(self.imagePathName)
        layout4.addWidget(self.saveLabel)
        layout4.addWidget(self.orLabel3)
        layout4.addWidget(self.browse3)
        self.layout1.addLayout(layout4)
        self.layout1.addWidget(self.savePath)
        self.layout1.addWidget(self.spacer)
        layout5.addWidget(self.apply)
        layout5.addWidget(self.backToMenu)
        self.layout1.addLayout(layout5)
        self.layout1.addWidget(self.message)
        
        self.setGeometry(590, 475, 350, 150)
        self.setWindowTitle('Option 3')
        
        self.CSVPath = ""
        self.imagePath = ""
        self.outputPath = ""
    
    ## @function showPathToCSV
    #  @brief Member function that gets path to CSV files from user-written path
    def showPathToCSV(self):
        text, ok = QInputDialog.getText(self, 'Input Path to CSV File', 
            'Enter path to valid CSV File:')
        if ok:
            if os.path.isfile(str(text)):
                self.CSVPathName.clear
                self.CSVPathName.setText("Path: " + str(text))
                self.CSVPath = str(text)
            else:
                self.CSVPathName.clear
                self.CSVPathName.setText("Given file is not valid: " + str(text))

    ## @function showPathToImage
    #  @brief Member function that gets path to images from user-written path        
    def showPathToImage(self):
        text, ok = QInputDialog.getText(self, 'Input Path to Images', 
            'Enter path to location of images:')
        if ok:
            if os.path.isdir(str(text)):  
                self.imagePathName.clear
                self.imagePathName.setText("Path: " + str(text))
                self.imagePath = str(text)
            else:
                self.imagePathName.clear
                self.imagePathName.setText("Given directory is not valid: " + str(text))

    ## @function showPathToSave
    #  @brief Member function that gets path to save montages from user-written path
    def showPathToSave(self):
        text, ok = QInputDialog.getText(self, 'Input Path to Save Montage', 
            'Enter path to directory:')
        if ok:
            if os.path.isdir(str(text)):
                self.savePath.clear
                self.savePath.setText("Path: " + str(text)) 
                self.outputPath = str(text)
            else:
                self.savePath.clear
                self.savePath.setText("Given directory is not valid: " + str(text))

    ## @function getCSVPath
    #  @brief Member function that gets path to CSV files from user-chosen folder using browse                 
    def getCSVPath(self):
        text = QFileDialog.getOpenFileName(self, 'Select File', 'C:\\', "CSV files (*.csv)")
        self.CSVPathName.clear
        self.CSVPathName.setText("Path: " + str(text))
        self.CSVPath = str(text)

    
    ## @function getImagePath
    #  @brief Member function that gets path to images from user-chosen folder using browse            
    def getImagePath(self):
        text = QFileDialog.getExistingDirectory(self, 'Select Folder', 'C:\\', QFileDialog.ShowDirsOnly)        
        self.imagePathName.clear
        self.imagePathName.setText("Path: " + str(text))        
        self.imagePath = str(text)
    
    ## @function getOutputPath
    #  @brief Member function that gets path to save montages from user-chosen folder using browse
    def getOutputPath(self):
        text = QFileDialog.getExistingDirectory(self, 'Select Folder', 'C:\\', QFileDialog.ShowDirsOnly)
        self.savePath.clear
        self.savePath.setText("Path: " + str(text))        
        self.outputPath = str(text)
 
    ## @function createMontage
    #  @brief Member function that given valid directories creates the montage         
    def createMontage(self):
        if self.CSVPath == "" or self.imagePath == "" or self.outputPath == "":
            self.error.exec_()
        else:
            self.montage.input_data(src_path = self.CSVPath, dest_path = self.outputPath, image_src_path = self.imagePath)
            self.montage.montages_from_csv_binned(ncols = 0, nrows = 1)
            self.message.setText("Montages created and saved.")

## @class ImageHistFromCSV
#  @brief Creates new window for creating image histogram from CSV files   
#
#  This class implements the functions needed to create image histograms from
#  CSV files provided by the user.         
class ImageHistFromCSV(QDialog):
    def __init__(self, parent = None): #Constructor
        super(ImageHistFromCSV,self).__init__(parent)
        self.montage = Montages()
        self.error = Error(self)
        self.createLabel = QPushButton('Provide full path to csv file for creating image histogram', self)
        QPushButtonStyleStr = 'QPushButton{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eafaf1, stop: 1 #d5f5e3); } \
            QPushButton:hover{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #a6e3ec); } \
            QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #60c1dc);}'
        self.createLabel.setStyleSheet(QPushButtonStyleStr)
        self.createLabel.setFixedWidth(350)
        self.createLabel.clicked.connect(self.showPathToCreate)
        self.orLabel1 = QLabel("or",self)
        self.orLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.browse1 = QPushButton("Browse",self)
        self.browse1.setStyleSheet(QPushButtonStyleStr)
        self.browse1.clicked.connect(self.getCSVPath)
        self.createPath = QLabel("Path: ",self)      
        self.saveLabel = QPushButton('Provide full path and filename to save image histogram', self)
        self.saveLabel.setStyleSheet(QPushButtonStyleStr)
        self.saveLabel.setFixedWidth(350)
        self.saveLabel.clicked.connect(self.showPathToSave)
        self.orLabel2 = QLabel("or",self)
        self.orLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.browse2 = QPushButton("Browse",self)
        self.browse2.setStyleSheet(QPushButtonStyleStr)
        self.browse2.clicked.connect(self.getOutputPath)
        self.savePath = QLabel("Path: ",self)
        self.spacer = QLabel("",self)
        self.apply = QPushButton("Apply",self)
        self.apply.setStyleSheet(QPushButtonStyleStr)
        self.apply.setFixedWidth(200)
        self.apply.clicked.connect(self.createHist)
        self.backToMenu = QPushButton("Back To Menu",self)
        self.backToMenu.setStyleSheet(QPushButtonStyleStr)
        self.backToMenu.setFixedWidth(200)
        self.backToMenu.clicked.connect(self.close)
        self.message = QLabel(self)
        self.layout1 = QVBoxLayout(self)
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        

        layout2.addWidget(self.createLabel)
        layout2.addWidget(self.orLabel1)
        layout2.addWidget(self.browse1)
        self.layout1.addLayout(layout2)
        self.layout1.addWidget(self.createPath)
        layout3.addWidget(self.saveLabel)
        layout3.addWidget(self.orLabel2)
        layout3.addWidget(self.browse2)
        self.layout1.addLayout(layout3)
        self.layout1.addWidget(self.savePath)
        self.layout1.addWidget(self.spacer)
        layout4.addWidget(self.apply)
        layout4.addWidget(self.backToMenu)
        self.layout1.addLayout(layout4)
        self.layout1.addWidget(self.message)
        
        self.setGeometry(590, 475, 350, 150)
        self.setWindowTitle('Option 4')
        
        self.inputPath = ""
        self.outputPath = ""

    ## @function showPathToCreate 
    #  @brief Member function that gets input path to create montage from user-written path         
    def showPathToCreate(self):
        text, ok = QInputDialog.getText(self, 'Input Path to Create Image Histogram', 
            'Enter path to directory:')
        if ok:
            if os.path.isdir(str(text)):  
                self.createPath.clear
                self.createPath.setText("Path: " + str(text))
                self.inputPath = str(text)
            else:
                self.createPath.clear
                self.createPath.setText("Given directory is not valid: " + str(text))

    ## @function showPathToSave
    #  @brief Member function that gets path to save montage from user-written path
    def showPathToSave(self):
        text, ok = QInputDialog.getText(self, 'Input Path to Save Image Histogram', 
            'Enter path to directory:')
        if ok:
            if os.path.isdir(str(text)):
                self.savePath.clear
                self.savePath.setText("Path: " + str(text)) 
                self.outputPath = str(text)
            else:
                self.savePath.clear
                self.savePath.setText("Given directory is not valid: " + str(text))
   
    ## @function getCSVPath
    #  @brief Member function that gets path to CSV files from user-chosen folder using browse                         
    def getCSVPath(self):
        text = QFileDialog.getExistingDirectory(self, 'Select Folder', 'C:\\', QFileDialog.ShowDirsOnly)        
        self.createPath.clear
        self.createPath.setText("Path: " + str(text))        
        self.inputPath = str(text)
    
    ## @function getOutputPath
    #  @brief Member function that gets path to save montages from user-chosen folder using browse    
    def getOutputPath(self):
        text = QFileDialog.getExistingDirectory(self, 'Select Folder', 'C:\\', QFileDialog.ShowDirsOnly)
        self.savePath.clear
        self.savePath.setText("Path: " + str(text))        
        self.outputPath = str(text)

    def createHist(self):
        if self.inputPath == "" or self.outputPath == "":
            self.error.exec_()
        else:
            self.montage.input_data(src_path = self.inputPath, dest_path = self.outputPath)
            self.montage.create_image_hist()
            self.message.setText("Image histogram created and saved.")
            
## @class PromptMenu
#  @brief Creates GUI menu for user to choose which type of montage to create
#
#  This class connects the GUI to classes that contain functions to create montages.
class PromptMenu(QWidget):
    def __init__(self, parent = None): #Constructor
        super(PromptMenu,self).__init__(parent)
        self.setGeometry(550,450,600,300)
        self.setWindowTitle("PyMontage Menu")
        self.setStyleSheet("QWidget{ background-color: #daf7a6;}")
        self.menuLabel = QLabel(self)
        self.menuLabel.setText("Welcome to PyMontage")
        self.menuLabel.setFont(QFont("Adobe Gothic Std B", 20))
        self.menuLabel.setStyleSheet("QLabel{ color: #566573; }")
        self.menuLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.button1 = QPushButton("1. Create montages recursively from given directory and sub-directories",self)
        QPushButtonStyleStr = 'QPushButton{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #eafaf1, stop: 1 #d5f5e3); } \
            QPushButton:hover{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #a6e3ec); } \
            QPushButton:pressed{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b4e6ed, stop: 1 #60c1dc);}'
        self.button1.setStyleSheet(QPushButtonStyleStr)
        self.button2 = QPushButton("2. Create montages from provided CSV files (split categories or bins)",self)
        self.button2.setStyleSheet(QPushButtonStyleStr)
        self.button3 = QPushButton("3. Create vertical montage from provided CSV file",self)
        self.button3.setStyleSheet(QPushButtonStyleStr)
        self.button4 = QPushButton("4. Create image histogram from provided CSV file",self)
        self.button4.setStyleSheet(QPushButtonStyleStr)
        self.exitBtn = QPushButton("Exit",self)
        self.exitBtn.setStyleSheet(QPushButtonStyleStr)
        self.exitBtn.setFixedWidth(50)
        self.layout = QVBoxLayout(self)
        self.button1.clicked.connect(self.b1Clicked)
        self.button2.clicked.connect(self.b2Clicked)
        self.button3.clicked.connect(self.b3Clicked)
        self.button4.clicked.connect(self.b4Clicked)
        self.exitBtn.clicked.connect(self.close)
        
        layout2 = QHBoxLayout()
        
        self.layout.addWidget(self.menuLabel)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        layout2.addWidget(self.exitBtn)
        layout2.setAlignment(self.exitBtn, QtCore.Qt.AlignCenter)
        self.layout.addLayout(layout2)
   
        self.montageDir = MontageDir(self) 
        self.montageFromCSV = MontageFromCSV(self)
        self.verticalMontageFromCSV = VerticalMontageFromCSV(self)
        self.imageHistFromCSV = ImageHistFromCSV(self)

    @QtCore.pyqtSlot()    
    ## @publicSlot b1Clicked
    #  @brief Creates new MontageDir window
    def b1Clicked(self):
        self.montageDir.exec_()
    ## @publicSlot b2Clicked
    #  @brief Creates new MontageFromCSV window
    def b2Clicked(self):
        self.montageFromCSV.exec_()
    ## @publicSlot b3Clicked
    #  @brief Creates new VerticalMontageFromCSV window
    def b3Clicked(self):
        self.verticalMontageFromCSV.exec_()   
    ## @publicSlot b4Clicked
    #  @brief Creates new ImageHistFromCSV window
    def b4Clicked(self):
        self.imageHistFromCSV.exec_()

def main():
    app = QApplication([])
    widget = PromptMenu();
    widget.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
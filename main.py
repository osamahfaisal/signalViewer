from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QFileDialog
from pyqtgraph import PlotWidget, plot 
import pyqtgraph as pg
from PyQt5.QtCore import QTimer
import sys
import pandas as pd
from GuiOfsignal import Ui_MainWindow


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)




#  variable 
ui.filePath=str
ui.timeAxis=[]
ui.amplitude=[]
ui.speed=2
ui.indx=0
ui.num=0
ui.leftXShift=0.6
ui.rightXShift=0.4
ui.downYShift=0.6
ui.upYShift=0.6




#  methods 

def loadFile():
    try:
        filePath= QtWidgets.QFileDialog.getOpenFileName(None, "Load Signal File 1", "", "*.csv;;")
        ui.filePath=filePath[0]
        ui.timeAxis=pd.read_csv(ui.filePath).iloc[: , 0]
        ui.amplitude=pd.read_csv(ui.filePath).iloc[: , 1]
        
    except:
        print("please try again")
    


def startplot():
    ui.indx=ui.speed+ui.indx
    
    try:
        if ui.comboBox.currentText()=="Wighte":
            ui.graphicsView.plotItem.clear()
            ui.graphicsView.plotItem.plot(ui.timeAxis[:ui.indx] , ui.amplitude[:ui.indx] , pen=pg.mkPen(color=(255, 255, 255)))

        elif ui.comboBox.currentText()=="Green": 
            ui.graphicsView.plotItem.clear()
            ui.graphicsView.plotItem.plot(ui.timeAxis[:ui.indx] , ui.amplitude[:ui.indx] , pen=pg.mkPen(color=(0, 255,0)))
            ui.graphicsView.plotItem.setXRange(ui.timeAxis[ui.indx]-ui.leftXShift,ui.timeAxis[ui.indx]+ui.rightXShift)
            
            
        elif ui.comboBox.currentText()=="Red":
            ui.graphicsView.plotItem.clear() 
            ui.graphicsView.plotItem.plot(ui.timeAxis[:ui.indx] , ui.amplitude[:ui.indx] , pen=pg.mkPen(color=(255, 0,0)))
            ui.graphicsView.plotItem.setXRange(ui.timeAxis[ui.indx]-ui.leftXShift,ui.timeAxis[ui.indx]+ui.rightXShift)
        
                    
        if ui.timeAxis[ui.indx] < 0.7 :
            ui.graphicsView.plotItem.setXRange(ui.leftXShift-0.6,ui.rightXShift+0.6)
            ui.graphicsView.plotItem.setYRange(-ui.downYShift,ui.upYShift)

        else:
            ui.graphicsView.plotItem.setXRange(ui.timeAxis[ui.indx]-ui.leftXShift,ui.timeAxis[ui.indx]+ui.rightXShift)
            ui.graphicsView.plotItem.setYRange(-ui.downYShift,ui.upYShift)
            
            
        ui.num +=1
        
    except:
        pass



def updateData(): # done 
    ui.timer=QTimer()
    ui.timer.timeout.connect(startplot)
    ui.timer.start(10)
    

def pause(): #done 
    try: 
        ui.timer=QTimer()
        ui.timer.timeout.connect(startplot)
        ui.timer.stop()
    except:
        print("no garph to pause it ")
   

def reset(): # done 
    try: 
        ui.graphicsView.plotItem.clear()
        ui.indx=0
        ui.num=0
        ui.speed=2

    except:
        print("not reset try  again")
    


def clear(): # done 
    try:
        ui.graphicsView.plotItem.clear()
        ui.indx=0
        ui.num=0
        ui.filePath=str
        ui.timeAxis=[]
        ui.amplitude=[]
        ui.speed=2
        ui.speedPushButton.setText("1X")
        ui.comboBox.setCurrentText("Wighte")
    except:
        print("not clear try again")
  
        
    
def speed(): # done 
    
    textOnPushButtonSpeed=ui.speedPushButton.text()
    if textOnPushButtonSpeed=="1x":
        ui.speed=4
        ui.speedPushButton.setText("2x")

    elif textOnPushButtonSpeed=="2x":
        ui.speed=8
        ui.speedPushButton.setText("4x")
        
    elif textOnPushButtonSpeed=="4x":
        ui.speed=16
        ui.speedPushButton.setText("8x")

    else:
        ui.speed=1
        ui.speedPushButton.setText("1x")
    

         
   

def zoomIn(): # same as zoom out 
    pass

def zoomOut(): # Done 
    textOnZoomOut=ui.zoomOutPushButton.text()
    
    if textOnZoomOut=="Zoom_out_100%":
        ui.leftXShift=0.75
        ui.rightXShift=0.50
        ui.downYShift=0.75
        ui.upYShift=0.75
        ui.zoomOutPushButton.setText("Zoom_out_25%")
    
    elif textOnZoomOut=="Zoom_out_25%":
        ui.leftXShift=0.90
        ui.rightXShift=0.60
        ui.downYShift=0.90
        ui.upYShift=0.90
        ui.zoomOutPushButton.setText("Zoom_out_50%")
        
    elif textOnZoomOut=="Zoom_out_50%":
        ui.leftXShift=1.05
        ui.rightXShift=0.7
        ui.downYShift=1.05
        ui.upYShift=1.05
        ui.zoomOutPushButton.setText("Zoom_out_75%")
    
    else:
        ui.leftXShift=0.6
        ui.rightXShift=0.4
        ui.downYShift=0.6
        ui.upYShift=0.6
        ui.zoomOutPushButton.setText("Zoom_out_100%")
        
    




def close():
    pass


# connection 

ui.loadFilePushButton.clicked.connect(loadFile)
ui.startPushButton.clicked.connect(updateData)
ui.pausePushButton.clicked.connect(pause)
ui.ResetPushButton.clicked.connect(reset)
ui.clearPushButton.clicked.connect(clear)
ui.speedPushButton.clicked.connect(speed)
ui.zoomOutPushButton.clicked.connect(zoomOut)
ui.zoomInPushButton.clicked.connect(zoomIn)






# timer to update data

MainWindow.show()
sys.exit(app.exec_())

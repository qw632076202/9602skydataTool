#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *
from UI.HeaderArea import *
from UI.DividingLine import *
from UI.ConfigAreaFactory import *
from UI.BottomArea import *
from UI.ConfigArea import *
from UI.MiddleArea import *
from DetailConfigOperateLogic import *
from SimpleConfigOperateLogic import *

class MainWindow:
  mainWindow = NONE
  __SkyDataToolVersion = '2020-7-3'

  __mainWindowWidth = 0
  __mainWindowHeight = 0
  
  headerArea = NONE
  __topDividingLine = NONE
  __middleArea = NONE

  detailConfigArea = NONE
  detailConfigOperateLogic = NONE
  simpleConfigArea = NONE
  simpleConfigOperateLogic = NONE

  __bottomDividingLine = NONE
  bottomArea = NONE

  __configAreaFactory = NONE

  def __init__(self):
    super().__init__()
    self.mainWindow = Tk()
    self.mainWindow.title('SkyDataTool_v' + self.__SkyDataToolVersion);
    self.mainWindow.resizable(0, 0) # 让最大化按钮不可操作 
    # self.__mainWindowWidth = 790
    self.__mainWindowWidth = 900 # 为了适配屏幕不匹配的问题
    self.__mainWindowHeight =  540
    self.mainWindow.geometry('%dx%d+%d+%d' % (self.__mainWindowWidth,self.__mainWindowHeight, 
         (self.mainWindow.winfo_screenwidth() - self.__mainWindowWidth ) / 2, 10))   # mainWindow定位

  def __addSonComponent(self):
    self.bottomArea = BottomArea(self, 0, 470)

    self.headerArea = HeaderArea(self, 0, 10)
    self.__topDividingLine = DividingLine(self.mainWindow, 0, 40)
    
    self.__middleArea = MiddleArea(self, 0, 60)
    self.__configAreaFactory = ConfigAreaFactory()
    self.detailConfigArea = self.__configAreaFactory.createDetailConfigArea(self.__middleArea)

    self.detailConfigOperateLogic = DetailConfigOperateLogic(self)
    self.simpleConfigArea = self.__configAreaFactory.createSimpleConfigArea(self.__middleArea)
    
    self.simpleConfigOperateLogic = SimpleConfigOperateLogic(self)

    self.simpleConfigArea.hideSelf()

    self.__bottomDividingLine = DividingLine(self.mainWindow, 0, 450)

  def windowInit(self):
    self.__addSonComponent()
    self.mainWindow.mainloop()
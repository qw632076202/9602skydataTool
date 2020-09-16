#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from tkinter import *
from UI.LableFrameItem.LableFrameItemFactory import LableFrameItemFactory

class ConfigArea:
  father = NONE
  mainFrame = NONE
  __verticalScrollbar = NONE
  __canvas = NONE
  widgetsContainer = NONE
  sonComponentMap = NONE
  configAreaName = None
  # sonComponentMap = {} , 这里遇到大坑，这是类成员变量，相当于c++类的static变量，是公用的，不是实例成员变量，md

  config_WriteEntryInfoToFile = NONE
  __lableFrameItemFactory = NONE

  def __init__(self, father, configAreaName):
    super().__init__()
    self.father = father
    self.sonComponentMap = {} # 这才是实例成员，实例成员变量要在__init__构造函数中定义，直接在外边定义的是类成员变量
    self.config_WriteEntryInfoToFile = NONE
    self.configAreaName = configAreaName

    self.__lableFrameItemFactory = LableFrameItemFactory()

    self.mainFrame = Frame(self.father.mainFrame)
    self.mainFrame.pack(fill="both", expand=True)

    self.__verticalScrollbar = Scrollbar(self.mainFrame)
    # 滑动区域的大小通过Canvas大小来设置
    # self.__canvas = Canvas(self.mainFrame, yscrollcommand = self.__verticalScrollbar.set, width = 770, height = 400)
    self.__canvas = Canvas(self.mainFrame, yscrollcommand = self.__verticalScrollbar.set, width = 880, height = 400) #适配屏幕不匹配
    self.__verticalScrollbar.config(command = self.__canvas.yview)
    self.__verticalScrollbar.pack(side = 'right', fill = "y")
    self.__canvas.pack(side="left", fill="both", expand=True)

    self.widgetsContainer = Frame(self.__canvas)
    self.__canvas.create_window(0, 0, window = self.widgetsContainer, anchor='nw')

    self.refreshPage()

  def showSelf(self):
    self.mainFrame.pack(fill="both", expand=True)
  
  def hideSelf(self):
    self.mainFrame.pack_forget()

  def addSonComponentInMap(self, itemName, type):
    self.sonComponentMap[itemName] = self.__lableFrameItemFactory.createLableFrameItem(self,
                                            itemName, type)

  def refreshPage(self):
    self.father.mainFrame.update()
    self.__canvas.config(scrollregion = self.__canvas.bbox("all"))

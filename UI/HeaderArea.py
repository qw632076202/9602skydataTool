#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *

class HeaderArea:
  __father = NONE
  mainFrame = NONE
  myLable = NONE
  tabRadiobuttonVar = NONE
  detailConfigRadiobutton = NONE
  simpleConfigRadiobutton = NONE

  curConfigArea = 'detailConfigArea'

  def __init__(self, father, placeX, placeY):
    super().__init__()
    self.__father = father

    self.mainFrame = Frame(self.__father.mainWindow, height = 50)
    self.mainFrame.place(x = placeX, y = placeY)

    self.myLable = Label(self.mainFrame, text='配置选择:', font=('宋体', 13))
    self.myLable.pack(side="left")

    self.tabRadiobuttonVar = StringVar()
    self.tabRadiobuttonVar.set('detailedConfigShow')

    self.detailConfigRadiobutton = Radiobutton(self.mainFrame, text='详细配置', 
      variable=self.tabRadiobuttonVar, value='detailedConfigShow',font=('宋体', 13),command=self.__detailConfigShow)
    self.detailConfigRadiobutton.pack(side="left")

    self.simpleConfigRadiobutton = Radiobutton(self.mainFrame, text='简易配置', 
      variable=self.tabRadiobuttonVar, value='__simpleConfigShow',font=('宋体', 13),command=self.__simpleConfigShow)
    self.simpleConfigRadiobutton.pack(side="left")

  def __detailConfigShow(self): 
    print('detailConfigShow')
    self.curConfigArea = 'detailConfigArea'
    if (self.__father.simpleConfigArea != NONE):
      self.__father.simpleConfigArea.hideSelf()
    if (self.__father.detailConfigArea != NONE):
      self.__father.detailConfigArea.showSelf()

  def __simpleConfigShow(self):
    print('simpleConfigShow')
    self.curConfigArea = 'simpleConfigArea'
    if (self.__father.detailConfigArea != NONE):
      self.__father.detailConfigArea.hideSelf()
    if (self.__father.simpleConfigArea != NONE):
      self.__father.simpleConfigArea.showSelf()

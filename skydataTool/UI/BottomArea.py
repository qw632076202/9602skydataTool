#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *

class BottomArea:
  __father = NONE
  __mainFrame = NONE
  __genetateButton = NONE
  __stateLabel = NONE
  stateStrVar = NONE

  def __init__(self, father, placeX, placeY):
    super().__init__()
    self.__father = father
    self.stateStrVar = StringVar()
    self.__mainFrame = Frame(self.__father.mainWindow, height = 70, width = 790)
    self.__addSonComponent()
    self.__mainFrame.place(x = placeX, y = placeY)

  def __addSonComponent(self):
    Label(self.__mainFrame, text = '状态 ：', font=('宋体', 13)).place(relx = 0, rely = 0)
    self.__stateLabel = Label(self.__mainFrame, textvariable = self.stateStrVar, font=('宋体', 13))
    self.__stateLabel.place(relx = 0.09, rely = 0)
    self.stateStrVar.set('no state...')

    self.__genetateButton = Button(self.__mainFrame,text="生成",font=('宋体', 13)
                                                                      ,command = self.__genetateButtonFun)
    self.__genetateButton.place(relx = 0.93, rely = 0)

    self.__aboutLabel = Label(self.__mainFrame, text = 'made by liukaifeng, have any'
                                        + ' problem to contact liukaifeng@skyworth.com', font=('宋体', 8))
    self.__aboutLabel.place(relx = 0.44, rely = 0.7)

  def __genetateButtonFun(self):
    if (self.__father.headerArea.curConfigArea == 'detailConfigArea'):
      self.__father.detailConfigOperateLogic.generate()
    elif (self.__father.headerArea.curConfigArea == 'simpleConfigArea'):
      self.__father.simpleConfigOperateLogic.generate()

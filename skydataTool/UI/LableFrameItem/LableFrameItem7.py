#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *
from tkinter import filedialog   #filedialog需要单独插入，类似于子类的存在
from UI.LableFrameItem.LableFrameItemBase import LableFrameItemBase
from UI.LableFrameItem.LoadIniFile import LoadIniFile
import logging

# 7、有一项：xxx
#    xxx：label、entey、button、button组合，可以浏览和加载文件

class LableFrameItem7(LableFrameItemBase):
  firstEntryStrVar = NONE
  __filedText = ''
  __myLoadIniFile = None

  def __init__(self, fatherComponent, moduleNameText, filedText):
    super().__init__(fatherComponent, moduleNameText)
    self.firstEntryStrVar = StringVar()
    self.__filedText = filedText
    self.__myLoadIniFile = LoadIniFile(fatherComponent)
    self.__firstItemFrameInit()

  def __firstItemFrameInit(self):
    self.firstItemFrame = Frame(self.lableFrameItem)
    self.firstLabel = Label(self.firstItemFrame, text = self.moduleNameText + self.__filedText, font=('宋体', 13))
    self.firstLabel.pack(side="left", ipadx= 0, ipady= 10)

    self.firstEntry = Entry(self.firstItemFrame, textvariable = self.firstEntryStrVar, font=('宋体', 14), width=30)
    self.firstEntry.pack(side="left", ipadx= 20, padx= 20)

    self.firstButton = Button(self.firstItemFrame,text="选择",font=('宋体', 13),command = self.__firstPathSelect)
    self.firstButton.pack(side="left", ipadx= 0, padx= 12)
    self.firstButton = Button(self.firstItemFrame,text="加载",font=('宋体', 13),command = self.__loadFile)
    self.firstButton.pack(side="left", ipadx= 0)

    self.firstItemFrame.pack(fill = 'x')

  def __firstPathSelect(self):
    fileName = filedialog.askopenfilename()
    self.firstEntryStrVar.set(fileName)

  def __loadFile(self):
    if (self.firstEntryStrVar.get() != ''):
      self.__myLoadIniFile.loadFile(self.firstEntryStrVar.get())
    else:
      print('未选择需要加载的文件...')
      logging.error('未选择需要加载的文件...')


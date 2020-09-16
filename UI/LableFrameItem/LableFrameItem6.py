#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *
from tkinter import filedialog   #filedialog需要单独插入，类似于子类的存在
from UI.LableFrameItem.LableFrameItemBase import LableFrameItemBase
import re

# 6、有一项：xxx
#    xxx：label、entey、button组合，按button显示【目录路径】

class LableFrameItem6(LableFrameItemBase):
  firstEntryStrVar = NONE
  __filedText = ''

  def __init__(self, fatherComponent, moduleNameText, filedText):
    super().__init__(fatherComponent, moduleNameText)
    self.firstEntryStrVar = StringVar()
    self.moduleNameText = moduleNameText
    self.__filedText = filedText
    self.__firstItemFrameInit()

  def __firstItemFrameInit(self):
    self.firstItemFrame = Frame(self.lableFrameItem)
    self.firstLabel = Label(self.firstItemFrame, text = self.moduleNameText + self.__filedText, font=('宋体', 13))
    self.firstLabel.pack(side="left", ipadx= 0, ipady= 10)

    self.firstEntry = Entry(self.firstItemFrame, textvariable = self.firstEntryStrVar, font=('宋体', 14),width=37)
    self.firstEntry.pack(side="left", ipadx= 20, padx= 20)

    self.firstButton = Button(self.firstItemFrame,text="浏览",font=('宋体', 13),command = self.__firstPathSelect)
    self.firstButton.pack(side="left", ipadx= 0)

    self.firstItemFrame.pack(fill = 'x')

  def __firstPathSelect(self):
    fileName = filedialog.askdirectory()
    if(self.moduleNameText.strip() == 'Base'):
      self.firstEntryStrVar.set(fileName)
      self.__setDefaultOpenPathForFiledialog(fileName)
    else:
      baseURL = self.__getBaseURL()
      shortFileName = re.sub(baseURL, '', fileName, count=0, flags=0)
      self.firstEntryStrVar.set(shortFileName)

  def __getBaseURL(self):
    return self.fatherComponent.sonComponentMap['Base'].firstEntryStrVar.get()

  def __setDefaultOpenPathForFiledialog(self, defaultOpenPath):
    for itemName in self.fatherComponent.sonComponentMap:
      if(hasattr( self.fatherComponent.sonComponentMap[itemName], 'filedialogDefaultOpenPath')):
        self.fatherComponent.sonComponentMap[itemName].filedialogDefaultOpenPath = defaultOpenPath

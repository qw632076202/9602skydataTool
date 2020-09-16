#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *
from tkinter import filedialog   #filedialog需要单独插入，类似于子类的存在
from UI.LableFrameItem.LableFrameItemBase import LableFrameItemBase

# 5、有一项：xxx
#    xxx：label、entey、button组合，按button显示【文件路径】

class LableFrameItem5(LableFrameItemBase):
  firstEntryStrVar = NONE
  __filedText = ''

  def __init__(self, fatherComponent, moduleNameText, filedText):
    super().__init__(fatherComponent, moduleNameText)
    self.firstEntryStrVar = StringVar()
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
      fileName = filedialog.askopenfilename()
      self.firstEntryStrVar.set(fileName)


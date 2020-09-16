#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *
from tkinter import filedialog   # filedialog需要单独插入，类似于子类的存在
import os
#正则表达式包
import re
import time;  # 引入time模块

from UI.LableFrameItem.LableFrameItemBase import LableFrameItemBase

# 2、有两项：url ver
#    url：label、entey、button组合，按button显示路径
#    ver：label、entey、button组合，按button显示时间信息

class LableFrameItem2(LableFrameItemBase):
  firstEntryStrVar = NONE
  secondEntryStrVar = NONE
  filedialogDefaultOpenPath = NONE

  def __init__(self, fatherComponent, moduleNameText):
    super().__init__(fatherComponent, moduleNameText)
    self.firstEntryStrVar = StringVar()
    self.secondEntryStrVar = StringVar()
    self.filedialogDefaultOpenPath = None

    self.__firstItemFrameInit()
    self.__secondItemFrameInit()

  def __firstItemFrameInit(self):
    self.firstItemFrame = Frame(self.lableFrameItem)
    self.firstLabel = Label(self.firstItemFrame, text = self.moduleNameText + '_URL', font=('宋体', 13))
    self.firstLabel.pack(side="left", ipadx= 0, ipady= 10)

    self.firstEntry = Entry(self.firstItemFrame, textvariable = self.firstEntryStrVar, font=('宋体', 14),width=37)
    self.firstEntry.pack(side="left", ipadx= 20, padx= 20)

    self.firstButton = Button(self.firstItemFrame,text="浏览",font=('宋体', 13),command = self.__firstPathSelect)
    self.firstButton.pack(side="left", ipadx= 0)

    self.firstItemFrame.pack(fill = 'x')

  def __secondItemFrameInit(self):
    self.secondItemFrame = Frame(self.lableFrameItem)

    self.secondLabel = Label(self.secondItemFrame, text = self.moduleNameText + '_VER', font=('宋体', 13))
    self.secondLabel.pack(side="left", ipadx= 0, ipady= 10)

    self.secondEntry = Entry(self.secondItemFrame,textvariable = self.secondEntryStrVar, font=('宋体', 14),width=37)
    self.secondEntry.pack(side="left", ipadx= 20, padx= 20)

    self.secondButton = Button(self.secondItemFrame,text="浏览",font=('宋体', 13),
                                                                state = DISABLED, command = self.__secondPathSelect)
    self.secondButton.pack(side="left", ipadx= 0)
    self.secondItemFrame.pack(fill = 'x')

  def __firstPathSelect(self):
    fileName = filedialog.askdirectory(initialdir = self.filedialogDefaultOpenPath)
    baseURL = self.__getBaseURL()
    shortFileName = re.sub(baseURL, '', fileName, count=0, flags=0)
    self.firstEntryStrVar.set(shortFileName)
    self.__secondPathSelect()

  def __secondPathSelect(self):
      timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
      self.secondEntryStrVar.set(timeStr)

  def __getBaseURL(self):
    return self.fatherComponent.sonComponentMap['Base'].firstEntryStrVar.get()

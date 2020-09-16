#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *
from tkinter import ttk
from UI.LableFrameItem.LableFrameItemBase import LableFrameItemBase
from GetDataFromExcel import *

# 4、有一项：xxx
#    xxx：label、Combobox（下拉框）组合，使用下拉框输入信息

class LableFrameItem4(LableFrameItemBase):
  firstEntryStrVar = NONE
  __comboxlistValueTuple = NONE

  def __init__(self, fatherComponent, moduleNameText, comboxlistValueTuple):
    super().__init__(fatherComponent, moduleNameText)
    self.__comboxlistValueTuple = comboxlistValueTuple
    self.firstEntryStrVar = StringVar()

    self.__firstItemFrameInit()

  def __firstItemFrameInit(self):
    self.firstItemFrame = Frame(self.lableFrameItem)
    self.firstLabel = Label(self.firstItemFrame, text = self.moduleNameText, font=('宋体', 13))
    self.firstLabel.pack(side="left", expand=True, ipadx= 20, ipady= 10)

    self.firstCombobox = ttk.Combobox(self.firstItemFrame, textvariable = self.firstEntryStrVar)
    self.firstCombobox.bind("<<ComboboxSelected>>", self.__comboxlistChange) # 绑定虚拟事件函数
    self.firstCombobox["values"] = self.__comboxlistValueTuple
    self.firstCombobox.current(0) # 默认选择第0项
    self.firstCombobox.pack(side = "left", expand = True, ipadx = 20, padx = 20)

    self.firstItemFrame.pack(fill = 'x')
  
  def __comboxlistChange(self, defaultArg): # defaultArg是tkinter规定带的默认参数
    if (self.moduleNameText.strip() == 'AREA'):
      if (self.firstEntryStrVar.get() == '亚太&欧洲'):
        self.__renderData('亚太&欧洲')
      elif (self.firstEntryStrVar.get() == '南美'):
        self.__renderData('南美')  
      elif (self.firstEntryStrVar.get() == '北美'):
        self.__renderData('北美') 
      elif (self.firstEntryStrVar.get() == '香港'):
        self.__renderData('香港')
      elif (self.firstEntryStrVar.get() == '台湾'):
        self.__renderData('台湾')

  def __renderData(self, area):
    countryDate = GetDataFromExcel.getCountryORLanguage(area, 'country', 0)[1]
    languageDate = GetDataFromExcel.getCountryORLanguage(area, 'language', 0)[1]
    self.fatherComponent.sonComponentMap['COUNTRY'].firstCombobox["values"] = tuple(countryDate)
    self.fatherComponent.sonComponentMap['COUNTRY'].firstCombobox.current(0)
    self.fatherComponent.sonComponentMap['LANGUAGE'].firstCombobox["values"] = tuple(languageDate)
    self.fatherComponent.sonComponentMap['LANGUAGE'].firstCombobox.current(0)

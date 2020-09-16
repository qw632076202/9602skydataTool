#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *
from tkinter import filedialog   #filedialog需要单独插入，类似于子类的存在
import os
#正则表达式包
import re
import time;  # 引入time模块

class LableFrameItemBase:
  fatherComponent = NONE
  lableFrameItem = NONE
  moduleNameText = NONE

  def __init__(self, fatherComponent, moduleNameText):
    super().__init__()
    self.fatherComponent = fatherComponent
    self.moduleNameText = moduleNameText

    self.lableFrameItem = LabelFrame(self.fatherComponent.widgetsContainer, text=self.moduleNameText, )
    self.lableFrameItem.pack(fill = 'x', expand = True)
    # self.lableFrameItem.place(relx=1.0, rely=0.5, anchor=E)

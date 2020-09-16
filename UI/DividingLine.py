#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *

class DividingLine:
  fatherComponent = NONE
  dividingLine = NONE

  def __init__(self, fatherComponent, placeX, placeY):
    self.fatherComponent = fatherComponent
    super().__init__()
    self.dividingLine  = Label(self.fatherComponent, text='-'*180, font=('宋体', 13))
    self.dividingLine.place(x = placeX, y = placeY)

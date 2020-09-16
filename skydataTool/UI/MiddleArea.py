#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *

class MiddleArea:
  father = None
  mainFrame = None
  def __init__(self, father, placeX, placeY):
    super().__init__()
    self.father = father
    self.mainFrame = Frame(father.mainWindow, height = 400)
    self.mainFrame.place(x = placeX, y = placeY)
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from UI.MainWindow import MainWindow
import logging

logging.basicConfig(filename='./LOG/'+'skydataTool'+'.log',
            format='[%(asctime)s； %(filename)s]：%(levelname)s：%(message)s', 
            level = logging.ERROR, filemode='a', datefmt='%Y-%m-%d  %I:%M:%S %p')

if __name__ == '__main__':
  mainWindow = MainWindow()
  mainWindow.windowInit()
#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import re
import logging

# 这个类暂未使用，可能跑不通，用时修改
class DynamicRenderItem:

  def __init__(self):
    super().__init__()

  def __getRenderItemTexts(self):
    pidIniFilePath = ''
    pidIniFile = None
    for itemName in self.__simpleConfigArea.sonComponentMap:
      if (itemName == 'PID'):
        pidIniFilePath = self.__simpleConfigArea.sonComponentMap[itemName].firstEntryStrVar.get()
        break
    try:
      pidIniFile = open(pidIniFilePath, "r+", encoding = 'ascii')
      strList = pidIniFile.readlines()
      for oneStr in strList:
        if (self.__getItemTextFromStr(oneStr) != ''):
          self.__renderItemStrList.append(self.__getItemTextFromStr(oneStr))
    except FileNotFoundError as fnferror:
      pass
    finally:
      if (pidIniFile != None):
        pidIniFile.close()
      else:
        print('PID.ini文件打开失败...')
        logging.error('PID.ini文件打开失败...')
  def __getItemTextFromStr(self, str1):
    pattern = '\[.+\]'
    findedStrList = re.findall(pattern, str1)
    if findedStrList != []:
      itemText = re.sub('\[', '', findedStrList[0], count=0, flags=0)
      itemText = re.sub('\]', '', itemText, count=0, flags=0)
      return itemText
    else:
      return ''

  def __renderItem(self):
    for i in self.__renderItemStrList:
      self.__simpleConfigArea.addSonComponentInMap(i, [1])
    self.__simpleConfigArea.refreshPage()
    print('渲染页面成功！！！')
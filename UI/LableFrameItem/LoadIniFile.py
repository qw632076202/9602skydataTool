#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import re # 正则表达式包
from Write_ConfigData_ini import Write_ConfigData_ini
import logging

class LoadIniFile:
  item_EntryValue_Map = None
  __configArea = None
  __myWrite_ConfigData_ini = None

  def __init__(self, configArea):
    super().__init__()
    self.item_EntryValue_Map = {}
    self.__configArea = configArea
    if (self.__configArea.configAreaName == 'simpleConfig'):
      self.__myWrite_ConfigData_ini = Write_ConfigData_ini.getInstance(self.__configArea)

  def loadFile(self, filePath):
    strList = self.__get_strList_from_IniFile(filePath)
    self.__setItem_EntryValue_Map(strList)
    if (self.__configArea.configAreaName == 'detailConfig'):
      self.__renderDataToDetailConfigArea()
    elif (self.__configArea.configAreaName == 'simpleConfig'):
      self.__renderDataToSimpleConfigArea()
  
  def __get_strList_from_IniFile(self, filePath):
    iniFile = None
    try:
      iniFile = open(filePath, "r+", encoding = 'utf8')
      strList = iniFile.readlines()
      return strList
    except (FileExistsError,FileNotFoundError):
      print('打开PID.ini文件失败...')
      logging.error('打开PID.ini文件失败...')
      return []
    finally:
      if (iniFile != None):
        iniFile.close()

  def __setItem_EntryValue_Map(self, strList):
    for str1 in strList:
      pattern = '.*=.*'
      findedStrList = re.findall(pattern, str1)
      if findedStrList != [] and findedStrList != None:
        item = re.sub(' =.*', '', findedStrList[0], count=0, flags=0)
        entryValue = re.sub('.*= ', '', findedStrList[0], count=0, flags=0)
        self.item_EntryValue_Map[item] = entryValue

  def __renderDataToDetailConfigArea(self):
    for item in  self.__configArea.sonComponentMap:
      if (item == 'PID'):
        if (item + '_NUM' in self.item_EntryValue_Map):
          self.__configArea.sonComponentMap[item].firstEntryStrVar.set(self.item_EntryValue_Map[item + '_NUM'])
      elif(item == 'load'):
        pass
      else:
        if (hasattr( self.__configArea.sonComponentMap[item], 'firstEntryStrVar')):
          if (item + '_URL' in self.item_EntryValue_Map):
            self.__configArea.sonComponentMap[item].firstEntryStrVar.set(self.item_EntryValue_Map[item + '_URL'])
        if (hasattr( self.__configArea.sonComponentMap[item], 'secondEntryStrVar')):
          if (item + '_VER' in self.item_EntryValue_Map):
            self.__configArea.sonComponentMap[item].secondEntryStrVar.set(self.item_EntryValue_Map[item + '_VER'])
    print('PID.ini文件加载完成！！！')

  def __renderDataToSimpleConfigArea(self):
    for item in  self.__configArea.sonComponentMap:
      if (item == 'PowerOnMode'):
        if (hasattr( self.__configArea.sonComponentMap[item], 'firstEntryStrVar')):
          if (item in self.item_EntryValue_Map):
            num_text_Map = {'0': '0:上电待机', '1': '1:上电开机', '2': '2:记忆模式'}
            self.__configArea.sonComponentMap[item].firstEntryStrVar.set(num_text_Map[self.item_EntryValue_Map[item]])
      elif (item == 'PVRTYPE'):
        if (hasattr( self.__configArea.sonComponentMap[item], 'firstEntryStrVar')):
          if (item in self.item_EntryValue_Map):
            EN_CH_Map = {'On-NoActivePin':'支持，不需要激活', 'On-NeedActivePin':'支持，需要激活', 'Off':'不支持'}
            self.__configArea.sonComponentMap[item].firstEntryStrVar.set(EN_CH_Map[self.item_EntryValue_Map[item]])
      elif (item == 'COUNTRY'):
        if (hasattr( self.__configArea.sonComponentMap[item], 'firstEntryStrVar')):
          if (item in self.item_EntryValue_Map):
            self.__configArea.sonComponentMap[item].firstEntryStrVar.set(
                      self.__myWrite_ConfigData_ini.code_CountryORLanguage_Map[self.item_EntryValue_Map[item]])
      elif (item == 'LANGUAGE'):
        if (hasattr( self.__configArea.sonComponentMap[item], 'firstEntryStrVar')):
          if (item in self.item_EntryValue_Map):
            self.__configArea.sonComponentMap[item].firstEntryStrVar.set(
                      self.__myWrite_ConfigData_ini.code_CountryORLanguage_Map[self.item_EntryValue_Map[item]])
      elif (item == 'CustomerID'):
        if (hasattr( self.__configArea.sonComponentMap[item], 'firstEntryStrVar')):
          if (item in self.item_EntryValue_Map):
            self.__configArea.sonComponentMap[item].firstEntryStrVar.set(
                      self.__myWrite_ConfigData_ini.shortCustomID_customID_Map[self.item_EntryValue_Map[item]])
      elif (item == 'PID'):
        if (item in self.item_EntryValue_Map):
          self.__configArea.sonComponentMap[item].firstEntryStrVar.set(self.item_EntryValue_Map[item])
      elif(item == 'load'):
        pass
      elif(item == 'AREA'):
        pass
      else:
        if (hasattr( self.__configArea.sonComponentMap[item], 'firstEntryStrVar')):
          if (item in self.item_EntryValue_Map):
            self.__configArea.sonComponentMap[item].firstEntryStrVar.set(self.item_EntryValue_Map[item])
    print('ConfigData.ini文件加载完成！！！')

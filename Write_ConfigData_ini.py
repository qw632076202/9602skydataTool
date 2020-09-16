#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import re # 正则表达式包
from GetDataFromExcel import *
import logging
import time

class Write_ConfigData_ini:
  myInstance = None
  __simpleConfigArea = None
  __countryORLanguage_Code_Map = None
  code_CountryORLanguage_Map = None
  customID_shortCustomID_Map = None
  shortCustomID_customID_Map = None

  def __init__(self, simpleConfigArea):
    super().__init__()
    self.__simpleConfigArea = simpleConfigArea
    self.__countryORLanguage_Code_Map = {}
    self.code_CountryORLanguage_Map = {}
    self.customID_shortCustomID_Map = {}
    self.shortCustomID_customID_Map = {}
    self.__set_countryORLanguage_Code_Map()
    self.__set_customID_shortCustomID_Map()

  @classmethod
  def getInstance(cls, simpleConfigArea = None):
    if (cls.myInstance == None):
      cls.myInstance = Write_ConfigData_ini(simpleConfigArea)
    return cls.myInstance

  def __putAAreaDataToMap(self, area):
    countrykeys = GetDataFromExcel.getCountryORLanguage(area, 'country', 0)[0]
    countryvalues = GetDataFromExcel.getCountryORLanguage(area, 'country', 1)[0]
    for i in range(min(len(countrykeys), len(countryvalues))):
      self.__countryORLanguage_Code_Map[countrykeys[i]] = countryvalues[i]
      # self.code_CountryORLanguage_Map[countryvalues[i]] = countrykeys[i]

    languagekeys = GetDataFromExcel.getCountryORLanguage(area, 'language', 0)[0]
    languagevalues = GetDataFromExcel.getCountryORLanguage(area, 'language', 1)[0]
    for i in range(min(len(languagekeys), len(languagevalues))):
      self.__countryORLanguage_Code_Map[languagekeys[i]] = languagevalues[i]
      # self.code_CountryORLanguage_Map[languagevalues[i]] = languagekeys[i]

  def __set_countryORLanguage_Code_Map(self):
    areaList = ['亚太&欧洲', '南美', '北美', '香港', '台湾']
    for area in areaList:
      self.__putAAreaDataToMap(area)

  def __set_customID_shortCustomID_Map(self):
    customID = GetDataFromExcel.getBrandORCustomerID('CustomerID')[0]
    shortCustomerID = GetDataFromExcel.getBrandORCustomerID('ShortCustomerID')[0]
    for i in range(len(customID)):
      self.customID_shortCustomID_Map[customID[i]] = shortCustomerID[i]
      # self.shortCustomID_customID_Map[shortCustomerID[i]] = customID[i] 这里不要load功能了，就不需要这个反向map

  def write_ConfigData_ini(self, specifiedPath):
    configDataIniPath = specifiedPath + '\\Config\\ConfigData.ini'
    configDataIniFile = None
    try:
      configDataIniString = ""
      for itemName in self.__simpleConfigArea.sonComponentMap:
        if (itemName == 'PowerOnMode'):
          configDataIniString += ('[' + itemName+ ']\n')
          onlyNumberText = re.sub(':.*', '', self.__simpleConfigArea.sonComponentMap[itemName].
                                                                              firstEntryStrVar.get(), count=0, flags=0)
          configDataIniString +=(itemName + ' = ' + onlyNumberText + '\n')
        elif (itemName == 'PVRTYPE'):
          configDataIniString +=('[' + itemName+ ']\n')
          CH_EN_Map = {'支持，不需要激活': 'On-NoActivePin', '支持，需要激活': 'On-NeedActivePin', '不支持': 'Off'}
          configDataIniString +=(itemName + ' = ' + CH_EN_Map[self.__simpleConfigArea.
                                                            sonComponentMap[itemName].firstEntryStrVar.get()] + '\n')
        elif (itemName == 'COUNTRY'):
          configDataIniString +=('[' + itemName+ ']\n')
          countryKey = self.__simpleConfigArea.sonComponentMap[itemName].firstEntryStrVar.get()
          countryCode = self.__countryORLanguage_Code_Map[countryKey]
          configDataIniString +=(itemName + ' = ' + countryCode + '\n')
        elif (itemName == 'LANGUAGE'):
          configDataIniString +=('[' + itemName+ ']\n')
          countryKey = self.__simpleConfigArea.sonComponentMap[itemName].firstEntryStrVar.get()
          countryCode = self.__countryORLanguage_Code_Map[countryKey]
          configDataIniString +=(itemName + ' = ' + countryCode + '\n')
        elif (itemName == 'AREA'):
          pass
        elif (itemName == 'PID'):
          pass
        elif (itemName == 'Base'):
          pass
        elif (itemName == 'CustomerID'):
          configDataIniString +=('[' + itemName+ ']\n')
          customerIDkey = self.__simpleConfigArea.sonComponentMap[itemName].firstEntryStrVar.get()
          customerIDValue = self.customID_shortCustomID_Map[customerIDkey]
          configDataIniString +=(itemName + ' = ' + customerIDValue + '\n')
        else:
          configDataIniString +=('[' + itemName+ ']\n')
          configDataIniString +=(itemName + ' = ' + self.__simpleConfigArea.sonComponentMap[itemName].
                                                                                       firstEntryStrVar.get() + '\n')
      configDataIniString+=('[' + 'GenerateTime'+ ']\n') 
      timeStr = time.strftime("%Y", time.localtime())
      configDataIniString+=('GenerateTime' + ' = ' +  timeStr +'\n') 

      configDataIniFile = open(configDataIniPath, "wb+")
      configDataIniFile.write(bytes(configDataIniString, "ascii"))
    except (FileExistsError,FileNotFoundError):
      print('写configData.ini文件异常，可能指定文件夹不存在...')
      logging.error('写configData.ini文件异常，可能指定文件夹不存在...')
    finally:
      if (configDataIniFile != None):
        configDataIniFile.close()
      else:
        print('写configData.ini文件失败...')
        logging.error('写configData.ini文件失败...')

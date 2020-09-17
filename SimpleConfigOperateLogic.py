#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import shutil # 移动文件功能的包
import re # 正则表达式包
import xlrd # 读取excel表格的包
import logging
from Write_ConfigData_ini import Write_ConfigData_ini
from UI.LableFrameItem.LoadIniFile import LoadIniFile

class SimpleConfigOperateLogic:
  __father = None
  __simpleConfigArea = None
  __mywrite_ConfigData_ini = None
  __my_loadIniFile = None


  def __init__(self, father):
    super().__init__()
    self.__father = father
    self.__simpleConfigArea = self.__father.simpleConfigArea
    self.__mywrite_ConfigData_ini = Write_ConfigData_ini.getInstance(self.__simpleConfigArea)
    self.__my_loadIniFile = LoadIniFile(self.__simpleConfigArea)

  def generate(self):
    self.__copyAllFilesToSpecifiedPath()
    self.__mywrite_ConfigData_ini.write_ConfigData_ini(self.__getSpecifiedPath())
    self.__copyLogoFileToSpecifiedPathAndRename()
    self.__father.bottomArea.stateStrVar.set('SimpleConfig generete finished！！！')

  def __getPID_NUMFromStr(self, str1):
    pattern = 'PID_NUM.*'
    findedStrList = re.findall(pattern, str1)
    if findedStrList != [] and findedStrList != None:
      PID_NUM = re.sub('PID_NUM = ', '', findedStrList[0], count=0, flags=0)
      return PID_NUM
    else:
      return ''

  def __getPID_NUMFromPIDIniFile(self):
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
        if (self.__getPID_NUMFromStr(oneStr) != None and self.__getPID_NUMFromStr(oneStr) != ''):
          return self.__getPID_NUMFromStr(oneStr)
      return ''
    except (FileExistsError,FileNotFoundError):
      print('打开PID.ini文件失败...')
      logging.error('打开PID.ini文件失败...')
      return ''
    finally:
      if (pidIniFile != None):
        pidIniFile.close()    

  def __getSpecifiedPath(self):
    PID_NUM = self.__getPID_NUMFromPIDIniFile()
    specifiedPath = os.getcwd() + '\\'+ PID_NUM +'\\Android_9602_tvconfig'
    return specifiedPath

  def __getBaseURL(self):
    return self.__simpleConfigArea.sonComponentMap['Base'].firstEntryStrVar.get()
  
  def __getRelativeLogoURL(self):
    return self.__simpleConfigArea.sonComponentMap['Logo'].firstEntryStrVar.get()

  def __copyAllFilesToSpecifiedPath(self):
    baseURL = self.__getBaseURL()
    sourcePathAndItemNameList = self.__get_URLsAndItemNames_FromPIDIniFile()
    for sourcePathAndItemName in sourcePathAndItemNameList:
      if (sourcePathAndItemName[0] != '' and sourcePathAndItemName[1] != ''):
        fromDir = baseURL + sourcePathAndItemName[0]
        itemName = sourcePathAndItemName[1]
        toDir = self.__getSpecifiedPath() + '\\' + itemName
        if (fromDir != '' and toDir != ''):
          try:
            shutil.copytree(fromDir, toDir) # 递归复制
          except (FileExistsError, FileNotFoundError):
            logging.error(FileExistsError, FileNotFoundError)
            if (FileExistsError):
              self.__father.bottomArea.stateStrVar.set('文件已经存在，请删除原文件后重新生成...')
    self.__copyPIDInitFileToSpecifiedPath()
    print ("复制文件成功！！！")

  def __get_URLsAndItemNames_FromPIDIniFile(self):
    resultURLList = []
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
        if (self.__get_URLAndItemName_FromStr(oneStr) != None and self.__get_URLAndItemName_FromStr(oneStr) != ''):
          resultURLList.append(self.__get_URLAndItemName_FromStr(oneStr))
      return resultURLList
    except (FileExistsError, FileNotFoundError):
      self.__father.bottomArea.stateStrVar.set('打开PID.ini文件失败...')
      print('打开PID.ini文件失败...')
      logging.error('打开PID.ini文件失败...')
      return resultURLList
    finally:
      if (pidIniFile != None):
        pidIniFile.close()

  def __get_URLAndItemName_FromStr(self, str1):
    pattern = '.*_URL.*'
    findedStrList = re.findall(pattern, str1)
    if findedStrList != [] and findedStrList != None:
      URLText = re.sub('.*_URL = ', '', findedStrList[0], count=0, flags=0)
      ItemNameText = re.sub('_URL.*', '', findedStrList[0], count=0, flags=0)
      return [URLText, ItemNameText]
    else:
      return None 

  def __copyPIDInitFileToSpecifiedPath(self):
    pidIniFilePath = ''
    for itemName in self.__simpleConfigArea.sonComponentMap:
      if (itemName == 'PID'):
        pidIniFilePath = self.__simpleConfigArea.sonComponentMap[itemName].firstEntryStrVar.get()
        break
    if (pidIniFilePath == ''):
      self.__father.bottomArea.stateStrVar.set('未选择PID.ini文件...')
      print('PID.ini文件的路径为空...')
      logging.error('PID.ini文件的路径为空...')
    fromPath = pidIniFilePath
    toPath = self.__getSpecifiedPath()
    shutil.copy(fromPath, toPath) # 拷贝文件

  # def __scanDirToGetFileWholePaths(self, dir):
  #   fileWholePaths = []
  #   for root, dirs, nondirs in os.walk(dir):
  #     for name in nondirs:
  #       fileWholePaths.append(os.path.join(root, name))
  #   return fileWholePaths

  # def __findLogoFileAndRename(self, fileWholePaths):
  #   pattern = '.*logo.jpg.*'
  #   for fileWholePath in fileWholePaths:
  #     if(re.search(pattern, fileWholePath, flags=0)):
  #       disFileWholePath = re.sub('logo.jpg', 'bootlogo.jpg', fileWholePath, count=0, flags=0)
  #       os.rename(fileWholePath, disFileWholePath)
  #       print('重命名成功！！！')
  #       return
  #   logging.error('重命名文件失败，没有找到指定文件...')

  def __copyLogoFileToSpecifiedPathAndRename(self):
    basePath = self.__getBaseURL()
    relativeLogoURL = self.__getRelativeLogoURL()
    fromLogoPath = basePath + relativeLogoURL + '/logo.jpg'
    toLogoPath = self.__getSpecifiedPath() + '/bootlogo.jpg'
    try:
      shutil.copyfile(fromLogoPath, toLogoPath)
    except Exception:
      logging.error('复制logo文件失败...')

  def load_configData_ini(self):
    print('auto load_configData_ini...')

    configDataIniPath = self.__getBaseURL() + '\\Config\\ConfigData.ini'
    print('configDataIniPath == ', configDataIniPath)
    self.__my_loadIniFile.loadFile(configDataIniPath)
     

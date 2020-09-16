#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#图形库包
from tkinter import *
from tkinter import filedialog   #filedialog需要单独插入，类似于子类的存在
import os
#正则表达式包
import re
import logging
from UI.LableFrameItem.LableFrameItemBase import LableFrameItemBase

# 1、有两项：url ver
#    url：label、entey、button组合，按button显示路径
#    ver：label、entey、button组合，按button显示versionInfo信息

class LableFrameItem1(LableFrameItemBase):
  firstEntryStrVar = NONE
  secondEntryStrVar = NONE
  filedialogDefaultOpenPath = NONE

  def __init__(self, fatherComponent, moduleNameText):
    super().__init__(fatherComponent, moduleNameText)
    self.firstEntryStrVar = StringVar()
    self.secondEntryStrVar = StringVar()
    self.__firstItemFrameInit()
    self.__secondItemFrameInit()
    self.filedialogDefaultOpenPath = None

  def __firstItemFrameInit(self):
    self.firstItemFrame = Frame(self.lableFrameItem)
    self.firstLabel = Label(self.firstItemFrame, text = self.moduleNameText + '_URL', font=('宋体', 13))
    self.firstLabel.pack(side="left", ipadx= 0, ipady= 10)

    self.firstEntry = Entry(self.firstItemFrame, textvariable = self.firstEntryStrVar, font=('宋体', 14), width = 37)
    self.firstEntry.pack(side="left", ipadx= 20, padx= 20)

    self.firstButton = Button(self.firstItemFrame,text="浏览",font=('宋体', 13),command = self.__firstButtonClick)
    self.firstButton.pack(side="left", ipadx= 0)

    self.firstItemFrame.pack(fill = 'x')

  def __secondItemFrameInit(self):
    self.secondItemFrame = Frame(self.lableFrameItem)

    self.secondLabel = Label(self.secondItemFrame, text = self.moduleNameText + '_VER', font=('宋体', 13))
    self.secondLabel.pack(side="left", ipadx= 0, ipady= 10, anchor = 'w')

    self.secondEntry = Entry(self.secondItemFrame,textvariable = self.secondEntryStrVar, font=('宋体', 14), width=37)
    self.secondEntry.pack(side="left", ipadx= 20, padx= 20)

    self.secondButton = Button(self.secondItemFrame, text="浏览", font=('宋体', 13), 
                                                                  state = DISABLED, command = self.__secondButtonClick)
    self.secondButton.pack(side="left", ipadx= 0)
    self.secondItemFrame.pack(fill = 'x')

  def __firstButtonClick(self):
    wholeDirPath = filedialog.askdirectory(initialdir = self.filedialogDefaultOpenPath)

    self.__putShortDirPathIntoFirstEntry(wholeDirPath)
    self.__setVersionInfoIntoSecondEntry(wholeDirPath)
    if (self.moduleNameText.strip() == 'hashkey'):
      self.__controlDolbyItemDisplay(wholeDirPath)

  def __secondButtonClick(self):
    pass

  def __controlDolbyItemDisplay(self, wholeDirPath):
    DD_VISION_ATMOS_State = self.__get_DD_VISION_ATMOS_State(wholeDirPath)
    self.__dolbyItemDisplayByDD_VISION_ATMOS_State(DD_VISION_ATMOS_State)

  def __putShortDirPathIntoFirstEntry(self, wholeDirPath):
    baseURL = self.__getBaseURL()
    shortDirPath = re.sub(baseURL, '', wholeDirPath, count=0, flags=0)
    self.firstEntryStrVar.set(shortDirPath)

  def __getVersionInfo(self, versionFilePath):
    versionFile = None
    try:
      versionFile = open(versionFilePath, "r+", encoding = 'ascii')
      versionFileContentList = versionFile.readlines()
      for i in versionFileContentList:
        versionInfoStr = self.__findVersionInfoInStr(i)
        if versionInfoStr != '':
          return versionInfoStr
          break
    except (FileExistsError,FileNotFoundError):
      logging.error(FileExistsError)
      logging.error(FileNotFoundError)
    finally:
      if(versionFile != None):
        versionFile.close()
      else:
        print('打开VersionInfo文件失败...')
        logging.error('打开VersionInfo文件失败...')

  def __setVersionInfoIntoSecondEntry(self, wholeDirPath):
    files = self.__scanDirToGetFiles(wholeDirPath)
    file = self.__getSpecifyFileFromFiles(files)
    if (file != ''):
      versionFilePath = wholeDirPath + '\\' + file
      versionInfoStr = self.__getVersionInfo(versionFilePath)
      self.secondEntryStrVar.set(versionInfoStr)
    else:
      print('versionFilePath为空...')
      logging.error('versionFilePath为空...')

  def __findVersionInfoInStr(self, str1):
    pattern = 'ver = .+'
    findedStrList = re.findall(pattern, str1)
    if findedStrList != []:
      versionInfoStr = re.sub('ver = ', '', findedStrList[0], count=0, flags=0)
      return versionInfoStr
    else:
      return ''

  def __scanDirToGetFiles(self, dir):
    for top, dirs, nondirs in os.walk(dir):
      return nondirs

  def __getSpecifyFileFromFiles(self, files):
    for file in files:
      pattern = '.*version.*'
      searchObj = re.search(pattern, file, flags=0)
      if (searchObj != None):
        return searchObj.group()
    return ''

  def __getBaseURL(self):
    return self.fatherComponent.sonComponentMap['Base'].firstEntryStrVar.get()

  def __findDD_VISION_ATMOSInfoInStr(self, str1):
    pattern = 'DD_VISION_ATMOS = .+'
    findedStrList = re.findall(pattern, str1)
    if findedStrList != []:
      DD_VISION_ATMOSInfo = re.sub('DD_VISION_ATMOS = ', '', findedStrList[0], count=0, flags=0)
      DD_VISION_ATMOSInfo = re.sub(';', '', DD_VISION_ATMOSInfo, count=0, flags=0)
      return DD_VISION_ATMOSInfo
    else:
      return ''

  def __get_DD_VISION_ATMOS_State(self, wholeDirPath):
    files = self.__scanDirToGetFiles(wholeDirPath)
    file = self.__getSpecifyFileFromFiles(files)
    if (file != ''):
      versionFilePath = wholeDirPath + '\\' + file
      versionFile = None
      try:
        versionFile = open(versionFilePath, "r+", encoding = 'ascii')
        versionFileContentList = versionFile.readlines()
        for i in versionFileContentList:
          DD_VISION_ATMOSInfo = self.__findDD_VISION_ATMOSInfoInStr(i)
          if DD_VISION_ATMOSInfo != '':
            if (DD_VISION_ATMOSInfo == 'enable'):
              return True
            else:
              return False
            break
      except (FileExistsError,FileNotFoundError):
        logging.error('FileExistsError or FileNotFoundError...')
      finally:
        if(versionFile != None):
          versionFile.close()
        else:
          print('打开VersionInfo文件失败...')
          logging.error('打开VersionInfo文件失败...')

  def __dolbyItemDisplayByDD_VISION_ATMOS_State(self, DD_VISION_ATMOS_State):
    if (DD_VISION_ATMOS_State == True):
      pass
    else:
      self.fatherComponent.sonComponentMap['Dolby'].firstButton['state'] = DISABLED
      self.fatherComponent.sonComponentMap['Dolby'].firstEntryStrVar.set('null')
      self.fatherComponent.sonComponentMap['Dolby'].secondEntryStrVar.set('null')
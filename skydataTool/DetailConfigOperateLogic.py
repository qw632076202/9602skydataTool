#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import shutil # 移动文件功能的包
import logging
import time

class DetailConfigOperateLogic:
  __father = None
  __detailConfigArea = None

  def __init__(self, father):
    super().__init__()
    self.__father = father
    self.__detailConfigArea = self.__father.detailConfigArea

  def generate(self):
      self.__writePIDInfoToPidIniFile()
      self.__father.bottomArea.stateStrVar.set('DetailedConfig generete finished！！！')
      print('DetailedConfig generete finished！！！')

  def __writePIDInfoToPidIniFile(self):
    pidIniFile = None
    try:
      pidIniFileString = ""
      pidIniFile = open(os.getcwd() + '\\PID.ini', "wb+")
      for item in  self.__detailConfigArea.sonComponentMap:
        if (item == 'PID'):
          if (pidIniFile != None):
            pidIniFileString+=('[' + item+ ']\n')
            pidIniFileString+=(item + '_NUM' + ' = ' +  self.__detailConfigArea.sonComponentMap[item]
                                                                          .firstEntryStrVar.get()+'\n')
          else:
            print('__pidIniFile == None...')
            logging.error('__pidIniFile == None...')
        elif (item == 'load'):
          pass
        elif (item == 'Base'):
          pass
        else:
          if (pidIniFile != None):
            pidIniFileString+=('[' + item+ ']\n')
            if (hasattr( self.__detailConfigArea.sonComponentMap[item], 'firstEntryStrVar')):
              pidIniFileString+=(item + '_URL' + ' = ' +  self.__detailConfigArea.sonComponentMap[item]
                                                                          .firstEntryStrVar.get()+'\n')
            # if (hasattr( self.__detailConfigArea.sonComponentMap[item], 'secondEntryStrVar')):
            #   pidIniFileString+=(item + '_VER' + ' = ' +  self.__detailConfigArea.sonComponentMap[item]
            #                                                               .secondEntryStrVar.get()+'\n')
      pidIniFileString+=('[' + 'GenerateTime'+ ']\n')
      timeStr = time.strftime("%Y%m%d%H%M", time.localtime())
      pidIniFileString+=('GenerateTime' + ' = ' +  timeStr +'\n')

      pidIniFile.write(bytes(pidIniFileString, 'ascii'))
    except (FileExistsError,FileNotFoundError):
      logging.error(FileExistsError)
      logging.error(FileNotFoundError)
    finally:
      pidIniFile.close()

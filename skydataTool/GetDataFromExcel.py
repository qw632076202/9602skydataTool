#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from UI.ConfigArea import *
import os
import xlrd # 读取excel表格的包
import logging

class GetDataFromExcel:
  excelFileForCountryAndLanguage = None
  excelFileForBrandORCustomerID = None
  
  def __init__(self):
    super().__init__()

  @classmethod 
  def eliminateListDuplicateElement(cls, list1):
    resultList = []
    for a in list1:
      if a not in resultList:
        resultList.append(a)
    return resultList

  @classmethod 
  def getBrandORCustomerID(cls, dataType):
    columnNum = 0
    if (dataType == 'Brand'):
      columnNum = 5
    elif (dataType == 'CustomerID'):
      columnNum = 3
    elif (dataType == 'ShortCustomerID'):
      columnNum = 4

    excelPath = os.getcwd() + '\\数据分离-客户-品牌-标准化V1.0.xlsx'
    try:
      if (cls.excelFileForBrandORCustomerID == None):
        cls.excelFileForBrandORCustomerID = xlrd.open_workbook(excelPath)
        if (cls.excelFileForBrandORCustomerID != None):
          print('打开excel文件成功！！！')
        else:
          print('打开excel文件失败！！！')
      sheet = cls.excelFileForBrandORCustomerID.sheet_by_name('客户')
      excelData = []
      for row in range(sheet.nrows): 
          rowDatas = sheet.row_values(row)  # 每行数据赋值给rowDatas
          oneBrandData = rowDatas[columnNum]  # 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
          excelData.append(oneBrandData)
      validList = cls.eliminateListDuplicateElement(excelData)[2:] # 去除了前两行的无效数据
      validList = sorted(validList, key=str.lower)
      return [excelData[2:] ,validList] # [0]原始数组 [1]去重后的数组
    except (FileExistsError, FileNotFoundError):
      print('打开excel文件失败...')
      logging.error('打开excel文件失败...')
      return ['']

  @classmethod 
  def getCountryORLanguage(cls, area, dataType, becomeCode):
    columnNum = 0
    if (area == '亚太&欧洲'):
      columnNum = 0 + becomeCode
    elif (area == '南美'):
      columnNum = 5 + becomeCode
    elif (area == '北美'):
      columnNum = 10 + becomeCode
    elif (area == '香港'):
      columnNum = 15 + becomeCode
    elif (area == '台湾'):
      columnNum = 20 + becomeCode

    if (dataType == 'language'):
      columnNum += 2
    elif (dataType == 'country'):
      pass
    excelPath = os.getcwd() + '\\MT9602_国家语言列表.xlsx'
    try:
      if (cls.excelFileForCountryAndLanguage == None):
        cls.excelFileForCountryAndLanguage = xlrd.open_workbook(excelPath)
        if (cls.excelFileForCountryAndLanguage != None):
          print('打开excel文件成功！！！')
        else:
          print('打开excel文件失败！！！')
      sheet = cls.excelFileForCountryAndLanguage.sheet_by_name('国家-OSD语言调整版')
      excelData = []
      for row in range(sheet.nrows): 
          rowDatas = sheet.row_values(row)
          oneBrandData = rowDatas[columnNum]
          excelData.append(oneBrandData)
      validList =  cls.eliminateListDuplicateElement(excelData)[2:] # 去除了前两行的无效数据
      return [excelData[2:] ,validList] # [0]原始数组 [1]去重后的数组
    except (FileExistsError, FileNotFoundError):
      print('打开excel文件失败...')
      logging.error(FileExistsError)
      logging.error(FileNotFoundError)
      return ['']

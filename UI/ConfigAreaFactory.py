#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from UI.ConfigArea import *
from GetDataFromExcel import *

class ConfigAreaFactory:
  def __init__(self):
    super().__init__()

  def createDetailConfigArea(self, father):
    detailConfigArea = ConfigArea(father, 'detailConfig')

    detailConfigArea.addSonComponentInMap('Load', [7, '_PID'])
    detailConfigArea.addSonComponentInMap('Base', [6, '_URL'])
    detailConfigArea.addSonComponentInMap('PID', [3, '_NUM'])
    detailConfigArea.addSonComponentInMap('AQ', [1])
    detailConfigArea.addSonComponentInMap('apollo', [1])
    detailConfigArea.addSonComponentInMap('hashkey', [1])
    detailConfigArea.addSonComponentInMap('Board', [1])
    detailConfigArea.addSonComponentInMap('Config', [2])
    detailConfigArea.addSonComponentInMap('Dolby', [1])
    detailConfigArea.addSonComponentInMap('EDID', [1])
    detailConfigArea.addSonComponentInMap('IR', [1])
    detailConfigArea.addSonComponentInMap('Overscan', [1])
    detailConfigArea.addSonComponentInMap('Panel', [1])
    detailConfigArea.addSonComponentInMap('PQ', [1])
    detailConfigArea.addSonComponentInMap('WIFI_limit', [2])

    detailConfigArea.refreshPage() # 这条是为了满足Scrollbar显示滑动条的逻辑
    return detailConfigArea

  def createSimpleConfigArea(self ,father):
    simpleConfigArea = ConfigArea(father, 'simpleConfig')

    # simpleConfigArea.addSonComponentInMap('Load',    [7, '_Conf'])
    simpleConfigArea.addSonComponentInMap('PID',     [5, '.ini'])
    simpleConfigArea.addSonComponentInMap('Base',    [6, '_URL'])
    simpleConfigArea.addSonComponentInMap('Logo',    [6, '_URL'])
    simpleConfigArea.addSonComponentInMap('VERSION', [3, ''])
    simpleConfigArea.addSonComponentInMap('BRAND',   [4, tuple(GetDataFromExcel.getBrandORCustomerID('Brand')[1])])
    simpleConfigArea.addSonComponentInMap('CustomerID', [4, tuple(GetDataFromExcel.getBrandORCustomerID('CustomerID')[1])])
    simpleConfigArea.addSonComponentInMap('AREA',    [4, ('亚太&欧洲', '南美', '北美', '香港', '台湾')])
    simpleConfigArea.addSonComponentInMap('COUNTRY', [4, tuple(GetDataFromExcel.
                                                      getCountryORLanguage('亚太&欧洲','Country', 0)[1])])
    simpleConfigArea.addSonComponentInMap('LANGUAGE', [4, tuple(GetDataFromExcel
                                                      .getCountryORLanguage('亚太&欧洲','language', 0)[1])])
    simpleConfigArea.addSonComponentInMap('PowerOnMode', [4, ('0:上电待机', '1:上电开机', '2:记忆模式')])
    simpleConfigArea.addSonComponentInMap('FourHourAutoStandby', [4, ('Off', 'On')])
    simpleConfigArea.addSonComponentInMap('NetflixSupport', [4, ('Yes', 'No')])
    simpleConfigArea.addSonComponentInMap('PVRTYPE',   [4, ('支持，不需要激活', '支持，需要激活', '不支持')])
    simpleConfigArea.addSonComponentInMap('APVSupport', [4, ('Yes', 'No')])

    simpleConfigArea.refreshPage()
    return simpleConfigArea

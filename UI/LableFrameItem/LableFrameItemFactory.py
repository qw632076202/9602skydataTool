#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from UI.LableFrameItem.LableFrameItem1 import LableFrameItem1
from UI.LableFrameItem.LableFrameItem2 import LableFrameItem2
from UI.LableFrameItem.LableFrameItem3 import LableFrameItem3
from UI.LableFrameItem.LableFrameItem4 import LableFrameItem4
from UI.LableFrameItem.LableFrameItem5 import LableFrameItem5
from UI.LableFrameItem.LableFrameItem6 import LableFrameItem6
from UI.LableFrameItem.LableFrameItem7 import LableFrameItem7

# LableFrameItem的子组件组合情况：
# 1、有两项：url ver
#    url：label、entey、button组合，按button显示路径
#    ver：label、entey、button组合，按button显示versionInfo信息
# 2、有两项：url ver
#    url：label、entey、button组合，按button显示路径
#    ver：label、entey、button组合，按button显示时间信息
# 3、有一项：xxx
#    xxx：label、entey组合，手动输入信息
# 4、有一项：xxx
#    xxx：label、Combobox（下拉框）组合，使用下拉框输入信息
# 5、有一项：xxx
#    xxx：label、entey、button组合，按button显示【文件路径】
# 6、有一项：xxx
#    xxx：label、entey、button组合，按button显示【目录路径】
# 7、有一项：xxx
#    xxx：label、entey、button、button组合，可以浏览和加载文件

class LableFrameItemFactory:
  def __init__(self):
    super().__init__()

  def createLableFrameItem(self, fatherComponent, itemName, type):
    if (type[0] == 1):
      return LableFrameItem1(fatherComponent, self.__textAlignment(itemName))
    elif (type[0] == 2):
      return LableFrameItem2(fatherComponent, self.__textAlignment(itemName))
    elif (type[0] == 3):
      return LableFrameItem3(fatherComponent, self.__textAlignment(itemName), type[1])
    elif (type[0] == 4):
      return LableFrameItem4(fatherComponent, self.__textAlignment(itemName), type[1])
    elif (type[0] == 5):
      return LableFrameItem5(fatherComponent, self.__textAlignment(itemName), type[1])
    elif (type[0] == 6):
      return LableFrameItem6(fatherComponent, self.__textAlignment(itemName), type[1])
    elif (type[0] == 7):
      return LableFrameItem7(fatherComponent, self.__textAlignment(itemName), type[1])
  
  def __textAlignment(self, text):
    specifyLength = 21
    if (len(text) < specifyLength):
      return (specifyLength - len(text)) * ' ' + text
# 9602skydataTool

##### 运行代码
python ./skydataTool.py

##### build exe文件（不配置icon图标）
pyinstaller -F ./skydataTool.py

##### build exe文件（配置icon图标）
pyinstaller -F ./skydataTool.py -i ./icon/skydataTool3.ico

##### build exe文件（配置icon图标，不带黑窗口）
pyinstaller -F ./skydataTool.py -i ./icon/skydataTool3.ico --noconsole

## 程序结构
- skydataTool.py：入口文件
- Write_ConfigData_ini.py
- SimpleConfigOperateLogic.py
- DetailConfigOperateLogic.py
- GetDataFromExcel.py
- DynamicRenderItem.py：用于实现动态渲染的，暂未使用
- UI
  - MainWindow.py
  - HeaderArea.py
  - MiddleArea.py
  - DividingLine.py
  - BottomArea.py
  - ConfigArea.py
  - ConfigAreaFactory.py
  - LableFrameItem
    - LableFrameItemBase.py
    - LableFrameItem1.py
    - LableFrameItem2.py
    - LableFrameItem3.py
    - LableFrameItem4.py
    - LableFrameItem5.py
    - LableFrameItem6.py
    - LableFrameItem7.py
    - LableFrameItemFactory.py
    - LoadIniFile.py


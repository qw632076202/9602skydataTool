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
- Write_ConfigData_ini.py：用于将simpleConfigArea中显示的内容写进configData.ini文件中
- SimpleConfigOperateLogic.py：simpleConfigArea中点击生成时，所运行的操作逻辑
- DetailConfigOperateLogic.py：detailConfigArea中点击生成时，所运行的操作逻辑
- GetDataFromExcel.py：用于从excel表格中获取country、language、customID、brand信息
- DynamicRenderItem.py：用于实现动态渲染ui组件，暂未使用
- UI：存放ui代码的文件夹
  - MainWindow.py
  - HeaderArea.py
  - MiddleArea.py
  - DividingLine.py
  - BottomArea.py
  - ConfigArea.py：simpleConfigArea和detailConfigArea的父类
  - ConfigAreaFactory.py：simpleConfigArea和detailConfigArea的配置工厂类
  - LableFrameItem：ConfigArea所需使用的组件模块
    - LableFrameItemBase.py
    - LableFrameItem1.py
    - LableFrameItem2.py
    - LableFrameItem3.py
    - LableFrameItem4.py
    - LableFrameItem5.py
    - LableFrameItem6.py
    - LableFrameItem7.py
    - LableFrameItemFactory.py：LableFrameItem生成工厂类，ConfigArea去调用它去生成对应组件
    - LoadIniFile.py：用于加载ini文件，并将其内容渲染到ui中


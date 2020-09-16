# 9602skydataTool

### 运行代码
python ./skydataTool.py

### build exe文件（不配置icon图标）
pyinstaller -F ./skydataTool.py

### build exe文件（配置icon图标）
pyinstaller -F ./skydataTool.py -i ./icon/skydataTool3.ico

### build exe文件（配置icon图标，不带黑窗口）
pyinstaller -F ./skydataTool.py -i ./icon/skydataTool3.ico --noconsole


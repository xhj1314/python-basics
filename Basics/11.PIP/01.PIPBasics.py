# PIP基础

# 什么是PIP？
# PIP是Python的包管理工具，用于安装和管理第三方库

# 常用命令（在命令行中执行）：

# 1. 安装包
# pip install 包名
# pip install requests

# 2. 卸载包
# pip uninstall 包名
# pip uninstall requests

# 3. 查看已安装的包
# pip list

# 4. 查看包的详细信息
# pip show 包名
# pip show requests

# 5. 升级包
# pip install --upgrade 包名
# pip install --upgrade requests

# 6. 安装指定版本的包
# pip install 包名==版本号
# pip install requests==2.25.1

# 7. 导出已安装的包列表
# pip freeze > requirements.txt

# 8. 从文件安装包
# pip install -r requirements.txt

# 示例：使用第三方库
import random

# 使用random库
print(f"随机数: {random.randint(1, 100)}")

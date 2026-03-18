# PIP教程.md

# Python PIP教程 

## 1. 什么是PIP？

PIP是Python的包管理工具，用于安装和管理第三方库。

## 2. 常用命令

### 安装包
```bash
pip install requests
```

### 卸载包
```bash
pip uninstall requests
```

### 查看已安装的包
```bash
pip list
```

### 升级包
```bash
pip install --upgrade requests
```

## 3. 使用第三方库

```python
import requests

response = requests.get("https://www.baidu.com")
print(response.status_code)
```

## 4. 总结

PIP让Python更强大！
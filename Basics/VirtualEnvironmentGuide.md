# Python 虚拟环境完整教学指南

## 什么是虚拟环境？

虚拟环境是 Python 中的一个隔离环境，允许你在计算机上独立运行和测试 Python 项目。

### 核心概念

将虚拟环境想象为每个 Python 项目的独立容器：

- ✅ 拥有自己的 Python 解释器
- ✅ 拥有独立的已安装包集合
- ✅ 与其他虚拟环境完全隔离
- ✅ 可以安装相同包的不同版本

## 为什么需要虚拟环境？

| 优势 | 说明 |
| --- | --- |
| 避免冲突 | 防止不同项目间的包版本冲突 |
| 提高可移植性 | 使项目更加便携和可重复 |
| 保持系统清洁 | 不污染系统全局 Python 环境 |
| 灵活测试 | 可以使用不同 Python 版本进行测试 |

## 创建虚拟环境

Python 内置了 venv 模块用于创建虚拟环境。

### 创建步骤

1. 打开命令提示符/终端
2. 导航到项目文件夹
3. 执行创建命令

```bash
# 创建名为 myVenv 的虚拟环境
python -m venv myVenv
```

### 生成的文件结构

```
myVenv/
├── Include/
├── Lib/
├── Scripts/
├── .gitignore
└── pyvenv.cfg
```

## 激活虚拟环境

### 激活命令

```bash
# Windows
myVenv\Scripts\activate

# macOS/Linux
source myVenv/bin/activate
```

### 激活后的提示

激活成功后，命令行提示符会显示环境名称：

```bash
(myVenv) C:\Users\Your Name>
```

## 在虚拟环境中工作

### 安装包

```bash
# 安装 cowsay 包（仅在当前虚拟环境中）
pip install cowsay
```

### 使用示例

创建 test.py 文件：

```python
import cowsay
cowsay.cow("Good Mooooorning!")
```

运行程序：

```bash
python test.py
```

输出效果：

```
  _________________
| Good Mooooorning! |
  =================
                 \
                  \
                    ^__^
                    (oo)\_______
                    (__)\       )\/\
                        ||----w |
                        ||     ||
```

## 管理虚拟环境

### 停用虚拟环境

```bash
deactivate
```

停用后返回正常命令行界面。

### 删除虚拟环境

```bash
# 直接删除文件夹（Windows）
rmdir /s /q myVenv

# macOS/Linux
rm -rf myVenv
```

## 重要注意事项

### 环境隔离性

- ✅ 在虚拟环境内：`python test.py` → 正常运行
- ❌ 在虚拟环境外：`python test.py` → 报错（缺少模块）

### 错误示例

```bash
# 虚拟环境外部执行会报错
ModuleNotFoundError: No module named 'cowsay'
```

## 最佳实践建议

1. 为每个项目创建独立的虚拟环境
2. 将虚拟环境文件夹添加到 .gitignore
3. 使用 requirements.txt 记录项目依赖
4. 定期更新虚拟环境中的包

### 生成依赖文件

```bash
# 导出当前环境的所有包
pip freeze > requirements.txt

# 从文件安装所有依赖
pip install -r requirements.txt
```

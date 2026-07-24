# Python Agent Learning

这是一个面向 Java 开发工程师的 Python 与 Agent 开发学习项目。

## 第 1 天

目标：完成第一个交互式 Python 程序，建立本地 Python 3.12 开发环境。

运行练习：

```bash
.venv/bin/python src/day01/hello.py
```

当天完成标准：

- 输出当前 Python 版本
- 提示用户输入姓名
- 清理姓名首尾空格
- 姓名不为空时输出欢迎语
- 姓名为空时输出友好提示

学习总结：

- Python 文件可以直接作为脚本运行，不需要像 Java 一样先定义类。
- `import sys` 用于导入 Python 标准库模块，`sys.version` 可以读取当前解释器版本。
- `print()` 用于输出内容，`input()` 用于接收终端输入。
- `input()` 的返回值是字符串，常搭配 `.strip()` 清理用户输入。
- Python 使用缩进表示代码块，不使用 `{}`。
- `if not name` 是 Python 中判断空字符串的常见写法。
- f-string 写法 `f"你好，{name}"` 可以把变量嵌入字符串，类似 Java 中的字符串拼接或格式化。

验收用例：

```text
输入：Felix
预期：你好，Felix！欢迎开始 Python Agent 开发之旅。
```

```text
输入：三个空格
预期：名字不能为空，请重新运行程序再试一次。
```

## 第 2 天

目标：掌握 Python 常用基础类型，并能用 Java 经验快速建立对应关系。

运行练习：

```bash
.venv/bin/python src/day02/types_practice.py
```

当天完成标准：

- 创建并打印 `str`、`int`、`float`、`bool` 四种基础变量。
- 使用 `type()` 查看变量当前绑定对象的类型。
- 完成字符串 `"30"` 到整数，再从整数到字符串的转换。
- 创建 `list`，使用 `append()` 追加元素，并使用 `for` 遍历。
- 创建 `dict`，通过 key 读取 value。

学习总结：

- Python 变量不需要提前声明类型，变量名会绑定到具体对象。
- 同一个变量名可以先绑定字符串，再绑定整数，但业务代码中应避免频繁改变变量类型。
- `str` 类似 Java `String`，`float` 类似 Java `double`，`bool` 类似 Java `boolean`。
- Python 的 `int` 不需要像 Java 那样手动区分 `int`、`long`、`BigInteger`。
- `list` 类似 Java `ArrayList`，常用 `append()` 追加元素。
- `dict` 类似 Java `Map` / `HashMap`，使用 `profile["role"]` 通过 key 读取值。
- Python 使用 `for item in items` 遍历集合，接近 Java 增强 for 循环。

验收输出应包含：

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
Java
Python
Agent
Java 开发工程师
```

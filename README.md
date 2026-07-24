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

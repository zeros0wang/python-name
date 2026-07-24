# Java → Python 学习笔记

## Day 01

### 程序入口

Java 通常使用：

```java
public static void main(String[] args) {
}
```

Python 常见写法：

```python
def main() -> None:
    ...


if __name__ == "__main__":
    main()
```

对 Java 开发者来说，可以把 `if __name__ == "__main__"` 理解为 Python 脚本的启动入口保护：当文件被直接运行时执行 `main()`，当文件被其他模块导入时不会自动执行。

### 标准库导入

Python 使用 `import` 导入模块：

```python
import sys
```

`sys` 是 Python 自带标准库模块，不需要额外安装。`sys.version` 可以查看当前 Python 解释器版本。

### 变量与类型

Python 不需要提前声明局部变量类型：

```python
name = input("请输入你的名字: ").strip()
```

这里的 `name` 会绑定到 `input()` 返回的字符串对象。Python 是动态类型语言，但对象本身仍然有明确类型。

可以用 Java 的视角粗略理解为：

```java
String name = scanner.nextLine().trim();
```

只是 Python 通常不在变量声明处写类型。

### 字符串格式化

Python 推荐使用 f-string：

```python
print(f"你好，{name}！")
```

类似 Java 中的：

```java
System.out.println("你好，" + name + "！");
```

或者：

```java
System.out.printf("你好，%s！%n", name);
```

### 条件判断

Python 使用缩进表示代码块：

```python
if not name:
    print("名字不能为空，请重新运行程序再试一次。")
else:
    print(f"你好，{name}！欢迎开始 Python Agent 开发之旅。")
```

`if not name` 可以判断空字符串。空字符串在 Python 中会被视为 `False`，非空字符串会被视为 `True`。

### Day 01 收获

- 搭建了项目本地 Python 3.12 虚拟环境。
- 完成了第一个可运行的 Python 脚本。
- 学会了 `import`、`print()`、`input()`、`.strip()`、`if/else`、f-string。
- 理解了 Python 入口函数写法与 Java `main` 方法的关系。

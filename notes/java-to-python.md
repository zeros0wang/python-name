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

## Day 02

### 基础类型对比

| Python | Java 近似理解 | 说明 |
| --- | --- | --- |
| `str` | `String` | 字符串 |
| `int` | `int` / `long` / `BigInteger` | Python 整数不需要手动区分大小范围 |
| `float` | `double` | 浮点数 |
| `bool` | `boolean` | 取值是 `True` / `False`，首字母大写 |
| `list` | `ArrayList` | 有序、可变集合 |
| `dict` | `Map` / `HashMap` | key-value 映射 |

### 动态类型

Python 不需要在变量声明处写类型：

```python
age = 33
```

这不表示 Python 没有类型，而是变量名会绑定到对象，对象本身有明确类型：

```python
print(type(age))
```

同一个变量名可以重新绑定到不同类型的对象：

```python
num = "30"
num = int(num)
num = str(num)
```

这种写法能运行，但在真实业务代码里要克制使用。一个变量在一段逻辑中尽量保持含义和类型稳定，可读性会好很多。

### 类型转换

常见转换函数：

```python
age_text = "30"
age = int(age_text)
message = str(age)
height = float("171.55")
```

可以类比 Java 中的 `Integer.parseInt()`、`String.valueOf()`、`Double.parseDouble()`。

### list

Python 的 `list` 可以类比 Java `ArrayList`：

```python
skills = ["Java", "Python"]
skills.append("Agent")

for skill in skills:
    print(skill)
```

对应 Java 视角：

```java
List<String> skills = new ArrayList<>();
skills.add("Java");
skills.add("Python");
skills.add("Agent");

for (String skill : skills) {
    System.out.println(skill);
}
```

Python 的 `for skill in skills` 更接近 Java 增强 for 循环，而不是传统下标循环。

### dict

Python 的 `dict` 可以类比 Java `Map` / `HashMap`：

```python
profile = {
    "name": "felix",
    "role": "Java 开发工程师",
    "learning_day": 2,
}

print(profile["role"])
```

对应 Java 视角：

```java
Map<String, Object> profile = new HashMap<>();
profile.put("name", "felix");
profile.put("role", "Java 开发工程师");
profile.put("learning_day", 2);

System.out.println(profile.get("role"));
```

### Day 02 收获

- 掌握了 `str`、`int`、`float`、`bool`、`list`、`dict`。
- 学会了使用 `type()` 查看变量类型。
- 学会了使用 `int()`、`str()`、`float()` 做基础类型转换。
- 学会了 `list.append()` 和 `for` 遍历。
- 学会了通过 `dict` 的 key 读取 value。
- 建立了 Python 基础类型与 Java 常用类型之间的对应关系。

"""第 2 天：练习 Python 基础类型。"""


def main() -> None:
    #  1：创建 4 个基础变量：姓名 name、年龄 age、身高 height、是否是开发者 is_developer。
    # 类型分别使用 str、int、float、bool。
    name = "felix"
    age = 33
    height = 171.55
    is_developer = True
    #  2：打印每个变量的值和类型。
    # 提示：type(name)
    print(f"name:{name} type:{type(name)}")
    print(f"age:{age} type:{type(age)}")
    print(f"height:{height} type:{type(height)}")
    print(f"is_developer:{is_developer} type:{type(is_developer)}")
    #  3：把字符串 "30" 转成整数，再把整数转回字符串。
    # 提示：int("30")、str(30)
    num = "30"
    print(f"num:{num} type:{type(num)}")
    num = int(num)
    print(f"num:{num} type:{type(num)}")
    num = str(num)
    print(f"num:{num} type:{type(num)}")
    #  4：创建一个 skills 列表，放入 "Java"、"Python"。
    # 然后追加 "Agent"，并遍历打印每一项。
    skills = ["Java", "Python"]
    skills.append("Agent")
    for skill in skills:
        print(skill)
    #  5：创建一个 profile 字典，包含 name、role、learning_day。
    # 然后通过 key 读取并打印 role。
    profile = {
        "name": "felix",
        "role": "Java 开发工程师",
        "learning_day": 2,
    }
    print(profile["role"])


if __name__ == "__main__":
    main()

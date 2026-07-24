"""第 3 天：练习 Python 函数、参数和返回值。"""


def print_title() -> None:
    print("第 3 天：函数、参数和返回值")

def build_greeting(name: str) -> str:
    return f"你好，{name}！欢迎继续 Python 学习。"

def add(left: int, right: int) -> int:
    return left + right

def describe_profile(name: str, role: str, day: int = 3) -> str:
    return f"{name} 是 {role}，正在学习第 {day} 天"

def print_skills(skills: list[str]) -> None:
    for skill in skills:
        print(skill)


def main() -> None:
    #  1：定义一个 print_title() 函数，无参数、无返回值。
    # 函数内部打印：第 3 天：函数、参数和返回值
    # 然后在 main() 中调用它。
    print_title()
    #  2：定义一个 build_greeting(name: str) -> str 函数。
    # 返回：你好，{name}！欢迎继续 Python 学习。
    # 然后在 main() 中调用，并打印返回值。
    msg = build_greeting("felix")
    print(msg)
    #  3：定义一个 add(left: int, right: int) -> int 函数。
    # 返回两个整数的和。
    # 然后在 main() 中调用 add(10, 20)，打印结果。
    res = add(10,20)
    print(res)
    #  4：定义一个 describe_profile(name: str, role: str, day: int = 3) -> str 函数。
    # 返回：{name} 是 {role}，正在学习第 {day} 天。
    # 分别调用一次传 day 的版本、一次不传 day 的版本。
    print(describe_profile("felix","java 开发"))
    print(describe_profile("felix","java 开发",1))
    #  5：把下面 skills 列表的遍历打印逻辑抽成函数 print_skills(skills: list[str]) -> None。
    skills = ["Java", "Python", "Agent"]
    print_skills(skills)


if __name__ == "__main__":
    main()

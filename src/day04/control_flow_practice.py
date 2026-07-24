"""第 4 天：练习条件判断、循环和集合遍历。"""

def get_score_level(score: int) -> str:
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

def main() -> None:
    #  1：定义 get_score_level(score: int) -> str。
    # 规则：
    # - score >= 90 返回 "优秀"
    # - score >= 60 返回 "及格"
    # - 其他返回 "不及格"
    # 在 main() 中分别测试 95、75、50。
    print(get_score_level(95))
    print(get_score_level(75))
    print(get_score_level(50))
    #  2：使用 range() 打印 1 到 5。
    # 提示：range(1, 6)
    for num in range(1, 6):
        print(num)

    #  3：遍历 skills 列表，打印每一项。
    skills = ["Java", "Python", "Agent", "FastAPI"]
    for skill in skills:
        print(skill)

    #  4：使用 enumerate() 遍历 skills，同时打印序号和技能名。
    # 输出示例：1. Java
    for index, skill in enumerate(skills, start=1):
        print(index, skill)
    #  5：遍历 profile 字典，打印 key 和 value。
    profile = {
        "name": "felix",
        "role": "Java 开发工程师",
        "learning_day": 4,
    }
    for key, value in profile.items():
        print(key, value)

    #  6：从 scores 中筛选出及格分数，放入 passed_scores。
    # 提示：先创建空列表 passed_scores = []，再循环判断 >= 60 后 append。
    scores = [95, 40, 75, 59, 88]
    passed_scores = []
    for score in scores:
        if score >= 60:
            passed_scores.append(score)
    print(passed_scores)

    #  7：遍历 tools，遇到 "disabled_tool" 时跳过，遇到 "stop" 时结束循环。
    # 提示：continue 和 break。
    tools = ["search", "disabled_tool", "calculator", "stop", "weather"]
    for tool in tools:
        if tool=="disabled_tool":
            continue
        if tool=="stop":
            break
        print(tool)


if __name__ == "__main__":
    main()

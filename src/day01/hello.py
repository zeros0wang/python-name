"""第 1 天：完成第一个交互式 Python 程序。"""
import sys


def main() -> None:
    print(f"当前 Python 版本: {sys.version}")

    name = input("请输入你的名字: ").strip()

    if not name:
        print("名字不能为空，请重新运行程序再试一次。")
    else:
        print(f"你好，{name}！欢迎开始 Python Agent 开发之旅。")


if __name__ == "__main__":
    main()

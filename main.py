import random
from datetime import datetime as dt

"""
制表符：
┌ ┬ ┐
├ ┼ ┤
└ ┴ ┘
│─
.ljust(16, "\u3000").center(33, "\u3000")
"""


class table:
    def __init__(self) -> None:
        pass

    def makeheadline():
        print("┌" + "─" * 62 + "┐")

    def makeline(line: str, ex: int = 0):
        print("│" + line.center(32 + ex, "\u3000") + "│")

    def makesepline():
        print("├" + "─" * 62 + "┤")

    def makendline():
        print("└" + "─" * 62 + "┘")

    def makemenu(menu: list, depth: int):
        if depth == 3:
            for i in range(len(menu)):
                table.makeline(f"{i+1}.  {menu[i][0][0]}".ljust(16, "\u3000"), 1)
        elif depth == 2:
            pass
        table.makeline(f"{i+2}.{' '*(2-i//8)}随机！！".ljust(16, "\u3000"), 1)
        table.makendline()

    def makechoice(start, end):
        choice = input(f"您的选择是[{start}-{end}]：")
        return choice


def loadMenu():
    with open("./menu.txt", "r", encoding="utf-8") as menuData:
        menu = menuData.read().split("\n---\n")
        for i in range(len(menu)):
            menu[i] = menu[i].split("\n--\n")
            for j in range(len(menu[i])):
                ij = menu[i][j].split("\n")
                menu[i][j] = [ij[0], ij[1:]]
    return menu


def main():
    menu = loadMenu()
    random.seed(int(dt.now().timestamp()))
    print(menu)

    table.makeheadline()
    table.makeline("今天吃什么呢~ ")
    table.makesepline()
    table.makemenu(menu, 3)

    choice = int(table.makechoice(1, 10)) - 1
    if choice == 9:
        choice = random.randint(1, 9)
        print("随机选择到：" + str(choice))
    elif choice not in range(0, 9):
        raise ValueError

    table.makeheadline()
    table.makeline(menu[choice][0][0], -1)
    table.makesepline()
    print(menu[choice])
    if len(menu[choice]) == 1:
        pass


# while True:
#     try:
#         main()
#     except Exception as e:
#         print(f"{type(e).__name__}: 啊哦，请按照标准格式输入呢~")
main()

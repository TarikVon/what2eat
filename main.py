import random
from datetime import datetime as dt


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
        if depth == 2:
            prices = []
            for i in range(len(menu)):
                parts = menu[i].split()
                parts[1] = float(parts[1])
                prices.append(parts)
                table.makeline(f"{i+1}.{' '*(3-len(str(i+1)))}{parts[0]}".ljust(16, "\u3000") + f"  {str(parts[1]).rjust(6," ")}元\u3000\u3000", 5)
            table.makeline(f"{i+2}.{' '*(3-len(str(i+2)))}随机！！".ljust(23, "\u3000"), 1)
            table.makendline()
            return prices

        else:
            if depth == 3:
                for i in range(len(menu)):
                    table.makeline(f"{i+1}.{' '*(3-len(str(i+1)))}{menu[i][0][0]}".ljust(16, "\u3000"), 1)
            else:
                for i in range(len(menu)):
                    table.makeline(f"{i+1}.{' '*(3-len(str(i+1)))}{menu[i]}".ljust(16, "\u3000"), 1)
            table.makeline(f"{i+2}.{' '*(3-len(str(i+2)))}随机！！".ljust(16, "\u3000"), 1)
            table.makendline()

    def makechoice(end):
        choice = int(input(f"您的选择是[1-{end+1}]："))
        if choice == end + 1:
            choice = random.randint(1, end)
            print("随机选择到：" + str(choice))
        elif choice not in range(1, end + 1):
            raise ValueError
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


def main(menu):
    # print(menu)
    bill = []
    count = 0
    random.seed(int(dt.now().timestamp()))

    table.makeheadline()
    table.makeline("今天吃什么呢~ ")
    table.makesepline()
    table.makemenu(menu, 3)
    choice1 = table.makechoice(len(menu)) - 1  # 选择大类

    table.makeheadline()
    table.makeline(menu[choice1][0][0], -1)
    table.makesepline()
    prices = table.makemenu(menu[choice1][0][1], 2)
    choice2 = int(table.makechoice(len(menu[choice1][0][1]))) - 1  # 选择菜品
    dish = prices[choice2][0]

    if len(menu[choice1]) >= 2:  # 选择口味
        table.makeheadline()
        table.makeline(menu[choice1][1][0], -1)
        table.makesepline()
        table.makemenu(menu[choice1][1][1], 1)
        choice3 = int(table.makechoice(len(menu[choice1][1][1]))) - 1
        dish += " " + menu[choice1][1][1][choice3]

        if len(menu[choice1]) == 3:  # 选择基底
            table.makeheadline()
            table.makeline(menu[choice1][2][0], -1)
            table.makesepline()
            table.makemenu(menu[choice1][2][1], 1)
            choice4 = int(table.makechoice(len(menu[choice1][2][1]))) - 1
            dish += " " + menu[choice1][2][1][choice4]

    price = prices[choice2][1]
    bill.append(dish)
    count += price
    if input("还需要继续点单么[y/n]：") == "y":
        bills, counts = main(menu)
        bill.extend(bills)
        count += counts

    return bill, count


# while True:
#     try:
#         main()
#     except Exception as e:
#         print(f"{type(e).__name__}: 啊哦，请按照标准格式输入呢~")
bill, count = main(loadMenu())
print(bill, count)

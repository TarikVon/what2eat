import random
from datetime import datetime as dt


class table:
    def makeheadline():
        print("┌" + "─" * 62 + "┐")

    def makeline(line: str, ex: int = 0):
        print("│" + line.center(32 + ex, "\u3000") + "│")

    def makesepline():
        print("├" + "─" * 62 + "┤")

    def makendline():
        print("└" + "─" * 62 + "┘")

    def makemenu(menu: list, depth: int = 1, end: bool = True):
        if depth == 2:
            prices = []
            for i in range(len(menu)):
                parts = menu[i].split()
                parts[1] = float(parts[1])
                prices.append(parts)
                table.makeline(f"{i+1}.{' '*(3-len(str(i+1)))}{parts[0]}".ljust(16, "\u3000") + f"  {str(parts[1]).rjust(6," ")}元\u3000\u3000", 5)
            if end:
                table.makeline(f"↵.  随机！！".ljust(24, "\u3000"), 1)
                table.makendline()
            return prices

        else:
            if depth == 3:
                for i in range(len(menu)):
                    table.makeline(f"{i+1}.{' '*(3-len(str(i+1)))}{menu[i][0][0]}".ljust(16, "\u3000"), 1)
            elif depth == 1:
                for i in range(len(menu)):
                    table.makeline(f"{i+1}.{' '*(3-len(str(i+1)))}{menu[i]}".ljust(16, "\u3000"), 1)
            if end:
                table.makeline(f"↵.  随机！！".ljust(16, "\u3000"), 1)
                table.makendline()

    def makechoice(end):
        choice = input(f"您的选择是[1-{end+1}]：") or (end + 1)
        choice = int(choice)
        if choice == end + 1:
            choice = random.randint(1, end)
            print("随机选择到：" + str(choice))
        elif choice not in range(1, end + 1):
            raise ValueError
        return choice


def loadmenu():
    with open("./menu.txt", "r", encoding="utf-8") as menuData:
        menu = menuData.read().split("\n---\n")
        for i in range(len(menu)):
            menu[i] = menu[i].split("\n--\n")
            for j in range(len(menu[i])):
                ij = menu[i][j].split("\n")
                menu[i][j] = [ij[0], ij[1:]]
    return menu


def main(menu):
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
        dish += "\u3000" + menu[choice1][1][1][choice3]

        if len(menu[choice1]) == 3:  # 选择基底
            table.makeheadline()
            table.makeline(menu[choice1][2][0], -1)
            table.makesepline()
            table.makemenu(menu[choice1][2][1], 1)
            choice4 = int(table.makechoice(len(menu[choice1][2][1]))) - 1
            dish += "\u3000" + menu[choice1][2][1][choice4]

    price = prices[choice2][1]
    bill.append(dish)
    count += price
    if input("还需要继续点单么[y/↵]：") == "y":
        bills, counts = main(menu)
        bill.extend(bills)
        count += counts

    return bill, count


if __name__ == "__main__":
    try:
        bill, count = main(loadmenu())
        table.makeheadline()
        table.makeline("账单", -1)
        table.makesepline()
        table.makemenu(bill, 1, False)
        table.makesepline()
        table.makeline(f"总价：{' '*(4-len(str(count)))}{count}元".ljust(16, "\u3000"), 1)
        table.makendline()
        if input("是否生成订单[↵/*]：") == "":
            time = input("送达时间[↵: 做好即送]：") or "做好即送"
            address = input("地址[*]号楼：")
            if not address.endswith("号楼"):
                address += "号楼"
            tel = input("联系电话：")
            print("\n以下是您的订单：\n" + "─" * 64)
            for i in bill:
                print(i.replace("\u3000"," "))
            print(f"{count}元\n{time}{"\n" + address if address!="号楼" else ""}{"\n" + tel if tel else ""}")

    except Exception as e:
        print(f"{type(e).__name__}: 啊哦，请按照标准格式输入呢~")

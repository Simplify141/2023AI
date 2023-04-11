"""
第4次作业, 选择其中一种算法实现即可.
Puzzle问题的输入数据类型为二维嵌套list, 空位置用 `0`表示. 输出的解数据类型为 `list`, 是移动数字方块的次序.
"""

import copy


class Node():
    def __init__(self, list1, depth1, father1, target):
        self.depth = depth1
        self.diff = 0
        self.father = father1
        self.list = list1
        for i in range(len(target)):
            for j in range(len(target)):
                if self.list[i][j] != target[i][j]:
                    self.diff += 1
        self.fx = self.depth+self.diff
        if father1 != None:
            self.move = copy.deepcopy(father1.move)
        else:
            self.move = []


def find(least):
    for i in range(len(least)):
        for j in range(len(least)):
            if least[i][j] == 0:
                return (i, j)
    return (-1, -1)


def A_star(puzzle):
    lens = len(puzzle)
    target = [[j*lens+i for i in range(1, lens+1)] for j in range(lens)]
    target[-1][-1] = 0  # 初始化目标
    openlist = []
    closelist = []
    origin = Node(puzzle, 0, None, target)
    openlist.append(origin)
    while len(openlist) != 0:
        least = openlist[0]
        for node in openlist:
            if node.fx < least.fx:
                least = node
        openlist.remove(least)
        closelist.append(least)
        # extend
        (i, j) = find(least.list)
        if i+1 < lens:
            temp = copy.deepcopy(least.list)
            temp[i][j] = temp[i+1][j]
            temp[i+1][j] = 0
            new1 = Node(temp, least.depth+1, least, target)
            new1.move.append(temp[i][j])
            flag = False
            for p in closelist:
                if new1.list == p.list:
                    flag = True
            if not flag and new1 not in openlist:
                openlist.append(new1)
                if new1.diff == 0:
                    break
        if i-1 >= 0:
            temp = copy.deepcopy(least.list)
            temp[i][j] = temp[i-1][j]
            temp[i-1][j] = 0
            new2 = Node(temp, least.depth+1, least, target)
            new2.move.append(temp[i][j])
            flag = False
            for p in closelist:
                if new2.list == p.list:
                    flag = True
            if not flag and new2 not in openlist:
                openlist.append(new2)
                if new2.diff == 0:
                    break
        if j+1 < lens:
            temp = copy.deepcopy(least.list)
            temp[i][j] = temp[i][j+1]
            temp[i][j+1] = 0
            new3 = Node(temp, least.depth+1, least, target)
            new3.move.append(temp[i][j])
            flag = False
            for p in closelist:
                if new3.list == p.list:
                    flag = True
            if not flag and new3 not in openlist:
                openlist.append(new3)
                if new3.diff == 0:
                    break
        if j-1 >= 0:
            temp = copy.deepcopy(least.list)
            temp[i][j] = temp[i][j-1]
            temp[i][j-1] = 0
            new4 = Node(temp, least.depth+1, least, target)
            new4.move.append(temp[i][j])
            flag = False
            for p in closelist:
                if new4.list == p.list:
                    flag = True
            if not flag and new4 not in openlist:
                openlist.append(new4)
                if new4.diff == 0:
                    break
    return openlist[-1].move


def IDA_star(puzzle):
    lens = len(puzzle)
    target = [[j*lens+i for i in range(1, lens+1)] for j in range(lens)]
    target[-1][-1] = 0  # 初始化目标
    openlist = []
    closelist = []
    origin = Node(puzzle, 0, None, target)
    openlist.append(origin)
    flag = False
    for max in range(1000):
        while len(openlist) != 0:
            while openlist[-1].depth > max:
                openlist.remove(openlist[-1])
                if len(openlist) == 0:
                    break
            if len(openlist) == 0:
                break
            least = openlist[0]
            for node in openlist:
                if node.fx < least.fx:
                    least = node
            openlist.remove(least)
            closelist.append(least)
            # extend
            (i, j) = find(least.list)
            if i+1 < lens:
                temp = copy.deepcopy(least.list)
                temp[i][j] = temp[i+1][j]
                temp[i+1][j] = 0
                new1 = Node(temp, least.depth+1, least, target)
                new1.move.append(temp[i][j])
                flag = False
                for p in closelist:
                    if new1.list == p.list:
                        flag = True
                if not flag and new1 not in openlist:
                    openlist.append(new1)
                    if new1.diff == 0:
                        flag = True
                        break
            if i-1 >= 0:
                temp = copy.deepcopy(least.list)
                temp[i][j] = temp[i-1][j]
                temp[i-1][j] = 0
                new2 = Node(temp, least.depth+1, least, target)
                new2.move.append(temp[i][j])
                flag = False
                for p in closelist:
                    if new2.list == p.list:
                        flag = True
                if not flag and new2 not in openlist:
                    openlist.append(new2)
                    if new2.diff == 0:
                        flag = True
                        break
            if j+1 < lens:
                temp = copy.deepcopy(least.list)
                temp[i][j] = temp[i][j+1]
                temp[i][j+1] = 0
                new3 = Node(temp, least.depth+1, least, target)
                new3.move.append(temp[i][j])
                flag = False
                for p in closelist:
                    if new3.list == p.list:
                        flag = True
                if not flag and new3 not in openlist:
                    openlist.append(new3)
                    if new3.diff == 0:
                        flag = True
                        break
            if j-1 >= 0:
                temp = copy.deepcopy(least.list)
                temp[i][j] = temp[i][j-1]
                temp[i][j-1] = 0
                new4 = Node(temp, least.depth+1, least, target)
                new4.move.append(temp[i][j])
                flag = False
                for p in closelist:
                    if new4.list == p.list:
                        flag = True
                if not flag and new4 not in openlist:
                    openlist.append(new4)
                    if new4.diff == 0:
                        flag = True
                        break
        if flag == True:
            break
    return openlist[-1].move


if __name__ == '__main__':
    # 可自己创建更多用例并分析算法性能
    puzzle3 = [[5, 1, 2, 4], [9, 6, 3, 8], [13, 15, 10, 11], [14, 0, 7, 12]]
    sol3 = A_star(puzzle3)
    print(sol3)

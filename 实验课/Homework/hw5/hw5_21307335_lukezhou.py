"""
第5次作业, 用遗传算法解决TSP问题
本次作业可使用`numpy`库和`matplotlib`库以及python标准库
请不要修改类名和方法名
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import copy as cp
import random as rd
import datetime
CHANCE_HOLD = 0.4
NUMCHILD = 100
RETREAT = 2000
GENE_TIME = 2000
BORNNUM = 2*NUMCHILD
HOLDS = 80
TIME_HOLD = 10


def check(p):
    for i in range(1, 39):
        if i not in p:
            return False
    return True


class GeneticAlgTSP:
    def __init__(self, tsp_filename):
        df = pd.read_csv('实验课\\Homework\\hw5\\'+tsp_filename,
                         sep=" ", skiprows=7, header=None)
        city = np.array(df[0][0:len(df)-1])  # 最后一行为EOF，不读入
        self.city_name = city.tolist()
        # print(city_name)
        city_x = np.array(df[1][0:len(df)-1])
        city_y = np.array(df[2][0:len(df)-1])
        self.city_location = list(zip(city_x, city_y))
        self.length = len(df)-1
        stand = list(range(1, self.length+1))
        self.population = []
        for i in range(NUMCHILD):
            temp = cp.deepcopy(stand)
            rd.shuffle(temp)
            self.population.append(temp)  # 初始化种群, 会随着算法迭代而改变
        self.num = []
        self.routing = []
    # 随机选择父代

    def choose2(self,  parent):
        begin = rd.randint(0, len(parent)-1)
        end = rd.randint(begin, len(parent)-1)
        return (cp.deepcopy(parent[begin]), cp.deepcopy(parent[end]))
    # 染色体交换

    def exchange(self, p1, p2):
        begin = rd.randint(0, len(p1)-1)
        end = rd.randint(begin, len(p1)-1)
        p1[begin:end+1], p2[begin:end+1] = p2[begin:end+1], p1[begin:end+1]
        dict = {}
        dicts = {}
        for i in range(begin, end+1):
            flag = 0
            if p2[i] in dict.keys() and p1[i] in dicts.keys():
                dicts[dict[p2[i]]] = dicts[p1[i]]
                dict[dicts[p1[i]]] = dict[p2[i]]
                del dict[p2[i]]
                del dicts[p1[i]]
            elif p2[i] in dict.keys():
                dict[p1[i]] = dict[p2[i]]
                dicts[dict[p2[i]]] = p1[i]
                del dict[p2[i]]
            elif p1[i] in dicts.keys():
                dicts[p2[i]] = dicts[p1[i]]
                dict[dicts[p1[i]]] = p2[i]
                del dicts[p1[i]]
            else:
                dict[p1[i]] = p2[i]
                dicts[p2[i]] = p1[i]

        for i in range(0, begin):
            if p1[i] in dict:
                p1[i] = dict[p1[i]]
            if p2[i] in dicts:
                p2[i] = dicts[p2[i]]
        for i in range(end+1, self.length):
            if p1[i] in dict:
                p1[i] = dict[p1[i]]
            if p2[i] in dicts:
                p2[i] = dicts[p2[i]]
        return (p1, p2)
# 变异

    def vary(self, c1, c2):
        hold = rd.random()
        if hold <= CHANCE_HOLD:
            return (c1, c2)
        (begin, end) = (rd.randint(0, self.length), rd.randint(0, self.length))
        while begin >= end:
            (begin, end) = (rd.randint(0, self.length), rd.randint(0, self.length))
        c1[begin:end+1] = list(reversed(c1[begin:end+1]))
        c2[begin:end+1] = list(reversed(c2[begin:end+1]))
        return (c1, c2)
# 选出最优父代

    def pick(self, parent):
        point = parent[0]
        min = self.compute(parent[0])
        for i in parent:
            temp = self.compute(i)
            # print(temp)
            if temp < min:
                min = temp
                point = i
        return cp.deepcopy(point)
# 计算路径长度

    def compute(self, route):
        cost = 0
        for i in range(self.length):
            cost += ((self.city_location[route[i]-1][0]-self.city_location[route[i-1]-1][0])**2+(
                self.city_location[route[i]-1][1]-self.city_location[route[i-1]-1][1])**2)**0.5
        return cost
# 选择下一批父代

    def choose(self, parent, child):
        num = []
        new = []
        parent.extend(child)
        for i in range(len(parent)):
            num.append(self.compute(parent[i]))
        temp = np.argsort(num)
        best = parent[num.index(np.min(num))]
        for i in range(NUMCHILD):
            new.append(parent[temp[i]])
        return (new, best)
# 迭代

    def iterate(self, num_iterations):
        parent = self.population
        for nums in range(num_iterations):
            # print(nums)
            child = []
            if parent[0] == parent[-1]:
                del parent[-1]
                del parent[0]
                temp = list(range(1, self.length+1))
                rd.shuffle(temp)
                parent.append(temp)
                rd.shuffle(temp)
                parent.append(temp)
            # 一旦有稳定趋向就把相同项保留一个并且引入新子代
            for i in range(BORNNUM):
                (p1, p2) = self.choose2(parent)  # 随机选择父代
                (c1, c2) = self.exchange(p1, p2)  # 染色体交叉
                (c1, c2) = self.vary(c1, c2)  # 染色体变异
                child.append(c1)
                child.append(c2)
            #starttime = datetime.datetime.now()
            (parent, best) = self.choose(parent, child)  # 父代子代共同挑选下一轮父代
            #endtime = datetime.datetime.now()
            # 显示当前最优状态：
            self.num.append(nums)
            self.routing.append(self.compute(best))
            plt.plot(self.num, self.routing)
            plt.show(block=False)
            plt.pause(0.1)
            plt.cla()
            # print(endtime-starttime)
        return self.pick(parent)  # 选出最好的


if __name__ == "__main__":
    tsp = GeneticAlgTSP("qa194.tsp")  # 读取Djibouti城市坐标数据
    T = GENE_TIME
    tour = tsp.iterate(T)  # 对算法迭代T次
    print(tsp.compute(tour))
    plt.figure(1)
    plt.plot(tsp.num, tsp.routing)
    plt.show(block=False)
    xpoint = []
    ypoint = []
    for i in range(len(tour)):
        xpoint.append(tsp.city_location[tour[i]-1][0])
        ypoint.append(tsp.city_location[tour[i]-1][1])
    xpoints = np.array(xpoint)
    ypoints = np.array(ypoint)
    plt.figure(2)
    plt.plot(xpoints, ypoints)
    plt.scatter(xpoints, ypoints, color='red', s=10)
    plt.show(block=False)
    plt.pause(20000)
    plt.cla()
    print(tsp.compute(tour))

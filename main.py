# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import pylab as mpl  # import matplotlib as mpl
import math


def loss(data, predict):
    Sum_Loss = 0
    for i in range(len(predict)):
        Sum_Loss += (data[i][1] - predict[i][1]) * (data[i][1] - predict[i][1])
    return Sum_Loss


def Draw(dataA, dataB):
    x = []
    A = []
    B = []
    for i in dataA:
        x.append(i[0])
        A.append(i[1])
        print(i[1])
    for i in dataB:
        print(i[1])
        B.append(i[1])

    mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

    plt.plot(x, A, c='red', label='实际数据')
    plt.plot(x, B, c='blue', label='拟合数据')
    plt.xlabel('传播天数')
    plt.ylabel('传播人数')
    plt.legend(loc='best')
    plt.show()


def sir(times, step):
    # Use a breakpoint in the code line below to debug your script.
    x = 2.0  # 传染系数
    cure = 0.0  # 治愈系数
    gover = 1.0  # 政府管控系数
    data = [[1, 10.0], [2, 14.0], [3, 22.0], [4, 26.0], [5, 36.0], [6, 41.0], [7, 51.0], [8, 68.0], [9, 72], [10, 80.0]]
    LOSS = []
    Nums = []
    for z in range(times): # 调整策略
        loss = SIR(x, cure, gover, data)
        if SIR(x, cure, gover - step, data) < loss and gover - step > 0 and x - gover - step != 0:
            gover -= step
        elif SIR(x, cure, gover + step, data) < loss and gover + step > 0 and x - gover + step != 0:
            gover += step
        if SIR(x, cure - step, gover, data) < loss and cure - step > 0:
            cure -= step
        elif SIR(x, cure + step, gover, data) < loss and cure + step > 0:
            cure += step
        if SIR(x - step, cure, gover, data) < loss and x - step > 0 and x - gover - step != 0:
            x -= step
        elif SIR(x + step, cure, gover, data) < loss and x + step > 0 and x - gover + step != 0:
            x += step
        LOSS.append(SIR(x, cure, gover, data))
        Nums.append([x, cure, gover])
    for i in range(len(Nums)):
        print(Nums[i], LOSS[i])
    Draw(data, fit(x, cure, gover, data))

    print("传染系数:%f\n治愈系数：%f\n政府管控系数:%f\n" % (x, cure, gover))


def Func(pre, cure, gover, x): # 计算公式
    try:
        return pre * (1.0 - cure) ** (x - gover)
    except:
        print(pre, cure, gover, x)


def fit(x, cure, gover, data):
    NewData = [data[0]]
    for i in range(1, len(data)):
        NewElem = [i, Func(NewData[i - 1][1], cure, x, gover)]
        NewData.append(NewElem)
    return NewData


def SIR(x, cure, gover, data):
    NewData = [data[0]]
    for i in range(1, len(data)):
        NewElem = [i, Func(NewData[i - 1][1], cure, x, gover)]
        NewData.append(NewElem)
    Loss = loss(data, NewData)
    return Loss


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sir(300, 0.005)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# pip install matplotlib
import matplotlib.pyplot as plt
import math
# pip install texttable
from texttable import Texttable

def pack_result_and_return(result_list):
    index_list = []
    return_list = []
    for a,b,c in result_list:
        index_list.append(a)
        return_list.append(c)
    return index_list, return_list

def irvin_method(data_list):
    print(5*"=", "irvin method", 5*"=")

    y_average = sum(data_list) / len(data_list)
    print("average:", y_average)

    s = 0
    for i in data_list:
        s += math.pow(i - y_average, 2)
    d_dispersion = round(s / (len(data_list) - 1), 2)
    print("dispersion:", d_dispersion)

    g_deviation = round(math.sqrt(d_dispersion), 2)
    print("deviation", g_deviation)

    result_list = []
    for i, data in enumerate(data_list):
        if i == 0:
            result_list.append((i, data, None))
        else:
            l = round(abs(data - data_list[i - 1]) / g_deviation, 2)
            result_list.append((i, data, l))
    
    t = Texttable()
    t.add_rows([["index", "input data ", "irvin method"], *result_list])
    print(t.draw())

def moving_average(data_list, n):
    print(5*"=", "moving average", 5*"=")
    result_list = []

    for i, data in enumerate(data_list):
        if i < (n // 2) or i > ((len(data_list) - 1) - (n // 2)):
            result_list.append((i, data, None))
        else:
            it = n // 2
            result = data_list[i]
            while it:
                result += data_list[i-it]
                it -= 1
            it = n // 2
            while it:
                result += data_list[i+it]
                it -= 1
            result /= n
            result_list.append((i, data, result))

    t = Texttable()
    t.add_rows([["index", "input data ", "moving average"], *result_list])
    print(t.draw())
    
    return pack_result_and_return(result_list)

def weighted_average5(data_list):
    print(5*"=", "weighted average5", 5*"=")
    factor_list = [-3, 12, 17, 12, -3]    
    n = len(factor_list)
    result_list = []
    print("factor list:", factor_list)

    for i, data in enumerate(data_list):
        if i < (n // 2) or i > ((len(data_list) - 1) - (n // 2)):
            result_list.append((i, data, None))
        else:
            factor_index = len(factor_list) // 2
            factor = factor_list[factor_index]
            result = data_list[i] * factor

            factor_index = 0
            it = n // 2
            while it:
                result += (data_list[i-it] * factor_list[factor_index])
                it -= 1
                factor_index +=1

            factor_index = (len(factor_list) // 2) + 1
            it = 1
            while it <= n // 2:
                result += (data_list[i+it] * factor_list[factor_index])
                it += 1
                factor_index += 1

            result /= 35
            result_list.append((i, data, round(result, 2)))

    t = Texttable()
    t.add_rows([["index", "input data ", "weighted average5"], *result_list])
    print(t.draw())

    return pack_result_and_return(result_list)

def weighted_average7(data_list):
    print(5*"=", "weighted average7", 5*"=")
    factor_list = [-2, 3, 6, 7, 6, 3, -2]    
    n = len(factor_list)
    result_list = []
    print("factor list:", factor_list)

    for i, data in enumerate(data_list):
        if i < (n // 2) or i > ((len(data_list) - 1) - (n // 2)):
            result_list.append((i, data, None))
        else:
            factor_index = len(factor_list) // 2
            factor = factor_list[factor_index]
            result = data_list[i] * factor

            factor_index = 0
            it = n // 2
            while it:
                result += (data_list[i-it] * factor_list[factor_index])
                it -= 1
                factor_index +=1

            factor_index = (len(factor_list) // 2) + 1
            it = 1
            while it <= n // 2:
                result += (data_list[i+it] * factor_list[factor_index])
                it += 1
                factor_index += 1

            result /= 21
            result_list.append((i, data, round(result, 2)))


    t = Texttable()
    t.add_rows([["index", "input data ", "weighted average7"], *result_list])
    print(t.draw())

    return pack_result_and_return(result_list)

def exponential_smoothing(data_list):
    print(5*"=", "exponential smoothing", 5*"=")
    a = 0.1
    s0 = round((data_list[0] + data_list[1] + data_list[2]) / 3, 2)
    print("s0:", s0)
    result_list = [(None, s0, None)]

    for i, data in enumerate(data_list):
        sn = (1 - a) * data_list[i] + 0.1 * result_list[len(result_list) - 1:][0][1]
        result_list.append((i, data, round(sn, 2)))

    t = Texttable()
    t.add_rows([["index", "input data ", "exponential smoothing"], *result_list[1:]])
    print(t.draw())

    return pack_result_and_return(result_list)

def chronological_average(data_list):
    print(5*"=", "exponential smoothing", 5*"=")
    result_list = []
    n = 12
    print(data_list)

    for i, data in enumerate(data_list):
        if i < (n // 2) or i > ((len(data_list) - 1) - (n // 2)):
            result_list.append((i, data, None))
        else:
            result = data_list[i - (n // 2)] / 2
            it = 1
            while it < (n // 2):
                result += data_list[i - it]
                it += 1

            result += data_list[i]

            it = 1
            while it < (n // 2):
                result += data_list[i + it]
                it += 1
            result += data_list[i + (n // 2)] / 2

            result /= 12
            result_list.append((i, data, round(result, 2)))

    t = Texttable()
    t.add_rows([["index", "input data ", "chronological average"], *result_list])
    print(t.draw())

    return pack_result_and_return(result_list)

def main():
    fig, ax = plt.subplots()
    ax.set_xlabel("x - index")
    ax.set_ylabel("y - calculated data")

    # Student1 ####################################################
    data1 = [115, 112, 118, 122, 115, 121, 126, 132, 134, 131, 135, 134, 138, 135, 137, 139, 140, 136, 138, 140]
    irvin_method(data1)

    x, y = moving_average(data1, 5)
    ax.plot(x, data1, label="исходные данные")
    ax.plot(x, y, label="среднеарифметическая по 5 точкам")

    x, y = weighted_average5(data1)
    ax.plot(x, y, label="средневзвешенная по 5 точкам")
    
    x, y = weighted_average7(data1)
    ax.plot(x, y, label="средневзвешенная по 7 точкам")

    x, y = chronological_average(data1)
    ax.plot(x, y, label="среднехронологическая по 12 точкам")

    x, y = exponential_smoothing(data1)
    ax.plot(x, y, label="экспоненциальное сглаживание")

    # Student2 ####################################################
    # data2 = [799, 864, 990, 1163, 1140, 1173, 1290, 1302, 1295, 1355, 1464, 1559, 1581, 1931, 2032, 2260, 2093, 2123, 2210, 2130]
    # irvin_method(data2)

    # x, y = moving_average(data2, 5)
    # ax.plot(x, data2, label="исходные данные")
    # ax.plot(x, y, label="среднеарифметическая по 5 точкам")

    # x, y = weighted_average5(data2)
    # ax.plot(x, y, label="средневзвешенная по 5 точкам")
    
    # x, y = weighted_average7(data2)
    # ax.plot(x, y, label="средневзвешенная по 7 точкам")

    # x, y = chronological_average(data2)
    # ax.plot(x, y, label="среднехронологическая по 12 точкам")

    # x, y = exponential_smoothing(data2)
    # ax.plot(x, y, label="экспоненциальное сглаживание")
    ##############################################################

    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
